########################################################################################
#                                 程序说明
# 该程序用来实现自动生成版本，版本生成分以下几步：
# 0.输入版本号作为全局变量
# 1.根据版本号创建文件夹,拷贝相应的安装手册、版本说明书（重命名）、代码清单
# 2.从ftp下载源码和执行码，并将放到指定“下发包”文件夹下
# 3.修改版本说明书、代码清单内容
# 4. 压缩成zip包
# 5. 传至初审服务器
########################################################################################

import os
import shutil
import FileChange
import zip

path=r"D:\Users\Desktop\版本\交易银行版本" #指定目录
#path=s = os.getcwd() #获取根目录  系统所在目录，不是.py文件的目录
example_doc="软件产品版本说明书"
example_xls="下发清单"
example_zip="安装手册"

########################################################################################
# 0.获取版本号
########################################################################################
version = input("输入版本号：")
print("版本号为："+version)

########################################################################################
# 1.根据版本号创建文件夹,拷贝相应的安装手册、版本说明书（重命名）、代码清单
########################################################################################
version_path=path+"\\"+version #版本文件目录
# os.makedirs(version_path) #创建版本文件夹
# print("已完成：创建文件夹  "+version_path)
if not os.path.exists(version_path):
    print(version_path,'不存在！请下载该文件夹')
    exit()

#将源码移入下发包
code_path=version_path+"\\下发包"
os.makedirs(code_path) #创建下发包目录
print("已完成：创建子文件夹  下发包")
for file in os.listdir(version_path):
    if file.startswith('igtb-'):
        shutil.move(version_path+'\\'+file,code_path)
print('已完成：将源码移入下发包')



#拷贝安装手册、版本说明书、代码清单
version_doc=example_doc+"-"+version+".doc"
version_xls=example_xls+".xls"
version_zip=example_zip+".zip"
shutil.copy(path+"\\模板\\"+example_doc+".doc",version_path+"\\"+version_doc)
print("已完成： 创建版本说明书")
shutil.copy(path+"\\模板\\"+example_xls+".xls",version_path+"\\"+version_xls)
print("已完成： 创建下发清单")
shutil.copy(path+"\\模板\\"+example_zip+".zip",version_path+"\\"+version_zip)
print("已完成： 创建安装手册")

########################################################################################
#3.版本说明书替换版本号、下发清单修改
########################################################################################

# 输入项目、问题单信息
taskId=input('输入任务编号：')
taskInfo=input('输入需求简述/变更点简述： ')
problemId=input('输入问题单编号：')
problemInfo=input('输入问题单简述/问题变更点简述：')

FileChange.updateDoc(version_path,version_doc,version,taskId,taskInfo, problemId,problemInfo)
FileChange.updateXls(version_path,version_xls,version_doc)


########################################################################################
# 4.压缩成zip包
########################################################################################
zip.zip_ya(version_path)
shutil.move(version_path+'.zip',path+'\\zip')
print('已完成 版本文件',version)

########################################################################################
########################################################################################

