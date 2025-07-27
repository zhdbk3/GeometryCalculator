import webview

from api import api
from logger import backend_logger

__version__ = '2.2.0'

backend_logger.info(f'几何计算器，启动！版本：{__version__}')

window = webview.create_window('几何计算器', 'ui/index.html', js_api=api, maximized=True)
webview.start()
