# decode

import os


APKpath = "/home/xueling/apkAnalysis/APK/"
apkPath = "/home/xueling/apkAnalysis/invokeDetection/apks/"
smaliPath = "/home/xueling/apkAnalysis/invokeDetection/smalis/"
keyPath = "/home/xueling/apkAnalysis/invokeDetection/keys/"
rebuildApkPath = "/home/xueling/apkAnalysis/invokeDetection/rebuildApk/"
apk_signedPath = "/home/xueling/apkAnalysis/invokeDetection/apk_signed/"
apkNameList = []


#decode 1007 apks
def decompile():

    # get apkNamelist_1007
    for line in open("/home/xueling/apkAnalysis/invokeDetection/apkName_1007").readlines():
        line = line.strip() + ".apk"
        apkNameList.append(line)
    print len(apkNameList)


    i = 1
    files = os.listdir(smaliPath)
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
            cmd = "apktool d %s%s -o %s%s" %(apkPath, line, smaliPath, line)
            print cmd
            os.system(cmd)
            i += 1

        # # rebuild APK
        # line = line[:-5]
        # # cmd = "apktool b %s%s -o %s" %(smaliPath, line, rebuildApkPath)
        # # os.system(cmd)


# decompile()

#move to library name
for line in open("/home/xueling/apkAnalysis/invokeDetection/mixpanel/smaliName").readlines():
    line = line.strip() + ".apk"
    cmd = "mv %s%s %s" %(smaliPath, line, "/home/xueling/apkAnalysis/invokeDetection/mixpanel/")
    print cmd
    os.system(cmd)
