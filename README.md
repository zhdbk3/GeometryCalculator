# 几何计算器 2

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
