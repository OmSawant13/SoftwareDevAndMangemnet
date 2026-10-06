# Software Testing & Quality Assurance Plan
## Project Name: SalesLens - Unified Sales Reporting Dashboard
**Document Version:** 1.0  
**Course:** B.Tech CSE Semester III — Software Engineering & Project Management  
**Prescribed Text:** *Software Testing* by Ron Patton | *Software Engineering* by Ian Sommerville

---

## 1. Quality Assurance Strategy & Scope

The testing strategy follows the **V-Model of Software Development**, ensuring verification and validation at every layer:
1. **Unit Testing:** Validates mathematical calculations (quotas, variances, percentage pacing) and data cleaning functions.
2. **Integration Testing:** Validates data pipeline transformations between the Legacy Billing DB, ETL Cleaning Engine, and Analytical DataStore.
3. **Black-Box Functional Testing:** Evaluates system behavior using Boundary Value Analysis (BVA), Equivalence Class Partitioning (ECP), and Decision Tables.
4. **Security & RBAC Verification:** Ensures non-leakage of territorial data across unauthorized regional roles.
5. **Performance Testing:** Evaluates sub-1.5s query response times and ETL pipeline duration.

---

## 2. Test Design Techniques

### 2.1 Boundary Value Analysis (BVA)

#### A. Field: `Sales Transaction Amount` ($)
- **Specification:** The system accepts positive billing transactions from $\$0.01$ up to $\$1,000,000.00$ per line item. Zero or negative values represent refunds/credit memos requiring special tagging. Amounts exceeding $\$1,000,000.00$ require executive audit flags.
- **Boundaries:** $[0.00, 0.01, 0.02, \dots, 999999.99, 1000000.00, 1000000.01]$

```
+---------+--------------------+------------------------+-------------------------------+
| Test ID | Input Value ($)    | Boundary Category      | Expected System Behavior      |
+---------+--------------------+------------------------+-------------------------------+
| BVA-A1  | -0.01              | Just below Min-1       | Reject: Invalid Negative Value|
| BVA-A2  | 0.00               | Minimum Boundary (0)   | Flag: Zero-Dollar Promo Item  |
| BVA-A3  | 0.01               | Min Valid (Min)        | Accept: Process as Small Sale |
| BVA-A4  | 0.02               | Just above Min (Min+1) | Accept: Normal Processing     |
| BVA-A5  | 500,000.00         | Nominal Midpoint       | Accept: Normal Processing     |
| BVA-A6  | 999,999.99         | Just below Max (Max-1) | Accept: Normal Processing     |
| BVA-A7  | 1,000,000.00       | Maximum Boundary (Max) | Accept: Max Single Invoice    |
| BVA-A8  | 1,000,000.01       | Just above Max (Max+1) | Accept: Flag for Exec Audit   |
+---------+--------------------+------------------------+-------------------------------+
```

#### B. Field: `Date Range Filter` (Selection Interval)
- **Specification:** Historical date picker accepts transactions from Company Inception ($2020-01-01$) to Yesterday ($T-1$). Future dates ($T+1$) and inverted ranges ($Start > End$) are rejected. Leap days ($Feb 29$) must resolve correctly.

```
+---------+--------------------------+-------------------+------------------------------+
| Test ID | Input Date Range         | Boundary Type     | Expected Behavior            |
+---------+--------------------------+-------------------+------------------------------+
| BVA-B1  | 2019-12-31 to 2020-01-01 | Below Lower Bound | Reject: Pre-inception date   |
| BVA-B2  | 2020-01-01 to 2020-01-01 | Lower Bound (Day1)| Accept: 1-Day Oldest Range   |
| BVA-B3  | 2024-02-28 to 2024-02-29 | Leap Year Boundary| Accept: Processes Leap Day   |
| BVA-B4  | Today to Today           | Today (Partial)   | Accept: Warn (Unsettled day) |
| BVA-B5  | Tomorrow (T+1)           | Future Date       | Reject: Future Date Disabled |
| BVA-B6  | 2026-10-15 to 2026-10-01 | Inverted Range    | Reject: Auto-flip or Error   |
+---------+--------------------------+-------------------+------------------------------+
```

---

### 2.2 Equivalence Class Partitioning (ECP)

