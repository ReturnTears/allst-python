# author        JUNN
# since         2019-09-01 下午 02:46
# description   logging

import logging
# 日志级别依次
# 方式1
# logging.basicConfig(level=logging.INFO,
#                     format='%(asctime)s - %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S',
#                     filename='test.log',
#                     filemode='a')
#
# logging.debug('debug log record method 1')
# logging.info('info log record method 1')
# logging.warning('warning log record method 1')
# logging.error('error log record method 1')
# logging.critical('critical log record method 1')

# 方式2
# LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"    # 日志格式化输出
# DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"                        # 日期格式
# fp = logging.FileHandler('test.log', encoding='utf-8')
# fs = logging.StreamHandler()
# logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT, handlers=[fp, fs])    # 调用
#
#
# logging.debug("This is a debug log.哈哈")
# logging.info("This is a info log.")
# logging.warning("This is a warning log.")
# logging.error("This is a error log.")
# logging.critical("This is a critical log.")

# 方式3即打印到文件又打印到控制台
# 创建一个logger对象
logger = logging.getLogger()
# 创建一个handler,用于写入日志文件
fh = logging.FileHandler('test.log')
# 在创建以恶handler,用于输出到控制台
ch = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')

fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)

logger.debug('debug log record method 3')
logger.info('info log record method 3')
logger.warning('warning log record method 3')
logger.error('error log record method 3')
logger.critical('critical log record method 3')


