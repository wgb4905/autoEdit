########################################################################################
#                                 程序说明
# 程序用来修改xls文件的内容
# 上送参数为xls文件名，路径
########################################################################################

"""
上送参数为xls文件名，路径
"""
___Author___ = "Frank Wang"
___Date_____ = "2020/8/16"
___Version___= "1.0"

import pyexcel_xls
import os
import win32com.client



def updateXls(file_path,version_xls,version_doc):
    
    excel = win32com.client.Dispatch('Excel.Application')
    excel.Visible = False #后台运行
    excel.DisplayAlerts = False
    myBook = excel.Workbooks.Open(file_path+"\\"+version_xls)

    #更新下发程序清单sheet
    mySheet = myBook.Worksheets("下发程序清单")
    code_path=file_path+"\\下发包"
    files=os.listdir(code_path)
    i=1 #下发包序号初始化
    row = 3 #从第三行开始写
    mySheet.Rows("3:500").delete # 删除行，清除历史数据
    for file in files:
        mySheet.Cells(row,1).Value=i #下发包序号
        mySheet.Cells(row,2).Value=file #下发包序号
        i=i+1
        row=row+1
        print(version_xls,"下发程序清单  增加下发包："+file)    

    #更新下发文档清单sheet
    mySheet = myBook.Worksheets("下发文档清单")
    mySheet.Rows("4:500").delete # 删除行，清除历史数据
    mySheet.Cells(4,1).Value= 2
    mySheet.Cells(4,2).Value=version_doc
    print(version_xls,"下发文档清单  增加："+version_doc)

    #保存xls
    myBook.Save()

    # 退出
    myBook.Close()
    # print('保存并退出',version_xls)


def updateDoc( file_path,version_doc,version,taskId,taskInfo, problemId,problemInfo):
    word = win32com.client.Dispatch('Word.Application')
    word.Visible = False # 后台运行
    myDoc = word.Documents.Open(file_path+"\\"+version_doc) # 打开一个已有的word文档

    #替换关键字
    word.Selection.Find.ClearFormatting()
    word.Selection.Find.Replacement.ClearFormatting()
    word.Selection.Find.Execute('$version$', False, True, False, False, False, True, 1, True, version, 2)
    print(version_doc,'完成替换版本号 新版本号为：', version)
    word.Selection.Find.Execute('$taskId$', False, True, False, False, False, True, 1, True, taskId, 2)
    word.Selection.Find.Execute('$taskInfo$', False, True, False, False, False, True, 1, True, taskInfo, 2)
    word.Selection.Find.Execute('$problemId$', False, True, False, False, False, True, 1, True, problemId, 2)
    word.Selection.Find.Execute('$problemInfo$', False, True, False, False, False, True, 1, True, problemInfo, 2)
    print(version_doc,'完成任务单、问题单信息更新')

    #保存
    myDoc.Save()
    #退出
    myDoc.Close()
    word.Quit()
    # print('保存并退出',version_doc)

