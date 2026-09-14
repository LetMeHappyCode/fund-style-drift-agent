# fund-style-drift-agent
基于 AI 智能体的基金风格漂移检测与量化分析工具。核心场景是主要配置美股科技股的 QDII 基金 / 全球公募基金，自动抓取基金净值与美股基准数据，计算风格漂移得分，持续监控基金在美股科技细分风格（大盘科技、半导体、软件云计算、颠覆性成长、通讯服务等）上的配置一致性。

## 核心方法：基于收益率的风格分析（RBSA）

采用威廉·夏普（William Sharpe）提出的 Returns-Based Style Analysis，将基金日收益率拟合为多个美股科技基准资产收益率的线性组合：

$$R_{fund, t} = \sum_{i=1}^{k} w_{i, t} \cdot R_{style\_i, t} + \varepsilon_t$$

约束条件：

- $\sum_{i=1}^{k} w_{i, t} = 1$（权重和为 1）
- $w_{i, t} \ge 0$（不允许卖空）

风格偏移度指标：

- **权重波动率**：滚动计算各项风格权重 $w_{i,t}$ 的标准差，权重变化越大，偏移越严重。
- **R² / 残差方差**：$1 - R^2$ 或残差 $\varepsilon_t$ 的方差。若 $R^2$ 显著下降，说明基金经理配置进入了基准池之外的领域（如大幅建仓中概股、现金比例过高、或买入了非科技类股票）。

### 数据预处理

计算前需完成两项跨市场对齐：

1. **汇率换算（USD → CNY）**：国内 QDII 基金净值以人民币计价，美股基准（如 QQQ、XLK）以美元计价，需按每日 USD/CNY 中间价换算：

   $$R_{USD\_asset, t}^{CNY} = (1 + R_{USD\_asset, t}^{USD}) \times (1 + R_{USD/CNY, t}) - 1$$

2. **时差对齐（T 与 T-1）**：美股夜间交易，QDII 基金 T 日公布净值实际对应美股 T-1 交易日收盘表现，需将基金 T 日收益率与美股基准 T-1 日收益率错位对齐（Lag Alignment）。

### 美股科技基准资产池

| 基准代码 | 代表资产 | 检测的风格 |
| --- | --- | --- |
| XLK | 美股科技精选行业 ETF | 大盘巨头科技风格（微软、苹果、英伟达等） |
| SOXX / SMH | 费城半导体 ETF | 硬件/芯片硬科技风格 |
| IGV / WCLD | 软件/云计算 ETF | SaaS/软件科技风格 |
| ARKK | 创新科技 ETF | 高估值/颠覆性成长科技风格 |
| XLC | 通讯服务 ETF | 互联网/社交媒体巨头（Google、Meta 等） |
| SPY / IWM | 标普500 / 罗素2000 | 非科技风格（检测是否漂移到大盘价值股或小盘股） |

## 环境准备

本项目使用 Python 3.12，详见 [docs/python-env.md](docs/python-env.md)。

```bash
python -m venv .venv
source .venv/Scripts/activate
python -m pip install -r requirements.txt
```
