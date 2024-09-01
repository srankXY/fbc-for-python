# -*- utf-8 -*-

import random
import requests
from concurrent.futures import ProcessPoolExecutor
import time


class FBC(object):

    # fbc api path
    _api_path = "/fbc/system/debugPort"
    _driver_path = "/FBC/plugins/driver"

    def __init__(self, fbc_addr):

        self.addr = fbc_addr                # FBC地址
        self.delay = None                   # 是否开启延迟
        self.random_start = None            # 延迟开启时的随机数开始位置
        self.random_end = None              # 延迟开启时的随机数结束位置
        self.maxThreads = None              # 多进程最大进程数，不设置时默认根据操控的窗口数决定，最大不能超过20

    # 常量只读
    @property
    def constant(self):
        return (self._api_path,
                self._driver_path)

    # 设置相关
    # 延迟
    def set_delay(self, random_start: int, random_end: int, enable: bool = False):
        """
        :param random_start:        起始随机数
        :param random_end:          结尾随机数
        :param enable:              延迟状态，默认不开启
        :return:
        """

        self.delay = enable
        self.random_start = random_start
        self.random_end = random_end

    # 同时控制多少浏览器
    def set_maxThreads(self, maxThreads: int):
        """
        :param maxThreads:      同时控制的最大浏览器数
        :return:
        """

        self.maxThreads = maxThreads

    # 获取FBC chrome调试地址
    def get_chromeDebugAddr(self, serials: list = None, runInFBC: bool = None):
        """
        :param serials:    要查询的窗口编号，默认为空
        :param runInFBC:   是否在FBC设备内运行，默认为空
        :return:
        """

        # headers
        headers = {
            "content-type": "application/json"
        }

        # post数据
        post_data = {
            "serials": [],
            "runInFBC": runInFBC
        }

        # 覆盖post_data
        if serials:
            post_data["serials"] = serials

        # 提交请求
        try:
            res = requests.post(url="http://"+self.addr+":20001"+self._api_path, headers=headers, json=post_data)
        except Exception as e:
            print("获取窗口地址失败，错误信息: %s", e)
            exit(1)

        # 返回
        return res.json()

    # 多进程启动，传入具体的浏览器操控方法
    def start(self, spiderFunc, serials: list = None, runInFBC: bool = None):
        """
        :param spiderFunc:        浏览器操作函数.
        :param serials:     操作的窗口, 默认为所有
        :param runInFBC:    是否在FBC盒子中运行，上传到脚本商城的脚本必须为True
        :return:
        """

        # 获取浏览器远端调试地址
        addrs = self.get_chromeDebugAddr(serials=serials, runInFBC=runInFBC)["data"]

        # 没有设置最大进程
        if not self.maxThreads:

            # 获取需要操作的窗口数量
            serials_length = len(addrs)

            # 设置最大进程数量
            if serials_length > 20:
                self.maxThreads = 20
            else:
                self.maxThreads = serials_length

        # 启动
        while True:

            # 所有浏览器操作完成，则退出
            if len(addrs) == 0:
                exit(0)

            # 多进程
            # 定义进程池
            p = ProcessPoolExecutor(max_workers=self.maxThreads)
            for i in range(self.maxThreads):

                # 判断是否还存在未执行的窗口
                try:
                    chrome_addr = addrs.pop()
                except IndexError:
                    break

                # 加入执行进程
                if runInFBC:
                    p.submit(spiderFunc, chrome_addr, self._driver_path)
                else:
                    p.submit(spiderFunc, chrome_addr)

                # 开启延迟
                if self.delay:
                    second = random.randint(self.random_start, self.random_end)
                    time.sleep(second)

            # 等待进程组执行完成
            p.shutdown()


if __name__ == '__main__':
    fbc = FBC(fbc_addr="192.168.3.15")
    print(type(fbc.get_chromeDebugAddr(serials=[1,2])["data"]))