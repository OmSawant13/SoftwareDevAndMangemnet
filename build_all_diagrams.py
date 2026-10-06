import os
import math
from PIL import Image, ImageDraw, ImageFont

def get_font(size=14, bold=False):
    font_paths = [
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/SFNSText.ttf",
        "/Library/Fonts/Arial.ttf",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Geneva.ttf"
    ]
    for p in font_paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, int(size))
            except Exception:
                pass
    return ImageFont.load_default()

def draw_rounded_rect(draw, coords, radius=8, fill=None, outline=None, width=1):
    x1, y1, x2, y2 = coords
    draw.rounded_rectangle([int(x1), int(y1), int(x2), int(y2)], radius=int(radius), fill=fill, outline=outline, width=int(width))

def draw_arrow(draw, start, end, color="#1e3a8a", width=2, arrow_size=6):
    x1, y1 = start
    x2, y2 = end
    draw.line([(int(x1), int(y1)), (int(x2), int(y2))], fill=color, width=int(width))
    angle = math.atan2(y2 - y1, x2 - x1)
    x3 = x2 - arrow_size * math.cos(angle - math.pi / 6)
    y3 = y2 - arrow_size * math.sin(angle - math.pi / 6)
    x4 = x2 - arrow_size * math.cos(angle + math.pi / 6)
    y4 = y2 - arrow_size * math.sin(angle + math.pi / 6)
    draw.polygon([(int(x2), int(y2)), (int(x3), int(y3)), (int(x4), int(y4))], fill=color)

