import os

decodeFilePath = "/home/xueling/apkAnalysis/invokeDetection/decodeFile/mixpanel/"

APIfileName = "MixpanelAPI.smali"
APIname = ".method public identify"

locals_org = "locals"
locals_new = "locals 5"
targetStatement = "locals"
text_toBeAdd = " \
    new-instance v3, Ljava/lang/Exception;\n \
    const-string v4, \"Xueling:printTrace with parameter UserID:\"\n \
    invoke-direct {v3,v4}, Ljava/lang/Exception;-><init>(Ljava/lang/String;)V\n \
    invoke-virtual {v3}, Ljava/lang/Exception;->printStackTrace()V\n \
    invoke-static{v4, p1},Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I"

count = 0



def generateNewAPIfile(decodeFile):
    global count
    index = -1

    flag = 0
    flag_goPart2 = 0
    test_org = []

    text_part1 = []
    text_part2 = []
    text_new = []

    cmd = "find %s -iname \"%s\" " %(decodeFile, APIfileName)
    path = os.popen(cmd).readlines()
    print decodeFile


    if path == "null":
        return -1
    APIfilePath = path[0].strip()

    # cmd = "grep -A 1 \".method public identify\" %s" %APIfilePath     # check the locals
    # result = os.popen(cmd).readlines()
    # print result

    print APIfilePath
    APIfile = open(APIfilePath)
    text_org = APIfile.readlines()
    print "text_org len before: %d " %len(text_org)



    for line in text_org:
        index += 1
        if APIname in line:              # locate the API method
            flag = 1
            count += 1
            print count
            print "APIname : %d" %index

        if flag == 1 and locals_org in line:    # change the locals
            text_part1.append(locals_new)
            print "locals: %d" %index


        if flag == 1 and targetStatement in line:       # the place to insert
            if  locals_org in targetStatement:                     # locals is the place to insert
                text_part1.append(text_toBeAdd)
            else:
                text_part1.append(line)
                text_part1.append(text_toBeAdd)
            flag = 0
            flag_goPart2 = 1
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


for file in os.listdir(decodeFilePath):
    if os.path.isfile(os.path.join(decodeFilePath, file)):
        continue
    if generateNewAPIfile(decodeFilePath + file + "/") == -1:
        print "No API file found!"
        continue