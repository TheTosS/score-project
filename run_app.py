import webview
import threading
import subprocess
import time
import os


def start_server():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # 🔥 ЖЁСТКО указываем python из venv
    python_path = os.path.join(base_dir, ".venv", "Scripts", "python.exe")

    subprocess.Popen(
        [python_path, "manage.py", "runserver", "127.0.0.1:8000"],
        cwd=base_dir
    )


# запускаем сервер
threading.Thread(target=start_server, daemon=True).start()

# ждём запуск
time.sleep(3)

# окно
webview.create_window("SCORE NLP", "http://127.0.0.1:8000")

# запуск GUI
webview.start(gui="edgechromium")