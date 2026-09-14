# fund-style-drift-agent
基于 AI 智能体的基金风格漂移检测与量化分析工具。自动抓取持仓数据，多维度计算风格漂移得分（SDS），持续监控基金在市值、价值成长、行业配置上的风格一致性。

## 环境准备

本项目使用 Python 3.12，详见 [docs/python-env.md](docs/python-env.md)。

```bash
python -m venv .venv
source .venv/Scripts/activate
python -m pip install -r requirements.txt
```
