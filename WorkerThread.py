from tqsdk import TqApi, TqAuth
from MACD_test import MACD_test
import threading

class WorkerThread(threading.Thread):
    def __init__(self, api, symbol):
        threading.Thread.__init__(self)
        self.api = api
        self.symbol = symbol

    def run(self):
        MACD_test(self.api, self.symbol).start


if __name__ == "__main__":

    api_master = TqApi(web_gui=True, auth=TqAuth("18156827586", "john120520"))
    # Create new threads
    thread1 = WorkerThread(api_master.copy(), "DCE.cs2105")
    thread2 = WorkerThread(api_master.copy(), "DCE.m2105")
    thread3 = WorkerThread(api_master.copy(), "DCE.p2105")
    thread4 = WorkerThread(api_master.copy(), "DCE.m2108")
    #thread5 = WorkerThread(api_master.copy(), "SHFE.au2108")
    #thread6 = WorkerThread(api_master.copy(), "CZCE.CF101")
    #thread7 = WorkerThread(api_master.copy(), "CZCE.OI101")
    #thread8 = WorkerThread(api_master.copy(), "CZCE.SF101")
    #thread9 = WorkerThread(api_master.copy(), "CZCE.FG101")
    #thread10 = WorkerThread(api_master.copy(), "SHFE.sp2101")
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    #thread5.start()
    #thread6.start()
    #thread7.start()
    #thread8.start()
    #thread9.start()
    #thread10.start()

    while True:
        api_master.wait_update()
