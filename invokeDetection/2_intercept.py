
import os\
import re
# com.flurry.android.FlurryAgent.setUserId
flurryPath = "/home/xueling/apkAnalysis/invokeDetection/interception/flurry/"
smaliPath = "/home/xueling/apkAnalysis/invokeDetection/smalis/"
# for line in open(flurryPath + 'apkName_flurry').readlines():
#     line = line.strip() + ".apk"
#     cmd = "cp -r %s%s %s"%(smaliPath, line, flurryPath)
#     print cmd
#     os.system(cmd)




#delete:
cmd = "find . -name "MixpanelAPI.smali""
APIfile = os.popen(cmd).readlines()
cmd1 = "sed -i '/.method public identify/{n;d}' MixpanelAPI.smali"
#add:
scmd2 = "ed -i '/.method public identify/a\1111111\n2222222' MixpanelAPI.smali"


1. find FlurryAgent.smlai
2. find .method public static setUserId