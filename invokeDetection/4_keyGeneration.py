import pexpect
import sys

keyPath = "/home/xueling/apkAnalysis/invokeDetection/keys/"
apkNameList = []

for line in open("/home/xueling/apkAnalysis/invokeDetection/apkName_1007").readlines():
    line = line.strip() + ".apk"
    apkNameList.append(line)
print len(apkNameList)

i = 1
for line in apkNameList:
    print i
    cmd = "keytool -genkey -alias abc.keystore -keyalg RSA -validity 20000 -keystore %s%s.keystore"%(keyPath, line)
    print cmd
    child = pexpect.spawn(cmd, logfile = sys.stdout)

    #password
    try:
        if(child.expect([pexpect.TIMEOUT, 'password'])):
            child.sendline('123456')
    except:
        print (str(child))


    #re-enter password
    try:
        if (child.expect([pexpect.TIMEOUT, 'Re-enter'])):
            child.sendline('123456')
    except:
        print (str(child))


    # last name
    try:
        if (child.expect([pexpect.TIMEOUT, 'last'])):
            child.sendline('zhang')
    except:
        print (str(child))


    # unit
    try:
        if (child.expect([pexpect.TIMEOUT, 'unit'])):
            child.sendline('utsa')
    except:
        print (str(child))


    # organization
    try:
        if (child.expect([pexpect.TIMEOUT, 'organization'])):
            child.sendline('utsa')
    except:
     print (str(child))


    # city
    try:
        if (child.expect([pexpect.TIMEOUT, 'City'])):
            child.sendline('SA')
    except:
        print (str(child))


    # state
    try:
        if (child.expect([pexpect.TIMEOUT, 'State'])):
            child.sendline('Tx')
    except:
        print (str(child))

    # country code
    try:
        if (child.expect([pexpect.TIMEOUT, 'country code'])):
            child.sendline('01')
    except:
        print (str(child))

    # correct?
    try:
        if (child.expect([pexpect.TIMEOUT, 'correct'])):
            child.sendline('y')
    except:
        print (str(child))


    # RETURN
    try:
        if (child.expect([pexpect.TIMEOUT, 'RETURN'])):
            child.sendline('\n')
    except:
        print (str(child))


    try:
        child.expect([pexpect.TIMEOUT, pexpect.EOF])
    except:
        print (str(child))

    i+= 1