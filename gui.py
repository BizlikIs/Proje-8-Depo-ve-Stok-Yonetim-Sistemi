from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import database as db

COMPANY_NAME = "DEPO PRO"

# ─── STYLES ──────────────────────────────────────────────────────────────────
_BTN_COMMON = """
QPushButton{background:#2563eb;color:#fff;border:none;border-radius:8px;
  padding:8px 18px;font-size:13px;font-weight:600;}
QPushButton:hover{background:#3b82f6;}
QPushButton:pressed{background:#1d4ed8;}
QPushButton#btnDanger{background:#dc2626;}
QPushButton#btnDanger:hover{background:#ef4444;}
QPushButton#btnSuccess{background:#16a34a;}
QPushButton#btnSuccess:hover{background:#22c55e;}
QPushButton#btnGray{background:#374151;color:#d1d5db;}
QPushButton#btnGray:hover{background:#4b5563;}
QPushButton#btnNav{background:transparent;color:#94a3b8;border:none;
  border-radius:8px;padding:8px 16px;font-size:13px;font-weight:600;
  min-width:100px;min-height:34px;}
QPushButton#btnNav:hover{background:#1e293b;color:#e2e8f0;}
QPushButton#btnNavActive{background:#2563eb;color:#fff;border:none;
  border-radius:8px;padding:8px 16px;font-size:13px;font-weight:600;
  min-width:100px;min-height:34px;}
QScrollBar:vertical{width:8px;border-radius:4px;}
QScrollBar::handle:vertical{border-radius:4px;}
QScrollBar::add-line:vertical,QScrollBar::sub-line:vertical{height:0;}
QScrollBar:horizontal{height:8px;border-radius:4px;}
QScrollBar::handle:horizontal{border-radius:4px;}
QScrollBar::add-line:horizontal,QScrollBar::sub-line:horizontal{width:0;}
QTabWidget::pane{border:none;}
"""

STYLE = _BTN_COMMON + """
QMainWindow,QWidget{background:#0f1117;color:#e2e8f0;font-family:'Segoe UI';}
QLabel{color:#e2e8f0;background:transparent;}
QLineEdit,QTextEdit,QSpinBox,QDoubleSpinBox,QComboBox{
  background:#1e293b;color:#e2e8f0;border:1px solid #334155;
  border-radius:8px;padding:8px 12px;font-size:13px;}
QLineEdit:focus,QTextEdit:focus,QSpinBox:focus,QDoubleSpinBox:focus,QComboBox:focus{
  border:1px solid #3b82f6;}
QComboBox::drop-down{border:none;width:28px;}
QComboBox::down-arrow{image:none;border-left:5px solid transparent;
  border-right:5px solid transparent;border-top:6px solid #94a3b8;margin-right:8px;}
QComboBox QAbstractItemView{background:#1e293b;color:#e2e8f0;
  selection-background-color:#2563eb;border:1px solid #334155;}
QTableWidget{background:#1e293b;color:#e2e8f0;border:none;
  gridline-color:#273549;border-radius:8px;font-size:12px;
  alternate-background-color:#162032;}
QTableWidget::item{padding:6px 8px;}
QTableWidget::item:selected{background:#2563eb;}
QHeaderView::section{background:#0f172a;color:#94a3b8;border:none;
  padding:8px;font-size:12px;font-weight:600;border-bottom:1px solid #334155;}
QScrollBar:vertical{background:#1e293b;}
QScrollBar::handle:vertical{background:#334155;}
QScrollBar:horizontal{background:#1e293b;}
QScrollBar::handle:horizontal{background:#334155;}
QFrame#card{background:#1e293b;border-radius:12px;border:1px solid #273549;}
QFrame#sideNav{background:#0a0d14;border-right:1px solid #1e293b;}
QStatusBar{background:#0a0d14;color:#64748b;font-size:12px;}
QDialog{background:#1e293b;}
QMessageBox{background:#1e293b;color:#e2e8f0;}
QWidget#txRow{background:transparent;}
"""

STYLE_LIGHT = _BTN_COMMON + """
QMainWindow,QWidget{background:#f1f5f9;color:#1e293b;font-family:'Segoe UI';}
QLabel{color:#1e293b;background:transparent;}
QLineEdit,QTextEdit,QSpinBox,QDoubleSpinBox,QComboBox{
  background:#ffffff;color:#1e293b;border:1px solid #cbd5e1;
  border-radius:8px;padding:8px 12px;font-size:13px;}
QLineEdit:focus,QTextEdit:focus,QSpinBox:focus,QDoubleSpinBox:focus,QComboBox:focus{
  border:1px solid #2563eb;}
QComboBox::drop-down{border:none;width:28px;}
QComboBox::down-arrow{image:none;border-left:5px solid transparent;
  border-right:5px solid transparent;border-top:6px solid #64748b;margin-right:8px;}
QComboBox QAbstractItemView{background:#ffffff;color:#1e293b;
  selection-background-color:#2563eb;border:1px solid #cbd5e1;}
QTableWidget{background:#ffffff;color:#1e293b;border:none;
  gridline-color:#e2e8f0;border-radius:8px;font-size:12px;
  alternate-background-color:#f8fafc;}
QTableWidget::item{padding:6px 8px;}
QTableWidget::item:selected{background:#2563eb;color:#fff;}
QHeaderView::section{background:#e2e8f0;color:#64748b;border:none;
  padding:8px;font-size:12px;font-weight:600;border-bottom:1px solid #cbd5e1;}
QScrollBar:vertical{background:#e2e8f0;}
QScrollBar::handle:vertical{background:#94a3b8;}
QScrollBar:horizontal{background:#e2e8f0;}
QScrollBar::handle:horizontal{background:#94a3b8;}
QFrame#card{background:#ffffff;border-radius:12px;border:1px solid #e2e8f0;}
QFrame#sideNav{background:#e2e8f0;border-right:1px solid #cbd5e1;}
QPushButton#btnNav{background:transparent;color:#64748b;border:none;
  border-radius:8px;padding:8px 16px;font-size:13px;font-weight:600;
  min-width:100px;min-height:34px;}
QPushButton#btnNav:hover{background:#cbd5e1;color:#1e293b;}
QStatusBar{background:#e2e8f0;color:#64748b;font-size:12px;}
QDialog{background:#f1f5f9;}
QMessageBox{background:#f1f5f9;color:#1e293b;}
QWidget#txRow{background:transparent;}
"""

