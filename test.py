#encoding=utf-8
import json
import requests
import time
import hmac
import hashlib
import logging
nowTime = lambda:int(round(time.time()* 1000))
# api : z5FIfLj4NBd5AFXCGRA7TVzMxQqlm15qkEGb7WEL6E6WrQNSP4zf8aiqChdFjctW
# key： I2A2qsyXjjMoE3NBLcaGhRs2QSWZP6AgJjX2ZVqAsGodVVCftENCucz9S5sH4gd3
logging.basicConfig(filename="out2.log", level=logging.INFO)


# 最低数量为0.000001
def BuyBtc(symbol='BTCUSDT', quantity=0.000001):
    nowtime = nowTime()
    headersp = {'X-MBX-APIKEY': 'z5FIfLj4NBd5AFXCGRA7TVzMxQqlm15qkEGb7WEL6E6WrQNSP4zf8aiqChdFjctW'}
    signap = (hmac.new(bytes('I2A2qsyXjjMoE3NBLcaGhRs2QSWZP6AgJjX2ZVqAsGodVVCftENCucz9S5sH4gd3', encoding='utf-8'),
                       bytes('symbol=BTCUSDT&side=BUY&type=MARKET&'+'quantity='+str(quantity)+'&timestamp=' + str(nowtime),
                             encoding='utf-8'), digestmod=hashlib.sha256).digest()).hex()
    paramsp = {'symbol': symbol, 'side' : 'BUY', 'type': 'MARKET', 'quantity': quantity , 'timestamp':nowtime ,'signature': signap}
    respon = requests.post(url='https://api.binance.com/api/v3/order',headers=headersp,data=paramsp)
    if respon.status_code != 200:
        print(respon.content)
        logging.info(respon.content)
        return False

# 最低数量为0.000001
def SellBtc(symbol='BTCUSDT', quantity=0.000001):
    nowtime = nowTime()
    headersp = {'X-MBX-APIKEY': 'z5FIfLj4NBd5AFXCGRA7TVzMxQqlm15qkEGb7WEL6E6WrQNSP4zf8aiqChdFjctW'}
    signap = (hmac.new(bytes('I2A2qsyXjjMoE3NBLcaGhRs2QSWZP6AgJjX2ZVqAsGodVVCftENCucz9S5sH4gd3', encoding='utf-8'),
                       bytes('symbol=BTCUSDT&side=SELL&type=MARKET&'+'quantity='+str(quantity)+'&timestamp=' + str(nowtime),
                             encoding='utf-8'), digestmod=hashlib.sha256).digest()).hex()
    paramsp = {'symbol': symbol, 'side' : 'SELL', 'type': 'MARKET', 'quantity': quantity , 'timestamp':nowtime ,'signature': signap}
    respon = requests.post(url='https://api.binance.com/api/v3/order', headers=headersp, data=paramsp)
    if respon.status_code != 200:
        print(respon.content)
        logging.info(respon.content)
        return False


# 拿到当前的usdt数量
def getUsdtCount():
    while True:
        nowtime = nowTime()
        headersp = {'X-MBX-APIKEY': 'z5FIfLj4NBd5AFXCGRA7TVzMxQqlm15qkEGb7WEL6E6WrQNSP4zf8aiqChdFjctW'}
        signap = (hmac.new(bytes('I2A2qsyXjjMoE3NBLcaGhRs2QSWZP6AgJjX2ZVqAsGodVVCftENCucz9S5sH4gd3', encoding='utf-8'),
                           bytes('timestamp=' + str(nowtime),
                                 encoding='utf-8'), digestmod=hashlib.sha256).digest()).hex()
        paramsp = {'timestamp': nowtime,
                   'signature': signap}
        res = requests.get(url='https://api.binance.com/api/v3/account', headers=headersp, params=paramsp)
        if res.status_code != 200:
            print(res.content)
            logging.info(res.content)
            continue
        res = res.json()['balances']
        for item in res:
            if item['asset'] == 'USDT':
                return float(item['free'])

