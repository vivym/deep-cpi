import pandas as pd

INDICATORS1 = [
    "美国:失业率:季调",
    "美国:CPI:环比",
    "美国:CPI:当月同比",
    "美国:M1",
    "美国:M2",
    "美国:密歇根大学消费者预期指数",
    "OECD:产出缺口:美国",
    "LIBOR:美元:3个月",
    "美国:个人可支配收入(不变价):季调:折年数",
    "美国:失业率:季调",
]
INDICATORS2 = [
    "名义美元指数:广义",
    "美国:贸易差额:季调",
    "美国:工业总产值:最终产品:季调",
    "美国:零售和食品服务销售额:总计",
    "美国:外汇",
    "美国:新建住房销售:折年数:季调",
    "美国:纳斯达克综合指数",
    "工业增加值:按本币计算:不变价:美国",
    "美国:联邦政府:经常性支出:总计:未季调",
    "美国:外债总额",
    "汽油价格:常规零售:美国",
]
INDICATORS = INDICATORS1 + INDICATORS2

SELECTED_INDICATORS = [
    "美国:失业率:季调",
    "美国:M1",
    "美国:M2",
    "美国:密歇根大学消费者预期指数",
    "美国:个人可支配收入(不变价):季调:折年数",
    "美国:工业总产值:最终产品:季调",
    "美国:新建住房销售:折年数:季调",
    "美国:纳斯达克综合指数",
    "美国:联邦政府:经常性支出:总计:未季调",
    "汽油价格:常规零售:美国",
]


def main():
    dataset = {
        indicator: {}
        for indicator in INDICATORS
    }

    df1 = pd.read_excel("data/data_raw1.xlsx")
    df2 = pd.read_excel("data/data_raw2.xlsx")
    df = pd.merge(df1, df2, on="日期", how="outer")
    df.to_excel("data/data_raw.xlsx")

    df_month = df.resample("M", on="日期").mean()
    df_month.to_excel("data/data_raw_month.xlsx")

    df_month = df_month.dropna(thresh=20)
    print(df_month)

if __name__ == "__main__":
    main()
