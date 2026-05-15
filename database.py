import sqlite3, os, random
from datetime import datetime, timedelta

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "depo.db")

CATEGORIES = ["Elektronik","Giyim","Gıda","Mobilya","Kırtasiye","Spor","Araç-Gereç"]
SHELF_MAP  = {"Elektronik":"Raf A1","Giyim":"Raf B1","Gıda":"Raf C1",
              "Mobilya":"Raf D1","Kırtasiye":"Raf C2","Spor":"Raf B2","Araç-Gereç":"Raf A2"}
SKU_PFX    = {"Elektronik":"ELK","Giyim":"GYM","Gıda":"GDA",
              "Mobilya":"MOB","Kırtasiye":"KRT","Spor":"SPR","Araç-Gereç":"ARG"}

SEED = [
    ("Samsung Galaxy S23","Elektronik",45,12999.90,10),
    ("Apple AirPods Pro","Elektronik",30,4599.90,5),
    ("Polo Tişört Beyaz","Giyim",120,299.90,20),
    ("Denim Jean Slim Fit","Giyim",85,599.90,15),
    ("Organik Zeytinyağı 1L","Gıda",200,189.90,30),
    ("Granola Bar 12li","Gıda",500,29.90,50),
    ("Ergonomik Ofis Koltuğu","Mobilya",12,3499.90,3),
    ("Ayarlanabilir Çalışma Masası","Mobilya",8,2799.90,2),
    ("A4 Fotokopi Kağıdı","Kırtasiye",300,89.90,40),
    ("Tükenmez Kalem Seti","Kırtasiye",150,49.90,30),
    ("Yoga Matı Premium","Spor",60,449.90,10),
    ("Dumbbell Set 20kg","Spor",25,1299.90,5),
    ("Tornavida Seti 18 Parça","Araç-Gereç",40,349.90,8),
    ("Pense Takımı","Araç-Gereç",30,249.90,6),
    ("Kablosuz Mouse","Elektronik",55,399.90,10),
    ("Mekanik Klavye","Elektronik",20,1299.90,4),
    ("Spor Ayakkabı","Spor",70,1799.90,10),
    ("Bisiklet Kaskı","Spor",8,599.90,4),
    ("Notebook A5 Çizgili","Kırtasiye",400,39.90,60),
    ("Makas Seti","Kırtasiye",200,29.90,40),
]

def conn():
    c = sqlite3.connect(DB_PATH)
    c.row_factory = sqlite3.Row
    return c

