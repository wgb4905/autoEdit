
import FileChange
import zip
import singleFileCreate
import shutil

# file_name="下发清单.xls"
# file_path=r"D:\python测试\模板"
# version_doc="软件产品版本说明书-IGTBNET-BAS_V01.0A_B08.02.doc"
# version='IGTBNET-BAS_V01.0A_B08.02'

path=r"D:\python测试" 
moudle_path=r"D:\python测试\模板"
# path=r"D:\Users\Desktop\版本\交易银行版本\源码" 
# moudle_path=r"D:\Users\Desktop\版本\交易银行版本\模板" 


# taskId=input('输入任务编号：')
# taskInfo=input('输入需求简述/变更点简述： ')
# problemId=input('输入问题单编号：')
# problemInfo=input('输入问题单简述/问题变更点简述：')
version=input('请输入版本号： ')


# XlsChange.updateXls(file_name,file_path,version_doc)
# XlsChange.updateDoc( file_path,version_doc,version,taskId,taskInfo, problemId,problemInfo)
# zip.zip_ya(r'D:\python测试\111')
# singleFileCreate.create_single(version,path,moudle_path,taskId,taskInfo, problemId,problemInfo)
shutil.copytree(path+"\\"+version,path+"\\"+version+'tmp')