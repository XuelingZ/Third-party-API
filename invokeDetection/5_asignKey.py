
import pexpect
import sys

keyPath = "/home/xueling/apkAnalysis/invokeDetection/keys/"
apk_signedPath = "/home/xueling/apkAnalysis/invokeDetection/apk_signed/"
rebuildApkPath = "/home/xueling/apkAnalysis/invokeDetection/rebuildApk/"
apkNameList = []

for line in open("/home/xueling/apkAnalysis/invokeDetection/apkName_1007").readlines():
    line = line.strip() + ".apk"
    apkNameList.append(line)
print len(apkNameList)

i = 1
for line in apkNameList:
    print i
    key = line + ".keystore"
    cmd = "jarsigner -verbose -keystore %s%s -storepass 123456 -signedjar %s%s %s%s abc.keystore" %(keyPath, key,apk_signedPath,line, rebuildApkPath, line)
    print cmd
    child = pexpect.spawn(cmd, logfile = sys.stdout)

    # #password
    # try:
    #     if(child.expect([pexpect.TIMEOUT, 'password'])):
    #         child.sendline('123456')
    # except:
    #     print (str(child))
    #

    try:
        child.expect([pexpect.TIMEOUT, pexpect.EOF])
    except:
        print (str(child))


