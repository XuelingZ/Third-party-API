# install apk (10 app each batch) and start the app on device


import os
import time
apk_signedPath = "/home/xueling/apkAnalysis/invokeDetection/apk_signed/"
platformPath = "/home/xueling/Android/Sdk/platform-tools"
packageNameListALL = []


def uninstallApk(packageName):
    cmd="adb uninstall %s"%packageName
    print getCmdEexcuteResult(cmd)

#

def getCmdEexcuteResult(cmd):
    tmp = os.popen(cmd).readlines()
    # print "command result : "
    # print tmp
    return tmp


def getPackageName(installName):
    installName = apk_signedPath + installName
    # cmd='aapt dump badging "%s"  | findstr "package"'%installName
    cmd = 'aapt dump badging "%s" '%installName
    print cmd
    str= getCmdEexcuteResult(cmd)[0].split(" ")[1]
    return str[6:-1]

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
        print packagename_mainActivity
    except:
        print "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        packagename_mainActivity = packageName + "/"

    print packagename_mainActivity
    cmd = "adb shell am start %s"%packagename_mainActivity
    print getCmdEexcuteResult(cmd)

def installApk(name):
    print name
    name = apk_signedPath + name
    cmd='./adb  install "%s"' %name
    os.chdir(platformPath)
    return os.system(cmd)

def batch(apkNameList,index):
    print "under rank()"
    packageNameList=[]
    print "the %dth batch"%index
   # install 10apk
    apkName_installed=[]
    for apkName in apkNameList:
        print "%s installing"%apkName
        if ((installApk(apkName)) == 0):
            apkName_installed.append(apkName)
    #     writeFile("apkInstalled.log",apkName)
    # writeFile("apkInstalled.log", "************************")

    # get packageName and main activity
    for apkName in apkName_installed:
        packageName = getPackageName(apkName)
        print "packageName: " + packageName
        # writeFile("apkInstalledPackageName.log",packageName)
        packageNameList.append(packageName)
        packageNameListALL.append(packageName)
    # writeFile("apkInstalledPackageName.log", "************************")

    # print "loging..."
    # i = 1
    # while i <= 5:
    #     meminfoLog("noStartApkMeminfo_%d.txt"%index, i)
    #     cpuinfoLog("noStartApkCPUinfo_%d.txt" % index, i)
    #     if i == 5:
    #         break
    #     time.sleep(60)  # 休眠60秒
    #     i += 1
    # print "log all done"
    print "start Apk..........................."
    # start APK
    for packageName in packageNameList:
        startApk(packageName)
    time.sleep(30)
    console=raw_input("delete all apk in this batch,enter y")
    if console =='y':
        for packageName in packageNameList:
            uninstallApk(packageName)
    # print "loging..."
    # i = 1
    # while i <= 5:
    #     meminfoLog("startApkMeminfo_%d.txt"%index, i)
    #     cpuinfoLog("startApkCPUinfo_%d.txt" % index, i)
    #     if i == 5:
    #         break
    #     time.sleep(60)  # 休眠60秒
    #     i += 1
    # print "log all done"
    # print "all done"


def installAndStart():
    apkNameList=[]       # complete list
    apkNameList10N=[]        # 10 apks
    count = 0
    for i in os.listdir(apk_signedPath):
        if os.path.isfile(os.path.join(apk_signedPath, i)):
            if i[-4:] == '.apk':
                apkName = i
                apkNameList.append(apkName)
    index=1
    print apkNameList

    for apkName in apkNameList:
        apkNameList10N.append(apkName)
        count+=1
        if count%10 == 0:
            print apkNameList10N
            batch(apkNameList10N, index)            #rank every 10 apks
            index += 1



# def writeFile(fileName,data):
#     f=open(fileName,'a+')
#     f.write(data+"\r\n")
#     f.close
#
# def outputLog(cmd,fileName,index):
#
#         writeFile(fileName,"#########%d bigin#########\r\n"%index)
#         exeResult=getCmdEexcuteResult(cmd)
#         writeFile(fileName,"\r\n".join(exeResult))
#         writeFile(fileName,"#########%d end#########\r\n"%index)
#
#
# def meminfoLog(fileName,index):
#     cmd='adb shell dumpsys meminfo'
#     outputLog(cmd,fileName,index)
#
# def cpuinfoLog(fileName,index):
#     cmd='adb shell dumpsys cpuinfo'
#     outputLog(cmd,"fileName",index)