def init_db():
    db = conn()
    cur = db.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sku TEXT UNIQUE NOT NULL, name TEXT NOT NULL,
        category TEXT NOT NULL, shelf TEXT NOT NULL,
        quantity INTEGER NOT NULL DEFAULT 0,
        price REAL NOT NULL DEFAULT 0.0,
        min_stock INTEGER NOT NULL DEFAULT 5,
        image_path TEXT DEFAULT '', created_at TEXT NOT NULL)""")
    cur.execute("""CREATE TABLE IF NOT EXISTS transactions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER NOT NULL, type TEXT NOT NULL,
        quantity INTEGER NOT NULL, note TEXT DEFAULT '',
        date TEXT NOT NULL, FOREIGN KEY(product_id) REFERENCES products(id))""")
    cur.execute("""CREATE TABLE IF NOT EXISTS settings(
        key TEXT PRIMARY KEY, value TEXT NOT NULL)""")
    defaults = [("company_name","DEPO PRO"),("currency","₺"),
                ("low_stock_threshold","10"),("theme","dark")]
    for k,v in defaults:
        cur.execute("INSERT OR IGNORE INTO settings(key,value) VALUES(?,?)",(k,v))
    db.commit()
    cur.execute("SELECT COUNT(*) FROM products")
    if cur.fetchone()[0] == 0:
        _seed(db)
    db.close()

def _make_sku(cat, used):
    pfx = SKU_PFX.get(cat,"GEN")
    while True:
        s = f"{pfx}-{random.randint(10000,99999)}"
        if s not in used: return s

def _seed(db):
    cur = db.cursor(); used = set()
    for name,cat,qty,price,mins in SEED:
        sku = _make_sku(cat, used); used.add(sku)
        shelf = SHELF_MAP.get(cat,"Raf A1")
        created = (datetime.now()-timedelta(days=random.randint(1,300))).strftime("%Y-%m-%d %H:%M:%S")
        cur.execute("INSERT INTO products(sku,name,category,shelf,quantity,price,min_stock,created_at) VALUES(?,?,?,?,?,?,?,?)",
                    (sku,name,cat,shelf,qty,price,mins,created))
        pid = cur.lastrowid
        for _ in range(random.randint(2,5)):
            t = random.choice(["Stok Giriş","Stok Çıkış"])
            tq = random.randint(1,20)
            td = (datetime.now()-timedelta(days=random.randint(0,180))).strftime("%Y-%m-%d %H:%M:%S")
            cur.execute("INSERT INTO transactions(product_id,type,quantity,note,date) VALUES(?,?,?,?,?)",(pid,t,tq,"",td))
    db.commit()

# ── PRODUCTS ──────────────────────────────────────────────
def get_products(search="", category="", page=1, per_page=15):
    db=conn(); cur=db.cursor()
    q="SELECT * FROM products WHERE 1=1"; p=[]
    if search: q+=" AND (name LIKE ? OR sku LIKE ?)"; p+=[f"%{search}%"]*2
    if category and category!="Tümü": q+=" AND category=?"; p.append(category)
    cur.execute(q+" ORDER BY id DESC", p)
    rows=cur.fetchall(); total=len(rows)
    s=(page-1)*per_page
    db.close()
    return [dict(r) for r in rows[s:s+per_page]], total

def get_product(pid):
    db=conn(); cur=db.cursor()
    cur.execute("SELECT * FROM products WHERE id=?",(pid,))
    r=cur.fetchone(); db.close()
    return dict(r) if r else None

def add_product(sku,name,cat,shelf,qty,price,mins,img=""):
    db=conn(); cur=db.cursor()
    cur.execute("INSERT INTO products(sku,name,category,shelf,quantity,price,min_stock,image_path,created_at) VALUES(?,?,?,?,?,?,?,?,?)",
                (sku,name,cat,shelf,qty,price,mins,img,datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    db.commit(); pid=cur.lastrowid; db.close(); return pid

def update_product(pid,name,cat,shelf,qty,price,mins,img=""):
    db=conn(); cur=db.cursor()
    cur.execute("UPDATE products SET name=?,category=?,shelf=?,quantity=?,price=?,min_stock=?,image_path=? WHERE id=?",
                (name,cat,shelf,qty,price,mins,img,pid))
    db.commit(); db.close()

def delete_product(pid):
    db=conn(); cur=db.cursor()
    cur.execute("DELETE FROM products WHERE id=?",(pid,))
    cur.execute("DELETE FROM transactions WHERE product_id=?",(pid,))
    db.commit(); db.close()

def generate_sku(cat):
    db=conn(); cur=db.cursor()
    cur.execute("SELECT sku FROM products")
    used={r[0] for r in cur.fetchall()}; db.close()
    return _make_sku(cat,used)

# ── TRANSACTIONS ──────────────────────────────────────────
def get_transactions(search="", ttype="", page=1, per_page=20):
    db=conn(); cur=db.cursor()
    q="""SELECT t.id,p.sku,p.name,t.type,t.quantity,p.category,p.shelf,t.note,t.date
         FROM transactions t JOIN products p ON t.product_id=p.id WHERE 1=1"""
    p=[]
    if search: q+=" AND (p.name LIKE ? OR p.sku LIKE ?)"; p+=[f"%{search}%"]*2
    if ttype and ttype!="Tümü": q+=" AND t.type=?"; p.append(ttype)
    cur.execute(q+" ORDER BY t.id DESC", p)
    rows=cur.fetchall(); total=len(rows)
    s=(page-1)*per_page; db.close()
    return [dict(r) for r in rows[s:s+per_page]], total

def add_transaction(pid, ttype, qty, note=""):
    db=conn(); cur=db.cursor()
    cur.execute("INSERT INTO transactions(product_id,type,quantity,note,date) VALUES(?,?,?,?,?)",
                (pid,ttype,qty,note,datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    if ttype=="Stok Giriş":
        cur.execute("UPDATE products SET quantity=quantity+? WHERE id=?",(qty,pid))
    elif ttype=="Stok Çıkış":
        cur.execute("UPDATE products SET quantity=MAX(0,quantity-?) WHERE id=?",(qty,pid))
    db.commit(); db.close()

def delete_transaction(tid):
    db=conn(); cur=db.cursor()
    cur.execute("DELETE FROM transactions WHERE id=?",(tid,))
    db.commit(); db.close()

# ── DASHBOARD STATS ───────────────────────────────────────
def get_stats():
    db=conn(); cur=db.cursor()
    cur.execute("SELECT COUNT(*) FROM products"); total=cur.fetchone()[0]
    cur.execute("SELECT SUM(quantity*price) FROM products"); val=cur.fetchone()[0] or 0.0
    cur.execute("SELECT COUNT(*) FROM products WHERE quantity<=min_stock"); crit=cur.fetchone()[0]
    cur.execute("""SELECT t.type,t.quantity,t.date,p.name FROM transactions t
                   JOIN products p ON t.product_id=p.id ORDER BY t.id DESC LIMIT 8""")
    recent=[dict(r) for r in cur.fetchall()]
    chart=[]
    for i in range(6,-1,-1):
        day=(datetime.now()-timedelta(days=i)).strftime("%Y-%m-%d")
        lbl=(datetime.now()-timedelta(days=i)).strftime("%a")
        cur.execute("SELECT COALESCE(SUM(quantity),0) FROM transactions WHERE type='Stok Giriş' AND date LIKE ?",(day+"%",))
        ins=cur.fetchone()[0]
        cur.execute("SELECT COALESCE(SUM(quantity),0) FROM transactions WHERE type='Stok Çıkış' AND date LIKE ?",(day+"%",))
        out=cur.fetchone()[0]
        chart.append({"label":lbl,"in":ins,"out":out})
    db.close()
    return {"total":total,"value":val,"critical":crit,"recent":recent,"chart":chart}

# ── SETTINGS ─────────────────────────────────────────────
def get_setting(k, default=""):
    db=conn(); cur=db.cursor()
    cur.execute("SELECT value FROM settings WHERE key=?",(k,))
    r=cur.fetchone(); db.close()
    return r[0] if r else default

def set_setting(k, v):
    db=conn(); cur=db.cursor()
    cur.execute("INSERT OR REPLACE INTO settings(key,value) VALUES(?,?)",(k,v))
    db.commit(); db.close()

def get_all_settings():
    db=conn(); cur=db.cursor()
    cur.execute("SELECT key,value FROM settings")
    r={row[0]:row[1] for row in cur.fetchall()}; db.close()
    return r
