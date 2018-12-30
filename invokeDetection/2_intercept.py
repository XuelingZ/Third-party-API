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



#===================================crashlytics.setUserEmail / setUserIdentifier /setUserName ================= 5 6 7
# decodeFilePath = "/home/xueling/apkAnalysis/invokeDetection/decodeFile/crashlytics/300/"  #ubuntu
# # decodeFilePath = "/Users/xueling/Desktop/anonymous/invokeDetection/apk/" # mac
# APIfileName = "Crashlytics.smali"
# APIname_1 = ".method public static setUserEmail(Ljava/lang/String;)V"
# APIname_2 = ".method public static setUserIdentifier(Ljava/lang/String;)V"
# APIname_3 = ".method public static setUserName(Ljava/lang/String;)V"
#
# locals_org = "locals"
# locals_new_1 = "    .locals 3"
# locals_new_2 = "    .locals 3"
# locals_new_3 = "    .locals 3"
#
# targetStatement_1 = "Lcom/crashlytics/android/core/CrashlyticsCore;->setUserEmail(Ljava/lang/String;)V"
# targetStatement_2 = "Lcom/crashlytics/android/core/CrashlyticsCore;->setUserIdentifier(Ljava/lang/String;)V"
# targetStatement_3 = "Lcom/crashlytics/android/core/CrashlyticsCore;->setUserName(Ljava/lang/String;)V"
#
# text_toBeAdd_1 = " \
#     new-instance v1, Ljava/lang/Exception; \n \
#     const-string v2, \"Xueling:printTrace with parameter:\"\n \
#     invoke-direct {v1,v2}, Ljava/lang/Exception;-><init>(Ljava/lang/String;)V\n \
#     invoke-virtual {v1}, Ljava/lang/Exception;->printStackTrace()V\n \
#     invoke-static{v2, p0},Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I"
#
# text_toBeAdd_2 = " \
#     new-instance v1, Ljava/lang/Exception; \n \
#     const-string v2, \"Xueling:printTrace with parameter:\"\n \
#     invoke-direct {v1,v2}, Ljava/lang/Exception;-><init>(Ljava/lang/String;)V\n \
#     invoke-virtual {v1}, Ljava/lang/Exception;->printStackTrace()V\n \
#     invoke-static{v2, p0},Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I"
#
#
# text_toBeAdd_3 = " \
#     new-instance v1, Ljava/lang/Exception; \n \
#     const-string v2, \"Xueling:printTrace with parameter:\"\n \
#     invoke-direct {v1,v2}, Ljava/lang/Exception;-><init>(Ljava/lang/String;)V\n \
#     invoke-virtual {v1}, Ljava/lang/Exception;->printStackTrace()V\n \
#     invoke-static{v2, p0},Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I"



#==================================================== com.amplitude.api.AmplitudeClient.setUserId ==================== 8
# decodeFilePath = "/home/xueling/apkAnalysis/invokeDetection/decodeFile/crashlytics/300/"  #ubuntu
decodeFilePath = "/Users/xueling/Desktop/anonymous/invokeDetection/apk/" # mac
APIfileName = "Amplitude.smali"
APIname_1 = ".method public static setUserId(Ljava/lang/String;)V"
locals_org = "locals"
locals_new_1 = "    .locals 3"
targetStatement_1 = "Lcom/amplitude/api/AmplitudeClient;->setUserId(Ljava/lang/String;)Lcom/amplitude/api/AmplitudeClient"

text_toBeAdd_1 = " \
    new-instance v1, Ljava/lang/Exception; \n \
    const-string v2, \"Third-party API invoke detection:Print StackTrace with parameter:\"\n \
    invoke-direct {v1,v2}, Ljava/lang/Exception;-><init>(Ljava/lang/String;)V\n \
    invoke-virtual {v1}, Ljava/lang/Exception;->printStackTrace()V\n \
    invoke-static{v2, p0},Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I"

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

# APIname_1
        if APIname_1 in line:              # locate the API method
            flag = 1
            print "%s : %d" %(APIname_1, index)
            text_part1.append(line)
            continue

        if flag == 1 and locals_org in line:    # change the locals
            text_part1.append(locals_new_1)
            print "locals: %d" %index
            if locals_org in targetStatement_1:                     # locals is the place to insert
                text_part1.append(text_toBeAdd_1)
                continue
            continue

        if flag == 1 and targetStatement_1 in line:       # the place to insert
            text_part1.append(line)
            text_part1.append(text_toBeAdd_1)
            flag = 0
            # flag_goPart2 = 1
            print "target 1: %d" %index
            continue
# # second API
#         if APIname_2 in line:              # locate the API method
#             flag = 2
#             print "%s : %d" %(APIname_2, index)
#             text_part1.append(line)
#             continue
#
#         if flag == 2 and locals_org in line:    # change the locals
#             text_part1.append(locals_new_2)
#             print "locals: %d" %index
#             if locals_org in targetStatement_2:                     # locals is the place to insert
#                 text_part1.append(text_toBeAdd_2)
#                 continue
#             continue
#
#         if flag == 2 and targetStatement_2 in line:       # the place to insert
#             text_part1.append(line)
#             text_part1.append(text_toBeAdd_2)
#             flag = 0
#             # flag_goPart2 = 1
#             print "target 2: %d" %index
#             continue
#
#         # else:
#         #     text_part1.append(line)
#
# # API_3
#         if APIname_3 in line:  # locate the API method
#             flag = 3
#             print "%s : %d" % (APIname_3, index)
#             text_part1.append(line)
#             continue
#
#         if flag == 3 and locals_org in line:  # change the locals
#             text_part1.append(locals_new_3)
#             print "locals: %d" % index
#             if locals_org in targetStatement_3:  # locals is the place to insert
#                 text_part1.append(text_toBeAdd_3)
#                 continue
#             continue
#
#         if flag == 3 and targetStatement_3 in line:  # the place to insert
#             text_part1.append(line)
#             text_part1.append(text_toBeAdd_3)
#             flag = 0
#             # flag_goPart2 = 1
#             print "target 3: %d" % index
#             continue

        else:
            text_part1.append(line)

    APIfile.close()
    os.rename(APIfilePath, APIfilePath + "_bak")
    fw = open(APIfilePath, 'w+')
    for line in text_part1:
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
            path_smali = os.popen(cmd).readlines()

            cmd = "find %s -iname \"%s\" " % (decodeFilePath + file, APIfileName + "_bak")
            path_bak = os.popen(cmd).readlines()

            print path_smali
            print path_bak
            if path_smali and path_bak:
                APIfilePath_smali = path_smali[0].strip()
                APIfilePath_bak = path_bak[0].strip()

                os.remove(APIfilePath_smali)
                os.rename(APIfilePath_bak, APIfilePath_smali)
            else:
                print ".smali or bak No found! "


# redo()
intercept()
