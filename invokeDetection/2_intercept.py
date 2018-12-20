import os

apkPath = "/Users/xueling/Desktop/smalis/"

APIfileName = "MixpanelAPI.smali"
APIname = ".method public identify"

locals_org = "locals 3"
locals_new = "locals 4"
targetStatement = "locals"
text_toBeAdd = " \
    new-instance v2, Ljava/lang/Exception;\n \
    const-string v3, \"Xueling:printTrace with parameter UserID:\"\n \
    invoke-direct {v2,v3}, Ljava/lang/Exception;-><init>(Ljava/lang/String;)V\n \
    invoke-virtual {v2}, Ljava/lang/Exception;->printStackTrace()V\n \
    invoke-static{v3, p1},Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I"


flag = 0
flag_goPart2 = 0
test_org = []

text_part1 = []
text_part2 = []
text_new = []



def generateNewAPIfile(file):
    cmd = "find . -name \"%s\" %s" %(APIfileName, apkPath+file)
    print cmd
    path = os.popen(cmd).readlines()
    print path
    if path == "null":
        return -1
    APIfilePath = path[0].strip()
    print APIfilePath
    APIfile = open(APIfilePath)
    text_org = APIfile.readlines()
    print "text_org len before: %d " %len(text_org)
    os.rename(APIfilePath, APIfilePath + "_bak")

    for line in text_org:
        if APIname in line:              # locate the API method
            flag = 1

        if flag ==1 and locals_org in line:             # change the locals
            text_part1.append(locals_new)
            continue

        if flag == 1 and targetStatement in line:       # the place to insert
            text_part1.append(line)
            text_part1.append(text_toBeAdd)
            flag = 0
            flag_goPart2 = 1
            continue

        if flag_goPart2 == 1:
            text_part2.append(line)
            continue

        text_part1.append(line)

    APIfile.close()
    text_new = text_part1 + text_part2

    fw = open(APIfileName, 'w+')
    for line in text_new:
        fw.write(line + '\n')


for file in os.listdir(apkPath):
    if os.path.isfile(os.path.join(apkPath, file)):
        continue
    if generateNewAPIfile(file) == -1:
        print "No API file found!"
        continue