# ─── HELPERS ──────────────────────────────────────────────────────────────────
def card(parent=None):
    f = QFrame(parent); f.setObjectName("card"); return f

def label(text, size=13, bold=False, color="#e2e8f0"):
    l = QLabel(text)
    f = l.font(); f.setPointSize(size)
    if bold: f.setBold(True)
    l.setFont(f); l.setStyleSheet(f"color:{color};background:transparent;")
    return l

def hline():
    f = QFrame(); f.setFrameShape(QFrame.HLine)
    f.setStyleSheet("color:#273549;"); return f

# ─── CHART PANEL (başlık + legend + barlar + gün etiketleri tek widget) ──────────────
class BarChart(QWidget):
    """Tüm çizimi (başlık, legend, barlar, gün etiketleri) kendi paintEvent'i içinde yapar."""
    TITLE_H  = 28
    LEGEND_H = 22
    LABEL_H  = 20
    PAD_L    = 16
    PAD_R    = 16

    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.data = data
        self._hover_i = -1
        self.setMinimumHeight(220)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMouseTracking(True)   # tıklamadan fare hareketi al

    def set_data(self, data):
        self.data = data; self.update()

    def _slot_index(self, mx):
        """Fare x koordinatından hangi slot'ta olduğunu döndür."""
        if not self.data: return -1
        W = self.width()
        slot_w = (W - self.PAD_L - self.PAD_R) / len(self.data)
        i = int((mx - self.PAD_L) / slot_w)
        return i if 0 <= i < len(self.data) else -1

    def mouseMoveEvent(self, e):
        i = self._slot_index(e.x())
        if i != self._hover_i:
            self._hover_i = i
            self.update()
        if i >= 0:
            d = self.data[i]
            txt = (f"📅 {d.get('label','')}\n"
                   f"↑ Giriş : {d.get('in', 0)}\n"
                   f"↓ Çıkış : {d.get('out', 0)}")
            QToolTip.showText(e.globalPos(), txt, self)
        else:
            QToolTip.hideText()

    def leaveEvent(self, e):
        self._hover_i = -1
        self.update()
        QToolTip.hideText()

    def paintEvent(self, e):
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        W, H = self.width(), self.height()

        title_y  = 0
        legend_y = self.TITLE_H
        bar_top  = self.TITLE_H + self.LEGEND_H
        bar_bot  = H - self.LABEL_H
        bar_h    = bar_bot - bar_top

        # ── 1. BAŞLIK ──
        p.setPen(QColor("#e2e8f0"))
        p.setFont(QFont("Segoe UI", 11, QFont.Bold))
        p.drawText(QRectF(self.PAD_L, title_y, W - self.PAD_L - self.PAD_R, self.TITLE_H),
                   Qt.AlignLeft | Qt.AlignVCenter, "Haftalık Hareketler")

        # ── 2. LEGEND ──
        p.setFont(QFont("Segoe UI", 9))
        sq = 10
        lx = self.PAD_L
        ly = int(legend_y + (self.LEGEND_H - sq) / 2)
        p.fillRect(QRectF(lx, ly, sq, sq), QColor("#3b82f6"))
        p.setPen(QColor("#94a3b8"))
        p.drawText(QRectF(lx + sq + 4, legend_y, 50, self.LEGEND_H),
                   Qt.AlignLeft | Qt.AlignVCenter, "Giriş")
        lx2 = lx + sq + 4 + 46
        p.fillRect(QRectF(lx2, ly, sq, sq), QColor("#f59e0b"))
        p.setPen(QColor("#94a3b8"))
        p.drawText(QRectF(lx2 + sq + 4, legend_y, 50, self.LEGEND_H),
                   Qt.AlignLeft | Qt.AlignVCenter, "Çıkış")

        if not self.data or bar_h <= 0:
            p.setPen(QColor("#273549"))
            for i in range(4):
                y = int(bar_top + i * bar_h / 3)
                p.drawLine(self.PAD_L, y, W - self.PAD_R, y)
            return

        # ── 3. BARLAR ──
        n = len(self.data)
        max_v = max(max(d.get("in", 0), d.get("out", 0)) for d in self.data) or 1
        slot_w = (W - self.PAD_L - self.PAD_R) / n

        # yatay ızgara çizgileri
        p.setPen(QColor("#273549"))
        for i in range(5):
            y = int(bar_top + i * bar_h / 4)
            p.drawLine(self.PAD_L, y, W - self.PAD_R, y)

        f_lbl = QFont("Segoe UI", 8)
        for i, d in enumerate(self.data):
            x   = self.PAD_L + i * slot_w
            gap = 4
            # Slot'un %78'ini barlar doldursun — dolgun görünüm
            total_bar_w = slot_w * 0.78
            bw  = (total_bar_w - gap) / 2
            bw  = max(8, bw)
            rx  = x + (slot_w - 2 * bw - gap) / 2

            # Hover vurgulama — hafif beyaz overlay
            if self._hover_i == i:
                p.fillRect(QRectF(x + 1, bar_top, slot_w - 2, bar_h),
                           QColor(255, 255, 255, 22))

            # Giriş barı — mavi, yuvarlatılmış üst köşe
            hIN = (d.get("in", 0) / max_v) * bar_h
            if hIN > 0:
                path = QPainterPath()
                path.addRoundedRect(QRectF(rx, bar_bot - hIN, bw, hIN), 3, 3)
                p.fillPath(path, QColor("#3b82f6" if self._hover_i != i else "#60a5fa"))

            # Çıkış barı — turuncu, yuvarlatılmış üst köşe
            hOUT = (d.get("out", 0) / max_v) * bar_h
            if hOUT > 0:
                path2 = QPainterPath()
                path2.addRoundedRect(QRectF(rx + bw + gap, bar_bot - hOUT, bw, hOUT), 3, 3)
                p.fillPath(path2, QColor("#f59e0b" if self._hover_i != i else "#fbbf24"))

            # Gün etiketi
            p.setPen(QColor("#94a3b8" if self._hover_i == i else "#64748b"))
            p.setFont(f_lbl)
            p.drawText(QRectF(x, bar_bot + 2, slot_w, self.LABEL_H),
                       Qt.AlignHCenter, d.get("label", ""))

