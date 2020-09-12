
import shutil
import singleFileCreate
import configparser
import os
import selectDoc

#定义根目录
path=r"D:\Users\Desktop\版本\交易银行版本\源码" 
moudle_path=r"D:\Users\Desktop\版本\交易银行版本\模板" 
path_des=r"D:\Users\Desktop\版本\交易银行版本\版本"
# path=r"D:\python测试\源码" 
# moudle_path=r"D:\python测试\模板"
# path_des=r"D:\python测试\版本"

# 读取配置文件中版本号、项目、问题单信息
cf = configparser.ConfigParser(allow_no_value=True)
# cf.read(r"D:\python测试\config.txt",encoding='utf-8')
cf.read(r"D:\Users\Desktop\版本\交易银行版本\config.txt",encoding='utf-8')

taskId=cf.get("任务", "任务号")
taskInfo=cf.get("任务", "需求简述")
problemId=cf.get("问题单", "问题单号")
problemInfo=cf.get("问题单", "问题变更点简述")
versions=cf.options("版本号")

#生成版本文件
for v in versions:
    #配置文件读出来会是小写，转换为大写
    version=v.upper()

    #备份源码
    shutil.copytree(path+"\\"+version,path+"\\"+version+'tmp')

    #生成版本文件
    docType=selectDoc.select(version)#根据版本号取不同的版本模板
    singleFileCreate.create_single(version,path,moudle_path+docType,taskId,taskInfo, problemId,problemInfo)

    #将版本文件移动至指定目录
    shutil.move(path+"\\"+version+'.zip',path_des)
    print('将版本文件',version+'.zip','移动至指定目录')

    #删除中间文件夹
    shutil.rmtree(path+"\\"+version)
    os.rename(path+"\\"+version+'tmp',path+"\\"+version)

print('版本文件已全部生成！！')