# Risk Management, RMMM, Issue Log & Project Closure
## Project Name: SalesLens Dashboard Implementation
**Document Version:** 1.0  
**Course:** B.Tech CSE Semester III — Software Engineering & Project Management  
**Prescribed Text:** *Software Engineering* by Ian Sommerville | *Software Project Management* by Bob Hughes & Mike Cotterell

---

## 1. Risk Register & Exposure Matrix

Risk Exposure ($RE$) is computed using the standard formula:
$$RE = \text{Probability } (P) \times \text{Impact } (I)$$
*Scale: Probability (1 = Very Low to 5 = Very High) | Impact (1 = Negligible to 5 = Critical / Project Killer).*

```
+----+--------------------------------------------+---+---+----+------+-----------------------------+---------------+
| ID | Risk Description                           | P | I | RE | Rank | Risk Response Strategy      | Risk Owner    |
+----+--------------------------------------------+---+---+----+------+-----------------------------+---------------+
| R1 | 14% Missing Region Data Cleaning Complexity| 4 | 5 | 20 | **1**| Mitigate (4-Tier Rule Engine)| BI Dev / Analy|
| R2 | Annual Sales Conference Deadline (8 Weeks) | 4 | 5 | 20 | **2**| Mitigate (Strict 9-View Cut)| Project Mgr   |
| R3 | Analyst Fear of Replacement / Resistance   | 4 | 4 | 16 | **3**| Mitigate (Upskill to QA/Gov)| Sales Director|
| R4 | Legacy Billing System Schema Inconsistency | 3 | 4 | 12 | **4**| Avoid (Read-Only ETL Staging)| IT Systems Adm|
| R5 | Scope Creep from Regional Managers (Extra) | 3 | 4 | 12 | **5**| Avoid (Formal Change Control)| Project Mgr   |
| R6 | Performance Bottleneck on Large Queries    | 2 | 4 |  8 | **6**| Mitigate (Pre-agg Material) | BI Developer  |
| R7 | Single Point of Failure (1 BI Developer)   | 2 | 4 |  8 | **7**| Mitigate (Clean Code / Docs) | Tech Lead     |
| R8 | User Adoption Reluctance vs Legacy 40p PDF | 2 | 3 |  6 | **8**| Accept (Interactive Training)| Data Analyst  |
+----+--------------------------------------------+---+---+----+------+-----------------------------+---------------+
```

---

## 2. Risk Mitigation, Monitoring, and Management (RMMM) for Top 3 Risks

### 2.1 Risk 1: 14% Missing Region Data Cleaning Complexity ($RE = 20$)
- **Mitigation (Pre-emptive Action):**
  - Formulate an unambiguous 4-tier waterfall resolution hierarchy (Postal Code $\rightarrow$ Customer Master $\rightarrow$ Sales Rep $\rightarrow$ Unassigned Queue) in Week 1 with the senior data analyst.
  - Implement automated confidence scoring and transformation logging for every cleaned record.
- **Monitoring (Early Warning Signs):**
  - Daily monitoring of unassigned record percentage. If unassigned records exceed $1.0\%$ after applying rules, trigger an immediate postal dictionary lookup audit.
- **Management (Contingency Action if Triggered):**
  - Route remaining ambiguous transactions to a dedicated 'Unassigned-Audit View' on the dashboard. This ensures top-line national revenue matches billing totals without distorting regional quotas.

---

### 2.2 Risk 2: Annual Sales Conference 8-Week Hard Deadline ($RE = 20$)
- **Mitigation (Pre-emptive Action):**
  - Strictly constrain the implementation scope from the 26 legacy reports down to the 9 high-value operational views. This saves 51 person-days and provides a 2.67-week buffer.
  - Adopt iterative 1-week sprint cadence with live working prototypes shown to the Sales Director every Friday.
- **Monitoring (Early Warning Signs):**
  - Weekly tracking of Earned Value Management (EVM) metrics: Schedule Performance Index ($SPI = EV/PV$). If $SPI < 0.90$, initiate fast-tracking.
- **Management (Contingency Action if Triggered):**
  - If unexpected ETL delays occur, deploy Phase 1 with the top 6 core views (Views 1–6) for the conference stage showcase, delivering the remaining 3 analytical views in a post-conference patch.

---

### 2.3 Risk 3: Analyst Fear of Replacement & Stakeholder Resistance ($RE = 16$)
- **Mitigation (Pre-emptive Action):**
  - The Sales Director conducts a 1-on-1 realignment meeting in Week 1, positioning SalesLens not as a replacement, but as an automation tool that eliminates exhausting weekend manual spreadsheet assembly.
  - Formally transition the analysts' roles to **High-Value Data Quality Governors, Financial Strategists, and Anomaly Auditors**.
- **Monitoring (Early Warning Signs):**
  - Reluctance during requirements walkthroughs, delays in providing postal mapping rules, or low attendance at sprint demos.
- **Management (Contingency Action if Triggered):**
  - Involve the analyst as the primary co-owner and presenter of View 9 (Data Quality Console) at the Annual Sales Conference, giving them public leadership visibility.

---

## 3. Historical Issue Log (Known Past Problems)

*In SEPM methodology, Risks are future uncertainties, whereas Issues are existing, materialized problems requiring immediate remediation.*

```
+--------+------------------------------------+---------------+---------------------------------+-----------+
| Issue# | Materialized Problem Description   | Date Incurred | Root Cause                      | Status    |
+--------+------------------------------------+---------------+---------------------------------+-----------+
| ISS-01 | Regional managers receive differing| Pre-Project   | Each analyst applies different  | RESOLVED  |
|        | sales numbers for the same week.   | (Historical)  | ad-hoc Excel formulas manually. | via FR-01 |
+--------+------------------------------------+---------------+---------------------------------+-----------+
| ISS-02 | Weekend analyst burnout preparing  | Pre-Project   | 16+ hours spent every weekend   | RESOLVED  |
|        | 40-page static PDF documents.      | (Historical)  | manually compiling static pages.| via ETL   |
+--------+------------------------------------+---------------+---------------------------------+-----------+
| ISS-03 | 14% of billing transactions lack   | Pre-Project   | Legacy billing UI does not make | RESOLVED  |
|        | region codes, causing distortions. | (Historical)  | region code a mandatory field.  | via Rule  |
+--------+------------------------------------+---------------+---------------------------------+-----------+
| ISS-04 | IT billing system query overload   | Pre-Project   | Ad-hoc daytime queries crashed  | RESOLVED  |
|        | during active business hours.      | (Historical)  | operational invoicing engine.   | via Rep   |
+--------+------------------------------------+---------------+---------------------------------+-----------+
```

---

## 4. Project Closure & Lessons Learned

### 4.1 Key Success Factors
1. **Scope Pruning Saved the Project:** Reducing the scope from 26 legacy reports to 9 active views was the single most impactful architectural decision, cutting development time by 56% and guaranteeing on-time launch.
2. **Deterministic Rules Over Subjective Spreadsheets:** Codifying the 4-tier region resolution table into code eliminated 100% of the historical report variances.
3. **Inclusive Stakeholder Management:** Transitioning analysts into data governors converted potential organizational resistance into strong internal advocacy.

### 4.2 Post-Mortem Recommendations for Future Phases
- **Phase 2 Roadmap:** Implement Automated Push Email Digests (FR-10), predictive demand forecasting using ML regression, and mobile-native iOS/Android applications for on-the-road sales reps.

---

*End of Risk Management & Closure Specification.*
