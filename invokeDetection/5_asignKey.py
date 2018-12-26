
import pexpect
import sys
import os

keyPath = "/home/xueling/apkAnalysis/invokeDetection/keys/"
apk_signedPath = "/home/xueling/apkAnalysis/invokeDetection/apk_signed/leanplum.setUserAttributes/"
rebuildApkPath = "/home/xueling/apkAnalysis/invokeDetection/rebuildApk/leanplum.setUserAttributes/"
apkNameList = []
#
# for line in open("/home/xueling/apkAnalysis/invokeDetection/apkName_1007").readlines():
#     line = line.strip() + ".apk"
#     apkNameList.append(line)
# print len(apkNameList)

i = 1
# for line in apkNameList:
for file in os.listdir(rebuildApkPath):
    if os.path.isfile(os.path.join(rebuildApkPath, file)):
        key = file + ".keystore"
        cmd = "jarsigner -verbose -keystore %s%s -storepass 123456 -signedjar %s%s %s%s abc.keystore" %(keyPath, key,apk_signedPath,file, rebuildApkPath, file)
        print cmd
        child = pexpect.spawn(cmd, logfile = sys.stdout)

        #password
        try:
            if(child.expect([pexpect.TIMEOUT, 'password'])):
                child.sendline('123456')
        except:
            print (str(child))
        try:
            child.expect([pexpect.TIMEOUT, pexpect.EOF])
        except:
            print (str(child))