# ─── STAT CARD ────────────────────────────────────────────────────────────────
def stat_card(title, value, sub, color="#3b82f6", icon="📦"):
    f = card()
    lay = QVBoxLayout(f); lay.setContentsMargins(18,16,18,16); lay.setSpacing(4)
    
    top = QHBoxLayout()
    ico = label(icon, 20)
    ico.setStyleSheet("color:#94a3b8;background:transparent;")
    top.addWidget(ico)
    top.addStretch()
    lay.addLayout(top)
    
    lay.addStretch() # Push texts downwards slightly so they use the space
    
    title_lbl = label(title, 13, False, "#94a3b8")
    title_lbl.setAlignment(Qt.AlignLeft)
    lay.addWidget(title_lbl)

    val_lbl = label(value, 26, True, color)
    val_lbl.setObjectName("val_lbl")
    val_lbl.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
    lay.addWidget(val_lbl)
    
    f.setFixedHeight(135)
    return f

# ─── DASHBOARD PAGE ───────────────────────────────────────────────────────────
class DashboardPage(QWidget):
    def __init__(self):
        super().__init__()
        self._build()

    def _build(self):
        root = QVBoxLayout(self); root.setContentsMargins(24,20,24,20); root.setSpacing(16)
        root.addWidget(label("Dashboard", 18, True))

        # stat cards
        self.c_total = stat_card("Toplam Ürün","0","ürün çeşidi","#3b82f6","📦")
        self.c_value = stat_card("Stok Değeri","₺0","toplam değer","#10b981","💰")
        self.c_crit  = stat_card("Kritik Stok","0","düşük stok uyarısı","#f59e0b","⚠️")
        cr = QHBoxLayout(); cr.setSpacing(14)
        for c_ in [self.c_total, self.c_value, self.c_crit]:
            cr.addWidget(c_)
        root.addLayout(cr)

        # chart + recent
        mid = QHBoxLayout(); mid.setSpacing(14)

        # chart — BarChart kendi içinde başlık+legend+barlar+etiketleri çiziyor
        chart_f = card()
        cl = QVBoxLayout(chart_f)
        cl.setContentsMargins(12, 10, 12, 10)
        cl.setSpacing(0)
        self.chart = BarChart([])
        cl.addWidget(self.chart)
        mid.addWidget(chart_f, 2)

        # recent tx
        rec_f = card(); rl = QVBoxLayout(rec_f); rl.setContentsMargins(16,14,16,14); rl.setSpacing(8)
        rl.addWidget(label("Son İşlemler",13,True))
        self.recent_layout = QVBoxLayout(); self.recent_layout.setSpacing(4)
        rl.addLayout(self.recent_layout)
        rl.addStretch()
        mid.addWidget(rec_f, 1)

        root.addLayout(mid)
        self.refresh()

    def refresh(self):
        stats = db.get_stats()
        # update cards
        for w in self.c_total.children():
            if isinstance(w, QLabel) and w.text().startswith("0") or (isinstance(w,QLabel) and "₺" in w.text()):
                pass
        # easier: rebuild label texts
        self._set_card(self.c_total, str(stats["total"]), "Toplam Ürün", "#3b82f6")
        self._set_card(self.c_value, f"₺{stats['value']:,.0f}", "Stok Değeri", "#10b981")
        self._set_card(self.c_crit,  str(stats["critical"]), "Kritik Stok", "#f59e0b")
        self.chart.set_data(stats["chart"])
        # recent
        while self.recent_layout.count():
            item = self.recent_layout.takeAt(0)
            if item.widget(): item.widget().deleteLater()
        for tx in stats["recent"][:7]:
            color = "#10b981" if tx["type"]=="Stok Giriş" else "#ef4444"
            ico   = "↑" if tx["type"]=="Stok Giriş" else "↓"
            row   = QHBoxLayout()
            row.setContentsMargins(4, 2, 4, 2)
            lbl_name = label(f"{ico} {tx['name'][:22]}", 11, False, color)
            lbl_name.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            lbl_qty = label(f"+{tx['quantity']}" if ico=="↑" else f"-{tx['quantity']}", 11, True, color)
            lbl_qty.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            row.addWidget(lbl_name)
            row.addStretch()
            row.addWidget(lbl_qty)
            w = QWidget(); w.setObjectName("txRow"); w.setLayout(row)
            w.setAttribute(Qt.WA_TranslucentBackground, True)
            self.recent_layout.addWidget(w)

    def _set_card(self, f, val, title, color):
        lbl = f.findChild(QLabel, "val_lbl")
        if lbl: lbl.setText(val); lbl.setStyleSheet(f"color:{color};background:transparent;")


