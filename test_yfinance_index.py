"""测试 yfinance 库查询美股指数（纳斯达克、标普500）信息。"""
import sys

import yfinance as yf

sys.stdout.reconfigure(encoding="utf-8")

# 纳斯达克综合指数、标普500指数、道琼斯工业指数
INDEX_SYMBOLS = {
    "^IXIC": "纳斯达克综合指数",
    "^GSPC": "标普500指数",
    "^DJI": "道琼斯工业指数",
}


def test_index_info(symbol: str, name: str) -> None:
    """测试单个指数的基本信息查询。"""
    print(f"\n=== {name}（{symbol}）基本信息 ===")
    ticker = yf.Ticker(symbol)
    info = ticker.info
    keys = ["shortName", "regularMarketPrice", "previousClose", "fiftyTwoWeekHigh", "fiftyTwoWeekLow"]
    for key in keys:
        print(f"{key}: {info.get(key)}")


def test_index_history(symbol: str, name: str, period: str = "5d") -> None:
    """测试指数历史行情查询。"""
    print(f"\n=== {name}（{symbol}）最近 {period} 行情 ===")
    df = yf.Ticker(symbol).history(period=period)
    print(df.tail())
    print(f"共 {len(df)} 条记录")


if __name__ == "__main__":
    for symbol, name in INDEX_SYMBOLS.items():
        test_index_info(symbol, name)
        test_index_history(symbol, name)
