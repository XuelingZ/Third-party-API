#coding=utf-8
#adb install Babe.apk
#aapt dump badging Babe.apk  | findstr "package"
import os
import time
def getCmdEexcuteResult(cmd):
    tmp = os.popen(cmd).readlines()
    return tmp

def getPackageName(installName):
    cmd='aapt dump badging "%s"  | findstr "package"'%installName

    print cmd
    str= getCmdEexcuteResult(cmd)[0].split(" ")[1]
    return str[6:-1]

def getPackageNameInfo(packageName):
    cmd='adb shell dumpsys package %s'%packageName
    print cmd
    exeResutl= getCmdEexcuteResult(cmd)[3]
    return exeResutl

def getPackageNameInfo(packageName):
    cmd='adb shell dumpsys package %s'%packageName
    print cmd
    exeResut= getCmdEexcuteResult(cmd)
    #print exeResut
    for index,val  in enumerate(exeResut):
        #print index ,val
        if val.strip("\r\n").strip()=='Action: "android.intent.action.MAIN"':
            return exeResut[index-1].strip().split(" ")[1]

def startApk(packageName):
    try:
        packagename_mainActivity = getPackageNameInfo(packageName)
    except:
        print "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        packagename_mainActivity = packageName + "/"

    print packagename_mainActivity
    cmd = "adb shell am start %s"%packagename_mainActivity
    print getCmdEexcuteResult(cmd)

def installApk(name):
    print name
    cmd='./adb  install -r "%s"'%name
    os.chdir("/Users/xueling/Library/Android/sdk/platform-tools")
    os.system(cmd)

def uninstallApk(packageName):
    cmd="adb uninstall %s"%packageName
    print getCmdEexcuteResult(cmd)

def writeFile(fileName,data):
    f=open(fileName,'a+')
    f.write(data+"\r\n")
    f.close

def outputLog(cmd,fileName,index):

        writeFile(fileName,"#########%d bigin#########\r\n"%index)
        exeResult=getCmdEexcuteResult(cmd)
        writeFile(fileName,"\r\n".join(exeResult))
        writeFile(fileName,"#########%d end#########\r\n"%index)


def meminfoLog(fileName,index):
    cmd='adb shell dumpsys meminfo'
    outputLog(cmd,fileName,index)

def cpuinfoLog(fileName,index):
    cmd='adb shell dumpsys cpuinfo'
    outputLog(cmd,"fileName",index)

def rank(apkNameList,index):
    packageNameList=[]
    print "the %dth"%index
    #install 10apk
    for apkName in apkNameList:
        print "%s installing"%apkName
        print "%s install  " % apkName ,
        installApk(apkName)
        writeFile("apkInstalled.log",apkName)
    writeFile("apkInstalled.log", "************************")

    # 获取包名和主界面名
    for apkName in apkNameList:
        packageName = getPackageName(apkName)
        print packageName
        writeFile("apkInstalledPackageName.log",packageName)
        packageNameList.append(packageName)
        packageNameListALL.append(packageName)
    writeFile("apkInstalledPackageName.log", "************************")

    print "loging..."
    i = 1
    while i <= 5:
        meminfoLog("noStartApkMeminfo_%d.txt"%index, i)
        cpuinfoLog("noStartApkCPUinfo_%d.txt" % index, i)
        if i == 5:
            break
        time.sleep(60)  # 休眠60秒
        i += 1
    print "log all done"
    print "start Apk"
    # 启动应用
    for packageName in packageNameList:
        startApk(packageName)
    print "loging..."
    i = 1
    while i <= 5:
        meminfoLog("startApkMeminfo_%d.txt"%index, i)
        cpuinfoLog("startApkCPUinfo_%d.txt" % index, i)
        if i == 5:
            break
        time.sleep(60)  # 休眠60秒
        i += 1
    print "log all done"
    print "all done"

def doWork():
    apkNameList=[]       # complete list
    apkNameList10N=[]        # 10 apks


    s = os.sep
    root = os.getcwd()  # current work directory
    count = 0
    for i in os.listdir(root):
        if os.path.isfile(os.path.join(root, i)):
            if i[-4:] == '.apk':
                count+=1
                apkName = i
                apkNameList10N.append(apkName)
                if count==10:
                    apkNameList.append(apkNameList10N)         #apkNameList -- complete list
                    apkNameList10N=[]
                    print apkNameList10N
                    count=0

    index=1
    for apkNameList10N in apkNameList:    #rank every 10 apks
        print apkNameList10N
        rank(apkNameList10N,index)
        index += 1




if __name__=="__main__":
    packageNameListALL = []
    doWork()
    console=raw_input("delete all apk,enter y")
    if console=='y':
        for packageName in packageNameListALL:
            uninstallApk(packageName)