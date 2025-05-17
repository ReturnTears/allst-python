# Python 3 的学习
'''text

'''
## basic 基础部分
***
    能调用方法的一定是对象
***
## advs  高级部分
## algo  算法部分
## func  函数部分
### 装饰器(函数)
    作用域: LEGB
    高阶函数: 函数名可以作为参数输入、函数名也可以作为返回值
    闭包: 如果在一个内部函数里,对在外部作用域(但不是在全局作用域)的变量进行引用，那么内部函数就被认为是闭包(closure)
    闭包 = 函数块 + 定义函数时的环境

### Importance
```
什么是迭代器?
生成器都是迭代器, 迭代器不一定是生成器
满足两个条件: 
1 - 有iter方法
2 - 有next方法

for循环内部实现的三件事(即for内部实现机制):
1 - 调用可迭代对象的iter方法返回一个迭代器对象
2 - 不断调用迭代器对象的next方法
3 - 处理StopIteration

列表生成式
>>> [x*2 for x in range(10)]
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# 生成器(generator)
生成器有两种生成方式:
    1、(x for x in range(n))
    2、yield关键字
    
什么式迭代器?
满足迭代器协议:内部有next方法和内部有iter方法
    



Day18-3 sys模块

Day18-4 hashlib模块
主要用于加密



```
    
# todo
   
    
# Python
```text
1、查看版本
   python -V

2、在Python中可以使用pip与conda工具安装第三方库
pip install 库的名称
conda install 库的名称

```    


# Excel
```text
1、openpyxl 是 Python 3 操作 Excel 文件的 de-facto 标准库。它提供了一系列全面的功能

包括：
读/写支持： 读取和写入 Excel 电子表格，包括工作表、单元格、公式和图表。
格式化选项： 设置单元格格式、字体、对齐方式和条件格式。
数据验证： 添加数据验证规则以限制用户输入。
图片和形状支持： 插入和操作图片、形状和图表。

优点：
易于使用且广泛采用
全面的功能集
活跃的支持社区

缺点：
对于大型文件可能存在性能问题
缺少高级功能，例如分页和保护

安装openpyxl
pip install openpyxl



2、xlrd 和 xlwt 是两个较老的 Excel 操作库，它们专注于分别读取和写入 Excel 文件

xlrd： 仅用于读取 Excel 文件，以支持广泛的数据类型和格式。
xlwt： 仅用于写入 Excel 文件，提供丰富的格式化和样式选项。

优点：
对于较小的文件非常高效
非常适合需要专门读取或写入功能的情况

缺点：
缺少对其他操作（例如修改或删除）的支持
不再积极开发


3、pandas 是一个专门用于数据分析和处理的 Python 库。它提供了与 Excel 文件交互的强大功能
包括 ：
数据帧表示： 将 Excel 电子表格表示为数据帧，易于操作和分析。
数据导入/导出： 从 Excel 文件导入数据或将数据导出到 Excel 文件。
数据清理： 移除重复项、填充缺失值和进行其他数据清理操作。
数据透视表和图表： 创建数据透视表和图表以分析和可视化数据。

优点：
强大的数据处理能力
直观的界面和广泛的文档
适用于大数据集

缺点：
可能不适合需要高级 Excel 功能（例如公式或宏）的情况


除了上述库之外，还有许多其他 Python 库可以用于操作 Excel 文件，例如：
xlsxwriter： 一个用于写入 Excel 文件的高性能库，具有创建交互式图表和图形的功能。
PyParsing： 一个用于解析 Excel 文件的库，提供对子文件、单元格和公式的高级访问。
pyexcel： 一个模块化的库，允许您使用不同的后端（例如 openpyxl 和 xlrd）操作 Excel 文件。

```

# MySQL
```text
在 Python 3.12 中连接 MySQL 数据库，通常使用 mysql-connector-python 或 PyMySQL 这样的库.
安装库
pip install mysql-connector-python

使用PyMysql连接MySQL
pip3 install pymysql



```

# Caddy
```text
Caddy是一个开源的Web服务器和反向代理服务器，它使用Go语言编写，具有高度的扩展性，支持各种功能，如HTTPS、负载均衡、反向代理、WebSocket、静态文件服务器等。

以管理员模式运行cmd:
命令1:显示帮助文本：caddy  / caddy_windows_amd64.exe
命令2:将Caddy作为守护进程启动：caddy run  / caddy_windows_amd64.exe run
访问地址： https://localhost:2019/ https://localhost:2019/config/ https://localhost:2019/load/

caddy

caddy run

caddy start

curl localhost:2019/load \
  -X POST \
  -H "Content-Type: application/json" \
  -d @caddy.json

curl localhost:2019/config/

新建Caddyfile文件，内容如下：
:2016

respond "Halo, Caddy ~!"
或者
localhost {
	respond "Hello, Caddy!"
}

localhost:2016 {
	respond "Goodbye, Caddy!"
}

caddy reload 重新加载Caddy配置
在同时存在json配置和Caddyfile配置时，Caddy会优先使用Caddyfile配置。

caddy stop 停止Caddy

caddy status 查看Caddy状态

caddy version 查看Caddy版本

静态文件
caddy file-server --listen :2015

在Caddyfile的文件中配置如下：
localhost:2017 {
	file_server browse
}

运行caddy: caddy run
访问地址： http://localhost:2017/ 即可查看到文件目录站点

localhost:2018 {
  root * D:\TestData\template
	file_server
    handle_errors {
        rewrite * /error.html
        file_server
    }
}
在template目录中添加错误页：error.html以及初始化页面index.html


反向代理
localhost:2020 {
    reverse_proxy localhost
}


```
 
