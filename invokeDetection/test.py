



flag = 0
flag_goPart2 = 0
test_org = []

text_part1 = []
text_part2 = []
text_new = []

APIname = ".method public identify"
count = 0
index = -1
locals_org = "locals"
locals_new = "locals 5"
targetStatement = "locals"
text_toBeAdd = " \
    new-instance v3, Ljava/lang/Exception;\n \
    const-string v4, \"Xueling:printTrace with parameter UserID:\"\n \
    invoke-direct {v3,v4}, Ljava/lang/Exception;-><init>(Ljava/lang/String;)V\n \
    invoke-virtual {v3}, Ljava/lang/Exception;->printStackTrace()V\n \
    invoke-static{v4, p1},Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I"

text_org = open("/home/xueling/apkAnalysis/invokeDetection/decodeFile/mixpanel/com.miniclip.dinopets.apk/smali/com/mixpanel/android/mpmetrics/MixpanelAPI.smali").readlines()
for line in text_org:
    count += 1
    index += 1
    # print count
    # print line
    # print flag
    if APIname in line:  # locate the API method
        flag = 1
        print "APIname : %d" %index

    if flag == 1 and locals_org in line:  # change the locals
        text_part1.append(locals_new)
        print line
        print "locals: %d" %index

    if flag == 1 and targetStatement in line:  # the place to insert
        flag = 0
        if locals_org in line:  # locals is the place to insert
            text_part1.append(text_toBeAdd)
        else:
            text_part1.append(line)
            text_part1.append(text_toBeAdd)
        flag = 0
        flag_goPart2 = 1

    if flag_goPart2 == 1:
        text_part2.append(line)

    else:
        text_part1.append(line)
