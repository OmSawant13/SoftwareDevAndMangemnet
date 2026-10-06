# Software Design & UML Architecture Package
## Project Name: SalesLens - Enterprise BI Dashboard
**Document Version:** 1.0  
**Course:** B.Tech CSE Semester III — Software Engineering & Project Management  
**Prescribed Textbooks:** *Software Engineering* by Ian Sommerville | *Software Project Management* by Bob Hughes & Mike Cotterell

---

## 1. Executive Design Summary & Architectural Overview

SalesLens adopts a **Layered Service-Oriented Model-View-Controller (MVC) Architecture** with an asynchronous **Extract-Transform-Load (ETL) Pipeline Pipeline-and-Filter Subsystem**. 

The design strictly enforces:
- **Low Coupling:** The Data Cleaning Engine operates independently of the Presentation Layer. Dashboard views interact exclusively with an aggregated Data Access Layer (DAL) through standardized Data Transfer Objects (DTOs). If billing schema or region mapping logic changes, dashboard views require zero code modifications.
- **High Cohesion:** Each module is single-purposed. The `RegionResolutionEngine` only handles address and territory reconciliation; the `QuotaComputationEngine` solely calculates variances; and the `DashboardViewRenderer` only manages visual presentation and UI state.

---

## 2. UML Diagrams

### 2.1 Use Case Diagram

```mermaid
flowchart LR
    %% Actors
    Director((Sales Director))
    Manager((Regional Manager))
    Analyst((Data Analyst))
    ITAdmin((IT Admin / Cron))

    %% System Boundary
    subgraph SalesLens_System [SalesLens System Boundary]
        UC1([UC-01: View Executive National Sales Pulse])
        UC2([UC-02: Compare Regional Performance Matrix])
        UC3([UC-03: View Filtered Regional Territory Report])
        UC4([UC-04: Analyze Target vs Actual Quotas])
        UC5([UC-05: Inspect Top & Bottom Product SKUs])
        UC6([UC-06: Inspect Data Quality & Clean Anomaly Log])
        UC7([UC-07: Ingest & Clean Daily Billing Transactions])
        UC8([UC-08: Export Executive PDF / CSV Briefing])
        UC9([UC-09: Configure User Roles & Permissions])
    end

    %% Associations
    Director --> UC1
    Director --> UC2
    Director --> UC4
    Director --> UC5
    Director --> UC8

    Manager --> UC3
    Manager --> UC4
    Manager --> UC5

    Analyst --> UC1
    Analyst --> UC5
    Analyst --> UC6
    Analyst --> UC8

    ITAdmin --> UC7
    ITAdmin --> UC9
```

#### Use Case Specification Summary
- **UC-01 (Executive Sales Pulse):** Sales Director reviews national totals, daily pacing, and macro trends.
- **UC-03 (Regional Territory Report):** Regional Manager analyzes territory-specific revenue bounded by RBAC.
- **UC-06 (Data Quality Audit):** Analyst audits the 14% resolved missing region transactions to ensure mapping rule integrity.
- **UC-07 (Ingest & Clean Data):** Automated overnight ETL batch extracts raw billing lines, executes cleaning rules, and updates the analytical data warehouse.

---

### 2.2 Class Diagram (Domain & Subsystem Design)

```mermaid
classDiagram
    %% Core Entities & Domain Model
    class Transaction {
        -String transactionId
        -Date date
        -String customerId
        -String productSku
        -Double amount
        -String rawRegionCode
        -String resolvedRegionCode
        -String cleaningStatus
        +getAmount() Double
        +getResolvedRegion() String
        +setCleaningStatus(String status) void
    }

    class CustomerMaster {
        -String customerId
        -String customerName
        -String postalCode
        -String registeredRegion
        -String assignedSalesRepId
        +lookupRegion() String
    }

    class SalesRepDirectory {
        -String salesRepId
        -String repName
        -String territoryRegion
        +getAssignedRegion() String
    }

    %% ETL Subsystem (Data Cleaning Layer)
    class RegionResolutionEngine {
        -Map~String, String~ postalToRegionLookup
        -Float confidenceThreshold
        +cleanMissingRegions(List~Transaction~ rawBatch) List~Transaction~
        -resolveByPostalCode(String postalCode) String
        -resolveByCustomerMaster(String custId) String
        -resolveBySalesRep(String repId) String
        -flagAsUnassigned(Transaction tx) void
    }

    class AuditLogger {
        -String logSessionId
        +logTransformation(String txId, String ruleUsed, String resolvedRegion) void
        +generateCleaningSummaryReport() AuditReport
    }

    %% Business Logic / Aggregation Layer
    class SalesAggregatorService {
        +computeDailyTotals(Date startDate, Date endDate, String regionFilter) DailyAggregates
        +computeRegionalMatrix(Date period) List~RegionSummary~
        +computeProductRankings(Int topN, Int bottomN) ProductRankingResult
    }

    class QuotaComputationEngine {
        -Map~String, Double~ regionalTargets
        +calculateVariance(Double actual, Double target) VarianceResult
        +getPacingPercentage(Double actual, Double target) Float
    }

    %% Presentation / Controller Layer
    class DashboardController {
        -SalesAggregatorService aggregator
        -QuotaComputationEngine quotaEngine
        -SecurityContext authContext
        +getExecutiveDashboardData(FilterParams params) DashboardDTO
        +getRegionalView(String regionCode, FilterParams params) RegionalDTO
        +exportReport(ExportFormat format) BinaryData
    }

    class UserSession {
        -String userId
        -String role
        -String assignedRegion
        +hasPermission(String resource) Boolean
    }

    %% Relationships
    Transaction --> CustomerMaster : references
    Transaction --> SalesRepDirectory : maps through rep
    RegionResolutionEngine ..> Transaction : processes batch
    RegionResolutionEngine --> AuditLogger : emits audit trails
    SalesAggregatorService ..> Transaction : aggregates cleaned records
    SalesAggregatorService --> QuotaComputationEngine : uses for targets
    DashboardController --> SalesAggregatorService : delegates queries
    DashboardController --> UserSession : enforces RBAC
```

