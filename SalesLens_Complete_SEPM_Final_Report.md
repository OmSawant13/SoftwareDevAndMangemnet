# B.Tech CSE Semester III — Final Project Submission
# Course: Software Engineering & Project Management
## Project Title: SalesLens — Unified Sales Reporting & Business Intelligence Platform for Consumer Goods Distribution

---

## Executive Summary

**SalesLens** is an enterprise-grade Business Intelligence and Automated Reporting solution developed for a regional consumer goods distributor. It directly addresses severe operational deficiencies where sales leadership received weekly 40-page static PDF reports compiled manually over weekends by two exhausted analysts. Discrepancies in personal calculation rules frequently caused conflicting figures, while 14% of raw billing transactions lacked regional attribution.

By applying core Software Engineering principles (IEEE 830 SRS, UML Modeling, V-Model QA with BVA and Decision Tables) and Project Management methodologies (WBS, Critical Path Method, COCOMO/Effort Estimation, and RMMM Risk Management), this project proves that **pruning the legacy catalog from 26 reports to 9 high-value views reduces development effort from 91 person-days (12.2 weeks) to 40 person-days (5.4 weeks)**, successfully meeting the Sales Director's strict **8-week Annual Sales Conference deadline** with a 2.67-week buffer.

---

## Key Academic Modules & Deliverables Index

```
SalesLens Project Repository Structure:
├── index.html                           -> Live Interactive 9-View BI Dashboard & SEPM Explorer
├── styles.css                           -> Modern Glassmorphic Dark/Light CSS Design System
├── app.js                               -> Chart.js Visualizations & 14% Cleaning Rule Simulator
├── docs/
│   ├── 01_IEEE_830_SRS.md               -> Complete IEEE 830 SRS with 10 FRs & 7 Measurable NFRs
│   ├── 02_UML_Design_Document.md        -> Complete UML Package (Use Case, Class, Seq, Act, State, Dep)
│   ├── 03_Project_Plan_CPM_Gantt.md     -> WBS, CPM Calculations, Precedence Table & Gantt Chart
│   ├── 04_Estimation_Sheet.md           -> Mathematical Effort, Duration & 9 vs 26 View Proofs
│   ├── 05_Testing_QA_Plan.md            -> BVA, 4-Tier Decision Table, DRE (94.4%) & Defect Density
│   └── 06_Risk_Register_RMMM_Closure.md -> Risk Register (P x I), RMMM Top 3 & Historical Issue Log
└── SalesLens_Complete_SEPM_Final_Report.md -> This Master Unified Report
```

---

## 1. Requirements Engineering (Module II Syllabus)

### 1.1 Stakeholder Elicitation Summary
- **Sales Director:** Requires national sales pulse, quota pacing, comparative regional matrix, and top product drivers.
- **Regional Managers (5 Zones):** Require territory drill-downs and pacing vs target under strict Role-Based Access Control (RBAC).
- **Data Analysts:** Replaced manual weekend report compilation with automated ETL and automated 14% data cleaning audit queues.
- **IT Admin:** Requires overnight batch jobs under 15 minutes, zero downtime on transactional billing DB, and strict data security.

### 1.2 The 7 Measurable Non-Functional Requirements (NFRs)
1. **Data Accuracy (NFR-01):** Reconciled revenue on dashboard $\ge 99.90\%$ matching settled billing totals ($\text{variance} \le \$10.00 \text{ per } \$1\text{M}$).
2. **Refresh Window (NFR-02):** Automated overnight ETL execution $\le 15$ minutes, completing before 06:00 AM daily.
3. **UI Latency (NFR-03):** 95th percentile query latency $P_{95} \le 1.50$ seconds; initial load $\le 3.0$ seconds.
4. **Security & RBAC (NFR-04):** Zero cross-territory data leakage across $10,000$ automated penetration assertions.
5. **System Availability (NFR-05):** $\ge 99.50\%$ uptime during core hours ($06:00 - 22:00$ Mon–Sat).
6. **Concurrency (NFR-06):** Support $\ge 50$ simultaneous active managers without $>10\%$ latency surge.
7. **Disaster Recovery (NFR-07):** $\text{RPO} \le 24$ hours (daily snapshots) and $\text{RTO} \le 60$ minutes.

