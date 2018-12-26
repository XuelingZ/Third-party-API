
import os
rebuildApkPath = "/home/xueling/apkAnalysis/invokeDetection/rebuildApk/leanplum.setUserAttributes/"
decodeFilePath = "/home/xueling/apkAnalysis/invokeDetection/decodeFile/leanplum.setUserAttributes/"
apkNameList = []

# for line in open("/home/xueling/apkAnalysis/invokeDetection/apkName_1007").readlines():
#     line = line.strip() + ".apk"
#     apkNameList.append(line)
# print len(apkNameList)

files = os.listdir(rebuildApkPath)

i = 1

for file in os.listdir(decodeFilePath):
    if os.path.isfile(os.path.join(decodeFilePath, file)):
        continue

    if file in os.listdir(rebuildApkPath):
        print "Exists!!!!"
    else:
        cmd = "apktool b %s%s -o %s%s" % (decodeFilePath, file, rebuildApkPath, file)
        print cmd
        os.system(cmd)