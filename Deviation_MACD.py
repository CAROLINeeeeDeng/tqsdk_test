from tqsdk import TqApi, TqAuth, TqSim, TqBacktest, ta, tafunc, TargetPosTask
from datetime import date, timedelta
import numpy
import pandas

class Deviation_Macd(object):
    def __init__(self, symbol):
        self.api = TqApi(TqSim(), backtest=TqBacktest(start_dt=date(2021, 1, 20), end_dt=date(2021, 1, 21)))
        self.kline = self.api.get_kline_serial(symbol, 60 * 15)
        self.target_pos = TargetPosTask(self.api, symbol)
        self.position = self.api.get_position(symbol)
        self.quote = self.api.get_quote(symbol)
        self.macd = 0
        self._lowest_md = []
        self._highest_md = []
        self.lowest = []
        self.highest = []

    def on_kline(self):
        self.macd = ta.MACD(self.kline, 12, 26, 9)
        self.kline['MACDValue'] = self.macd["diff"]
        self.kline['AvgMACD'] = self.macd["dea"]
        self.kline['MACDDiff'] = self.macd["bar"]
        self.kline['零轴'] = 0
        self.kline['cross_up'] = tafunc.crossup(self.kline['MACDValue'], self.kline['AvgMACD'])
        self.kline['cross_down'] = tafunc.crossdown(self.kline['MACDValue'], self.kline['AvgMACD'])
        self.kline['trend_long'] = tafunc.crossup(self.kline['AvgMACD'], self.kline['零轴'])
        self.kline['trend_short'] = tafunc.crossdown(self.kline['AvgMACD'], self.kline['零轴'])

    def main(self):
        while True:
            self.api.wait_update()
            self.on_kline()
if __name__ == '__main__':
    api_master = TqApi(web_gui=True, auth=TqAuth("18156827586", "john120520"))
    D_Macd = Deviation_Macd(symbol = "DCE.cs2105")
    D_Macd.main()
