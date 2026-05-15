"""
main.py — DEPO PRO Giriş Noktası
CMD penceresi açılmaz (pythonw ile çalıştırın veya .pyw uzantısını kullanın).
"""
import sys
import os

# Windows'ta CMD penceresini gizle
if sys.platform == "win32":
    import ctypes
    ctypes.windll.kernel32.FreeConsole()

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

import database as db
from gui import MainWindow, STYLE, STYLE_LIGHT


def main():
    # HiDPI desteği
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    app.setApplicationName("DEPO PRO")
    app.setOrganizationName("DepoPro")

    # Global font
    font = QFont("Segoe UI", 10)
    app.setFont(font)

    # Kaydedilen temayı yükle
    saved_theme = db.get_setting("theme", "dark")
    app.setStyleSheet(STYLE if saved_theme == "dark" else STYLE_LIGHT)

    # Veritabanını başlat / örnek veri ekle
    db.init_db()

    # Ana pencereyi aç
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
