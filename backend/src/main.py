import sys
import traceback
from logger import logging

def global_except_handler(exc_type, exc_value, exc_traceback):
    logging.error(f"Uncaught exception: {exc_value}")
    with open("/sdcard/crash_log.txt", "w") as f:
        traceback.print_exception(exc_type, exc_value, exc_traceback, file=f)
    sys.exit(1)

sys.excepthook = global_except_handler

# 原应用代码
if __name__ == "__main__":
    with open("/sdcard/test_log.txt", "w") as f:
        f.write("应用启动成功！\n")
    import webview

    from api import api
    from logger import backend_logger

    __version__ = '2.2.0'

    backend_logger.info(f'几何计算器，启动！版本：{__version__}')

    window = webview.create_window('几何计算器', 'ui/index.html', js_api=api, maximized=True)
    webview.start()
