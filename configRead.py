import configparser

# config = ConfigParser.ConfigParser(allow_no_value=True) #注意参数不能省
cf = configparser.ConfigParser(allow_no_value=True)
cf.read(r"D:\python测试\config.txt",encoding='utf-8')

secs = cf.sections()  # 获取文件中所有的section(一个配置文件中可以有多个配置，如数据库相关的配置，邮箱相关的配置，
                      # 每个section由[]包裹，即[section])，并以列表的形式返回
print(secs)


options = cf.options("版本号")  # 获取某个section名为Mysql-Database所对应的键
print(options)

items = cf.items("问题单")  # 获取section名为Mysql-Database所对应的全部键值对
print(items)

host = cf.get("任务", "任务号")  # 获取[Mysql-Database]中host对应的值
print(host)