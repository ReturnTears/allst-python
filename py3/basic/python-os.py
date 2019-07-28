# author        JUNN
# since         2019-07-27 下午 10:14
# description   OS模块, python操作操作系统(Important)


import os
# 当前工作目录current work dist
print(os.getcwd())
# 改变当前工作目录
os.chdir('C:\\Users')
print(os.getcwd())
# 当前目录 .
print(os.curdir)
# ..
print(os.pardir)
# 当前目录下创建文件夹,多文件夹就采用递归的方式
os.makedirs('os\\demo')
# 只能删除空文件夹
os.removedirs('os\\demo')
# 生成单个文件夹,多文件夹时报错
os.mkdir('dirname')
# 删除dir
os.rmdir('dirname')
# 列出指定目录下的所有文件和子目录,包括隐藏文件,以列表方式输出
os.listdir('dirname')
# 删除一个文件
os.remove()
# 重命名文件/目录
os.rename('old', 'new')
# 获取文件/目录信息
os.stat('path/pathname')
# 输出操作系统特定的路径分隔符, Windows下为'\\', Linux下为'/'
os.sep
# 输出当前平台使用的行为终止符, Windows下为'\r\n', Linux下为'\n'
os.linesep
# 输出用于分割文件路径的字符串, ;
os.pathsep
# 输出字符串指示当前使用平台, Windows -> 'nt', Linux -> 'posix'
os.name
# 运行shell命令, 直接显示
os.system('bash command')
# 获取系统环境变量
os.environ
# 返回path规范化的绝对路径
os.path.abspath('path')
# 将path分割成目录和文件名二元组返回
os.path.split('')
# 返回path目录,其实就是os.path.split('path')的第一个元组
os.path.dirname('path')
# 返回path最后的文件名,如果path以/或\结尾,那么就返回空值
os.path.basename('path')
# 判断是否存在path,存在返回True, 反之False
os.path.exists('path')
# 如果path是绝对路径,返回True
os.path.isabs('path')
#
os.path.isfile('path')
#
os.path.isdir('path')
# 将多个路径组合返回
os.path.join('path1', 'path2')
# 返回path所指向的文件或目录的最后存取时间
os.path.getatime('path')