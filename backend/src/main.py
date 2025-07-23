import webview

from problem import Problem

__version__ = '2.0.1'


class API:
    problem = Problem()


api = API()
window = webview.create_window('几何计算器', 'ui/index.html', js_api=api, maximized=True)
webview.start()
