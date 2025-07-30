> 啊对对对，我们都是初二的学生，用几何的方法做；你是初三的学生，用建系的高级方法做。我们的方法哪有建系快啊 😅
> <p align="right">——我们初中一位数学老师</p>

# 几何计算器 2

## 其它语言

* [English (US)](README.en.md)
* [简体中文](README.md)

借助计算机的强大算力，使用解析几何暴力计算几何问题！

- [使用文档](frontend/src/pages/docs.md)
- [关于 几何计算器 2](frontend/src/pages/about.md)

## 新版本特点

- ✨ 页面美观：全面支持 LaTeX，对人类~~和猫娘~~友好
- ⚡ 运行流畅：前后端分离，告别旧版本中的卡顿
- 💪 功能强大：
    - 🔢 支持添加未知数并限定取值范围
    - 📍 添加点的逻辑更加合理、人性化
    - 📈 表达式解析全面升级：
        - 👍 更加人性化的语法，告别特殊字符
        - ➡️ 支持向量运算
        - 📄 条件可以显示原始形式（也会用 LaTeX 排得美观），管理更方便
    - 📐 直线平行、垂直
    - 🔺 快速添加复合条件：三角形全等、相似
    - 🧩 快速添加特殊图形：平行四边形、菱形、矩形、正方形、等边三角形
    - 🗑️ 更易于操作的删除条件
    - 💾 可以把数据保存到文件、从文件加载数据

## 致谢

见 [`ACKNOWLEDGMENTS.md`](ACKNOWLEDGMENTS.md)

## TODO

- [ ] 给软件设计一个图标
- [ ] 打包为 APK

## Windows 下无法运行？

请用**管理员**身份打开 PowerShell，执行命令：

```shell
Get-ChildItem -Path <你的几何计算器文件夹路径> -Recurse -Filter *.dll | Unblock-File -Confirm:$false
```

参考：https://github.com/r0x0r/pywebview/issues/1638#issuecomment-2896747582

## 在开发模式下运行项目

### 1. 安装依赖

在 `frontend/` 目录下执行：

```bash
pnpm install
```

在 `backend/` 目录下执行：

```bash
uv sync
```

或

```bash
pip install -r requirements.txt
```

### 2. 启动前端

在 `frontend/` 目录下执行：

```bash
quasar dev
```

看到刚刚打开的浏览器页面了吗？对，这个没有用，把它叉掉。

前端可以热更新，你修改代码之后会立即得到反馈，无需重启前端。

### 3. 启动后端

在 `backend/` 目录下运行 `main_dev.py`，这样整个项目就启动完成了。