def getBtcCount():
    while True:
        nowtime = nowTime()
        headersp = {'X-MBX-APIKEY': 'z5FIfLj4NBd5AFXCGRA7TVzMxQqlm15qkEGb7WEL6E6WrQNSP4zf8aiqChdFjctW'}
        signap = (hmac.new(bytes('I2A2qsyXjjMoE3NBLcaGhRs2QSWZP6AgJjX2ZVqAsGodVVCftENCucz9S5sH4gd3', encoding='utf-8'),
                           bytes('timestamp=' + str(nowtime),
                                 encoding='utf-8'), digestmod=hashlib.sha256).digest()).hex()
        paramsp = {'timestamp': nowtime,
                   'signature': signap}
        res = requests.get(url='https://api.binance.com/api/v3/account', headers=headersp, params=paramsp)
        if res.status_code != 200:
            print(res.content)
            logging.info(res.content)
            continue
        res = res.json()['balances']
        for item in res:
            if item['asset'] == 'BTC':
                return float(item['free'])

def GetHistoryData():
    paramsp = {'symbol': 'BTCUSDT',
               'interval': '1m',
               'startTime': 1559836800000,
               'limit':1000}
    res = requests.get(url='https://api.binance.com/api/v1/klines', params=paramsp)



# 拿到当前的Eos价格
def getBtcPrice():
    # /api/v3/ticker/price
    while True:
        res = requests.get(url='https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT')
        if res.status_code == 200:
            print(res.content)
            logging.info(res.content)
            break
    return float((res).json()['price'])


# 每次买多少，卖多少呢？
# 按all in all out 来算。
# 买入的时候，先看看有多少usdt，然后根据刚刚的拿到的价格，usdt除以刚刚的价格再乘以0.95，取6位小数（舍），即为买入btc的数量
# 卖出的时候，查询一共有多少btc，取6位小数，卖出。


# 买入卖出的策略：
#

def SELL_():
    while True:
        x = round(round(getBtcCount(), 6) - 0.000001,6)
        if (SellBtc(quantity=x) != False ):
            break

def BUY_():
    while True:
        x = getUsdtCount()
        y = getBtcPrice()
        if (BuyBtc(quantity=round(x * 0.95 / y, 6)) !=False ):
            break


def FirstTemp():
    print("Frist temp begins")
    logging.info("Frist temp begins")
    inorout = 0
    flag = 0
    in_price = 9992.16
    pre_price = getBtcPrice()
    time.sleep(300)
    i = 0
    while(True):
        print("Loop:"+str(i))
        logging.info("Loop:"+str(i))
        i = i + 1
        price = getBtcPrice()
        if inorout == 0: # 即将买入的状态
            if price > pre_price:
                flag = flag + 1
                pre_price = price
                if flag == 2:
                    BUY_()
                    in_price = getBtcPrice()
                    print("buy in at"+str(in_price))
                    logging.info("buy in at"+str(in_price))
                    flag = 0
                    inorout = 1
            else:
                pre_price = price
                flag = 0

        else: # 等待卖出状态
            if price - pre_price < 0:
                if (pre_price - price)/pre_price > 0.0030:
                    SELL_()
                    out_price = getBtcPrice()
                    print("Sell out at" + str(out_price) + "**" + str((out_price - in_price) / in_price - 0.002))
                    logging.info("Sell out at" + str(out_price) + "**" + str((out_price - in_price) / in_price - 0.002))
                    inorout = 0
                    flag = 0
                else:
                    flag = flag + 1
                    if flag == 2:
                        SELL_()
                        out_price = getBtcPrice()
                        print("Sell out at" + str(out_price)+"**"+str((out_price-in_price)/in_price -0.002))
                        logging.info("Sell out at" + str(out_price)+"**"+str((out_price-in_price)/in_price -0.002))
                        flag = 0
                        inorout = 0
                pre_price = price
            else:
                pre_price = price
                flag = 0
        time.sleep(300)

def secondTemp():
    stat = 0
    while (True):
        pr = getBtcPrice()

        logging.info(pr)
        if(pr <= 9950 and stat == 0):
            BUY_()
            stat = 1
        else:
            if(pr >= 10300 and stat == 1):
                SELL_()
                stat = 0
        time.sleep(30)

def thirdTemp():
    '''
    1. 连续两个5mins上涨，买入
    2. 跌幅超过千分之5，卖出，亏千分之7
    3. 涨幅超过千分之5，卖出，盈利千分之3
    4. 检测市场以分钟秒为单位
    :return:
    '''
    print("Third Temps begins")
    logging.info("Third temp begins")




if __name__ == '__main__':
    secondTemp()