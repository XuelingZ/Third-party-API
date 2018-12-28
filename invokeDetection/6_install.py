# install apk (10 app each batch) and start the app on device


import os
import time
apk_signedPath = "/home/xueling/apkAnalysis/invokeDetection/apk_signed/crashlytics/100/100/"
platformPath = "/home/xueling/Android/Sdk/platform-tools"
packageNameListALL = []
apkNameList = []


def uninstallApk(packageName):
    cmd="adb uninstall %s"%packageName
    print cmd
    print getCmdEexcuteResult(cmd)

#

def getCmdEexcuteResult(cmd):
    tmp = os.popen(cmd).readlines()
    return tmp


def getPackageName(installName):
    installName = apk_signedPath + installName
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
    packageNameList=[]
    count_installed = 0
    print "the %dth batch:"%index
    print apkNameList
    # print "len(apkNameList) : %d" %len(apkNameList)
    apkName_installed=[]
    for apkName in apkNameList:                      # install 10apk
        print "%s installing"%apkName
        if ((installApk(apkName)) == 0):
            count_installed += 1
            print "apk_installed: %d" %count_installed
            apkName_installed.append(apkName)
    print " the appInstalled in this bath:"
    print apkName_installed
    for apkName in apkName_installed:
        packageName = getPackageName(apkName)
        packageNameList.append(packageName)
        # packageNameListALL.append(packageName)

    # print "start Apk..........................."
    # # start APK
    # for packageName in packageNameList:
    #     startApk(packageName)
    # time.sleep(30)
    print "login to the app...................."
    # time.sleep(180)
    console=raw_input("delete all apk in this batch,enter y")
    if console =='y':
        for packageName in packageNameList:
            uninstallApk(packageName)


def installAndStart():
    apkNameList=[]       # complete list
    apkNameList10N=[]        # 10 apks
    apkNameList_lastbatch = []
    count = 0
    for i in os.listdir(apk_signedPath):
        if os.path.isfile(os.path.join(apk_signedPath, i)):
            if i[-4:] == '.apk':
                apkName = i
                apkNameList.append(apkName)
    print len(apkNameList)

    index=1
    for apkName in apkNameList:
        apkNameList10N.append(apkName)
        count+=1
        if count%10 == 0:
            # print apkNameList10N
            batch(apkNameList10N, index)            #rank every 10 apks
            index += 1
            apkNameList10N = []

        if len(apkNameList) - count < len(apkNameList)%10:
            apkNameList_lastbatch.append(apkName)

        if count == len(apkNameList):
            batch(apkNameList_lastbatch, index)

    # print apkNameList10N



installAndStart()