#### Parameter: `User Role & Regional Data Access`
- **Valid Partitions:**
  - $EP_1$: Role = `Sales Director` $\rightarrow$ National Access (All Regions: North, South, East, West, Central).
  - $EP_2$: Role = `Regional Manager` $\rightarrow$ Single Assigned Region (e.g., North only).
  - $EP_3$: Role = `Data Analyst` $\rightarrow$ National Access + Audit Queue Access.
- **Invalid Partitions:**
  - $EP_4$: Role = `Unauthenticated User` $\rightarrow$ HTTP 401 Unauthorized.
  - $EP_5$: Role = `Regional Manager` with forged JWT payload requesting foreign region $\rightarrow$ HTTP 403 Forbidden.

---

### 2.3 Decision Table for 14% Missing Region Code Cleaning Rules

The core business challenge is that **14% of transactions lack a region code in the legacy billing system**. A deterministic 4-tier decision table is designed and tested to eliminate analyst discrepancies:

```
+-------------------------------------------------------+----+----+----+----+----+----+----+----+
| CONDITIONS / INPUT ATTRIBUTES                          | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 |
+-------------------------------------------------------+----+----+----+----+----+----+----+----+
| C1: Is Raw Region Code present in billing line item?  | Y  | N  | N  | N  | N  | N  | N  | N  |
| C2: Is Postal Code mapped in Postal-Region Master?    | -  | Y  | Y  | Y  | N  | N  | N  | N  |
| C3: Is Customer Master record with region found?      | -  | Y  | N  | -  | Y  | Y  | N  | N  |
| C4: Is Active Sales Rep assigned to territory?        | -  | -  | -  | -  | Y  | N  | Y  | N  |
+-------------------------------------------------------+----+----+----+----+----+----+----+----+
| ACTIONS / RESOLUTION OUTCOME                          |    |    |    |    |    |    |    |    |
+-------------------------------------------------------+----+----+----+----+----+----+----+----+
| A1: Use Direct Raw Region Code                        | X  |    |    |    |    |    |    |    |
| A2: Map Region via Postal Code Table (Priority 1)     |    | X  | X  | X  |    |    |    |    |
| A3: Map Region via Customer Master Profile (Priority2)|    |    |    |    | X  | X  |    |    |
| A4: Map Region via Sales Rep Territory (Priority 3)   |    |    |    |    |    |    | X  |    |
| A5: Assign to 'Unassigned-Audit Queue' (Fallback)     |    |    |    |    |    |    |    | X  |
| A6: Emit Transformation Audit Log Entry               |    | X  | X  | X  | X  | X  | X  | X  |
+-------------------------------------------------------+----+----+----+----+----+----+----+----+
```

*Rule Analysis:*
- **Rule 1:** 86% of transactions have native valid region codes $\rightarrow$ Direct pass-through.
- **Rules 2–4:** Missing region, but postal code matches $\rightarrow$ Resolved instantly via postal directory (covers $\approx 10\%$ of total data).
- **Rules 5–6:** Missing region and invalid postal code, but customer ID exists $\rightarrow$ Resolved via customer master (covers $\approx 3\%$ of total data).
- **Rule 7:** Fallback to assigned sales rep territory (covers $\approx 0.7\%$ of total data).
- **Rule 8:** True orphan transaction $\rightarrow$ Safely routed to the 'Unassigned-Audit Queue' ($\approx 0.3\%$ of total data) so totals reconcile with 100% financial auditability without dropping revenue.

---

## 3. Comprehensive Test Case Log (TC-01 to TC-10)

