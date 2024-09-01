# FBC-SDK技术文档

## 简介

> 名称：FBC SDK for python
>
> 作用：
>
> - 允许用户自己编写自动化脚本对接FBC指纹浏览器
> - 允许用户在本地运行脚本控制FBC指纹浏览器窗口
>
> `目前只支持python`

## 快速开始

### 首先

你需要安装`FBC SDK`

```shell
pip install fbc-for-python
```

### 本地控制FBC

> 如果你希望在本地运行你的 RPA 脚本，控制FBC浏览器

你可以这样：

- 下载适配的`webdriver`，FBC版本目前为：`chromium 117`，chrome_driver下载地址：[历史chrome driver](https://vikyd.github.io/download-chromium-history-version/#/)
- 编写你的 RPA 脚本，并使用 FBC SDK 启动脚本

函数形式：

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from fbc-for-python import FBC

def spider(chrome_addr):
    options = webdriver.ChromeOptions()
    s = Service(r"您的webdriver路径")
    options.debugger_address = chrome_addr
    driver = webdriver.Chrome(service=s, options=options)
    driver.get('https://baidu.com')

if __name__ == '__main__':
    fbc = FBC.FBC(fbc_addr="您的FBC地址")
    fbc.start(spider)

```

`spider`为你自行编写的代码，但你的函数入口需要准备一个参数用于接受 FBC 浏览器的调试地址，如：`chrome_addr`



而如果的代码是用类封装的，你可以这样：

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from fbc-for-python import FBC

class spider(object):

    def run(self, chrome_addr):
        options = webdriver.ChromeOptions()
        s = Service(r"您的webdriver路径")
        options.debugger_address = chrome_addr
        driver = webdriver.Chrome(service=s, options=options)
        driver.get('https://baidu.com')
        
if __name__ == '__main__':
fbc = FBC.FBC(fbc_addr="您的FBC地址")
s = spider()
fbc.start(s.run)
```

同样，你的入口也需要准备一个参数用于接受 FBC 浏览器的调试地址

### 在FBC设备内控制FBC

> 而如果你希望脚本在FBC设备内运行，你还需要在入口多准备一个参数，用于接受`webdriver`的路径，并且你需要在调用SDK启动脚本的时候显式指定`runInFBC=True`来告诉SDK本脚本是放在FBC设备内运行的（后期脚本商城）。

比如，像这样（函数）：

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from fbc-for-python import FBC

def spider(chrome_addr, driver_path):
    options = webdriver.ChromeOptions()
    s = Service(driver_path)
    options.debugger_address = chrome_addr
    driver = webdriver.Chrome(service=s, options=options)
    driver.get('https://baidu.com')

if __name__ == '__main__':
    fbc = FBC.FBC(fbc_addr="您的FBC地址")
    fbc.start(spider, runInFBC=True)
```

又或者，像这样（类）：

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from fbc-for-python import FBC

class spider(object):

    def run(self, chrome_addr, driver_path):
        options = webdriver.ChromeOptions()
        s = Service(driver_path)
        options.debugger_address = chrome_addr
        driver = webdriver.Chrome(service=s, options=options)
        driver.get('https://baidu.com')
        
if __name__ == '__main__':
fbc = FBC.FBC(fbc_addr="您的FBC地址")
s = spider()
fbc.start(s.run, runInFBC=True)
```

OK，现在你将可以在FBC RPA中为所欲为了。

## SDK

### 安装sdk

`pip install fbc-for-python`

### 设置

#### 延迟

> 用于设置控制各个窗口的随机时间间隔.

示例：

开启延迟，并把随机间隔控制在 **3-5s** 之间

```python
fbc = FBC.FBC(fbc_addr="FBC设备IP")
fbc.set_delay(
    random_start=3,
    random_end=5,
    enable=True
)
```

#### 最大进程

> 表示同时可以操作的浏览器窗口数量，如果您在本地运行您的脚本，您可以根据您本地电脑的CPU核心数调整，但如果您是在FBC设备内运行，建议保留默认值

示例：

指定最大同时控制的浏览器窗口数量为 **30**

```python
fbc = FBC.FBC(fbc_addr="FBC设备IP")
fbc.set_maxThreads(maxThreads=30)
```

### 获取浏览器窗口调试地址

**获取工作区全部窗口地址**

```python
fbc = FBC.FBC(fbc_addr="FBC设备IP")
addrs = fbc.get_chromeDebugAddr()
```

**获取指定的的窗口地址**

```python
fbc = FBC.FBC(fbc_addr="FBC设备IP")
addrs = fbc.get_chromeDebugAddr(serials=[1,2])
```

**如果你希望获取设备本地127.0.0.1的调试地址，你可以这样：**

```python
fbc = FBC.FBC(fbc_addr="FBC设备IP")
addrs = fbc.get_chromeDebugAddr(runInFBC=True)
```

### 启动参数

**爬虫函数**(`必传`)

```python
fbc = FBC.FBC(fbc_addr="FBC设备IP")
fbc.start(spiderFunc=spider)
```

**指定控制的窗口编号**

> 所有地址默认不传`serials`就是操控所有工作区的窗口

```python
fbc = FBC.FBC(fbc_addr="FBC设备IP")
fbc.start(spiderFunc=spider,serials=[1,2])
```

**指定在FBC设备内运行脚本**

```python
fbc = FBC.FBC(fbc_addr="FBC设备IP")
fbc.start(spiderFunc=spider, serials=[1,2], runInFBC=True)
```

## FAQ

> 其他SDK通用问题将在这儿展示

