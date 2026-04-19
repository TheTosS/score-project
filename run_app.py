import webview
import threading
import subprocess
import os
import sys
import time
import requests

server_process = None


# 🚀 запуск Django
def start_server():
    global server_process

    base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    python_path = sys.executable
    manage_path = os.path.join(base_dir, "manage.py")

    server_process = subprocess.Popen(
        [python_path, manage_path, "runserver", "127.0.0.1:8000"],
        cwd=base_dir
    )


# ⏳ ждём пока сервер реально поднимется
def wait_for_server():
    for _ in range(30):  # до ~15 секунд
        try:
            r = requests.get("http://127.0.0.1:8000")
            if r.status_code == 200:
                return True
        except:
            pass
        time.sleep(0.5)
    return False


# запуск сервера
t = threading.Thread(target=start_server)
t.daemon = True
t.start()

# ждём готовности
if not wait_for_server():
    print("❌ сервер не запустился")
    sys.exit(1)


# 🪟 окно
window = webview.create_window(
    "SCORE NLP",
    "http://127.0.0.1:8000",
    width=1200,
    height=800
)


# 💀 закрытие
def on_closed():
    global server_process

    print("APP CLOSED")

    if server_process:
        try:
            server_process.terminate()
            server_process.kill()
        except:
            pass

    os._exit(0)

print("START APP")
webview.start(gui="edgechromium")