| Test ID | Test Case Title | Input Data / Precondition | Test Steps | Expected Output | Status |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **TC-01** | Daily Sales Revenue Reconciliation | 50,000 settled transactions in billing DB ($1.25M) | Run overnight ETL; Query Executive View | Dashboard revenue displays $\$1,250,000.00 \pm 0.00$ | **PASS** |
| **TC-02** | Target Quota Variance Computation | Target = $\$500,000$, Actual = $\$450,000$ | Load View 2 for North Region | Variance shows $-\$50,000$ ($90.0\%$ attainment, Red status) | **PASS** |
| **TC-03** | Top 20 SKU Ranking Verification | Catalog of 1,200 SKUs with sales | Load View 3; Apply Top 20 filter | Exactly 20 highest-revenue SKUs in descending order | **PASS** |
| **TC-04** | Regional Manager RBAC Isolation | Log in as Manager `North_User` | Navigate to Region Deep-Dive View | Only North Region data visible; other regions blocked | **PASS** |
| **TC-05** | Missing Region Resolution via Postal | Transaction missing region, Postal = `110001` | Execute ETL Cleaning Engine | Assigned to `North Region` with confidence flag | **PASS** |
| **TC-06** | Orphan Transaction Fallback | Transaction missing region, postal & customer | Execute ETL Cleaning Engine | Assigned to `Unassigned-Audit`; Revenue included in National | **PASS** |
| **TC-07** | Custom Date Range Boundary Test | Select Range: `2026-01-01` to `2026-09-30` | Click Apply Filters on Dashboard | All KPIs recalculate in $< 1.2$s for selected 9 months | **PASS** |
| **TC-08** | Data Quality Audit Console | 500 cleaned missing region records | Open View 9 as Data Analyst | Displays 500 rows with before/after audit trail | **PASS** |
| **TC-09** | Executive PDF Briefing Export | View 1 Executive Pulse loaded | Click 'Export Executive PDF' | Generates valid 1-page PDF summary in $< 2.0$s | **PASS** |
| **TC-10** | High Concurrency Load Test | 50 virtual users executing simultaneous queries | JMeter 50-thread ramp up over 30s | Average response time $1.15$s; 0% HTTP 500 errors | **PASS** |

---

## 4. Software Quality Metrics: Defect Density & DRE

### 4.1 Defect Density Calculation
Defect Density measures the number of confirmed defects per unit size of software (Sommerville Ch. 24, Patton Ch. 20).

$$\text{Defect Density } (DD) = \frac{\text{Total Number of Confirmed Defects}}{\text{Software Size}}$$

#### Project Size Metric:
- **Size in Dashboard Views ($N_v$):** 9 Views.
- **Equivalent Size in Function Points ($FP$):** $180\text{ FP}$ (or $\approx 3.2\text{ KLOC}$ of modular Javascript/Python code).

#### Test Log Defect Summary:
- Requirements / Rule Ambiguity Defects: $4$
- ETL Cleaning & Mapping Logic Defects: $6$
- Frontend UI / Filter State Defects: $5$
- Performance / Query Latency Defects: $2$
- **Total Defects Discovered during Internal Testing ($D_{\text{internal}}$):** **17 Defects**.

#### Calculation:
$$DD_{\text{views}} = \frac{17 \text{ Defects}}{9 \text{ Views}} = \mathbf{1.89 \text{ Defects / View}}$$
$$DD_{\text{KLOC}} = \frac{17 \text{ Defects}}{3.2 \text{ KLOC}} = \mathbf{5.31 \text{ Defects / KLOC}}$$
*(Industry standard for commercial BI systems is $3.0 - 8.0 \text{ Defects/KLOC}$, confirming rigorous internal test depth).*

---

### 4.2 Defect Removal Efficiency (DRE) Calculation
DRE measures how effectively the verification and testing process filters out defects before software reaches production (Pressman Ch. 26).

$$\text{Defect Removal Efficiency } (DRE) = \left( \frac{D_{\text{internal}}}{D_{\text{internal}} + D_{\text{external}}} \right) \times 100\%$$

Where:
- $D_{\text{internal}}$ = Defects found during development, unit testing, integration testing, and internal QA = **17 Defects**.
- $D_{\text{external}}$ = Defects found by end-users during final UAT / Production pilot = **1 Defect** (minor date formatting glitch on iPad Safari).

#### Calculation:
$$DRE = \left( \frac{17}{17 + 1} \right) \times 100\% = \left( \frac{17}{18} \right) \times 100\% = \mathbf{94.44\%}$$

### 4.3 Interpretation & Quality Evaluation
- A DRE of **$94.44\%$** exceeds the industry benchmark standard of $90.0\%$ for enterprise software.
- This high efficiency proves that the 4-tier decision table and boundary value tests caught virtually all data mapping discrepancies internally, protecting the sales director and regional managers from data errors during the Annual Sales Conference.

---

*End of Testing & QA Plan.*
