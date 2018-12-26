# decode

import os


APKpath = "/home/xueling/apkAnalysis/APK/"
apkPath = "/home/xueling/apkAnalysis/invokeDetection/apks/"
smaliPath = "/home/xueling/apkAnalysis/invokeDetection/smalis/"
decodeFilePath = "/home/xueling/apkAnalysis/invokeDetection/decodeFile/leanplum.setUserAttributes/"
keyPath = "/home/xueling/apkAnalysis/invokeDetection/keys/"
rebuildApkPath = "/home/xueling/apkAnalysis/invokeDetection/rebuildApk/"
apk_signedPath = "/home/xueling/apkAnalysis/invokeDetection/apk_signed/"
apkNameList = []


#decode 1007 apks
def decode():
    # get apkNamelist_1007
    # for line in open("/home/xueling/apkAnalysis/invokeDetection/apkName_1007").readlines():
    for line in open("/home/xueling/apkAnalysis/invokeDetection/decodeFile/nameList/leanplum.setUserAttributes").readlines():
        line = line.strip() + ".apk"
        apkNameList.append(line)
    print len(apkNameList)


    i = 1
    files = os.listdir(decodeFilePath)
    for line in apkNameList:
        # # # copy 1007 apks to apkPath
        # cmd = "cp %s%s %s" %(APKpath,line, apkPath)
        # os.system(cmd)
        # i += 1

        # decompiile to smaliPath
        print i
        if line in files:
            print "exists!!!"
            i += 1
            continue

        else:
            cmd = "apktool d %s%s -o %s%s" %(apkPath, line, decodeFilePath, line)
            print cmd
            os.system(cmd)
            i += 1

        # # rebuild APK
        # line = line[:-5]
        # # cmd = "apktool b %s%s -o %s" %(smaliPath, line, rebuildApkPath)
        # # os.system(cmd)


decode()

# # move to library name
# for line in open("/home/xueling/apkAnalysis/invokeDetection/decodeFile/nameList/leanplum.setUserAttributes").readlines():
#     line = line.strip() + ".apk"
#     cmd = "mv %s%s %s" %(smaliPath, line, "/home/xueling/apkAnalysis/invokeDetection/decodeFile/leanplum.setUserAttributes/")
#     print cmd
#     os.system(cmd)
