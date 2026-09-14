# Python 环境说明

本项目统一使用 **Python 3.12**，通过虚拟环境 `.venv` 隔离依赖，避免与系统上其他 Python（如 Anaconda）混用导致的包安装错乱。

## 背景

开发机上同时存在多个 Python：

| 命令 | 实际指向 |
| --- | --- |
| `python` | Python 3.12（`C:\Users\<user>\AppData\Local\Programs\Python\Python312`） |
| `pip` | Anaconda Python 3.7（`E:\AiTrain\Anaconda3`） |

直接运行 `pip install xxx` 会把包装到 Anaconda 3.7 环境，而运行脚本用的是 `python`（3.12），导致 `ModuleNotFoundError`。因此项目内统一通过 `.venv` 虚拟环境来避免这个问题，不再依赖全局 `python` / `pip` 指向哪个安装。

## 初始化环境

在项目根目录下执行：

```bash
python -m venv .venv
```

激活虚拟环境：

```bash
# Windows (Git Bash)
source .venv/Scripts/activate

# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Windows (CMD)
.venv\Scripts\activate.bat
```

安装依赖：

```bash
python -m pip install -r requirements.txt
```

## 日常使用

激活虚拟环境后，直接用 `python` / `pip` 即可，会自动指向 `.venv` 内的解释器：

```bash
python test_yfinance_index.py
python test_akshare_fund.py
```

不激活虚拟环境时，也可以直接指定解释器路径：

```bash
./.venv/Scripts/python.exe test_yfinance_index.py
```

## 新增依赖

安装新包后，重新固化 `requirements.txt`：

```bash
python -m pip install <package>
python -m pip freeze > requirements.txt
```

提交代码时把更新后的 `requirements.txt` 一起提交，`.venv/` 目录本身已在 `.gitignore` 中排除，不进入版本库。

## 版本要求

- Python: **3.12.x**
- 依赖版本见 [requirements.txt](../requirements.txt)（`akshare`、`yfinance` 等均已固定版本号）
