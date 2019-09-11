import asyncio
import logging
from datetime import datetime
from aiowebsocket.converses import AioWebSocket
import requests
import time
from requests import exceptions

#
#
#
# async def startup(url):
#     async with AioWebSocket(url) as aws:
#         converse = aws.manipulator
#         while True:
#             mes = await converse.receive()
#             print('{time}-Client receive: {rec}'
#                   .format(time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), rec=mes))
#
#
# if __name__ == '__main__':
#     # 拿取btcusdt的数据
#     remote = 'wss://stream.binance.com:9443/ws/btcusdt@aggTrade'
#     try:
#         asyncio.get_event_loop().run_until_complete(startup(remote))
#     except KeyboardInterrupt as exc:
#         logging.info('Quit.')
#
#
#
# def mainfunction():
#
#     # 首先是一堆初始化地操作。
#     # 拿到exchangeinfo
#     while True:
#
#
#     pass
#
#
#
# try:
#     requests.get("https://api.binance.com/api/v1/exchangeInfo")
# except exceptions.Timeout as e:
#     print('请求超时：' + str(e.message))
#
#
#
#
#
#
# # 异步地获取行情数据
#
#
#
#
# # 虚拟货币基类
# class cryptocurrency:
#     def __init__(self):
#         pass
#
#
#
# # 交易对基类
# class TransactionPair:
#     def __init__(self):
#
#
#
#
# # 我需要一个函数处理交易所的信息，然后存储在相关的数据结构里面
# class exchangeInfo:
#     def __init__(self):
#
#         try:
#             requests.get("https://api.binance.com/api/v1/exchangeInfo")
#         except requests.exceptions.Timeout as e:
#             logging.info(str(e))
#         except requests.exceptions.BaseHTTPError as e:
#
#
# # 传入一个字典算了。














