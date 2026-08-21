# fund-style-drift-agent

基于 AI 智能体的基金风格漂移检测与量化分析工具。自动抓取持仓数据，多维度计算风格漂移得分（SDS），持续监控基金在市值、价值成长、行业配置上的风格一致性。

## 技术栈

- FastAPI：HTTP API 服务框架
- DeepAgents / LangGraph / LangChain：智能体编排与工具调用
- Pydantic Settings：环境变量配置
- Pytest / Ruff：测试与代码质量检查

## 本地环境

> 当前依赖生态建议使用 Python 3.11 或 3.12。仓库的 `pyproject.toml` 已限制为 `>=3.11,<3.13`。

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e '.[dev]'
cp .env.example .env
```

如果本机只有 `python3` 且版本满足要求，也可以将第一行替换为：

```bash
python3 -m venv .venv
```

## 启动服务

```bash
source .venv/bin/activate
uvicorn app.main:app --reload
```

健康检查：

```bash
curl http://127.0.0.1:8000/health
```

## 测试与检查

```bash
pytest
ruff check .
```