def build_diagrams():
    out_dir = "/Users/omsawant/Desktop/Software!/screenshots"
    os.makedirs(out_dir, exist_ok=True)
    
    font_title = get_font(20, bold=True)
    font_h2 = get_font(14, bold=True)
    font_body = get_font(12, bold=False)
    font_bold = get_font(12, bold=True)
    font_small = get_font(10, bold=False)
    font_small_bold = get_font(10, bold=True)
    
    # -------------------------------------------------------------
    # 1. USE CASE DIAGRAM
    # -------------------------------------------------------------
    W, H = 1000, 620
    im = Image.new("RGB", (W, H), "#ffffff")
    dr = ImageDraw.Draw(im)
    dr.text((30, 20), "UML Use Case Diagram — SalesLens Enterprise BI System", fill="#1e3a8a", font=font_title)
    dr.line([(30, 50), (970, 50)], fill="#cbd5e1", width=1)
    
    draw_rounded_rect(dr, (260, 65, 750, 595), radius=12, fill="#f8fafc", outline="#3b82f6", width=2)
    dr.text((280, 75), "System Boundary: SalesLens Reporting Engine", fill="#1e3a8a", font=font_h2)
    
    # Sales Director
    dr.ellipse([(50, 110), (90, 150)], fill="#dbeafe", outline="#1e3a8a", width=2)
    dr.line([(70, 150), (70, 200)], fill="#1e3a8a", width=2)
    dr.line([(40, 170), (100, 170)], fill="#1e3a8a", width=2)
    dr.line([(70, 200), (50, 240)], fill="#1e3a8a", width=2)
    dr.line([(70, 200), (90, 240)], fill="#1e3a8a", width=2)
    dr.text((30, 245), "Sales Director\n(Executive)", fill="#1e293b", font=font_small_bold, align="center")
    
    # Regional Manager
    dr.ellipse([(50, 310), (90, 350)], fill="#dbeafe", outline="#1e3a8a", width=2)
    dr.line([(70, 350), (70, 400)], fill="#1e3a8a", width=2)
    dr.line([(40, 370), (100, 370)], fill="#1e3a8a", width=2)
    dr.line([(70, 400), (50, 440)], fill="#1e3a8a", width=2)
    dr.line([(70, 400), (90, 440)], fill="#1e3a8a", width=2)
    dr.text((25, 445), "Regional Manager\n(Territory Lead)", fill="#1e293b", font=font_small_bold, align="center")

    # Data Analyst
    dr.ellipse([(870, 110), (910, 150)], fill="#fef3c7", outline="#d97706", width=2)
    dr.line([(890, 150), (890, 200)], fill="#d97706", width=2)
    dr.line([(860, 170), (920, 170)], fill="#d97706", width=2)
    dr.line([(890, 200), (870, 240)], fill="#d97706", width=2)
    dr.line([(890, 200), (910, 240)], fill="#d97706", width=2)
    dr.text((850, 245), "Data Analyst\n(Rule Validator)", fill="#1e293b", font=font_small_bold, align="center")

    # IT Admin
    dr.ellipse([(870, 340), (910, 380)], fill="#dcfce7", outline="#15803d", width=2)
    dr.line([(890, 380), (890, 430)], fill="#15803d", width=2)
    dr.line([(860, 400), (920, 400)], fill="#15803d", width=2)
    dr.line([(890, 430), (870, 470)], fill="#15803d", width=2)
    dr.line([(890, 430), (910, 470)], fill="#15803d", width=2)
    dr.text((845, 475), "IT Admin / ETL Cron\n(System Scheduler)", fill="#1e293b", font=font_small_bold, align="center")

    use_cases = [
        (300, 110, 500, 150, "UC-01: View Executive National Pulse", "#ffffff", "#2563eb"),
        (530, 110, 720, 150, "UC-02: Compare Regional Matrix", "#ffffff", "#2563eb"),
        (300, 175, 500, 215, "UC-03: Filter Territory Performance", "#ffffff", "#2563eb"),
        (530, 175, 720, 215, "UC-04: Target vs Actual Quotas", "#ffffff", "#2563eb"),
        (300, 240, 500, 280, "UC-05: Inspect Top/Bottom SKUs", "#ffffff", "#2563eb"),
        (530, 240, 720, 280, "UC-06: Audit 14% Cleaned Records", "#ffffff", "#d97706"),
        (300, 310, 500, 350, "UC-07: Ingest & Clean Daily Batch", "#ffffff", "#15803d"),
        (530, 310, 720, 350, "UC-08: Export PDF / CSV Summary", "#ffffff", "#2563eb"),
        (300, 380, 500, 420, "UC-09: Manage RBAC & Permissions", "#ffffff", "#15803d"),
        (300, 460, 500, 500, "UC-10: Map Missing Region Rules", "#fef3c7", "#d97706"),
        (530, 460, 720, 500, "UC-11: Enforce Row-Level Security", "#dcfce7", "#15803d")
    ]
    
    for x1, y1, x2, y2, text, bg, border in use_cases:
        draw_rounded_rect(dr, (x1, y1, x2, y2), radius=18, fill=bg, outline=border, width=2)
        dr.text((x1 + 12, y1 + 12), text, fill="#1e293b", font=font_small_bold)

    draw_arrow(dr, (110, 180), (300, 130), color="#1e3a8a", width=2)
    draw_arrow(dr, (110, 180), (530, 130), color="#1e3a8a", width=2)
    draw_arrow(dr, (110, 180), (530, 195), color="#1e3a8a", width=2)
    draw_arrow(dr, (110, 180), (300, 260), color="#1e3a8a", width=2)
    draw_arrow(dr, (110, 180), (530, 330), color="#1e3a8a", width=2)

    draw_arrow(dr, (110, 380), (300, 195), color="#1e3a8a", width=2)
    draw_arrow(dr, (110, 380), (530, 195), color="#1e3a8a", width=2)
    draw_arrow(dr, (110, 380), (300, 260), color="#1e3a8a", width=2)

    draw_arrow(dr, (850, 180), (500, 130), color="#d97706", width=2)
    draw_arrow(dr, (850, 180), (720, 260), color="#d97706", width=2)
    draw_arrow(dr, (850, 180), (500, 260), color="#d97706", width=2)
    draw_arrow(dr, (850, 180), (720, 330), color="#d97706", width=2)
    draw_arrow(dr, (850, 180), (500, 480), color="#d97706", width=2)

    draw_arrow(dr, (845, 410), (500, 330), color="#15803d", width=2)
    draw_arrow(dr, (845, 410), (500, 400), color="#15803d", width=2)
    draw_arrow(dr, (845, 410), (720, 480), color="#15803d", width=2)

    dr.line([(400, 350), (400, 460)], fill="#d97706", width=1)
    dr.text((405, 400), "<<include>>\nCleaning Rules", fill="#d97706", font=font_small)

    dr.line([(625, 215), (625, 460)], fill="#15803d", width=1)
    dr.text((630, 390), "<<include>>\nRow-Level RBAC", fill="#15803d", font=font_small)
    im.save(f"{out_dir}/uml_01_use_case.png", "PNG")

    # -------------------------------------------------------------
    # 2. CLASS DIAGRAM
    # -------------------------------------------------------------
    W, H = 1050, 680
    im = Image.new("RGB", (W, H), "#ffffff")
    dr = ImageDraw.Draw(im)
    dr.text((30, 20), "UML Class Diagram — High Cohesion & Loose Coupling Architecture", fill="#1e3a8a", font=font_title)
    dr.line([(30, 50), (1020, 50)], fill="#cbd5e1", width=1)
    
    def draw_class(x, y, w, h, name, attrs, methods, header_bg="#1e3a8a"):
        draw_rounded_rect(dr, (x, y, x+w, y+h), radius=6, fill="#ffffff", outline="#64748b", width=2)
        draw_rounded_rect(dr, (x, y, x+w, y+28), radius=6, fill=header_bg, outline=header_bg, width=1)
        dr.text((x + 10, y + 6), name, fill="#ffffff", font=font_bold)
        curr_y = y + 34
        for a in attrs:
            dr.text((x + 8, curr_y), a, fill="#334155", font=font_small)
            curr_y += 15
        dr.line([(x, curr_y + 2), (x + w, curr_y + 2)], fill="#cbd5e1", width=1)
        curr_y += 6
        for m in methods:
            dr.text((x + 8, curr_y), m, fill="#1e293b", font=font_small_bold)
            curr_y += 15

    draw_class(40, 70, 210, 165, "BillingTransaction", 
               ["- transactionId: String", "- invoiceDate: Date", "- customerId: String", "- sku: String", "- amount: Double", "- rawRegion: String", "- status: String"],
               ["+ getAmount(): Double", "+ getRawRegion(): String", "+ setResolved(reg): void"])

    draw_class(300, 70, 230, 165, "RegionResolutionEngine",
               ["- postalMapping: Map", "- customerMaster: Map", "- repDirectory: Map", "- quarantineQueue: List"],
               ["+ resolve(txn): String", "+ matchPostal(zip): String", "+ matchCustomer(id): String", "+ matchRep(id): String"],
               header_bg="#d97706")

    draw_class(580, 70, 230, 165, "CleanDataWarehouse",
               ["- factSalesTable: Table", "- dimProducts: Table", "- dimRegions: Table", "- lastSync: Timestamp"],
               ["+ bulkInsert(records): int", "+ queryAggregates(filter): DTO", "+ getRegionTotals(): Map"],
               header_bg="#15803d")

    draw_class(840, 70, 180, 165, "QuotaEngine",
               ["- monthlyTargets: Map", "- pacingFactor: Double"],
               ["+ calcVariance(act, tgt)", "+ getAttainment(): %", "+ getPacingStatus()"],
               header_bg="#2563eb")

    draw_class(40, 310, 210, 150, "SecurityRBACManager",
               ["- userSession: Session", "- roleMatrix: Map"],
               ["+ validateToken(jwt): bool", "+ applyRegionFilter(q)", "+ enforcePermissions()"])

    draw_class(300, 310, 240, 170, "DashboardRenderer",
               ["- activeFilters: FilterState", "- cachedKPIs: JSON", "- currentRole: String"],
               ["+ renderPulseCard(): HTML", "+ renderRegionMatrix()", "+ renderTopBottomSKUs()", "+ exportPDFReport()"],
               header_bg="#2563eb")

    draw_class(590, 310, 220, 150, "AuditLogManager",
               ["- logBuffer: List<AuditEntry>", "- anomalyStats: Map"],
               ["+ recordResolution(txnId)", "+ generateAuditLog(): CSV", "+ getCleaningStats(): Map"],
               header_bg="#d97706")

    draw_class(840, 310, 180, 150, "ETLController",
               ["- cronSchedule: String", "- isRunning: Boolean"],
               ["+ triggerNightlyBatch()", "+ monitorHealth(): Status", "+ sendAlert(msg): void"],
               header_bg="#15803d")

    draw_arrow(dr, (250, 140), (300, 140), color="#64748b", width=2)
    dr.text((255, 122), "1..* cleans", fill="#64748b", font=font_small)

    draw_arrow(dr, (530, 140), (580, 140), color="#64748b", width=2)
    dr.text((535, 122), "persists", fill="#64748b", font=font_small)

    draw_arrow(dr, (810, 140), (840, 140), color="#64748b", width=2)

    draw_arrow(dr, (650, 235), (480, 310), color="#2563eb", width=2)
    dr.text((560, 260), "queries DTO", fill="#2563eb", font=font_small_bold)

    draw_arrow(dr, (415, 235), (650, 310), color="#d97706", width=2)
    dr.text((510, 280), "logs 14% fixes", fill="#d97706", font=font_small)

    draw_arrow(dr, (250, 380), (300, 380), color="#64748b", width=2)
    dr.text((255, 362), "filters", fill="#64748b", font=font_small)

    draw_arrow(dr, (920, 310), (530, 190), color="#15803d", width=2)

    draw_rounded_rect(dr, (40, 510, 1020, 650), radius=8, fill="#eff6ff", outline="#3b82f6", width=2)
    dr.text((55, 520), "Architectural Justification: Loose Coupling & High Cohesion", fill="#1e3a8a", font=font_bold)
    text_expl = (
        "1. Loose Coupling: Dashboard Views never talk directly to legacy billing or raw cleaning algorithms. They consume clean DTOs from\n"
        "   CleanDataWarehouse via a standardized Data Access Layer. Changing the 14% region mapping heuristics requires ZERO changes in UI.\n"
        "2. High Cohesion: Each class has a single, well-defined responsibility (SRP). RegionResolutionEngine only fixes missing data; QuotaEngine\n"
        "   only handles mathematics; SecurityRBACManager strictly enforces data isolation; and DashboardRenderer focuses solely on DOM display."
    )
    dr.text((55, 545), text_expl, fill="#1e293b", font=font_small)
    im.save(f"{out_dir}/uml_02_class_diagram.png", "PNG")

    # -------------------------------------------------------------
    # 3. SEQUENCE DIAGRAM
    # -------------------------------------------------------------
    W, H = 1050, 700
    im = Image.new("RGB", (W, H), "#ffffff")
    dr = ImageDraw.Draw(im)
    dr.text((30, 20), "UML Sequence Diagram: Load Daily Sales & Refresh Dashboard Views", fill="#1e3a8a", font=font_title)
    dr.line([(30, 50), (1020, 50)], fill="#cbd5e1", width=1)

    lifelines = [
        ("Cron Scheduler", 90, "#15803d"),
        ("ETL Pipeline", 240, "#15803d"),
        ("Billing Source DB", 390, "#64748b"),
        ("Region Clean Engine", 540, "#d97706"),
        ("Clean Warehouse", 700, "#2563eb"),
        ("Dashboard Service", 850, "#2563eb"),
        ("Regional Mgr UI", 980, "#1e3a8a"),
    ]

    for name, x, color in lifelines:
        draw_rounded_rect(dr, (x-55, 65, x+55, 95), radius=6, fill=color, outline=color)
        dr.text((x-48, 73), name, fill="#ffffff", font=font_small_bold)
        for ly in range(105, 660, 10):
            dr.line([(x, ly), (x, ly+5)], fill="#cbd5e1", width=1)

    def draw_msg(y, x1, x2, text, is_return=False, color="#1e3a8a"):
        if is_return:
            for lx in range(min(x1, x2), max(x1, x2), 8):
                dr.line([(lx, y), (lx+4, y)], fill=color, width=1)
            draw_arrow(dr, (x1, y), (x2, y), color=color, width=1)
        else:
            draw_arrow(dr, (x1, y), (x2, y), color=color, width=2)
        dr.text((min(x1, x2) + 10, y - 14), text, fill=color, font=font_small_bold)

    draw_msg(130, 90, 240, "1. triggerNightlyETL(02:00 AM)", color="#15803d")
    draw_msg(160, 240, 390, "2. extractDailySettledTxns()", color="#334155")
    draw_msg(190, 390, 240, "3. return rawTxnsBatch (100k rows)", is_return=True, color="#334155")
    
    draw_rounded_rect(dr, (210, 215, 600, 355), radius=6, fill=None, outline="#d97706", width=2)
    dr.text((220, 220), "alt: 14% Missing Region Resolution Loop", fill="#d97706", font=font_small_bold)

    draw_msg(245, 240, 540, "4. resolveMissingRegion(txn)", color="#d97706")
    draw_msg(275, 540, 540, "5. match Postal -> CustMaster -> Rep", color="#d97706")
    draw_msg(305, 540, 240, "6. return CanonicalRegionCode / Flag Quarantine", is_return=True, color="#d97706")
    draw_msg(335, 240, 700, "7. bulkUpsertCleanRecords(factSales)", color="#15803d")

    draw_msg(380, 240, 850, "8. notifyDataRefreshComplete()", color="#15803d")
    draw_msg(410, 850, 850, "9. invalidateViewCache() & precomputeKPIs()", color="#2563eb")

    dr.line([(50, 445), (1000, 445)], fill="#e2e8f0", width=1)
    dr.text((60, 452), "Morning Operations (08:00 AM Login)", fill="#64748b", font=font_small_bold)

    draw_msg(485, 980, 850, "10. openDashboard(JWT_Token, Region='North')", color="#1e3a8a")
    draw_msg(520, 850, 700, "11. queryAggregates(Role='RegionalMgr', Region='North')", color="#2563eb")
    draw_msg(555, 700, 850, "12. return FilteredMetricsDTO (Sub-2s Query)", is_return=True, color="#2563eb")
    draw_msg(590, 850, 980, "13. renderDailyPulse, Quotas, SKUs & Matrix", is_return=True, color="#1e3a8a")
    draw_msg(630, 980, 980, "14. UI Interactive Drill-down Active", color="#059669")
    im.save(f"{out_dir}/uml_03_sequence_diagram.png", "PNG")

    # -------------------------------------------------------------
    # 4. ACTIVITY DIAGRAM
    # -------------------------------------------------------------
    W, H = 1000, 680
    im = Image.new("RGB", (W, H), "#ffffff")
    dr = ImageDraw.Draw(im)
    dr.text((30, 20), "UML Activity Diagram — Automated ETL & Region Resolution Pipeline", fill="#1e3a8a", font=font_title)
    dr.line([(30, 50), (970, 50)], fill="#cbd5e1", width=1)

    dr.ellipse([(480, 65), (504, 89)], fill="#1e293b", outline="#1e293b")
    draw_arrow(dr, (492, 90), (492, 120), color="#1e3a8a", width=2)

    draw_rounded_rect(dr, (390, 120, 594, 155), radius=6, fill="#eff6ff", outline="#3b82f6", width=2)
    dr.text((410, 130), "Extract Daily Billing Records", fill="#1e3a8a", font=font_small_bold)
    draw_arrow(dr, (492, 155), (492, 185), color="#1e3a8a", width=2)

    dr.polygon([(492, 185), (545, 215), (492, 245), (439, 215)], fill="#fef3c7", outline="#d97706")
    dr.text((458, 208), "14% Missing?", fill="#92400e", font=font_small_bold)

    draw_arrow(dr, (545, 215), (750, 215), color="#15803d", width=2)
    dr.text((580, 200), "[No: Region Valid]", fill="#15803d", font=font_small_bold)
    draw_arrow(dr, (750, 215), (750, 430), color="#15803d", width=2)

    draw_arrow(dr, (492, 245), (492, 280), color="#d97706", width=2)
    dr.text((500, 255), "[Yes: 14% Missing]", fill="#d97706", font=font_small_bold)

    draw_rounded_rect(dr, (380, 280, 604, 315), radius=6, fill="#fffbeb", outline="#d97706", width=2)
    dr.text((400, 290), "1. Match Customer Postal Code Master", fill="#92400e", font=font_small)
    draw_arrow(dr, (492, 315), (492, 345), color="#d97706", width=2)

    draw_rounded_rect(dr, (380, 345, 604, 380), radius=6, fill="#fffbeb", outline="#d97706", width=2)
    dr.text((400, 355), "2. Lookup Historical Account Territory", fill="#92400e", font=font_small)
    draw_arrow(dr, (492, 380), (492, 410), color="#d97706", width=2)

    draw_rounded_rect(dr, (380, 410, 604, 445), radius=6, fill="#fffbeb", outline="#d97706", width=2)
    dr.text((400, 420), "3. Map Sales Rep Assigned Zone", fill="#92400e", font=font_small)
    draw_arrow(dr, (492, 445), (492, 475), color="#d97706", width=2)

    dr.line([(350, 475), (780, 475)], fill="#1e3a8a", width=3)
    draw_arrow(dr, (750, 430), (750, 475), color="#15803d", width=2)
    draw_arrow(dr, (565, 475), (565, 505), color="#1e3a8a", width=2)

    draw_rounded_rect(dr, (450, 505, 680, 540), radius=6, fill="#eff6ff", outline="#3b82f6", width=2)
    dr.text((470, 515), "Compute 9-View Standardized KPIs", fill="#1e3a8a", font=font_small_bold)
    draw_arrow(dr, (565, 540), (565, 570), color="#1e3a8a", width=2)

    draw_rounded_rect(dr, (450, 570, 680, 605), radius=6, fill="#dcfce7", outline="#15803d", width=2)
    dr.text((465, 580), "Publish to Warehouse & Refresh Cache", fill="#15803d", font=font_small_bold)
    draw_arrow(dr, (565, 605), (565, 635), color="#1e3a8a", width=2)

    dr.ellipse([(553, 635), (577, 659)], fill="#ffffff", outline="#1e293b", width=2)
    dr.ellipse([(557, 639), (573, 655)], fill="#1e293b", outline="#1e293b")
    im.save(f"{out_dir}/uml_04_activity_diagram.png", "PNG")

    # -------------------------------------------------------------
    # 5. STATE DIAGRAM
    # -------------------------------------------------------------
    W, H = 1000, 600
    im = Image.new("RGB", (W, H), "#ffffff")
    dr = ImageDraw.Draw(im)
    dr.text((30, 20), "UML State Machine Diagram — Daily Data Load Lifecycle", fill="#1e3a8a", font=font_title)
    dr.line([(30, 50), (970, 50)], fill="#cbd5e1", width=1)

    states = [
        (60, 160, 180, 220, "IDLE / SCHEDULED\n(Waiting for 02:00 AM)", "#f8fafc", "#64748b"),
        (260, 160, 400, 220, "EXTRACTING_RAW\n(Reading Billing DB)", "#eff6ff", "#3b82f6"),
        (480, 160, 640, 220, "EVALUATING_RULES\n(Scanning 14% Missing)", "#fef3c7", "#d97706"),
        (720, 160, 890, 220, "TRANSFORMING_CLEAN\n(Applying Heuristics)", "#dcfce7", "#15803d"),
        (480, 360, 650, 420, "WAREHOUSE_COMMITTED\n(Indexed & Staged)", "#eff6ff", "#2563eb"),
        (720, 360, 890, 420, "DASHBOARD_ACTIVE\n(Sub-2s Query Ready)", "#dcfce7", "#15803d"),
        (260, 360, 400, 420, "QUARANTINED_AUDIT\n(Unresolvable Anomaly)", "#fee2e2", "#ef4444")
    ]

    for x1, y1, x2, y2, text, bg, border in states:
        draw_rounded_rect(dr, (x1, y1, x2, y2), radius=10, fill=bg, outline=border, width=2)
        dr.text((x1 + 12, y1 + 14), text, fill="#1e293b", font=font_small_bold, align="center")

    dr.ellipse([(20, 180), (40, 200)], fill="#1e293b")
    draw_arrow(dr, (40, 190), (60, 190), color="#1e3a8a", width=2)

    draw_arrow(dr, (180, 190), (260, 190), color="#1e3a8a", width=2)
    dr.text((190, 172), "cron_tick", fill="#1e3a8a", font=font_small)

    draw_arrow(dr, (400, 190), (480, 190), color="#1e3a8a", width=2)
    dr.text((408, 172), "batch_loaded", fill="#1e3a8a", font=font_small)

    draw_arrow(dr, (640, 190), (720, 190), color="#d97706", width=2)
    dr.text((645, 172), "14%_detected", fill="#d97706", font=font_small)

    draw_arrow(dr, (805, 220), (805, 360), color="#15803d", width=2)
    dr.text((815, 280), "all_resolved", fill="#15803d", font=font_small_bold)

    draw_arrow(dr, (720, 390), (650, 390), color="#2563eb", width=2)
    dr.text((660, 372), "cache_built", fill="#2563eb", font=font_small)

    draw_arrow(dr, (560, 220), (330, 360), color="#ef4444", width=2)
    dr.text((370, 280), "[unresolvable] > 0.1%", fill="#ef4444", font=font_small_bold)

    draw_arrow(dr, (330, 420), (330, 480), color="#ef4444", width=2)
    dr.line([(330, 480), (120, 480)], fill="#ef4444", width=2)
    draw_arrow(dr, (120, 480), (120, 220), color="#ef4444", width=2)
    dr.text((130, 460), "analyst_manual_review_complete", fill="#ef4444", font=font_small)
    im.save(f"{out_dir}/uml_05_state_diagram.png", "PNG")

    # -------------------------------------------------------------
    # 6. ARCHITECTURE / DEPLOYMENT
    # -------------------------------------------------------------
    W, H = 1000, 580
    im = Image.new("RGB", (W, H), "#ffffff")
    dr = ImageDraw.Draw(im)
    dr.text((30, 20), "Enterprise Deployment & 3-Tier Architecture Diagram", fill="#1e3a8a", font=font_title)
    dr.line([(30, 50), (970, 50)], fill="#cbd5e1", width=1)

    tiers = [
        (40, 70, 240, 540, "Tier 1: Data Source\n(Legacy Billing)", "#f8fafc", "#64748b"),
        (280, 70, 680, 540, "Tier 2: Business Logic & Data Warehouse\n(FastAPI / Node + PostgreSQL)", "#eff6ff", "#2563eb"),
        (720, 70, 960, 540, "Tier 3: Presentation\n(Interactive Browser Clients)", "#f0fdf4", "#15803d")
    ]

    for x1, y1, x2, y2, title, bg, border in tiers:
        draw_rounded_rect(dr, (x1, y1, x2, y2), radius=10, fill=bg, outline=border, width=2)
        dr.text((x1 + 15, y1 + 15), title, fill="#1e293b", font=font_small_bold)

    draw_rounded_rect(dr, (60, 160, 220, 250), radius=6, fill="#ffffff", outline="#64748b", width=2)
    dr.text((75, 175), "Legacy Billing DB\n(Read Replica)\n• 100k Daily Txns\n• 14% Missing Region", fill="#334155", font=font_small)

    draw_rounded_rect(dr, (300, 130, 470, 250), radius=6, fill="#ffffff", outline="#d97706", width=2)
    dr.text((315, 145), "ETL Cleaning Engine\n• Region Mapping Rules\n• Anomaly Quarantine\n• Nightly Cron 02:00 AM", fill="#92400e", font=font_small)

    draw_rounded_rect(dr, (490, 130, 660, 250), radius=6, fill="#ffffff", outline="#2563eb", width=2)
    dr.text((505, 145), "SalesLens Core API\n• Fast JSON Aggregator\n• Quota Variance Engine\n• RBAC Middleware", fill="#1e3a8a", font=font_small)

    draw_rounded_rect(dr, (300, 300, 660, 430), radius=6, fill="#ffffff", outline="#15803d", width=2)
    dr.text((315, 315), "PostgreSQL Analytical Data Warehouse\n• Indexed Fact_Sales (Star Schema)\n• Materialized Views for 9 Core Dashboards\n• Audit Logs Table (100% Traceability)", fill="#15803d", font=font_small)

    draw_rounded_rect(dr, (740, 130, 940, 230), radius=6, fill="#ffffff", outline="#1e3a8a", width=2)
    dr.text((755, 145), "Executive Portal\n(Sales Director)\n• National Pulse View\n• Regional Matrix Grid", fill="#1e3a8a", font=font_small)

    draw_rounded_rect(dr, (740, 260, 940, 360), radius=6, fill="#ffffff", outline="#1e3a8a", width=2)
    dr.text((755, 275), "Territory Portal\n(Regional Managers)\n• Quota Scorecards\n• Top/Bottom SKUs", fill="#1e3a8a", font=font_small)

    draw_rounded_rect(dr, (740, 390, 940, 490), radius=6, fill="#ffffff", outline="#d97706", width=2)
    dr.text((755, 405), "Audit Console\n(Data Analysts)\n• 14% Rule Verification\n• Anomaly Inspection", fill="#92400e", font=font_small)

    draw_arrow(dr, (220, 200), (300, 190), color="#d97706", width=2)
    dr.text((230, 175), "JDBC / SSL", fill="#d97706", font=font_small)

    draw_arrow(dr, (385, 250), (385, 300), color="#15803d", width=2)
    draw_arrow(dr, (575, 300), (575, 250), color="#2563eb", width=2)

    draw_arrow(dr, (660, 180), (740, 180), color="#1e3a8a", width=2)
    draw_arrow(dr, (660, 210), (740, 310), color="#1e3a8a", width=2)
    draw_arrow(dr, (660, 230), (740, 440), color="#d97706", width=2)
    dr.text((665, 260), "HTTPS / REST\nJWT Auth", fill="#1e3a8a", font=font_small_bold)
    im.save(f"{out_dir}/uml_06_architecture_deployment.png", "PNG")

    # -------------------------------------------------------------
    # 7. CPM NETWORK DIAGRAM
    # -------------------------------------------------------------
    W, H = 1050, 600
    im = Image.new("RGB", (W, H), "#ffffff")
    dr = ImageDraw.Draw(im)
    dr.text((30, 20), "CPM Network Diagram — Critical Path Analysis & Schedule Management", fill="#1e3a8a", font=font_title)
    dr.line([(30, 50), (1020, 50)], fill="#cbd5e1", width=1)

    nodes = [
        ("A", "Req Elicit", 2.0, 0.0, 2.0, 0.0, 2.0, 0.0, 50, 220, True),
        ("B", "Arch Design", 3.0, 2.0, 5.0, 4.5, 7.5, 2.5, 190, 110, False),
        ("C", "14% Clean Rules", 5.5, 2.0, 7.5, 2.0, 7.5, 0.0, 190, 330, True),
        ("D", "ETL Build", 4.0, 7.5, 11.5, 7.5, 11.5, 0.0, 340, 220, True),
        ("E", "Views 1-3", 9.0, 11.5, 20.5, 11.5, 20.5, 0.0, 470, 220, True),
        ("F", "Views 4-6", 9.0, 20.5, 29.5, 20.5, 29.5, 0.0, 600, 220, True),
        ("G", "Views 7-9", 9.0, 29.5, 38.5, 29.5, 38.5, 0.0, 730, 220, True),
        ("H", "RBAC Security", 2.0, 38.5, 40.5, 38.5, 40.5, 0.0, 860, 220, True),
        ("I", "Testing & BVA", 3.5, 40.5, 44.0, 40.5, 44.0, 0.0, 500, 450, True),
        ("J", "UAT Walks", 2.0, 44.0, 46.0, 44.0, 46.0, 0.0, 680, 450, True),
        ("K", "Deploy/Conf", 2.0, 46.0, 48.0, 46.0, 48.0, 0.0, 860, 450, True),
    ]

    def draw_cpm_node(item):
        nid, name, dur, es, ef, ls, lf, slack, nx, ny, crit = item
        border_col = "#dc2626" if crit else "#3b82f6"
        bg_col = "#fef2f2" if crit else "#eff6ff"
        w, h = 95, 75
        draw_rounded_rect(dr, (nx, ny, nx+w, ny+h), radius=6, fill=bg_col, outline=border_col, width=2 if crit else 1)
        dr.line([(nx, ny+25), (nx+w, ny+25)], fill=border_col, width=1)
        dr.line([(nx, ny+50), (nx+w, ny+50)], fill=border_col, width=1)
        dr.line([(nx+32, ny), (nx+32, ny+25)], fill=border_col, width=1)
        dr.line([(nx+64, ny), (nx+64, ny+25)], fill=border_col, width=1)
        dr.line([(nx+32, ny+50), (nx+32, ny+75)], fill=border_col, width=1)
        dr.line([(nx+64, ny+50), (nx+64, ny+75)], fill=border_col, width=1)

        dr.text((nx+4, ny+6), f"{es:g}", fill="#1e293b", font=font_small_bold)
        dr.text((nx+36, ny+6), f"d={dur:g}", fill="#1e293b", font=font_small_bold)
        dr.text((nx+68, ny+6), f"{ef:g}", fill="#1e293b", font=font_small_bold)

        dr.text((nx+8, ny+31), f"{nid}: {name}", fill=border_col, font=font_small_bold)

        dr.text((nx+4, ny+56), f"{ls:g}", fill="#1e293b", font=font_small)
        dr.text((nx+36, ny+56), f"S={slack:g}", fill="#dc2626" if slack==0 else "#059669", font=font_small_bold)
        dr.text((nx+68, ny+56), f"{lf:g}", fill="#1e293b", font=font_small)

    for n in nodes:
        draw_cpm_node(n)

    draw_arrow(dr, (145, 240), (190, 150), color="#64748b", width=2)
    draw_arrow(dr, (145, 270), (190, 360), color="#dc2626", width=3)
    draw_arrow(dr, (285, 150), (340, 240), color="#64748b", width=2)
    draw_arrow(dr, (285, 360), (340, 270), color="#dc2626", width=3)
    draw_arrow(dr, (435, 255), (470, 255), color="#dc2626", width=3)
    draw_arrow(dr, (565, 255), (600, 255), color="#dc2626", width=3)
    draw_arrow(dr, (695, 255), (730, 255), color="#dc2626", width=3)
    draw_arrow(dr, (825, 255), (860, 255), color="#dc2626", width=3)
    draw_arrow(dr, (905, 295), (595, 450), color="#dc2626", width=3)
    draw_arrow(dr, (595, 485), (680, 485), color="#dc2626", width=3)
    draw_arrow(dr, (775, 485), (860, 485), color="#dc2626", width=3)

    draw_rounded_rect(dr, (50, 440, 430, 560), radius=8, fill="#eff6ff", outline="#3b82f6", width=2)
    dr.text((65, 450), "Critical Path: A → C → D → E → F → G → H → I → J → K", fill="#dc2626", font=font_bold)
    dr.text((65, 475), "• Total Unoptimized Working Days = 48.0 days (9.6 Weeks)", fill="#1e293b", font=font_small)
    dr.text((65, 495), "• Fast-Tracking & Template Modularization = 39.0 days (7.8 Weeks)", fill="#059669", font=font_small_bold)
    dr.text((65, 515), "• Target Deadline: 8.0 Weeks (40 Working Days) -> ON TIME!", fill="#15803d", font=font_small_bold)
    dr.text((65, 535), "• 14% Data Cleaning is on Critical Path (Slack = 0.0 days)", fill="#d97706", font=font_small_bold)
    im.save(f"{out_dir}/cpm_network_diagram.png", "PNG")

    # -------------------------------------------------------------
    # 8. GANTT CHART
    # -------------------------------------------------------------
    W, H = 1050, 600
    im = Image.new("RGB", (W, H), "#ffffff")
    dr = ImageDraw.Draw(im)
    dr.text((30, 20), "8-Week Project Gantt Chart & Resource Allocation Timeline", fill="#1e3a8a", font=font_title)
    dr.line([(30, 50), (1020, 50)], fill="#cbd5e1", width=1)

    col_x = 280
    w_width = 85
    for w in range(1, 9):
        dr.rectangle([(col_x, 65), (col_x + w_width, 95)], fill="#1e3a8a" if w%2==0 else "#2563eb", outline="#ffffff")
        dr.text((col_x + 18, 73), f"Week {w}", fill="#ffffff", font=font_small_bold)
        for gy in range(95, 530, 10):
            dr.line([(col_x, gy), (col_x, gy+5)], fill="#e2e8f0", width=1)
        col_x += w_width

    tasks = [
        ("1. Inception & 9-View Scope", 0.0, 0.4, "#2563eb", "BI Dev + Analyst (1.5 FTE)"),
        ("2. Arch & Schema Design", 0.4, 1.0, "#64748b", "BI Dev (1.0 FTE)"),
        ("3. 14% Data Cleaning Rules", 0.4, 1.5, "#d97706", "Analyst (0.5) + BI Dev (1.0)"),
        ("4. Automated Overnight ETL", 1.5, 2.3, "#15803d", "BI Dev (1.0 FTE)"),
        ("5. Views 1-3 (Exec/Targets/Top)", 2.3, 4.1, "#2563eb", "BI Dev (1.0 FTE)"),
        ("6. Views 4-6 (Bottom/Regions)", 4.1, 5.9, "#2563eb", "BI Dev (1.0 FTE)"),
        ("7. Views 7-9 (Cat/Channel/Audit)", 5.0, 6.8, "#2563eb", "BI Dev (Fast-Tracked)"),
        ("8. RBAC & Filter Security", 6.5, 7.0, "#64748b", "BI Dev (1.0 FTE)"),
        ("9. QA, BVA & Decision Tests", 7.0, 7.7, "#dc2626", "Analyst (0.5) + BI Dev (1.0)"),
        ("10. UAT & Conference Launch", 7.7, 8.0, "#059669", "All Hands + Sales Director")
    ]

    ty = 105
    for name, s_wk, e_wk, color, res in tasks:
        dr.text((35, ty + 6), name, fill="#1e293b", font=font_small_bold)
        bx1 = 280 + int(s_wk * w_width)
        bx2 = 280 + int(e_wk * w_width)
        draw_rounded_rect(dr, (bx1, ty+2, bx2, ty+26), radius=5, fill=color, outline=color)
        dr.text((bx1 + 6, ty + 6), res, fill="#ffffff", font=font_small)
        ty += 38

    milestones = [
        (280 + int(0.4 * w_width), 120, "M1: Scope Freeze"),
        (280 + int(2.3 * w_width), 235, "M2: Clean ETL Active"),
        (280 + int(6.8 * w_width), 350, "M3: 9 Views Built"),
        (280 + int(7.7 * w_width), 425, "M4: QA Sign-Off"),
        (280 + int(8.0 * w_width), 465, "M5: Annual Conference Go-Live")
    ]

    for mx, my, mtext in milestones:
        dr.polygon([(mx, my-8), (mx+8, my), (mx, my+8), (mx-8, my)], fill="#f59e0b", outline="#b45309")
        dr.text((mx + 12, my - 6), mtext, fill="#b45309", font=font_small_bold)

    dr.line([(280 + 8 * w_width, 65), (280 + 8 * w_width, 530)], fill="#dc2626", width=2)
    dr.text((860, 500), "8-WEEK HARD DEADLINE\n(Annual Sales Conference)", fill="#dc2626", font=font_bold)
    im.save(f"{out_dir}/gantt_chart_timeline.png", "PNG")

    # -------------------------------------------------------------
    # 9. DECISION TABLE
    # -------------------------------------------------------------
    W, H = 1000, 600
    im = Image.new("RGB", (W, H), "#ffffff")
    dr = ImageDraw.Draw(im)
    dr.text((30, 20), "Decision Tree & Rule Engine for 14% Missing Region Codes", fill="#1e3a8a", font=font_title)
    dr.line([(30, 50), (970, 50)], fill="#cbd5e1", width=1)

    dr.ellipse([(140, 75), (164, 99)], fill="#1e293b")
    draw_arrow(dr, (152, 100), (152, 130), color="#1e3a8a", width=2)

    draw_rounded_rect(dr, (60, 130, 244, 175), radius=6, fill="#eff6ff", outline="#3b82f6", width=2)
    dr.text((75, 145), "Raw Region Code Present?", fill="#1e3a8a", font=font_small_bold)
    draw_arrow(dr, (244, 152), (320, 152), color="#15803d", width=2)
    dr.text((250, 135), "[Yes: 86%]", fill="#15803d", font=font_small_bold)
    draw_rounded_rect(dr, (320, 130, 480, 175), radius=6, fill="#dcfce7", outline="#15803d", width=2)
    dr.text((335, 145), "Assign Raw Region (Direct)", fill="#15803d", font=font_small_bold)

    draw_arrow(dr, (152, 175), (152, 215), color="#d97706", width=2)
    dr.text((158, 188), "[No: 14%]", fill="#d97706", font=font_small_bold)

    draw_rounded_rect(dr, (60, 215, 244, 260), radius=6, fill="#fffbeb", outline="#d97706", width=2)
    dr.text((75, 230), "Postal Code Match in Master?", fill="#92400e", font=font_small_bold)
    draw_arrow(dr, (244, 237), (320, 237), color="#15803d", width=2)
    dr.text((250, 220), "[Yes: 9.8%]", fill="#15803d", font=font_small_bold)
    draw_rounded_rect(dr, (320, 215, 480, 260), radius=6, fill="#dcfce7", outline="#15803d", width=2)
    dr.text((335, 230), "Assign Master Zip Territory", fill="#15803d", font=font_small_bold)

    draw_arrow(dr, (152, 260), (152, 300), color="#d97706", width=2)
    dr.text((158, 273), "[No]", fill="#d97706", font=font_small_bold)

    draw_rounded_rect(dr, (60, 300, 244, 345), radius=6, fill="#fffbeb", outline="#d97706", width=2)
    dr.text((75, 315), "Customer Account Registered?", fill="#92400e", font=font_small_bold)
    draw_arrow(dr, (244, 322), (320, 322), color="#15803d", width=2)
    dr.text((250, 305), "[Yes: 2.8%]", fill="#15803d", font=font_small_bold)
    draw_rounded_rect(dr, (320, 300, 480, 345), radius=6, fill="#dcfce7", outline="#15803d", width=2)
    dr.text((335, 315), "Assign Account Home Zone", fill="#15803d", font=font_small_bold)

    draw_arrow(dr, (152, 345), (152, 385), color="#d97706", width=2)
    dr.text((158, 358), "[No]", fill="#d97706", font=font_small_bold)

    draw_rounded_rect(dr, (60, 385, 244, 430), radius=6, fill="#fffbeb", outline="#d97706", width=2)
    dr.text((75, 400), "Sales Rep ID Valid in Master?", fill="#92400e", font=font_small_bold)
    draw_arrow(dr, (244, 407), (320, 407), color="#15803d", width=2)
    dr.text((250, 390), "[Yes: 1.3%]", fill="#15803d", font=font_small_bold)
    draw_rounded_rect(dr, (320, 385, 480, 430), radius=6, fill="#dcfce7", outline="#15803d", width=2)
    dr.text((335, 400), "Assign Rep Default Territory", fill="#15803d", font=font_small_bold)

    draw_arrow(dr, (152, 430), (152, 470), color="#ef4444", width=2)
    dr.text((158, 443), "[No: 0.1%]", fill="#ef4444", font=font_small_bold)

    draw_rounded_rect(dr, (60, 470, 244, 520), radius=6, fill="#fee2e2", outline="#ef4444", width=2)
    dr.text((75, 485), "QUARANTINE QUEUE\nAlert Data Analyst for Fix", fill="#ef4444", font=font_small_bold)

    draw_rounded_rect(dr, (520, 80, 970, 540), radius=8, fill="#f8fafc", outline="#64748b", width=2)
    dr.text((540, 95), "Formal Region-Code Mapping Decision Table", fill="#1e3a8a", font=font_bold)
    
    table_headers = ["Rule Condition / Action", "R1", "R2", "R3", "R4", "R5"]
    cols_x = [540, 720, 770, 820, 870, 920]
    
    draw_rounded_rect(dr, (535, 125, 955, 150), radius=4, fill="#1e3a8a", outline="#1e3a8a")
    for idx, htxt in enumerate(table_headers):
        dr.text((cols_x[idx] + (5 if idx>0 else 10), 132), htxt, fill="#ffffff", font=font_small_bold)

    t_rows = [
        ("C1: Raw Region Present?", "Y", "N", "N", "N", "N"),
        ("C2: Zip Match Found?", "-", "Y", "N", "N", "N"),
        ("C3: Customer Master Match?", "-", "-", "Y", "N", "N"),
        ("C4: Sales Rep Assigned?", "-", "-", "-", "Y", "N"),
        ("-----------------------", "-", "-", "-", "-", "-"),
        ("A1: Assign Raw Region", "X", "-", "-", "-", "-"),
        ("A2: Assign Zip Territory", "-", "X", "-", "-", "-"),
        ("A3: Assign Cust Territory", "-", "-", "X", "-", "-"),
        ("A4: Assign Rep Territory", "-", "-", "-", "X", "-"),
        ("A5: Flag Quarantine Audit", "-", "-", "-", "-", "X"),
        ("-----------------------", "-", "-", "-", "-", "-"),
        ("Expected Volume %", "86.0%", "9.8%", "2.8%", "1.3%", "0.1%")
    ]

    ry = 158
    for r in t_rows:
        for cidx, val in enumerate(r):
            col_fill = "#1e293b" if val != "X" and val != "Y" else ("#15803d" if val=="Y" or cidx<5 else "#ef4444")
            if val == "X":
                col_fill = "#2563eb"
            dr.text((cols_x[cidx] + (10 if cidx>0 else 10), ry), val, fill=col_fill, font=font_small_bold if cidx>0 else font_small)
        dr.line([(535, ry+18), (955, ry+18)], fill="#e2e8f0", width=1)
        ry += 24
    im.save(f"{out_dir}/decision_table_flowchart.png", "PNG")

    # -------------------------------------------------------------
    # 10. RISK MATRIX HEATMAP
    # -------------------------------------------------------------
    W, H = 1000, 600
    im = Image.new("RGB", (W, H), "#ffffff")
    dr = ImageDraw.Draw(im)
    dr.text((30, 20), "Risk Exposure Heatmap Matrix (Probability × Impact)", fill="#1e3a8a", font=font_title)
    dr.line([(30, 50), (970, 50)], fill="#cbd5e1", width=1)

    grid_x, grid_y = 120, 90
    cell_w, cell_h = 90, 75
    prob_labels = ["5: Very High", "4: High", "3: Medium", "2: Low", "1: Very Low"]
    imp_labels = ["1: Negligible", "2: Minor", "3: Moderate", "4: Major", "5: Critical"]

    def get_heat_color(p, i):
        score = p * i
        if score >= 15:
            return "#fee2e2", "#ef4444"
        elif score >= 8:
            return "#fef3c7", "#d97706"
        else:
            return "#dcfce7", "#15803d"

    for r in range(5):
        p_val = 5 - r
        dr.text((20, grid_y + r*cell_h + 28), prob_labels[r], fill="#1e293b", font=font_small_bold)
        for c in range(5):
            i_val = c + 1
            bg, border = get_heat_color(p_val, i_val)
            cx1 = grid_x + c * cell_w
            cy1 = grid_y + r * cell_h
            dr.rectangle([(cx1, cy1), (cx1 + cell_w, cy1 + cell_h)], fill=bg, outline=border, width=1)
            dr.text((cx1 + 8, cy1 + 8), f"P={p_val}, I={i_val}", fill="#64748b", font=font_small)
            dr.text((cx1 + 8, cy1 + 25), f"Exp = {p_val*i_val}", fill=border, font=font_small_bold)

    for c in range(5):
        dr.text((grid_x + c*cell_w + 10, grid_y + 5*cell_h + 10), imp_labels[c], fill="#1e293b", font=font_small_bold)

    dr.text((grid_x + 160, grid_y + 5*cell_h + 35), "IMPACT LEVEL →", fill="#1e3a8a", font=font_bold)

    risks_plot = [
        ("RSK-01: 14% Data Quality (P4, I5 = 20)", 4, 5, "#ef4444", 2),
        ("RSK-02: 8-Wk Conference (P3, I5 = 15)", 3, 5, "#ef4444", 3),
        ("RSK-03: Analyst Resistance (P4, I3 = 12)", 4, 3, "#d97706", 1),
        ("RSK-04: Billing DB Lock (P2, I4 = 8)", 2, 4, "#d97706", 4),
        ("RSK-05: RBAC Data Leak (P2, I4 = 8)", 2, 4, "#d97706", 5),
        ("RSK-06: Scope Creep >9 Views (P3, I3 = 9)", 3, 3, "#d97706", 6),
    ]

    draw_rounded_rect(dr, (610, 80, 970, 540), radius=8, fill="#f8fafc", outline="#64748b", width=2)
    dr.text((630, 95), "Exposure-Ranked Top Risks & RMMM Strategy", fill="#1e3a8a", font=font_bold)

    ry = 135
    for rname, p, i, col, rank in risks_plot:
        draw_rounded_rect(dr, (625, ry, 955, ry+55), radius=5, fill="#ffffff", outline=col, width=2)
        dr.text((635, ry+8), f"Rank #{rank}: {rname}", fill=col, font=font_small_bold)
        if rank == 1:
            desc = "Mitigation: Automated 4-tier fallback + daily audit log."
        elif rank == 2:
            desc = "Mitigation: Scope strict freeze to 9 used views (cut 17)."
        elif rank == 3:
            desc = "Mitigation: Retrain analysts as BI auditors & insight owners."
        else:
            desc = "Mitigation: Read replica + strict unit/integration security tests."
        dr.text((635, ry+30), desc, fill="#334155", font=font_small)
        ry += 65
    im.save(f"{out_dir}/risk_matrix_heatmap.png", "PNG")

    # -------------------------------------------------------------
    # 11. TESTING FUNNEL & DRE DEFECT METRICS
    # -------------------------------------------------------------
    W, H = 1000, 600
    im = Image.new("RGB", (W, H), "#ffffff")
    dr = ImageDraw.Draw(im)
    dr.text((30, 20), "Quality Assurance Funnel, Defect Density & DRE Calculations", fill="#1e3a8a", font=font_title)
    dr.line([(30, 50), (970, 50)], fill="#cbd5e1", width=1)

    stages = [
        ("1. Unit Testing (BVA on Sales & Dates)", "32 Defects Caught (E1)", 800, 480, "#2563eb", 90),
        ("2. Integration Testing (Overnight ETL Batch)", "18 Defects Caught (E2)", 650, 410, "#3b82f6", 165),
        ("3. System Testing (Region Decision Table)", "14 Defects Caught (E3)", 500, 340, "#60a5fa", 240),
        ("4. User Acceptance Testing (UAT Walkthroughs)", "4 Defects Caught (E4)", 360, 260, "#93c5fd", 315),
        ("5. Post-Release Annual Conference Target", "4 Residual Defects (D)", 220, 180, "#10b981", 390),
    ]

    for title, sub, w_top, w_bot, col, sy in stages:
        cx = 280
        x1 = cx - w_top // 2
        x2 = cx + w_top // 2
        x3 = cx + w_bot // 2
        x4 = cx - w_bot // 2
        dr.polygon([(x1, sy), (x2, sy), (x3, sy+60), (x4, sy+60)], fill=col, outline="#ffffff")
        dr.text((cx - 130, sy + 15), title, fill="#ffffff", font=font_small_bold)
        dr.text((cx - 80, sy + 35), sub, fill="#f8fafc", font=font_small)

    draw_rounded_rect(dr, (560, 80, 970, 540), radius=8, fill="#eff6ff", outline="#3b82f6", width=2)
    dr.text((580, 95), "Formal Software Engineering Quality Metrics", fill="#1e3a8a", font=font_bold)

    calc_text = (
        "1. Total Pre-Release Defects Caught (E):\n"
        "   E = E1 (Unit) + E2 (Integration) + E3 (System) + E4 (UAT)\n"
        "   E = 32 + 18 + 14 + 4 = 68 defects\n\n"
        "2. Post-Release Defects Observed / Target (D):\n"
        "   D = 4 defects (Target SLA)\n\n"
        "3. Defect Removal Efficiency (DRE) Formula:\n"
        "   DRE = [ E / (E + D) ] × 100%\n"
        "   DRE = [ 68 / (68 + 4) ] × 100% = [ 68 / 72 ] × 100%\n"
        "   DRE = 94.44% (Exceeds Industry Standard of 90%)\n\n"
        "4. Total Project Size & Defect Density:\n"
        "   Total Codebase = ~50,000 Lines of Code (50 KLOC)\n"
        "   Defect Density = Total Defects / KLOC\n"
        "   Defect Density = 68 / 50 = 1.36 defects / KLOC\n"
        "   (High Quality Rating for Enterprise Analytics Systems)\n\n"
        "5. Region-Code Rule Test Pass Rate:\n"
        "   Decision Table Coverage: 100% (5 Rules × 4 Combinations)\n"
        "   BVA Test Cases: 100% Pass across all boundary conditions."
    )
    dr.text((580, 130), calc_text, fill="#1e293b", font=font_small)
    im.save(f"{out_dir}/testing_dre_funnel.png", "PNG")
    print("SUCCESS: All 11 diagrams created successfully!")

if __name__ == "__main__":
    build_diagrams()
