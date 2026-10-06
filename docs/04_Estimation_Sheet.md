# Software Effort & Duration Estimation Sheet
## Project Name: SalesLens Dashboard Implementation
**Document Version:** 1.0  
**Course:** B.Tech CSE Semester III — Software Engineering & Project Management  
**Prescribed Text:** *Software Engineering* by Ian Sommerville | *Software Project Management* by Bob Hughes & Mike Cotterell

---

## 1. Primary Mathematical Formulas & Parameters

### 1.1 Fundamental Equations
1. **Total Engineering Effort ($E$):**
   $$E = \sum_{i=1}^{n} e_i = E_{\text{cleaning}} + E_{\text{views}} + E_{\text{testing}} + E_{\text{overhead}}$$
   *Where $e_i$ is the individual effort in Person-Days (PD).*

2. **Total Effective Team Capacity ($C$):**
   $$C = \sum_{j=1}^{m} \text{FTE}_j \quad (\text{Person-Days per Calendar Working Day})$$
   - BI Developer: $\text{FTE}_1 = 1.0$ (100% full-time commitment)
   - Data Analyst: $\text{FTE}_2 = 0.5$ (50% part-time commitment)
   $$C = 1.0 + 0.5 = \mathbf{1.5 \text{ Person-Days / Working Day}}$$

3. **Project Working Duration ($D$ in Days):**
   $$D = \frac{E}{C} = \frac{\text{Total Effort (Person-Days)}}{\text{Team Capacity (PD/Day)}}$$

4. **Project Duration in Calendar Weeks ($W$):**
   $$W = \frac{D}{5 \text{ working days/week}}$$

5. **Deadline Compliance Condition:**
   $$\text{Feasible if } W \le W_{\text{deadline}} = 8.0 \text{ Weeks} \quad (D \le 40 \text{ Working Days})$$

---

## 2. Comparative Mathematical Evaluation: 9-View vs. 26-View Scope

```
+----------------------------------------------------------------------------------------------------+
|                               ESTIMATION COMPARISON & DEADLINE CHECK                               |
+----------------------------------------+-----------------------------+-----------------------------+
| Metric / Parameter                     | 9-View In-Scope Dashboard   | Full 26-Report Legacy Scope |
+----------------------------------------+-----------------------------+-----------------------------+
| Number of Dashboard Views ($N$)        | 9 Views                     | 26 Reports                  |
| Effort per View ($e_v$)                | 3.0 Person-Days             | 3.0 Person-Days             |
| Total View Development Effort ($E_v$)  | $9 \times 3.0 = 27.0$ PD    | $26 \times 3.0 = 78.0$ PD   |
| Data Cleaning & Rule Effort ($E_c$)    | 8.0 Person-Days (14% fix)   | 8.0 Person-Days (14% fix)   |
| Verification & QA Testing Effort ($E_t$)| 5.0 Person-Days            | 5.0 Person-Days             |
+----------------------------------------+-----------------------------+-----------------------------+
| TOTAL EFFORT ($E$)                     | **40.0 Person-Days**        | **91.0 Person-Days**        |
| Team Capacity ($C$)                    | 1.5 Person-Days / Day       | 1.5 Person-Days / Day       |
| Total Working Duration ($D = E / C$)   | **26.67 Working Days**      | **60.67 Working Days**      |
| Project Duration in Weeks ($W = D / 5$)| **5.33 Weeks ($\approx 5.4$)**  | **12.13 Weeks ($\approx 12.2$)**|
| Target Deadline ($W_{\text{target}}$)  | 8.00 Weeks (40 Days)        | 8.00 Weeks (40 Days)        |
| Variance to Deadline ($\Delta$)        | **+2.67 Weeks BUFFER**      | **-4.13 Weeks OVERDUE**     |
| Project Feasibility Status             | **PASSED (100% FEASIBLE)**  | **FAILED (UNVIABLE)**       |
+----------------------------------------+-----------------------------+-----------------------------+
```

### 2.1 Step-by-Step Intermediate Calculations

#### Scenario A: The 9-View In-Scope Baseline (Target Solution)
- **Step 1: Calculate View Development Effort**
  $$E_{\text{views}} = 9 \text{ views} \times 3 \text{ PD/view} = 27.0 \text{ Person-Days}$$
- **Step 2: Add Data Cleaning and QA Testing**
  $$E_{\text{total}} = E_{\text{cleaning}} + E_{\text{views}} + E_{\text{testing}} = 8.0 + 27.0 + 5.0 = \mathbf{40.0 \text{ Person-Days}}$$
- **Step 3: Calculate Working Day Duration**
  $$D = \frac{40.0 \text{ PD}}{1.5 \text{ PD/Day}} = 26.666... \approx \mathbf{26.67 \text{ Working Days}}$$
