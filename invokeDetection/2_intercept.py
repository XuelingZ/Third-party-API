import os


#=================================================MixpanelAPI.identify==========================   1
# decodeFilePath = "/home/xueling/apkAnalysis/invokeDetection/decodeFile/mixpanel/"
# APIfileName = "MixpanelAPI.smali"
# APIname = ".method public identify"
#
# locals_org = "locals"
# locals_new = "    .locals 5"
# targetStatement = "locals"
# text_toBeAdd = " \
#     new-instance v3, Ljava/lang/Exception;\n \
#     const-string v4, \"Xueling:printTrace with parameter UserID:\"\n \
#     invoke-direct {v3,v4}, Ljava/lang/Exception;-><init>(Ljava/lang/String;)V\n \
#     invoke-virtual {v3}, Ljava/lang/Exception;->printStackTrace()V\n \
#     invoke-static{v4, p1},Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I"


# #=================================================Leanplum.setUserId==========================   2
# decodeFilePath = "/home/xueling/apkAnalysis/invokeDetection/decodeFile/leanplum.setUserId/"
# APIfileName = "Leanplum.smali"
# APIname = ".method public static setUserId"
#
# locals_org = "locals"
# locals_new = "    .locals 5"
# targetStatement = "locals"
# text_toBeAdd = " \
#     new-instance v3, Ljava/lang/Exception; \n \
#     const-string v4, \"Xueling:printTrace with parameter UserID:\"\n \
#     invoke-direct {v3,v4}, Ljava/lang/Exception;-><init>(Ljava/lang/String;)V\n \
#     invoke-virtual {v3}, Ljava/lang/Exception;->printStackTrace()V\n \
#     invoke-static{v4, p0},Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I"



# # #=================================================Leanplum.setUserAttributes==========================   3
# decodeFilePath = "/home/xueling/apkAnalysis/invokeDetection/decodeFile/leanplum.setUserAttributes/"
# APIfileName = "Leanplum.smali"
# APIname = ".method public static setUserAttributes(Ljava/lang/String;Ljava/util/Map;)V"
#
# locals_org = "locals"
# locals_new = "    .locals 6"
# targetStatement = "Ljava/util/HashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;"
# text_toBeAdd = " \
#     new-instance v4, Ljava/lang/Exception; \n \
#     const-string v5, \"Xueling:printTrace with parameter:\"\n \
#     invoke-direct {v4,v5}, Ljava/lang/Exception;-><init>(Ljava/lang/String;)V\n \
#     invoke-virtual {v4}, Ljava/lang/Exception;->printStackTrace()V\n \
#     invoke-static{v5, p0},Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I"

# #=================================================Leanplum.setDeviceId==========================   4
# decodeFilePath = "/home/xueling/apkAnalysis/invokeDetection/decodeFile/leanplum.setDeviceId/"
# APIfileName = "Leanplum.smali"
# APIname = ".method public static setDeviceId(Ljava/lang/String;)V"
#
# locals_org = "locals"
# locals_new = "    .locals 6"
# targetStatement = "locals"
# text_toBeAdd = " \
#     new-instance v4, Ljava/lang/Exception; \n \
#     const-string v5, \"Xueling:printTrace with parameter:\"\n \
#     invoke-direct {v4,v5}, Ljava/lang/Exception;-><init>(Ljava/lang/String;)V\n \
#     invoke-virtual {v4}, Ljava/lang/Exception;->printStackTrace()V\n \
#     invoke-static{v5, p0},Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I"



# #=================================================Leanplum.setDeviceId==========================   5
decodeFilePath = "/home/xueling/apkAnalysis/invokeDetection/decodeFile/leanplum.setDeviceId/"
APIfileName = "Leanplum.smali"
APIname = ".method public static setDeviceId(Ljava/lang/String;)V"

locals_org = "locals"
locals_new = "    .locals 6"
targetStatement = "locals"
text_toBeAdd = " \
    new-instance v4, Ljava/lang/Exception; \n \
    const-string v5, \"Xueling:printTrace with parameter:\"\n \
    invoke-direct {v4,v5}, Ljava/lang/Exception;-><init>(Ljava/lang/String;)V\n \
    invoke-virtual {v4}, Ljava/lang/Exception;->printStackTrace()V\n \
    invoke-static{v5, p0},Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I"

count = 0
def generateNewAPIfile(decodeFile):
    print decodeFile
    global count
    count += 1
    print count
    index = -1

    flag = 0
    flag_goPart2 = 0
    test_org = []

    text_part1 = []
    text_part2 = []
    text_new = []

    cmd = "find %s -iname \"%s\" " %(decodeFile, APIfileName)
    path = os.popen(cmd).readlines()
    print path
    if path:
        APIfilePath = path[0].strip()
    else:
        return -1

    # print APIfilePath
    APIfile = open(APIfilePath)
    text_org = APIfile.readlines()
    # print "text_org len before: %d " %len(text_org)

    for line in text_org:
        index += 1
        if APIname in line:              # locate the API method
            flag = 1
            print "APIname : %d" %index
            text_part1.append(line)
            continue

        if flag == 1 and locals_org in line:    # change the locals
            text_part1.append(locals_new)
            print "locals: %d" %index
            if locals_org in targetStatement:                     # locals is the place to insert
                text_part1.append(text_toBeAdd)
                continue
            continue

        if flag == 1 and targetStatement in line:       # the place to insert
            text_part1.append(line)
            text_part1.append(text_toBeAdd)
            flag = 0
            flag_goPart2 = 1
            print "target %d" %index
            continue

        if flag_goPart2 == 1:
            text_part2.append(line)

        else:
            text_part1.append(line)

    text_new = text_part1 + text_part2
    APIfile.close()

    os.rename(APIfilePath, APIfilePath + "_bak")
    fw = open(APIfilePath, 'w+')
    for line in text_new:
        fw.write(line + '\n')

def intercept():
    for file in os.listdir(decodeFilePath):
        if os.path.isfile(os.path.join(decodeFilePath, file)):
            continue
        if generateNewAPIfile(decodeFilePath + file + "/") == -1:
            print "No API file found!"
            continue


def redo():
    for file in os.listdir(decodeFilePath):
        if os.path.isfile(os.path.join(decodeFilePath, file)):
            continue
        else:
            cmd = "find %s -iname \"%s\" " % (decodeFilePath + file, APIfileName)
            print cmd + ".................."
            path = os.popen(cmd).readlines()
            print path
            if path:
                APIfilePath = path[0].strip()
                os.remove(APIfilePath)
                cmd = "find %s -iname \"%s\" " % (decodeFilePath + file, APIfileName + "_bak")
                print cmd + "................."

                path = os.popen(cmd).readlines()
                print path
                if path:
                    APIfilePath_bak = path[0].strip()
                    os.rename(APIfilePath_bak, APIfilePath)
                else:
                    print ".smali_bak No found! "
            else:
                print ".smali No found! "


# redo()
intercept()