# ─── INVENTORY PAGE ───────────────────────────────────────────────────────────
class InventoryPage(QWidget):
    edit_requested  = pyqtSignal(dict)
    stock_requested = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self._page = 1; self._per = 15; self._total = 0
        self._build()

    def _build(self):
        root = QVBoxLayout(self); root.setContentsMargins(24,20,24,20); root.setSpacing(14)

        # header
        hdr = QHBoxLayout()
        hdr.addWidget(label("Envanter Listesi",18,True))
        hdr.addStretch()
        b_add = QPushButton("+ Ürün Ekle"); b_add.clicked.connect(self._add)
        b_tx  = QPushButton("⇅ Stok Giriş/Çıkış"); b_tx.setObjectName("btnSuccess")
        b_tx.clicked.connect(self._stock)
        hdr.addWidget(b_tx); hdr.addWidget(b_add)
        root.addLayout(hdr)

        # filters
        fil = QHBoxLayout(); fil.setSpacing(8)
        self.s_search = QLineEdit(); self.s_search.setPlaceholderText("🔍  Ara...")
        self.s_search.textChanged.connect(self._filter)
        self.s_cat = QComboBox()
        self.s_cat.addItems(["Tümü"] + db.CATEGORIES)
        self.s_cat.currentTextChanged.connect(self._filter)
        b_ref = QPushButton("↺"); b_ref.setFixedWidth(38); b_ref.clicked.connect(self.refresh)
        fil.addWidget(self.s_search, 2); fil.addWidget(self.s_cat, 1); fil.addWidget(b_ref)
        root.addLayout(fil)

        # table
        self.table = QTableWidget()
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels(["SKU","Ürün Adı","Kategori","Raf","Miktar","Fiyat","Min.Stok","İşlem"])
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.verticalHeader().setVisible(False)
        self.table.verticalHeader().setDefaultSectionSize(46)
        self.table.setAlternatingRowColors(True)
        root.addWidget(self.table)

        # pagination
        pg = QHBoxLayout()
        self.b_prev = QPushButton("‹ Önceki"); self.b_prev.setObjectName("btnGray")
        self.b_next = QPushButton("Sonraki ›"); self.b_next.setObjectName("btnGray")
        self.lbl_pg = label("Sayfa 1", 11, False, "#94a3b8")
        self.b_prev.clicked.connect(self._prev); self.b_next.clicked.connect(self._next)
        pg.addWidget(self.b_prev); pg.addStretch()
        pg.addWidget(self.lbl_pg); pg.addStretch(); pg.addWidget(self.b_next)
        root.addLayout(pg)
        self.refresh()

    def refresh(self):
        search = self.s_search.text(); cat = self.s_cat.currentText()
        rows, total = db.get_products(search, cat, self._page, self._per)
        self._total = total
        pages = max(1, (total + self._per - 1) // self._per)
        self.lbl_pg.setText(f"Sayfa {self._page} / {pages}  ({total} kayıt)")
        self.b_prev.setEnabled(self._page > 1)
        self.b_next.setEnabled(self._page < pages)
        self.table.setRowCount(0)
        for r in rows:
            ri = self.table.rowCount(); self.table.insertRow(ri)
            qty_color = "#ef4444" if r["quantity"] <= r["min_stock"] else "#e2e8f0"
            for ci, (k, fmt) in enumerate([
                ("sku", lambda v: v),
                ("name", lambda v: v),
                ("category", lambda v: v),
                ("shelf", lambda v: v),
                ("quantity", lambda v: str(v)),
                ("price", lambda v: f"₺{v:,.2f}"),
                ("min_stock", lambda v: str(v)),
            ]):
                it = QTableWidgetItem(fmt(r[k]))
                it.setData(Qt.UserRole, r["id"])
                if k == "quantity":
                    it.setForeground(QColor(qty_color))
                self.table.setItem(ri, ci, it)
            # action buttons
            w = QWidget(); hl = QHBoxLayout(w); hl.setContentsMargins(4,4,4,4); hl.setSpacing(6)
            be = QPushButton("✏"); be.setToolTip("Düzenle")
            be.setFixedSize(32, 32)
            be.setStyleSheet("QPushButton { background-color: #2563eb; color: white; padding: 0px; border-radius: 6px; font-size: 16px; } QPushButton:hover { background-color: #3b82f6; }")
            bd = QPushButton("🗑"); bd.setToolTip("Sil")
            bd.setFixedSize(32, 32)
            bd.setStyleSheet("QPushButton { background-color: #dc2626; color: white; padding: 0px; border-radius: 6px; font-size: 16px; } QPushButton:hover { background-color: #ef4444; }")
            be.clicked.connect(lambda _, row=r: self.edit_requested.emit(row))
            bd.clicked.connect(lambda _, pid=r["id"]: self._delete(pid))
            hl.addWidget(be); hl.addWidget(bd)
            self.table.setCellWidget(ri, 7, w)

    def _filter(self): self._page = 1; self.refresh()
    def _prev(self): self._page -= 1; self.refresh()
    def _next(self): self._page += 1; self.refresh()
    def _add(self): self.edit_requested.emit({})
    def _stock(self):
        row = self.table.currentRow()
        if row < 0: self.stock_requested.emit({}); return
        pid = self.table.item(row, 0).data(Qt.UserRole)
        self.stock_requested.emit(db.get_product(pid) or {})
    def _delete(self, pid):
        if QMessageBox.question(self,"Sil","Bu ürünü silmek istiyor musunuz?",
            QMessageBox.Yes|QMessageBox.No) == QMessageBox.Yes:
            db.delete_product(pid); self.refresh()


# ─── ADD / EDIT PRODUCT DIALOG ────────────────────────────────────────────────
class ProductDialog(QDialog):
    def __init__(self, product=None, parent=None):
        super().__init__(parent)
        self.product = product or {}
        self.image_path = self.product.get("image_path","")
        self.setWindowTitle("Ürün Ekle" if not self.product else "Ürünü Düzenle")
        self.setMinimumWidth(460)
        self._build()

    def _build(self):
        lay = QVBoxLayout(self); lay.setContentsMargins(24,20,24,20); lay.setSpacing(14)
        lay.addWidget(label("Ürün Bilgileri",15,True))
        lay.addWidget(hline())

        form = QFormLayout(); form.setSpacing(10)

        # Category (first so SKU can be generated)
        self.f_cat = QComboBox(); self.f_cat.addItems(db.CATEGORIES)
        if self.product.get("category"): self.f_cat.setCurrentText(self.product["category"])
        form.addRow("Kategori *", self.f_cat)

        # SKU
        sku_row = QHBoxLayout()
        self.f_sku = QLineEdit(self.product.get("sku",""))
        self.f_sku.setPlaceholderText("Otomatik oluştur...")
        b_gen = QPushButton("Oluştur"); b_gen.setFixedWidth(90)
        b_gen.clicked.connect(self._gen_sku)
        sku_row.addWidget(self.f_sku); sku_row.addWidget(b_gen)
        form.addRow("SKU *", sku_row)

        self.f_name  = QLineEdit(self.product.get("name",""))
        self.f_name.setPlaceholderText("Ürün adı...")
        form.addRow("Ürün Adı *", self.f_name)

        self.f_shelf = QComboBox()
        shelves = ["Raf A1","Raf A2","Raf B1","Raf B2","Raf C1","Raf C2","Raf D1"]
        self.f_shelf.addItems(shelves)
        if self.product.get("shelf"): self.f_shelf.setCurrentText(self.product["shelf"])
        form.addRow("Raf Konumu *", self.f_shelf)

        self.f_qty = QSpinBox(); self.f_qty.setRange(0,999999)
        self.f_qty.setValue(self.product.get("quantity",0))
        form.addRow("Miktar", self.f_qty)

        self.f_price = QDoubleSpinBox(); self.f_price.setRange(0,9999999); self.f_price.setDecimals(2)
        self.f_price.setPrefix("₺ "); self.f_price.setValue(self.product.get("price",0.0))
        form.addRow("Fiyat", self.f_price)

        self.f_min = QSpinBox(); self.f_min.setRange(0,9999)
        self.f_min.setValue(self.product.get("min_stock",5))
        form.addRow("Min. Stok", self.f_min)

        lay.addLayout(form)

        # image picker
        img_row = QHBoxLayout()
        self.lbl_img = label("Resim seçilmedi",11,False,"#64748b")
        if self.image_path: self.lbl_img.setText(os.path.basename(self.image_path))
        b_img = QPushButton("📷 Resim Seç"); b_img.setObjectName("btnGray")
        b_img.clicked.connect(self._pick_image)
        img_row.addWidget(self.lbl_img); img_row.addStretch(); img_row.addWidget(b_img)
        lay.addLayout(img_row)

        lay.addWidget(hline())

        # buttons
        btn_row = QHBoxLayout()
        b_save = QPushButton("💾 Kaydet")
        b_cancel = QPushButton("İptal"); b_cancel.setObjectName("btnGray")
        b_save.clicked.connect(self._save); b_cancel.clicked.connect(self.reject)
        btn_row.addStretch(); btn_row.addWidget(b_cancel); btn_row.addWidget(b_save)
        lay.addLayout(btn_row)

    def _gen_sku(self):
        cat = self.f_cat.currentText()
        self.f_sku.setText(db.generate_sku(cat))

    def _pick_image(self):
        path, _ = QFileDialog.getOpenFileName(self,"Resim Seç","",
                    "Resimler (*.png *.jpg *.jpeg *.bmp *.gif)")
        if path:
            self.image_path = path
            self.lbl_img.setText(os.path.basename(path))

    def _save(self):
        import os as _os
        name  = self.f_name.text().strip()
        sku   = self.f_sku.text().strip()
        if not name or not sku:
            QMessageBox.warning(self,"Hata","Ürün adı ve SKU zorunludur!")
            return
        cat   = self.f_cat.currentText()
        shelf = self.f_shelf.currentText()
        qty   = self.f_qty.value()
        price = self.f_price.value()
        mins  = self.f_min.value()
        if self.product.get("id"):
            db.update_product(self.product["id"],name,cat,shelf,qty,price,mins,self.image_path)
        else:
            db.add_product(sku,name,cat,shelf,qty,price,mins,self.image_path)
        self.accept()


# ─── STOCK IN/OUT DIALOG ──────────────────────────────────────────────────────
class StockDialog(QDialog):
    def __init__(self, product=None, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Stok Giriş / Çıkış")
        self.setMinimumWidth(400)
        self.product = product
        self._build()

    def _build(self):
        lay = QVBoxLayout(self); lay.setContentsMargins(24,20,24,20); lay.setSpacing(14)
        lay.addWidget(label("Stok Giriş / Çıkış",15,True))
        lay.addWidget(hline())

        form = QFormLayout(); form.setSpacing(10)

        # product search
        self.f_product = QComboBox()
        self.f_product.setEditable(True)
        self.f_product.setPlaceholderText("Ürün ara / seç...")
        rows, _ = db.get_products(per_page=500)
        self._products = rows
        for r in rows:
            self.f_product.addItem(f"{r['sku']} — {r['name']}", r["id"])
        if self.product and self.product.get("id"):
            for i in range(self.f_product.count()):
                if self.f_product.itemData(i) == self.product["id"]:
                    self.f_product.setCurrentIndex(i); break
        form.addRow("Ürün *", self.f_product)

        self.f_type = QComboBox()
        self.f_type.addItems(["Stok Giriş","Stok Çıkış","İade"])
        form.addRow("İşlem Tipi", self.f_type)

        self.f_qty = QSpinBox(); self.f_qty.setRange(1,99999); self.f_qty.setValue(1)
        form.addRow("Miktar *", self.f_qty)

        self.f_note = QLineEdit(); self.f_note.setPlaceholderText("Not (isteğe bağlı)...")
        form.addRow("Not", self.f_note)

        lay.addLayout(form)
        lay.addWidget(hline())

        btn_row = QHBoxLayout()
        b_save = QPushButton("💾 Kaydet"); b_save.setObjectName("btnSuccess")
        b_cancel = QPushButton("İptal"); b_cancel.setObjectName("btnGray")
        b_save.clicked.connect(self._save); b_cancel.clicked.connect(self.reject)
        btn_row.addStretch(); btn_row.addWidget(b_cancel); btn_row.addWidget(b_save)
        lay.addLayout(btn_row)

    def _save(self):
        pid = self.f_product.currentData()
        if not pid:
            QMessageBox.warning(self,"Hata","Lütfen bir ürün seçin!"); return
        db.add_transaction(pid, self.f_type.currentText(),
                           self.f_qty.value(), self.f_note.text())
        self.accept()


# ─── TRANSACTIONS PAGE ────────────────────────────────────────────────────────
class TransactionsPage(QWidget):
    def __init__(self):
        super().__init__()
        self._page = 1; self._per = 20
        self._build()

    def _build(self):
        root = QVBoxLayout(self); root.setContentsMargins(24,20,24,20); root.setSpacing(14)

        hdr = QHBoxLayout()
        hdr.addWidget(label("Hareketler",18,True))
        hdr.addStretch()
        b_add = QPushButton("+ Yeni Hareket")
        b_add.clicked.connect(self._new_tx)
        hdr.addWidget(b_add)
        root.addLayout(hdr)

        fil = QHBoxLayout(); fil.setSpacing(8)
        self.s_search = QLineEdit(); self.s_search.setPlaceholderText("🔍  Ara...")
        self.s_search.textChanged.connect(self._filter)
        self.s_type = QComboBox()
        self.s_type.addItems(["Tümü","Stok Giriş","Stok Çıkış","İade"])
        self.s_type.currentTextChanged.connect(self._filter)
        b_ref = QPushButton("↺"); b_ref.setFixedWidth(38); b_ref.clicked.connect(self.refresh)
        fil.addWidget(self.s_search,2); fil.addWidget(self.s_type,1); fil.addWidget(b_ref)
        root.addLayout(fil)

        self.table = QTableWidget()
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels(["#","SKU","Ürün Adı","İşlem","Miktar","Kategori","Raf","Tarih"])
        self.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.verticalHeader().setVisible(False)
        self.table.setAlternatingRowColors(True)
        root.addWidget(self.table)

        pg = QHBoxLayout()
        self.b_prev = QPushButton("‹ Önceki"); self.b_prev.setObjectName("btnGray")
        self.b_next = QPushButton("Sonraki ›"); self.b_next.setObjectName("btnGray")
        self.lbl_pg = label("Sayfa 1",11,False,"#94a3b8")
        self.b_prev.clicked.connect(self._prev); self.b_next.clicked.connect(self._next)
        pg.addWidget(self.b_prev); pg.addStretch(); pg.addWidget(self.lbl_pg)
        pg.addStretch(); pg.addWidget(self.b_next)
        root.addLayout(pg)
        self.refresh()

    def refresh(self):
        rows, total = db.get_transactions(self.s_search.text(),
                                          self.s_type.currentText(),
                                          self._page, self._per)
        pages = max(1,(total+self._per-1)//self._per)
        self.lbl_pg.setText(f"Sayfa {self._page}/{pages}  ({total} kayıt)")
        self.b_prev.setEnabled(self._page>1)
        self.b_next.setEnabled(self._page<pages)
        self.table.setRowCount(0)
        for r in rows:
            ri = self.table.rowCount(); self.table.insertRow(ri)
            color = "#10b981" if r["type"]=="Stok Giriş" else ("#f59e0b" if r["type"]=="İade" else "#ef4444")
            vals  = [str(r["id"]),r["sku"],r["name"],r["type"],str(r["quantity"]),
                     r["category"],r["shelf"],r["date"][:16]]
            for ci,v in enumerate(vals):
                it = QTableWidgetItem(v)
                if ci==3: it.setForeground(QColor(color))
                self.table.setItem(ri,ci,it)

    def _filter(self): self._page=1; self.refresh()
    def _prev(self): self._page-=1; self.refresh()
    def _next(self): self._page+=1; self.refresh()
    def _new_tx(self):
        dlg = StockDialog(parent=self)
        if dlg.exec_() == QDialog.Accepted: self.refresh()


# ─── SETTINGS PAGE ────────────────────────────────────────────────────────────
class SettingsPage(QWidget):
    def __init__(self):
        super().__init__()
        self._build()

    def _build(self):
        root = QVBoxLayout(self); root.setContentsMargins(24,20,24,20); root.setSpacing(16)
        root.addWidget(label("Ayarlar",18,True))

        s = db.get_all_settings()

        # ── Görünüm / Tema kartı ──────────────────────────────────────────────
        ct = card(); lt = QVBoxLayout(ct); lt.setContentsMargins(20,16,20,16); lt.setSpacing(14)
        lt.addWidget(label("Görünüm",13,True))
        lt.addWidget(hline())

        theme_row = QHBoxLayout(); theme_row.setSpacing(12)
        theme_row.addWidget(label("Tema:",12,False,"#94a3b8"))

        self._current_theme = db.get_setting("theme","dark")

        self.btn_dark  = QPushButton("🌙  Koyu (Dark)")
        self.btn_light = QPushButton("☀️  Açık (Light)")
        self.btn_dark.setCheckable(True);  self.btn_dark.setObjectName("btnGray")
        self.btn_light.setCheckable(True); self.btn_light.setObjectName("btnGray")
        self._update_theme_btns()
        self.btn_dark.clicked.connect(lambda: self._apply_theme("dark"))
        self.btn_light.clicked.connect(lambda: self._apply_theme("light"))
        theme_row.addWidget(self.btn_dark)
        theme_row.addWidget(self.btn_light)
        theme_row.addStretch()
        lt.addLayout(theme_row)
        root.addWidget(ct)

        # ── Genel Ayarlar kartı ───────────────────────────────────────────────
        c1 = card(); l1 = QVBoxLayout(c1); l1.setContentsMargins(20,16,20,16); l1.setSpacing(10)
        l1.addWidget(label("Genel Ayarlar",13,True))
        l1.addWidget(hline())
        form1 = QFormLayout(); form1.setSpacing(10)

        # Şirket adı — sadece görüntüleme, değiştirilemez
        lbl_company = QLabel(COMPANY_NAME)
        lbl_company.setObjectName("companyLabel")
        lbl_company.setEnabled(False)  # grileştirir, temanın disabled stilini kullanır
        form1.addRow("Şirket Adı", lbl_company)

        self.f_currency = QComboBox(); self.f_currency.addItems(["₺","$","€","£"])
        self.f_currency.setCurrentText(s.get("currency","₺"))
        self.f_threshold = QSpinBox(); self.f_threshold.setRange(1,9999)
        self.f_threshold.setValue(int(s.get("low_stock_threshold","10")))
        form1.addRow("Para Birimi", self.f_currency)
        form1.addRow("Kritik Stok Eşiği", self.f_threshold)
        l1.addLayout(form1)
        root.addWidget(c1)

        # ── Veritabanı kartı ──────────────────────────────────────────────────
        c2 = card(); l2 = QVBoxLayout(c2); l2.setContentsMargins(20,16,20,16); l2.setSpacing(10)
        l2.addWidget(label("Veritabanı",13,True))
        l2.addWidget(hline())
        import database
        db_path_lbl = label(database.DB_PATH,11,False,"#64748b")
        db_path_lbl.setWordWrap(True)
        l2.addWidget(label("Veritabanı Yolu:",11,False,"#94a3b8"))
        l2.addWidget(db_path_lbl)
        btn_backup = QPushButton("💾 Yedek Al"); btn_backup.setObjectName("btnGray")
        btn_backup.clicked.connect(self._backup)
        l2.addWidget(btn_backup)
        root.addWidget(c2)

        # ── Hakkında kartı ────────────────────────────────────────────────────
        c3 = card(); l3 = QVBoxLayout(c3); l3.setContentsMargins(20,16,20,16); l3.setSpacing(6)
        l3.addWidget(label("Hakkında",13,True))
        l3.addWidget(hline())
        l3.addWidget(label("DEPO PRO — Depo & Stok Yönetim Sistemi",12,False,"#94a3b8"))
        l3.addWidget(label("Versiyon 1.0.0",11,False,"#64748b"))
        l3.addWidget(label("PyQt5 ile geliştirilmiştir.",11,False,"#64748b"))
        root.addWidget(c3)

        root.addStretch()

        btn_row = QHBoxLayout()
        b_save = QPushButton("💾 Ayarları Kaydet")
        b_save.clicked.connect(self._save)
        btn_row.addStretch(); btn_row.addWidget(b_save)
        root.addLayout(btn_row)

    def _update_theme_btns(self):
        is_dark = (self._current_theme == "dark")
        self.btn_dark.setStyleSheet(
            "QPushButton{background:#2563eb;color:#fff;}" if is_dark else "")
        self.btn_light.setStyleSheet(
            "QPushButton{background:#2563eb;color:#fff;}" if not is_dark else "")

    def _apply_theme(self, theme):
        self._current_theme = theme
        db.set_setting("theme", theme)
        app = QApplication.instance()
        # Temayı uygula — önce sıfırla, sonra yeni stili ver
        app.setStyleSheet("")
        app.setStyleSheet(STYLE if theme == "dark" else STYLE_LIGHT)
        # Tüm widget'ları yeniden polish et
        for w in app.allWidgets():
            w.style().unpolish(w)
            w.style().polish(w)
            w.update()
        self._update_theme_btns()

    def _save(self):
        # Şirket adı sabit — kaydedilmez
        db.set_setting("currency",            self.f_currency.currentText())
        db.set_setting("low_stock_threshold", str(self.f_threshold.value()))
        QMessageBox.information(self,"Kaydedildi","Ayarlar başarıyla kaydedildi.")

    def _backup(self):
        import shutil, database
        path, _ = QFileDialog.getSaveFileName(self,"Yedek Kaydet","depo_backup.db","SQLite (*.db)")
        if path:
            shutil.copy2(database.DB_PATH, path)
            QMessageBox.information(self,"Başarılı",f"Yedek oluşturuldu:\n{path}")


# ─── MAIN WINDOW ─────────────────────────────────────────────────────────────
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DEPO PRO — Depo & Stok Yönetim Sistemi")
        self.setMinimumSize(1100, 680)
        self.resize(1280, 760)
        # Stil app seviyesinde uygulanıyor — burada tekrar set edilmez
        self._build()
        self._nav_to(0)

    def _build(self):
        central = QWidget(); self.setCentralWidget(central)
        main_lay = QVBoxLayout(central); main_lay.setContentsMargins(0,0,0,0); main_lay.setSpacing(0)

        # ── top navbar ──
        nav = QFrame(); nav.setObjectName("sideNav")
        nav.setFixedHeight(54)
        nav_lay = QHBoxLayout(nav); nav_lay.setContentsMargins(16,6,16,6); nav_lay.setSpacing(6)

        # logo
        logo = label("📦 DEPO PRO", 14, True, "#3b82f6")
        nav_lay.addWidget(logo)
        nav_lay.addSpacing(20)

        # nav buttons
        self._nav_btns = []
        nav_items = [
            ("🏠  Dashboard","dashboard"),
            ("📋  Envanter","inventory"),
            ("➕  Ürün Ekle","add_product"),
            ("🔄  Hareketler","transactions"),
            ("⚙️  Ayarlar","settings"),
        ]
        for text, name in nav_items:
            b = QPushButton(text)
            b.setObjectName("btnNav")
            b.setFixedHeight(36)
            b.setMinimumWidth(110)
            b.setProperty("page", name)
            b.clicked.connect(lambda _, n=len(self._nav_btns): self._nav_to(n))
            nav_lay.addWidget(b)
            self._nav_btns.append(b)

        nav_lay.addStretch()

        # status indicator
        self.lbl_status = label("● Online",11,False,"#10b981")
        nav_lay.addWidget(self.lbl_status)

        main_lay.addWidget(nav)

        # ── page stack ──
        self.stack = QStackedWidget()
        self.pg_dash  = DashboardPage()
        self.pg_inv   = InventoryPage()
        self.pg_add   = self._build_add_page()
        self.pg_tx    = TransactionsPage()
        self.pg_set   = SettingsPage()
        for pg in [self.pg_dash, self.pg_inv, self.pg_add, self.pg_tx, self.pg_set]:
            self.stack.addWidget(pg)
        main_lay.addWidget(self.stack)

        # connect inventory signals
        self.pg_inv.edit_requested.connect(self._open_edit)
        self.pg_inv.stock_requested.connect(self._open_stock)

        # status bar
        sb = self.statusBar()
        sb.showMessage("  ● System Status: Online   |   Veritabanı: bağlı   |   DEPO PRO v1.0")

    def _build_add_page(self):
        """Wraps ProductDialog fields in a scroll page for 'Ürün Ekle' tab."""
        w = QWidget()
        lay = QVBoxLayout(w); lay.setContentsMargins(24,20,24,20); lay.setSpacing(14)
        lay.addWidget(label("Yeni Ürün Ekle",18,True))

        scroll = QScrollArea(); scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea{border:none;background:transparent;}")
        inner = QWidget()
        form_lay = QVBoxLayout(inner); form_lay.setContentsMargins(0,0,0,0); form_lay.setSpacing(14)

        cf = card(); cl = QVBoxLayout(cf); cl.setContentsMargins(24,20,24,20); cl.setSpacing(12)
        cl.addWidget(label("Ürün Bilgileri",13,True))
        cl.addWidget(hline())
        form = QFormLayout(); form.setSpacing(10)

        self.af_cat   = QComboBox(); self.af_cat.addItems(db.CATEGORIES)
        sku_r = QHBoxLayout()
        self.af_sku   = QLineEdit(); self.af_sku.setPlaceholderText("Otomatik oluştur...")
        b_gen = QPushButton("Oluştur"); b_gen.setFixedWidth(90)
        b_gen.clicked.connect(lambda: self.af_sku.setText(db.generate_sku(self.af_cat.currentText())))
        sku_r.addWidget(self.af_sku); sku_r.addWidget(b_gen)
        self.af_name  = QLineEdit(); self.af_name.setPlaceholderText("Ürün adını girin...")
        self.af_shelf = QComboBox()
        self.af_shelf.addItems(["Raf A1","Raf A2","Raf B1","Raf B2","Raf C1","Raf C2","Raf D1"])
        self.af_qty   = QSpinBox(); self.af_qty.setRange(0,999999)
        self.af_price = QDoubleSpinBox(); self.af_price.setRange(0,9999999)
        self.af_price.setDecimals(2); self.af_price.setPrefix("₺ ")
        self.af_min   = QSpinBox(); self.af_min.setRange(0,9999); self.af_min.setValue(5)

        form.addRow("Kategori *",   self.af_cat)
        form.addRow("SKU *",        sku_r)
        form.addRow("Ürün Adı *",   self.af_name)
        form.addRow("Raf Konumu *", self.af_shelf)
        form.addRow("Miktar",       self.af_qty)
        form.addRow("Fiyat (₺)",    self.af_price)
        form.addRow("Min. Stok",    self.af_min)
        cl.addLayout(form)

        # image
        img_r = QHBoxLayout()
        self.af_img_path = ""
        self.af_img_lbl  = label("Resim seçilmedi",11,False,"#64748b")
        b_img = QPushButton("📷 Resim Seç"); b_img.setObjectName("btnGray")
        def pick():
            p,_ = QFileDialog.getOpenFileName(self,"Resim Seç","","Resimler (*.png *.jpg *.jpeg)")
            if p:
                self.af_img_path = p
                self.af_img_lbl.setText(os.path.basename(p))
        b_img.clicked.connect(pick)
        img_r.addWidget(self.af_img_lbl); img_r.addStretch(); img_r.addWidget(b_img)
        cl.addLayout(img_r)

        cl.addWidget(hline())
        btn_r = QHBoxLayout()
        b_save  = QPushButton("💾 Ürünü Kaydet")
        b_clear = QPushButton("🗑 Temizle"); b_clear.setObjectName("btnGray")
        b_save.clicked.connect(self._save_new_product)
        b_clear.clicked.connect(self._clear_add_form)
        btn_r.addStretch(); btn_r.addWidget(b_clear); btn_r.addWidget(b_save)
        cl.addLayout(btn_r)

        form_lay.addWidget(cf); form_lay.addStretch()
        scroll.setWidget(inner)
        lay.addWidget(scroll)
        return w

    def _save_new_product(self):
        name  = self.af_name.text().strip()
        sku   = self.af_sku.text().strip()
        if not name or not sku:
            QMessageBox.warning(self,"Hata","Ürün adı ve SKU zorunludur!"); return
        db.add_product(sku, name, self.af_cat.currentText(), self.af_shelf.currentText(),
                       self.af_qty.value(), self.af_price.value(),
                       self.af_min.value(), self.af_img_path)
        QMessageBox.information(self,"Başarılı","Ürün başarıyla kaydedildi!")
        self._clear_add_form()
        self.pg_inv.refresh()
        self.pg_dash.refresh()

    def _clear_add_form(self):
        self.af_name.clear(); self.af_sku.clear()
        self.af_qty.setValue(0); self.af_price.setValue(0)
        self.af_min.setValue(5); self.af_img_path = ""
        self.af_img_lbl.setText("Resim seçilmedi")

    def _nav_to(self, index):
        self.stack.setCurrentIndex(index)
        for i, b in enumerate(self._nav_btns):
            b.setObjectName("btnNavActive" if i == index else "btnNav")
            b.style().unpolish(b)
            b.style().polish(b)
            # Boyutları korumak için sabit değerleri yeniden ata
            b.setFixedHeight(36)
            b.setMinimumWidth(110)
        if index == 0: self.pg_dash.refresh()
        if index == 1: self.pg_inv.refresh()
        if index == 3: self.pg_tx.refresh()

    def _open_edit(self, product):
        dlg = ProductDialog(product, self)
        if dlg.exec_() == QDialog.Accepted:
            self.pg_inv.refresh(); self.pg_dash.refresh()

    def _open_stock(self, product):
        dlg = StockDialog(product or None, self)
        if dlg.exec_() == QDialog.Accepted:
            self.pg_inv.refresh(); self.pg_dash.refresh(); self.pg_tx.refresh()


import os
