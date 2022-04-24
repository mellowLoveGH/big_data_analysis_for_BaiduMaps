import sys

def invalid(data):
    if len(data)<=0 or data[0]!="9":
        return True
    #
    category0 = {"9CN":"cell", "9WN": "wifi", "9PN": "prop", "9FN":"fp"}
    for k, v in category0.items():
        if data.startswith(k):
            return True
    #
    record = data.split("\t")
    if len(record) != 2:
        return True
    info, fre = record[0].strip(), int(record[1])
    if "-" in info:
        ps = info.split("-")
        if len(ps) != 3:
            return True
        for k in ["CN", "WN", "PN", "FN"]:
            if ps[-1].startswith(k):
                return True
    return False

def categorize(info):
    category0 = {"9C":"cl", "9W": "wf", "9P": "pp", "9F":"fp"}
    for k, v in category0.items():
        if info.startswith(k):
            dis = int( info.replace(k, "") )
            return [v, "all", dis]
    #
    ps = info.split("-")
    city = ps[1]
    #print("----------------", city)
    category1 = {"C":"cl", "W": "wf", "P": "pp", "F":"fp"}
    for k, v in category1.items():
        if ps[2].startswith(k):
            dis = int( ps[2].replace(k, "") )
            return [v, city, dis]
    return []


# ------------------------------ running from here
error_count = 0
valid_count = 0
col_list = []
error_list = []

for data in sys.stdin:
    data = data.strip()
    if invalid(data):
        #print("---------------------", data)
        error_list.append( data )
        error_count += 1
        continue
    try:
        record = data.split("\t")
        if len(record) == 2:
            info, fre = record[0], int(record[1])
            tmp = categorize(info)
            category, city, dis = tmp[0], tmp[1], tmp[2]
            it = (category, city, dis, fre)
            col_list.append( it )
            #st = category + "\t" + city + "\t" + str(dis) + "\t" + str(fre)
            #print(st)
        #
        valid_count += 1
    except:
        #
        error_count += 1
#
print( error_count, valid_count, error_count+valid_count )
tmp = sorted( col_list, key=lambda x: (x[0], x[1], x[2]) )
for it in tmp:
    category, city, dis, fre = it 
    st = category + "\t" + city + "\t" + str(dis) + "\t" + str(fre)
    print(st)
###
fg = True
fg = False
if fg:
    for it in error_list:
        print(it)