---

### 2.3 Sequence Diagram: "Load Daily Sales and Refresh the Dashboard"

*Demonstrates the complete end-to-end automated sequence from overnight legacy ingestion to executive UI refresh.*

```mermaid
sequenceDiagram
    autonumber
    actor Scheduler as Cron / Batch Scheduler
    participant BillingDB as Legacy Billing System
    participant ETL as ETL Ingestion Service
    participant CleaningEngine as Region Resolution Engine
    participant MasterDB as Customer & Postal Directory
    participant CleanDW as Clean Analytics DataStore
    participant API as SalesLens BI API Service
    actor Director as Sales Director / Client Browser

    %% Trigger Phase
    Note over Scheduler, BillingDB: Overnight Ingestion Trigger (02:00 AM)
    Scheduler ->> ETL: triggerDailyIngestion(Date: Yesterday)
    activate ETL

    %% Extraction Phase
    ETL ->> BillingDB: extractSettledTransactions(Date)
    BillingDB -->> ETL: return rawTransactions (Includes 14% missing regions)

    %% Transformation & Cleaning Phase
    ETL ->> CleaningEngine: cleanAndEnrichBatch(rawTransactions)
    activate CleaningEngine
    
    loop For each missing region transaction (14% subset)
        CleaningEngine ->> MasterDB: queryPostalCode & CustomerMaster(custId)
        MasterDB -->> CleaningEngine: return customer & territory metadata
        CleaningEngine ->> CleaningEngine: apply 4-Tier Resolution Rule
        CleaningEngine ->> CleaningEngine: logTransformationAuditTrail()
    end
    
    CleaningEngine -->> ETL: return cleanedTransactionBatch (100% auditable)
    deactivate CleaningEngine

    %% Loading Phase
    ETL ->> CleanDW: bulkUpsertCleanData(cleanedTransactionBatch)
    CleanDW -->> ETL: acknowledgeLoadSuccess(recordsInserted: 450,000)
    ETL ->> CleanDW: refreshMaterializedAggregates()
    CleanDW -->> ETL: aggregatesRefreshed()
    ETL -->> Scheduler: batchExecutionSuccess(duration: 8.4 mins)
    deactivate ETL

    %% User Interaction Phase (Morning 07:30 AM)
    Note over Director, API: Sales Director Morning Review
    Director ->> API: GET /api/v1/dashboard/executive (Bearer Token)
    activate API
    API ->> API: validateTokenAndRole(Role: Director)
    API ->> CleanDW: fetchAggregates(Period: MTD, Regions: ALL)
    CleanDW -->> API: return aggregatedSalesDTO
    API -->> Director: 200 OK (JSON Payload: KPIs, Targets, Regions, Top SKUs)
    deactivate API
    Director ->> Director: Render Interactive Visualizations in < 1.5s
```

---

### 2.4 Activity Diagram: Data Cleaning & Transformation Pipeline

```mermaid
flowchart TD
    Start([Start Daily ETL Pipeline]) --> ReadRaw[Read Raw Billing Transactions from Legacy DB]
    ReadRaw --> CheckTx{Is Region Code Present?}
    
    CheckTx -- Yes (86% of data) --> ValidateCode[Validate against Standard Region Master]
    ValidateCode --> Standardize[Mark as VALID_DIRECT_ASSIGNMENT]
    
    CheckTx -- No (14% missing data) --> CheckPostal{Is Postal Code Present in Master?}
    CheckPostal -- Yes --> MapPostal[Map Region via Postal Code Table]
    MapPostal --> MarkPostal[Mark as RESOLVED_POSTAL_RULE]
    
    CheckPostal -- No --> CheckCust{Is Customer Master ID Found?}
    CheckCust -- Yes --> MapCust[Map Region from Registered Customer Profile]
    MapCust --> MarkCust[Mark as RESOLVED_CUSTOMER_MASTER]
    
    CheckCust -- No --> CheckRep{Is Sales Rep Assigned?}
    CheckRep -- Yes --> MapRep[Map Region from Sales Rep Territory]
    MapRep --> MarkRep[Mark as RESOLVED_SALES_REP]
    
    CheckRep -- No --> FallbackUnassigned[Assign 'Unassigned-Manual Audit' Code]
    FallbackUnassigned --> FlagAnomaly[Log to Exception Queue for Analyst Review]
    
    Standardize --> MergeBatch[Merge Cleaned Transactions]
    MarkPostal --> MergeBatch
    MarkCust --> MergeBatch
    MarkRep --> MergeBatch
    FlagAnomaly --> MergeBatch
    
    MergeBatch --> ComputeAggs[Compute Daily Sales, Target Variance & SKU Metrics]
    ComputeAggs --> StoreDW[(Store into Clean Analytics Warehouse)]
    StoreDW --> NotifyReady[Emit Refresh Notification & Audit Log]
    NotifyReady --> Finish([Pipeline Finished])
```

