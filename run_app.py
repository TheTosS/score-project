import webview
import threading
import time
import os
import sys

from wsgiref.simple_server import make_server
from django.core.wsgi import get_wsgi_application


def start_django():
    base_dir = os.path.dirname(sys.executable) if getattr(sys, 'frozen', False) else os.path.dirname(
        os.path.abspath(__file__))
    os.chdir(base_dir)

    # 💣 фикс для PyInstaller
    if getattr(sys, 'frozen', False):
        os.chdir(sys._MEIPASS)
    else:
        os.chdir(base_dir)

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'score_project.settings')

    application = get_wsgi_application()

    server = make_server('127.0.0.1', 8000, application)
    server.serve_forever()


# 🚀 запускаем Django в потоке
threading.Thread(target=start_django, daemon=True).start()

# ждём старт
time.sleep(2)

# окно
webview.create_window("SCORE NLP", "http://127.0.0.1:8000")

# GUI
webview.start(gui="edgechromium")