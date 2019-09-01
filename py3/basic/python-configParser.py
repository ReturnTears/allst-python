# author        JUNN
# since         2019-09-01 下午 03:50
# description   configParser 生成配置文件

import configparser

# 写配置文件
# config = configparser.ConfigParser()
# config["DEFAULT"] = {
#     "ServerAliveInterval": "45",
#     "Compression": "yes",
#     "CompressionLevel": "9"
# }
# config["topsecret.server.com"] = {}
# topsecret = config['topsecret.server.com']
# topsecret['host port'] = '3456'
# topsecret['ForwardX11'] = 'no'
# config['DEFAULT']['ForwardX11']='yes'
#
#
# with open('../../static/resources/example.ini', 'w') as configFile:
#     config.write(configFile)


# 读取配置文件
config2 = configparser.ConfigParser()
config2.read('../../static/resources/example.ini')
# 除了default的其他内容
print(config2.sections())
# default
print(config2.defaults())

for key in config2['userinfo']:
    print(key)
