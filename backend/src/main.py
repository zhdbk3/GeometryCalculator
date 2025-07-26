import webview

from api import api

window = webview.create_window('几何计算器', 'ui/index.html', js_api=api, maximized=True)
webview.start()
