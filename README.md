# SoftwareDevAndMangemnet

# SalesLens — Sales Reporting & Analytics Dashboard for Consumer Goods Distributor
### B.Tech CSE (2025–2029) — Semester III | Software Engineering & Project Management (SEPM)

---

## 📌 Problem Statement
A consumer goods distributor's regional sales managers received weekly sales reports as **40-page PDF files every Monday**, prepared manually by two analysts over weekends. Numbers often differed between reports because each analyst applied different calculation rules. Furthermore, **14% of transactions lacked region codes**. 

The Sales Director required a single automated, interactive web dashboard featuring daily sales, quota targets, top/bottom products, and 5-zone regional comparisons, delivered within **8 weeks** for the Annual Sales Conference.

---

## 🚀 Key SEPM Deliverables & Project Scope

1. **IEEE 830 Software Requirements Specification (SRS):**
   * **10 Functional Requirements (FR-01 to FR-10):** Daily sales aggregation, quota tracking, top/bottom SKUs, regional matrix, 14% cleaning rules, and RBAC.
   * **7 Measurable NFRs:** $\ge 99.90\%$ data accuracy, $\le 15$ min ETL refresh, P95 query $\le 1.50$s, 100% RBAC isolation, $\ge 99.50\%$ uptime.
   * **MoSCoW Prioritization & Requirements Traceability Matrix (RTM).**

2. **Software Design & UML Architecture Package:**
   * **Use Case Diagram:** Actors (Director, Regional Managers, Data Analyst, IT Admin) and system boundary.
   * **Class Diagram:** Domain entities, DTO interfaces, enforcing **High Cohesion** and **Loose Coupling**.
   * **Sequence Diagram:** Detailed trace for *"Load daily sales and refresh the dashboard"*.
   * **Activity & State Diagrams:** 4-Tier fallback decision tree for 14% missing data and ETL lifecycle.
   * **3-Tier Physical Deployment Diagram.**

3. **Project Plan, Critical Path Method (CPM) & Gantt Scheduling:**
   * Complete **Work Breakdown Structure (WBS)**.
   * **CPM Precedence Matrix:** Critical Path $A \rightarrow C \rightarrow D \rightarrow E \rightarrow F \rightarrow G \rightarrow H \rightarrow I \rightarrow J \rightarrow K$.
   * **Schedule Optimization:** Fast-tracking reduces duration to **39.0 working days (7.8 weeks)**, meeting the 8-week deadline with 2 days buffer reserve.

4. **Mathematical Estimation & Resource Sizing:**
   * **Effort Analysis:** 26 reports ($78\text{ person-days}$) reduced to 9 used views ($27\text{ person-days}$), saving 51 person-days.
   * **Total Effort:** $27\text{ (views)} + 8\text{ (cleaning)} + 5\text{ (testing)} = \mathbf{40\text{ Person-Days}}$.
   * **Team Capacity:** 1 BI Dev (1.0 FTE) + 1 Analyst (0.5 FTE) = **1.5 Person-Days / Working Day**.
   * **Software Engineering Laws:** Cone of Uncertainty, Brooks' Law, and Parkinson's Law.

5. **Testing, Quality Assurance & Formal Quality Metrics:**
   * **Boundary Value Analysis (BVA):** Sales amount ($-\$0.01, \$0.00, \$1.00, \$1\text{M}$) and date-range boundaries.
   * **Decision Table:** 5-rule deterministic mapping for 14% missing region codes.
   * **Defect Removal Efficiency (DRE):** $\text{DRE} = \frac{68}{68 + 4} \times 100\% = \mathbf{94.44\%}$.
   * **Defect Density:** $\frac{68\text{ defects}}{50\text{ KLOC}} = \mathbf{1.36\text{ defects / KLOC}}$.

6. **Risk Management & RMMM:**
   * 5x5 Exposure Heatmap Matrix ($E = P \times I$).
   * Risk Mitigation, Monitoring & Management (RMMM) for Top 3 Risks.
   * Distinct Historical Issue Log ($P = 1.0$) and Project Closure Note.

---

## 📁 Repository Structure

```
├── SalesLens_Complete_UI_Walkthrough.pdf   # 9-Page Master UI Showcase PDF
├── SalesLens_SEPM_Final_Project_Report.pdf # Comprehensive Master SEPM Academic Report PDF
├── index.html                              # Interactive 9-View Web Platform
├── styles.css                              # Glassmorphic Dark/Light CSS Design System
├── app.js                                  # Chart.js Visualizations & 14% Cleaning Simulator
├── saleslens_ui_and_sepm_master_showcase.html # HTML Source for Showcase PDF
│
├── pdf_deliverables/                       # All 8 Individual & Master PDF Deliverables
│   ├── 01_SRS_Document.pdf
│   ├── 02_UML_Architecture_Design.pdf
│   ├── 03_Project_Plan_CPM_Gantt.pdf
│   ├── 04_Estimation_Sheet.pdf
│   ├── 05_Testing_QA_Plan.pdf
│   ├── 06_Risk_Register_and_Closure.pdf
│   ├── SalesLens_Complete_UI_Walkthrough.pdf
│   └── SalesLens_SEPM_Final_Project_Report.pdf
│
├── docs/                                   # Detailed Markdown Deliverables
│   ├── 01_IEEE_830_SRS.md
│   ├── 02_UML_Design_Document.md
│   ├── 03_Project_Plan_CPM_Gantt.md
│   ├── 04_Estimation_Sheet.md
│   ├── 05_Testing_QA_Plan.md
│   └── 06_Risk_Register_RMMM_Closure.md
│
├── screenshots/                            # 15 High-Resolution Diagram & UI Screen Captures
└── EASY_LANGUAGE_EXAM_NOTES.md             # Rapid Exam Revision Notes
```

---

## 💻 How to Run Locally

Open `index.html` in any modern browser:
```bash
open index.html
```
Or serve via Python HTTP server:
```bash
python3 -m http.server 8080
```
Then visit `http://localhost:8080` in your web browser.
