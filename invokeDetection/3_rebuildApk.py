
import os
rebuildApkPath = "/home/xueling/apkAnalysis/invokeDetection/rebuildApk/"
smaliPath = "/home/xueling/apkAnalysis/invokeDetection/smalis/"
apkNameList = []

for line in open("/home/xueling/apkAnalysis/invokeDetection/apkName_1007").readlines():
    line = line.strip() + ".apk"
    apkNameList.append(line)
print len(apkNameList)

files = os.listdir(rebuildApkPath)

i = 1
for line in apkNameList:
    print i
    if line in files:
        print "exists!!!"
        i += 1
        continue

    else:
        cmd = "apktool b %s%s -o %s%s" % (smaliPath, line, rebuildApkPath, line)
        print cmd
        os.system(cmd)
        i += 1