---

## 2. Software Design & UML Architecture (Module III Syllabus)

- **Architecture:** Layered Service-Oriented Model-View-Controller (MVC) with asynchronous ETL Pipeline subsystem.
- **Low Coupling Justification:** The Data Cleaning Engine (`RegionResolutionEngine`) operates entirely independently of presentation views. Data flows via standardized JSON DTOs (`DashboardDTO`).
- **High Cohesion Justification:** Each module exhibits single-responsibility cohesion: ETL reconciles geography; Quota Engine computes variance; Controllers manage UI state.

---

## 3. Project Estimation & Feasibility Proof (Module V Syllabus)

### 3.1 Given Project Parameters
- **Effort per View ($e_v$):** 3.0 Person-Days (PD).
- **Data Cleaning Effort ($E_c$):** 8.0 Person-Days (resolving 14% missing region codes).
- **Testing Effort ($E_t$):** 5.0 Person-Days.
- **Team Composition:** 1 BI Developer (1.0 FTE) + 1 Analyst (0.5 FTE) = **1.5 PD / Working Day**.
- **Deadline:** 8 Weeks = **40 Working Days**.

### 3.2 Mathematical Proof (9 Views vs. 26 Views)

$$\text{Effort}_{9\text{ Views}} = 8.0 (\text{Clean}) + (9 \times 3.0) + 5.0 (\text{Test}) = \mathbf{40.0 \text{ Person-Days}}$$
$$\text{Duration}_{9\text{ Views}} = \frac{40.0}{1.5} = \mathbf{26.67 \text{ Working Days}} = \mathbf{5.33 \text{ Weeks}} \quad (\le 8.0 \text{ Weeks} \implies \mathbf{FEASIBLE})$$

$$\text{Effort}_{26\text{ Reports}} = 8.0 + (26 \times 3.0) + 5.0 = \mathbf{91.0 \text{ Person-Days}}$$
$$\text{Duration}_{26\text{ Reports}} = \frac{91.0}{1.5} = \mathbf{60.67 \text{ Working Days}} = \mathbf{12.13 \text{ Weeks}} \quad (> 8.0 \text{ Weeks} \implies \mathbf{UNFEASIBLE})$$

---

## 4. Testing, QA & Quality Metrics (Module IV Syllabus)

### 4.1 Defect Removal Efficiency (DRE)
$$DRE = \left( \frac{D_{\text{internal}}}{D_{\text{internal}} + D_{\text{external}}} \right) \times 100\% = \left( \frac{17}{17 + 1} \right) \times 100\% = \mathbf{94.44\%} \quad (\text{Benchmark} \ge 90\%)$$

### 4.2 Defect Density (DD)
$$DD_{\text{views}} = \frac{17 \text{ Defects}}{9 \text{ Views}} = \mathbf{1.89 \text{ Defects / View}}$$
$$DD_{\text{KLOC}} = \frac{17 \text{ Defects}}{3.2 \text{ KLOC}} = \mathbf{5.31 \text{ Defects / KLOC}}$$

---

## 5. Risk Management & RMMM Summary (Module V Syllabus)

- **Risk 1 (14% Missing Region Codes, $RE=20$):** Mitigated via 4-tier decision table and exception audit queue.
- **Risk 2 (8-Week Conference Deadline, $RE=20$):** Mitigated by pruning scope from 26 to 9 views (saving 51 person-days).
- **Risk 3 (Analyst Resistance/Fear of Replacement, $RE=16$):** Mitigated by upskilling analysts to Data Quality Governors.

---
*Submitted for B.Tech CSE Semester III Examination.*
