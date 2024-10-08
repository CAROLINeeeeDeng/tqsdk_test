from tqsdk import TqApi, TqAuth, TargetPosTask, TqSim, TqBacktest, ta, tafunc
from tqsdk.ta import BOLL, MA, MACD, RSI
import time

class MACD_test():
    def __init__(self, api, symbol, symbol2=None, symbol3=None):
        self.api = api
        self.symbol = symbol
        self.symbol2 = symbol2
        self.symbol3 = symbol3

    @property
    def start(self):
        SYMBOL = self.symbol if self.symbol2 is None else self.symbol2
        quote = self.api.get_quote(SYMBOL)
        klines = self.api.get_kline_serial(SYMBOL, 5 * 60, data_length=15)
        # 60 * 60 * 24)

        lowest_md = []
        highest_md = []
        lowest = []
        highest = []

        position = self.api.get_position(SYMBOL)
        golden_cross_time = 0
        death_cross_time = 0

        # 获取 MACD，DIF，DEA
        def MACD_line(klines):
            macd = MACD(klines, 12, 26, 9)
            DIF = macd["diff"].iloc[-1]
            DEA = macd["dea"].iloc[-1]
            Macd = macd["bar"].iloc[-1]
            return Macd, DIF, DEA

        #
        def check_golden_cross(klines):
            macd = MACD(klines, 12, 26, 9)
            golden_cross = tafunc.crossup(MACD(klines, 12, 26, 9)["diff"], MACD(klines, 12, 26, 9)["dea"])

            return golden_cross

        def check_death_cross(klines):
            death_cross = tafunc.crossdown(MACD(klines, 12, 26, 9)["diff"], MACD(klines, 12, 26, 9)["dea"])
            return death_cross

            # if macd["diff"].iloc[-2] < macd["dea"].iloc[-2] and macd["diff"].iloc[-1] == macd["dea"].iloc[-1]:
            #   return "Golden_Cross"
            # elif macd["diff"].iloc[-2] > macd["dea"].iloc[-2] and macd["diff"].iloc[-1] == macd["dea"].iloc[-1]:
            #   return "Death_Cross"
            # else:
            #   return None

        def RSI_line(klines):
            rsi = RSI_line(klines)

        def time_check(a, secs):
            a.append(time.time())
            if len(a) == 1:
                return False
            else:
                if a[-1] - a[0] < secs:
  