---

### 2.5 State Machine Diagram: Sales Data Load Lifecycle

```mermaid
stateDiagram-v2
    [*] --> Idle : System Ready

    Idle --> Extracting : 02:00 AM Cron Event Triggered
    Extracting --> ExtractionFailed : DB Connection Timeout / Error
    ExtractionFailed --> Retrying : Exponential Backoff (Attempt <= 3)
    Retrying --> Extracting : Retry Execution
    Retrying --> IngestionAborted : Max Retries Exceeded -> Send Alert to IT

    Extracting --> RawStaged : Raw Extract Completed

    RawStaged --> CleaningAndResolving : Initiate Region Cleaning Engine
    CleaningAndResolving --> CleaningComplete : 100% Records Processed (Rules 1-4)
    
    CleaningComplete --> Aggregating : Compute Rollups & Quotas
    Aggregating --> LoadedAndIndexed : Persist to Analytics Warehouse

    LoadedAndIndexed --> DashboardLive : Invalidate Cache & Notify API
    DashboardLive --> Idle : Awaiting Next Cycle

    IngestionAborted --> [*]
```

---

### 2.6 Deployment Diagram

```mermaid
flowchart TD
    subgraph Client_Tier [Client Tier - Regional Devices]
        C1[Chrome / Safari / Edge Browser]
    end

    subgraph Application_Tier [Application & Web Tier - Containerized Docker]
        LB[Nginx Reverse Proxy / SSL Terminator]
        WebServer[Node.js / Express Presentation Layer]
        APIService[Analytics API Microservice]
        ETLEngine[Python / Node Data Pipeline Service]
    end

    subgraph Data_Tier [Data & Persistence Tier]
        AnalyticsDB[(PostgreSQL Analytics DW - Partitioned)]
        RedisCache[(Redis Query & Session Cache)]
    end

    subgraph Legacy_Tier [Legacy Corporate Infrastructure]
        LegacyDB[(Legacy Billing & ERP System DB)]
        CustomerMasterFile[Customer Directory & Postal DB]
    end

    C1 <-->|HTTPS / REST API / TLS 1.3| LB
    LB <--> WebServer
    WebServer <--> APIService
    APIService <--> RedisCache
    APIService <--> AnalyticsDB
    
    ETLEngine <-->|Read-Only SQL Extract| LegacyDB
    ETLEngine <-->|Master Lookups| CustomerMasterFile
    ETLEngine -->|Overnight Clean Bulk Load| AnalyticsDB
```

---

## 3. Cohesion and Coupling Architectural Justification

### 3.1 Loose Coupling Justification
1. **Separation of Cleaning Rules from Visualization:**  
   The `RegionResolutionEngine` has zero dependency on the frontend UI or charting library. It takes raw database records, applies deterministic mapping rules, and stores clean relational records. If the sales director later requests a new chart type (e.g., Radar Chart instead of Bar Chart), the data pipeline remains untouched. Conversely, if a new postal code is annexed, only the lookup table is updated without altering dashboard controllers.
2. **Standardized DTO Contract (Interface Segregation):**  
   Communication between the backend and frontend occurs over strict JSON REST interfaces (`DashboardDTO`). UI views never execute raw SQL against the legacy database, preventing schema coupling.
3. **Plug-and-Play Authentication Middleware:**  
   RBAC filters are implemented as decoupled HTTP interceptor middleware. The analytical query services receive an already-sanitized `UserContext` and simply append a `WHERE region = user.assignedRegion` clause if the user is a Regional Manager.

### 3.2 High Cohesion Justification
1. **Functional Cohesion in ETL:**  
   The `RegionResolutionEngine` performs only one logical task: resolving ambiguous geographic indicators to certified regional codes. It does not calculate quotas, render HTML, or authenticate users.
2. **Layered Architectural Cohesion:**  
   - **Data Access Layer:** Exclusively manages database connection pooling, caching, and SQL query execution.
   - **Service Layer:** Exclusively executes business domain calculations (e.g., target variance, compound growth).
   - **Presentation Layer:** Exclusively handles HTTP request parsing, response formatting, and responsive browser rendering.
3. **Maintainability Impact:**  
   Because every class has a single, well-defined responsibility (Single Responsibility Principle), unit testing is straightforward, defect isolation is instantaneous, and regression risks during future upgrades are minimized.

---

*End of Software Design & UML Specification.*