- **Step 4: Convert to Calendar Weeks (at 5 Days/Week)**
  $$W = \frac{26.67}{5} = \mathbf{5.33 \text{ Weeks}} \approx \mathbf{5 \text{ Weeks and } 2 \text{ Days}}$$
- **Step 5: Compute Contingency Reserve Buffer**
  $$\text{Reserve Buffer} = 8.0 \text{ Weeks} - 5.33 \text{ Weeks} = \mathbf{2.67 \text{ Weeks (13.33 Working Days)}}$$
  *Conclusion: The 9-view scope provides a healthy 33% schedule buffer to absorb UAT feedback, buffer the 14% missing data edge cases, and perform launch dry-runs.*

#### Scenario B: The Full 26-Report Unfiltered Scope (Why it must be rejected)
- **Step 1: Calculate View Development Effort**
  $$E_{\text{views}} = 26 \text{ reports} \times 3 \text{ PD/report} = 78.0 \text{ Person-Days}$$
- **Step 2: Add Cleaning and Testing**
  $$E_{\text{total}} = 8.0 + 78.0 + 5.0 = \mathbf{91.0 \text{ Person-Days}}$$
- **Step 3: Compute Working Day Duration**
  $$D = \frac{91.0 \text{ PD}}{1.5 \text{ PD/Day}} = 60.666... \approx \mathbf{60.67 \text{ Working Days}}$$
- **Step 4: Convert to Calendar Weeks**
  $$W = \frac{60.67}{5} = \mathbf{12.13 \text{ Weeks}}$$
- **Step 5: Compare Against 8-Week Deadline**
  $$\text{Deficit} = 8.00 - 12.13 = \mathbf{-4.13 \text{ Weeks (Overdue by 21 Working Days)}}$$
  *Conclusion: Attempting all 26 reports is mathematically impossible under the given constraints without incurring a catastrophic project delay of more than 4 weeks beyond the annual conference.*

---

## 3. Assumptions and Boundary Conditions

To maintain academic rigor and project predictability, the following explicit assumptions are documented:

1. **Standard Working Day Definition:** 1 working day equals 8 productive engineering hours. Overtime is not assumed in the baseline.
2. **Resource Availability & Stability:**
   - The BI Developer is dedicated 100% (40 hours/week) without reassignment to unrelated company fires.
   - The Data Analyst contributes 50% (20 hours/week) focusing on mapping rule verification, master customer directory lookups, and UAT reconciliation.
3. **Data Availability:** Read access to the legacy billing database and customer master files is granted in Week 1 without administrative IT red tape.
4. **Tooling & Infrastructure:** Development environments, container runtimes, and local database instances are provisioned within the first 2 working days.
5. **Requirements Freeze:** The 9 selected views are frozen after Week 1 inception sign-off. Any new feature requests will be channeled into Phase 2 backlog.

---

## 4. Software Engineering Theory: Why an Estimate is an Estimate and Not a Promise

In classical software project management (Sommerville Ch. 23, Hughes & Cotterell Ch. 5), treating an estimate as an inviolable promise is one of the leading causes of project failure.

```
       CONE OF UNCERTAINTY IN SOFTWARE ESTIMATION
      4.0x +      \
           |       \
      2.0x +        \
           |         \
Est.  1.0x +==========*==================== (Final Actual)
Multiplier |         /
      0.5x +        /
           |       /
     0.25x +      /
           +---------------------------------------->
           Initial      Reqs      Detailed   Final
           Concept    Approved     Design   Delivery
```

### 4.1 Theoretical Principles Influencing the Estimate
1. **The Cone of Uncertainty (Boehm, McConnell):**  
   At the initial concept phase, software estimation carries a variance multiplier of $0.25\times$ to $4.0\times$. Only as requirements are refined (such as locking down the 9 views and defining the 4-tier cleaning rule) does the uncertainty narrow to $\pm 10\%$.
2. **Parkinson's Law:**  
   *"Work expands to fill the time available for its completion."* If an unconstrained 8-week buffer is announced without strict intermediate sprint milestones, secondary features can consume buffer time.
3. **Student Syndrome (Goldratt's Critical Chain):**  
   Developers tend to delay intensive execution until the deadline approaches. Enforcing continuous integration and weekly sprint reviews mitigates this behavioral risk.
4. **Brooks' Law (The Mythical Man-Month):**  
   *"Adding manpower to a late software project makes it later."* If the project falls behind, introducing a second developer midway introduces communication overhead ($n(n-1)/2$ channels) and ramp-up friction that would jeopardize the 8-week deadline.
5. **Murphy's Law in Data Pipelines:**  
   *"Anything that can go wrong with legacy data, will go wrong."* The 14% missing region code issue may reveal undocumented edge cases (e.g., malformed zip codes, foreign buyers). The 2.67-week buffer is explicitly reserved to safeguard against these empirical unknowns.

---

*End of Estimation Sheet.*
