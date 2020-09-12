
import configparser
import ftpUtil

cf = configparser.ConfigParser(allow_no_value=True)
cf.read(r"D:\Users\Desktop\版本\交易银行版本\config.txt",encoding='utf-8')

#源码ftp配置
port=21
host_s=cf.get("下发",'host')
user_s=cf.get("下发",'user')
pass_s=cf.get("下发",'pass')
remotepath=cf.get("下发",'remotepath')
localpath=cf.get("下发",'localpath')

#下载源码
ftp=ftpUtil.ftpconnect(host_s,port,user_s,pass_s)
ftpUtil.downloadfile(ftp,remotepath, localpath)

#初审ftp配置
host_d=cf.get("初审",'host')
user_d=cf.get("初审",'user')
pass_d=cf.get("初审",'pass')
remotepath=cf.get("初审",'remotepath')
localpath=cf.get("初审",'localpath')

ftp=ftpUtil.ftpconnect(host_s,port,user_s,pass_s)
ftpUtil.uploadfile(ftp, remotepath, localpath)



