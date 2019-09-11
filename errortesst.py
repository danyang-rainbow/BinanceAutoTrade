import requests


def performOnHis(hislist):
    money = 10000
    quant = 0
    staus = 0 # 0 表示待买入
    upflag = 0
    intimeflag = 0
    i = 10
    inprice = 0
    while i < len(hislist):
        if i % 100 == 0:
            print(i)
        if staus == 0 and i % 5 ==0:  # 待买入
            if float(hislist[i]) > float(hislist[i-5]):
                upflag = upflag + 1
                if upflag == 2:
                    quant = (money / float(hislist[i])) *0.999
                    money = 0
                    inprice = float(hislist[i])
                    staus = 1
                    upflag = 0

        elif staus == 1: # 待卖出
            if (abs(float(hislist[i]) - inprice))/ inprice > 0.005:
                money = quant * float(hislist[i]) * 0.999
                staus = 0
        else:
            pass
    print(money)


def GetHistoryData():
    hislist = []
    all = 0
    trade = 0
    startime = 1559836800000 - 30 * 24 *60*1000
    flag = 0
    while flag < 153:
        print('flag'+str(flag))
        paramsp = {'symbol': 'BTCUSDT',
                   'interval': '1m',
                   'startTime': startime,
                   'limit': 1000}
        res = requests.get(url='https://api.binance.com/api/v1/klines', params=paramsp)
        x = res.json()
        i = 0
        while (i <= 999):
            hislist.append(x[i][1])
            i = i + 1
        flag = flag + 1
        startime = x[999][0] + 1000 * 60
    money = 10000
    quant = 0
    staus = 0  # 0 表示待买入
    upflag = 0
    intimeflag = 0
    i = 10
    inprice = 0
    while i < len(hislist):


        if staus == 0 and i % 5 == 0:  # 待买入
            if float(hislist[i]) > float(hislist[i - 10]):
                upflag = upflag + 1
                if upflag == 2:
                    quant = (money / float(hislist[i])) * 0.999
                    trade  = trade + 1
                    all = money
                    money = 0

                    inprice = float(hislist[i])
                    staus = 1
                    upflag = 0

        elif staus == 1:  # 待卖出
            if (float(hislist[i]) - inprice) / inprice > 0.005 :
                money = quant * float(hislist[i]) * 0.999
                quant = 0
                staus = 0
        else:
            pass
        i = i +1
    all = quant * float(hislist[-1]) + money
    print(all)
    print(trade)


GetHistoryData()