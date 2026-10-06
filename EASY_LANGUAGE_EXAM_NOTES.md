# SalesLens — Easy Exam & Viva Preparation Guide (Simple Language)
**Course:** B.Tech CSE Semester III — Software Engineering & Project Management (SEPM)

---

## 🎯 1. What is the Problem in Simple Words?
- **Current Situation:** A consumer goods distributor sends **40-page PDF reports** every Monday to regional managers.
- **The Problem:** 
  1. Two analysts spend their entire weekend building these PDFs manually in Excel.
  2. The numbers between reports **never match** because each analyst uses their own formulas.
  3. **14% of sales transactions have missing region codes** in the billing system.
  4. The analysts **fear losing their jobs** to automation.
- **The Goal:** Build an automated BI dashboard with **daily sales, target quotas, top products, and region comparisons** in **8 weeks** for the Annual Sales Conference.

---

## 🧮 2. The Estimation Math (Super Simple Step-by-Step)

### Given Numbers:
- **Total legacy reports:** 26 reports
- **Reports actually used:** 9 views
- **Effort per view:** 3 person-days
- **14% data cleaning effort:** 8 person-days
- **Testing effort:** 5 person-days
- **Team size:** 1 full-time BI Developer (1.0) + 1 part-time Analyst (0.5) = **1.5 person-days per working day**
- **Deadline:** 8 weeks (40 working days)

---

### Option A: Building All 26 Reports (Why it Fails ❌)
1. View building: $26 \times 3 = 78\text{ person-days}$
2. Add data cleaning: $78 + 8 = 86\text{ person-days}$
3. Add testing: $86 + 5 = \mathbf{91\text{ person-days total effort}}$
4. Duration in working days: $\frac{91}{1.5} = \mathbf{60.67\text{ working days}}$
5. Duration in weeks: $\frac{60.67}{5} = \mathbf{12.13\text{ weeks}}$
6. **Result:** $12.13 > 8\text{ weeks} \rightarrow \mathbf{FAILS\text{ by 4+ weeks!}}$

---

### Option B: Building the 9 Used Views (Why it Succeeds ✅)
1. View building: $9 \times 3 = 27\text{ person-days}$
2. Add data cleaning: $27 + 8 = 35\text{ person-days}$
3. Add testing: $35 + 5 = \mathbf{40\text{ person-days total effort}}$
4. Duration in working days: $\frac{40}{1.5} = \mathbf{26.67\text{ working days}}$
5. Duration in weeks: $\frac{26.67}{5} = \mathbf{5.33\text{ weeks}}\ (\approx 5.4\text{ weeks})$
6. **Result:** $5.33 \le 8\text{ weeks} \rightarrow \mathbf{PASSED\text{ with a 2.67-week (13-day) safety buffer!}}$

> **Exam Tip:** This math mathematically proves why scoping down from 26 to 9 views is strictly necessary!

---

## 🧹 3. How to Clean the 14% Missing Region Data (The 4-Tier Rule)
When an invoice has no region code, the automated engine checks in this priority order:
1. **Rule 1 (Direct):** If region is present (86% of data) $\rightarrow$ Use it directly.
2. **Rule 2 (Postal Code Lookup):** If postal code is known $\rightarrow$ Map to region using the Postal Master Table (resolves ~10% of data).
3. **Rule 3 (Customer Master Lookup):** If postal code is missing, look up Customer ID in the Customer Master profile (resolves ~3% of data).
4. **Rule 4 (Sales Rep Territory):** If customer is new, assign based on the Sales Rep's territory (resolves ~0.7% of data).
5. **Rule 5 (Fallback / Orphan):** If all 3 lookups fail $\rightarrow$ Send to **'Unassigned-Audit Queue'** (~0.3% of data) so total national revenue still reconciles 100%!

---

## 🧪 4. Testing & Quality Assurance Formulas

### 1. Defect Removal Efficiency (DRE)
- **Formula:** 
  $$\text{DRE} = \frac{D_{\text{internal}}}{D_{\text{internal}} + D_{\text{external}}} \times 100\%$$
- **Values:** Internal test lab bugs ($D_{\text{internal}}$) = 17, Bugs found in production/UAT ($D_{\text{external}}$) = 1
- **Calculation:** $\text{DRE} = \frac{17}{17 + 1} \times 100\% = \mathbf{94.44\%}$
- **Meaning:** 94.44% of all bugs were caught and removed before the software was launched (Industry benchmark is $\ge 90\%$).

### 2. Defect Density (DD)
- **Formula:** 
  $$\text{DD} = \frac{\text{Total Defects}}{\text{Size}}$$
- **Per View:** $\frac{17\text{ defects}}{9\text{ views}} = \mathbf{1.89\text{ defects/view}}$
- **Per KLOC:** $\frac{17\text{ defects}}{3.2\text{ KLOC}} = \mathbf{5.31\text{ defects/KLOC}}$ (Normal range is 3 to 8).

---

## 📐 5. Architecture: Cohesion & Coupling Explained Simply
- **High Cohesion (Good 👍):** Every module does **one specific job**.
  - `RegionResolutionEngine`: Only handles postal & address mapping.
  - `QuotaComputationEngine`: Only calculates targets and percentages.
  - `DashboardView`: Only draws the charts.
- **Loose Coupling (Good 👍):** The modules **do not depend heavily on each other**.
  - The Data Cleaning script runs independently overnight.
  - The Dashboard views only ask for data using clean JSON objects (`DashboardDTO`).
  - If the database structure changes, the frontend charts don't crash!

---

## 🛡️ 6. Top 3 Risks & How We Solve Them (RMMM)
1. **14% Missing Region Data ($RE = 20$):** Solved by the 4-tier decision rule and an audit queue.
2. **8-Week Hard Deadline ($RE = 20$):** Solved by cutting out 17 unused reports, saving 51 person-days.
3. **Analysts Fear Being Replaced ($RE = 16$):** Solved by promoting them to **Data Quality Governors & Financial Anomaly Auditors**, saving them from exhausting weekend shifts.

---

## 💻 7. Deliverable Files Overview
- 📄 **[SalesLens_SEPM_Final_Project_Report.pdf](file:///Users/omsawant/Desktop/Software!/SalesLens_SEPM_Final_Project_Report.pdf)** — Complete PDF report ready to submit or print.
- 🌐 **[index.html](file:///Users/omsawant/Desktop/Software!/index.html)** — Live interactive BI Dashboard & Decision Table Simulator (open in browser!).
- 📁 **[docs/](file:///Users/omsawant/Desktop/Software!/docs/)** — Complete IEEE 830 SRS, UML Diagrams, CPM Network, Estimation Sheet, QA Plan, and Risk Register.
