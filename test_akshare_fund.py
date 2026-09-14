"""测试 akshare 基金净值数据接口是否可用。"""
import sys

import akshare as ak

sys.stdout.reconfigure(encoding="utf-8")


def test_fund_open_fund_info(fund_code: str = "000001") -> None:
    """测试开放式基金历史净值查询（东方财富接口）。"""
    print(f"\n=== 单位净值走势（基金代码 {fund_code}） ===")
    df = ak.fund_open_fund_info_em(symbol=fund_code, indicator="单位净值走势")
    print(df.tail())
    print(f"共 {len(df)} 条记录")


def test_fund_name_em() -> None:
    """测试基金基本信息列表查询。"""
    print("\n=== 全市场基金列表（前 5 条） ===")
    df = ak.fund_name_em()
    print(df.head())
    print(f"共 {len(df)} 条记录")


def test_fund_portfolio_hold_em(fund_code: str = "000001", date: str = "2024") -> None:
    """测试基金持仓（股票）查询，用于后续风格漂移分析。"""
    print(f"\n=== 基金持仓（基金代码 {fund_code}，年度 {date}） ===")
    df = ak.fund_portfolio_hold_em(symbol=fund_code, date=date)
    print(df.head())
    print(f"共 {len(df)} 条记录")


if __name__ == "__main__":
    test_fund_open_fund_info()
    test_fund_name_em()
    test_fund_portfolio_hold_em()
