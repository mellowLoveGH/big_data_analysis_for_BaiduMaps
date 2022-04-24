
# parse every line
def parse01(ln):
    ps = ln.split("\t")
    if len(ps) == 4:
        category, city, dis, fre = ps[0], ps[1], int(ps[2]), int(ps[3])
        it = [category, city, dis, fre]
        return it
    return []

# search certain type of data by category and city
def search01(col_list, c1, c2): # c1 -> category, c2 -> city
    tmp = []
    for it in col_list:
        category, city, dis, fre = it[0], it[1], it[2], it[3]
        if category==c1 and city==c2:
            tmp.append( it )
    return tmp

def form_str(st, length=10):
    st = str(st)
    i = len(st)
    while i<=10:
        st = st + " "
        i += 1
    return st

def form_line(category, city, dis_range, fre, cumulative, total):
    st = ""
    st = st + category + "\t," + city + "\t," + form_str(dis_range, 10) + "\t,"
    st = st + form_str(fre, 10) + "\t," + form_str(cumulative, 10) + "\t," 
    st = st + str( round( float(cumulative)/total * 100, 2 ) ) + "%"
    return st

# 
def sub_report01(sub_list):
    if len(sub_list) <= 0:
        return 
    #
    category, city = sub_list[0][0], sub_list[0][1]
    dis_fre_dic = {}
    total = 0
    # initialize
    i = 0
    while i<=100:
        k = str(i) + "km"
        dis_fre_dic[k] = (0, 0)
        i += 1
    # add data to the dic
    for it in sub_list:
        dis, fre = it[2], it[3]
        dis_fre_dic[dis] = (fre, fre)
        total += fre
    # 
    i = 2
    while i<=99:
        fre, cumulative = dis_fre_dic[i]
        dis_fre_dic[i] = ( fre, cumulative + dis_fre_dic[i-1][1] )
        i += 1
    fre, cumulative = dis_fre_dic[100] # the last one
    dis_fre_dic[100] = ( fre + dis_fre_dic[101][0], cumulative + dis_fre_dic[101][1] ) # the last one
    #
    print(category, city, "total: ", total, "------------------------------------")
    i = 0
    while i<=100:
        if i==0:
            fre, cumulative = dis_fre_dic[i]
            dis_range = "<1km"
            st = form_line(category, city, dis_range, fre, cumulative, total)
            print(st)
        elif i<100:
            fre, cumulative = dis_fre_dic[i]
            dis_range = "1km~" + str(i+1) + "km"
            st = form_line(category, city, dis_range, fre, cumulative, total)
            print(st)
        else:
            fre, cumulative = dis_fre_dic[i]
            dis_range = "100+km"
            st = form_line(category, city, dis_range, fre, cumulative, total)
            print(st)
        i += 1
    #
    fg = True
    fg = False
    if fg:
        for k, v in dis_fre_dic.items():
            if k<=100:
                print(category, city, k, v)
    return 

#
def sub_report02(sub_list):
    if len(sub_list) <= 0:
        return 
    category, city = sub_list[0][0], sub_list[0][1]
    dis_fre_dic = {"30m": 0, "50m": 0, "100m": 0, "500m": 0}
    k_list = ["30m", "50m", "100m", "500m"]
    i = 1
    while i<=101:
        k = str(i) + "km"
        dis_fre_dic[k] = 0
        k_list.append( k )
        i += 1
    total = 0
    # add data to the dic
    for it in sub_list:
        dis, fre = it[2], it[3]
        if dis<1000:
            k = str(dis) + "m"
            dis_fre_dic[k] = fre
        else:
            k = str(dis/1000) + "km"
            dis_fre_dic[k] = fre
        total += fre
    #
    fg = True
    #fg = False
    if fg:
        acc = 0
        for k in k_list:
            fre = dis_fre_dic[k]
            acc += fre
            if k == "2km" or k == "101km":
                acc = fre
            rto = round( float( acc ) * 100 / total, 2 )
            print(category, city, k, fre, acc, rto)
    return 

#
def form_report(col_list):
    category_list = ["cl", "wf", "pp", "fp"]
    city_list = ["all", "BJ", "SH", "GZ", "SZ", "DG", "XA", "CD", "ZZ", "HE", "UN"]
    #
    for c1 in category_list:
        for c2 in city_list:
            sub_list = search01(col_list, c1, c2)
            sub_report02(sub_list)
    return 

#
def printing(col_list):
    c1, c2 = "cl", "BJ"
    tmp = search01(col_list, c1, c2)
    for it in tmp:
        print(it)
    return 

# ------------------------------------- running from here
f = open("/home/map/gh_internship/testing03.txt", "r")
counter = 0
col_list = []
for ln in f:
    ln = ln.strip()
    if len(ln) <= 0:
        continue
    it = parse01(ln) # parse 
    if len(it) != 4:
        if "/log/1630/dingwei_loc1" in ln:
            date_time = ln[23:23+8]
            print("date_time:" + date_time)
        continue
    #
    col_list.append( it )
    counter += 1

#print(counter)
form_report(col_list)