from pywinauto import Application
import time
import pywinauto
from private import APP_NAME, G_PATH

app = Application(backend="uia").start(APP_NAME)
time.sleep(30) # PW 로딩 시간 맞춤
name = "TeamViewer"
dig = app[name]

procs = pywinauto.findwindows.find_elements()

for proc in procs:
    if proc.name == "TeamViewer":
        break

app = Application(backend="uia").connect(process=proc.process_id) 
dig = app[name]
window = app.window(title=name)
password_text = window.child_window(auto_id="tvpassword-value-id", control_type="Edit")

new_value = password_text.window_text()

with open(G_PATH, 'w', encoding='utf-8') as file:
    file.write(new_value)
