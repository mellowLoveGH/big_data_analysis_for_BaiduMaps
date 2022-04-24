#
import sys
def segments(ln):
    L = len(ln)
    if L<=100:
        return False, []
    notice = ln.find('query[')
    info = ln.find('info[')
    result = ln.find('result[')
    if result>info and info>notice and notice>0:
        s1 = ln[0:notice]
        s2 = ln[notice:info]
        s3 = ln[info:result]
        s4 = ln[result:]
        return True, [s1, s2, s3, s4]
    return False, []

def notice_process01(notice_str):
    dic = {}
    cuid = "cuid"
    st = notice_str.find("[cuid:")
    if st<0:
        return {}
    v = ""
    ed = notice_str[st:].find("]") + st
    nl = ed - st
    if nl>6: # and nl<100:
        v = notice_str[st+6 : ed]
        dic[cuid] = v
    return dic

def user_counter(dic1, dic_data):
    k = "cuid"
    if k in dic1:
        #ul = min(len(dic1[k]), 45)
        #sys.stdout.write("%s\t%s\n"%("U"+dic1[k],1))
        dic_data.append("U"+dic1[k])
        #return True
    #return False
    return  

def query_process(query_str):
    con = query_str[6:-1]
    lns = con.split("&")
    dic = {}
    for ln in lns:
        ps = ln.split("=")
        if len(ps)==2:
            dic[ps[0]] = ps[1]
    #print(dic)
    return dic

def find_kv(tmp, k):
    st = tmp.find(k)
    if st<0:
        return False, ""
    L = len(k)
    ed = tmp.find("&", st+L)
    if ed<st:
        return False, ""
    return True, tmp[st+L:ed]

def query_process01(query_str):
    ks = ["&resid=", "&prod=", "&cl=", "&wf=", "&ll_t=", "&ll_r=", "&ll_h=", "&ll_n=", "&s=", "&ll="]
    dic = {}
    for k in ks:
        f, v = find_kv(query_str, k)
        if f:
            dic[k[1:-1]] = v
    return dic


def find_city(llx=0, lly=0):
  city_bound_dict = {}
  city_bound_dict['BJ'] = [(116.017248,39.650159), (116.766979,40.214805)]
  city_bound_dict['SH'] = [(121.077335, 30.940409), (121.870949, 31.441277)]
  city_bound_dict['GZ'] = [(113.133017,23.071346), (113.431903,23.502762)]
  city_bound_dict['SZ'] = [(113.563368,22.819244), (114.061192,23.132428)]
  city_bound_dict['DG'] = [(113.735851,22.487328), (114.583942,22.819245)]
  city_bound_dict['XA'] = [(108.770938, 34.178261), (109.100598, 34.420894)]
  city_bound_dict['CD'] = [(103.711202, 30.316450), (104.465004, 30.950671)]
  city_bound_dict['ZZ'] = [(113.436737, 34.649930), (113.883605, 34.856875)]
  city_bound_dict['HE'] = [(126.418295, 45.614860), (126.844325, 45.896207)]

  for k, v in city_bound_dict.items():
    #print(k, end=",")
    xl, xr = v[0][0], v[1][0]
    yl, yr = v[0][1], v[1][1]
    if llx >= xl and llx <= xr and lly >= yl and lly <= yr:
      return k
    #print(xl, xr, yl ,yr, k)
  return "UN"


def nlp_map_op(dic2, dic3, gps, dic_data, gps_ff01):
    #
    city_mode = "OT"
    if "ll" in dic2:
        dic_data.append("6G")
        gps = 1
        if "llx" in dic3 and "lly" in dic3:
            llx, lly = float(dic3["llx"]), float(dic3["lly"])
            if find_city(llx, lly) != "UN":
                city_mode = "MN"
        dic_data.append("6"+city_mode)
    else:
        dic_data.append("6N")
        gps = 0
    #
    v1 = ""
    k1 = "resid"
    f1 = False
    if k1 in dic2:
        v1 = dic2[k1]
        f1 = True
    #
    k2 = "prod"
    v2 = ""
    if k2 in dic2:
        v2 = dic2[k2]
    p1 = "com.baidu.map.location"
    p2 = "com.xiaomi.metoknlp"
    f2 = p1 in v2 or p2 in v2
    if v1=="11" or f2:
        #sys.stdout.write("%s\t%s\n"%("2R11",1))
        dic_data.append("2R11")
        if gps==1:
            #sys.stdout.write("%s\t%s\n"%("7GR11",1))
            dic_data.append("7GR11")
            dic_data.append("7"+city_mode+"11")
            if gps_ff01:
                dic_data.append("8GR11")
                dic_data.append("8"+city_mode+"11")
    elif v1=="13":
        #sys.stdout.write("%s\t%s\n"%("2R13",1))
        dic_data.append("2R13")
        if gps==1:
            #sys.stdout.write("%s\t%s\n"%("7GR13",1))
            dic_data.append("7GR13")
            dic_data.append("7"+city_mode+"13")
            if gps_ff01:
                dic_data.append("8GR13")
                dic_data.append("8"+city_mode+"13")
    elif f1:
        #sys.stdout.write("%s\t%s\n"%("2R*",1))
        dic_data.append("2R*")
        if gps==1:
            #sys.stdout.write("%s\t%s\n"%("7GR*",1))
            dic_data.append("7GR*")
            dic_data.append("7"+city_mode+"*")
            if gps_ff01:
                dic_data.append("8GR*")
                dic_data.append("8"+city_mode+"*")
    else:
        #sys.stdout.write("%s\t%s\n"%("2N",1))
        dic_data.append("2N")
        if gps==1:
            #sys.stdout.write("%s\t%s\n"%("7N",1))
            dic_data.append("7N")
            dic_data.append("7"+city_mode+"N")
            if gps_ff01:
                dic_data.append("8N")
                dic_data.append("8"+city_mode+"N")
    #
    return gps

def find_cl(dic2):
    k = "cl"
    if k in dic2:
        v = dic2[k] 
        if "-" in v:
            sys.stdout.write("%s\t%s\n"%("4CL-",1))
        else:   
            sys.stdout.write("%s\t%s\n"%("4CL+",1))
    else:   
        sys.stdout.write("%s\t%s\n"%("4N",1))


def info_process(info_str):
    con = info_str[5:-1]
    lns = con.split("&")
    dic = {}
    for ln in lns:
        ps = ln.split("=")
        if len(ps)==2:
            dic[ps[0]] = ps[1]
    #print(dic)
    return dic


def info_process01(info_str):
    ks = ["&inout_flag=", "&llflag=", "&cellflag=", "&wififlag=", "&prop_flag=", "&fp_flag=", "&cls_flag="]
    gps_ks = ["&llx=", "&lly=", "&cellx=", "&celly=", "&wifix=", "&wifiy=", "&propx=", "&propy=", "&fpx=", "&fpy=", "&create_time=", "&create_time_64="]
    dic = {}
    for k in ks:
        f, v = find_kv(info_str, k)
        if f:
            dic[k[1:-1]] = v
  #
    if "llflag" in dic and dic["llflag"]=="1":
        for k in gps_ks:
            f, v = find_kv(info_str, k)
            if f:
                dic[k[1:-1]] = v
    return dic


def find_cl_cellflag(dic2, dic3, dic_data):
    # cl 
    cl = 0
    k = "cl"
    if k in dic2:
        v = dic2[k]
        if "-" in v: #-1
            #sys.stdout.write("%s\t%s\n"%("4CL-",1))
            dic_data.append("4CL-")
        else: # 1
            cl = 1
            #sys.stdout.write("%s\t%s\n"%("4CL+",1))
            dic_data.append("4CL+")
    else: # 0
        #sys.stdout.write("%s\t%s\n"%("4N",1))
        dic_data.append("4N")
    
    # cellflag
    cf = 0
    k = "cellflag"
    if k in dic3:
        v = int(dic3[k])
        if v>0: # 1
            cf = 1
            #sys.stdout.write("%s\t%s\n"%("A+",1))
            dic_data.append("A+")
        else: # 0
            #sys.stdout.write("%s\t%s\n"%("A-",1))
            dic_data.append("A-")
    else: #-1
        #sys.stdout.write("%s\t%s\n"%("AN",1))
        dic_data.append("AN")
    #
    if cf>0 or cl==1:
        #sys.stdout.write("%s\t%s\n"%("B",1))
        dic_data.append("B")
    return 

def find_wf(dic2, dic_data):
    k = "wf"
    #if k in dic2 and ";" in dic2[k]:
    if k in dic2: # 1
        #sys.stdout.write("%s\t%s\n"%("5WF",1))
        dic_data.append("5WF")
        return 1
    else:
        #sys.stdout.write("%s\t%s\n"%("5N",1))
        dic_data.append("5N")
        return 0

def find_wififlag(dic3, dic_data):
    k = "wififlag"
    if k in dic3:
        v = int(dic3[k])
        if v==2: # 1
            #sys.stdout.write("%s\t%s\n"%("C+",1))
            dic_data.append("C+")
        else: # 0
            #sys.stdout.write("%s\t%s\n"%("C-",1))
            dic_data.append("C-")
    else:
        #sys.stdout.write("%s\t%s\n"%("CN",1))
        dic_data.append("CN")
    return

def find_propflag(dic3, dic_data):
    k = "prop_flag"
    if k in dic3:
        v = int(dic3[k])
        if v>0: # 1
            #sys.stdout.write("%s\t%s\n"%("D+",1))
            dic_data.append("D+")
        else: # 0
            #sys.stdout.write("%s\t%s\n"%("D-",1))
            dic_data.append("D-")
    else: # -1
        #sys.stdout.write("%s\t%s\n"%("DN",1))
        dic_data.append("DN")
    return

def find_fpflag(dic3, dic_data):
    k = "fp_flag"
    if k in dic3:
        v = int(dic3[k])
        if v>0: # 1
            #sys.stdout.write("%s\t%s\n"%("E+",1))
            dic_data.append("E+")
        else: # 0
            #sys.stdout.write("%s\t%s\n"%("E-",1))
            dic_data.append("E-")
    else:
        #sys.stdout.write("%s\t%s\n"%("EN",1))
        dic_data.append("EN")
    return 

def find_clsflag(dic3, dic_data):
    k = "cls_flag"
    if k in dic3:
        v = int(dic3[k])
        if v==2: # 1
            #sys.stdout.write("%s\t%s\n"%("F+",1))
            dic_data.append("F+")
        else:
            #sys.stdout.write("%s\t%s\n"%("F-",1))
            dic_data.append("F-")
    else: # -1
        #sys.stdout.write("%s\t%s\n"%("FN",1))
        dic_data.append("FN")
    return

def find_wifi_prop_fp_cls(dic3, dic_data):
    find_wififlag(dic3, dic_data)
    find_propflag(dic3, dic_data)
    find_fpflag(dic3, dic_data)
    find_clsflag(dic3, dic_data)
    return


def find_inoutflag(dic3, dic_data):
    k = "inout_flag"
    if k in dic3:
        #sys.stdout.write("%s\t%s\n"%("3IO"+dic3[k], 1))
        dic_data.append("3IO"+dic3[k])
    else:
        #sys.stdout.write("%s\t%s\n"%("3N", 1))
        dic_data.append("3N")
    return 

def find_gps(dic3, dic_data):
    k = "llflag"
    if k in dic3:
        if dic3[k]=="1":
            #sys.stdout.write("%s\t%s\n"%("6G1",1))
            dic_data.append("6G1")
            return 1
        else:
            #sys.stdout.write("%s\t%s\n"%("6G0",1))
            dic_data.append("6G0")
            return 0
    else:
        #sys.stdout.write("%s\t%s\n"%("6N", 1))
        dic_data.append("6N")
    return -1



import time
def get_time_interval(dic3):
    k = "create_time"
    if k not in dic3:
        return 0, 0
    #
    ct = dic3[k]
    date_str = ct.split(' ')[0]
    st = '%s 00:00:00' % (date_str)
    ed = '%s 23:59:59' % (date_str)
    s = int(time.mktime(time.strptime(st, '%Y-%m-%d %H:%M:%S')))
    e = int(time.mktime(time.strptime(ed, '%Y-%m-%d %H:%M:%S')))
    return s, e

def filter_gps01(dic2, dic3):
    ks1 = ["ll_t", "s", "ll_r", "ll_h", "ll_n"] 
    for k in ks1: 
        if k not in dic2:
            return False
    #
    ks2 = ["create_time", "create_time_64"]
    if ks2[0] not in dic3:
        return False
    #
    lln = int(dic2[ks1[-1]])
    if lln<4:
        return False
    #
    s = float(dic2[ks1[1]])
    if s<0 or s>=10:
        return False
    #
    llr = float(dic2[ks1[2]])
    if llr>20: 
        return False
    #
    return True


def filter_gps(dic2, dic3):
    ks1 = ["ll_t", "s", "ll_r", "ll_h", "ll_n"]
    ks2 = ["create_time", "create_time_64"]
    """
    ks1 = ["ll_t", "s", "ll_r", "ll_h", "ll_n"]
    for k in ks1:
        if k not in dic2:
            return False
    #
    ks2 = ["create_time", "create_time_64"]
    if ks2[0] not in dic3:
        return False
    #
    lln = int(dic2[ks1[-1]])
    if lln<4:
        return False
    #
    s = float(dic2[ks1[1]])
    if s<0 or s>=10:
        return False
    #
    llr = float(dic2[ks1[2]])
    if llr>20:
        return False
    """    
    # time check
    llt = int(dic2[ks1[0]])
    create_time_64 = int(dic3[ks2[1]])
    diff_time = create_time_64 - llt
    st, et = get_time_interval(dic3)
    if llt==0 or diff_time<=0 or llt<st or llt>et:
        return False
    #
    return True

# 10m * 10m grid
def grid_sample(lng, lat, grid_len=10):
  x = int(lng * 100000/grid_len)
  y = int(lat * 100000/grid_len)
  return x, y

from math import radians, cos, sin, asin, sqrt
# https://www.cnblogs.com/andylhc/p/9481636.html
def geodistance(lng1,lat1,lng2,lat2):
    #lng1,lat1,lng2,lat2 = (120.12802999999997,30.28708,115.86572000000001,28.7427)
    lng1, lat1, lng2, lat2 = map(radians, [float(lng1), float(lat1), float(lng2), float(lat2)])
    dlon=lng2-lng1
    dlat=lat2-lat1
    a=sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    distance=2*asin(sqrt(a))*6371*1000# earth radius: 6371
    distance=round(distance,3)
    return distance

def find_pos(dic3, pos_name):
    if pos_name in dic3:
        return float(dic3[pos_name])
    return ""

def find_positions(dic3):
    llx = find_pos(dic3, "llx")
    lly = find_pos(dic3, "lly")
    cellx = find_pos(dic3, "cellx")
    celly = find_pos(dic3, "celly")
    wifix = find_pos(dic3, "wifix")
    wifiy = find_pos(dic3, "wifiy")
    propx = find_pos(dic3, "propx")
    propy = find_pos(dic3, "propy")
    fpx = find_pos(dic3, "fpx")
    fpy = find_pos(dic3, "fpy")
    return [llx, lly, cellx, celly, wifix, wifiy, propx, propy, fpx, fpy]

"""
def gradient_dis(d):
    if d<=30:
        return 30
    elif d<=50:
        return 50
    elif d<=100:
        return 100
    elif d<=500:
        return 500
    elif d<=1000:
        return 1000
    return 1001
"""
def gradient_dis(d):
    d = int( round(d) )
    # accuracy
    if d<=30:
        return 30
    elif d<=50:
        return 50
    elif d<=100:
        return 100
    elif d<=500:
        return 500
    # bad-case
    elif d<=1000:
        return 1000
    return min( d/1000+1, 101 ) * 1000


def cal_dis(dic1, dic3, dic_data):
    ps = find_positions(dic3)
    #print(ps)
    llx, lly = ps[0], ps[1]
    if llx == "" or lly == "":
        return [-1, -1, -1, -1]
    # sampling
    sx, sy = grid_sample(llx, lly)
    #sys.stdout.write("%s\t%s\n"%("S"+str(sx)+"-"+str(sy),1))
    #
    #dis = []
    #
    cellx, celly = ps[2], ps[3]
    cld = -1
    if cellx != "" and celly != "":
        cld = geodistance(llx, lly, cellx, celly)
        cld = gradient_dis(cld)
        #dis.append( cld )
        #sys.stdout.write("%s\t%s\n"%("8C"+str(cld), 1))
    #else:
        #dis.append(-1)
        #sys.stdout.write("%s\t%s\n"%("8CN", 1))
    #
    wifix, wifiy = ps[4], ps[5]
    wfd = -1
    if wifix != "" and wifiy != "":
        wfd = geodistance(llx, lly, wifix, wifiy)
        wfd = gradient_dis(wfd)
        #dis.append( wfd )
        #sys.stdout.write("%s\t%s\n"%("8W"+str(wfd), 1))
    #else:
        #dis.append(-1)
        #sys.stdout.write("%s\t%s\n"%("8WN", 1))
    #
    propx, propy = ps[6], ps[7]
    ppd = -1
    if propx != "" and propy != "":
        ppd = geodistance(llx, lly, propx, propy)
        ppd = gradient_dis(ppd)
        #dis.append( ppd )
        #sys.stdout.write("%s\t%s\n"%("8P"+str(ppd), 1))
    #else:
        #dis.append(-1)
        #sys.stdout.write("%s\t%s\n"%("8PN", 1))
    #
    fpx, fpy = ps[8], ps[9]
    fpd = -1
    if fpx != "" and fpy != "":
        fpd = geodistance(llx, lly, fpx, fpy)
        fpd = gradient_dis(fpd)
        #dis.append( fpd )
        #sys.stdout.write("%s\t%s\n"%("8F"+str(fpd), 1))
    #else:
        #dis.append(-1) 
        #sys.stdout.write("%s\t%s\n"%("8FN", 1))
    
    tm = dic3["create_time"]
    hour = tm[-8:-6]
    dv = str(cld) + "&" + str(wfd) + "&" + str(ppd) + "&" + str(fpd)
    ds = "S&"
    ds = ds + hour + "&"
    #cuid = "none"
    #if "cuid" in dic1:
        #cuid = dic1["cuid"]
    #ds = ds + cuid + "&"
    ds = ds + str(sx)+"&"+str(sy)
    #sys.stdout.write("%s\t%s\n"%(ds, dv)) # sampling by hour
    dic_data.append(ds+":"+dv)
    return 

def write_data(dic_data, global_dic, user_set, gps_dic):
    s = ""
    for v in dic_data:
        ch = v[0]
        if ch=="U":
            user_set[v] = 1
            continue
        if ch=="S":
            ps = v.split(":")
            gps_dic[ps[0]] = ps[1]
            continue
        if v not in global_dic:
            global_dic[v] = 1
        else:
            global_dic[v] = global_dic[v] + 1
    #
    #sys.stdout.write("%s\n"%(s[:-1]))
    return 

def print_user_gps(ug_dic):
    st = ""
    for k, v in ug_dic.items():
        st = st + k + "\t" + str(v) + "\n"
    sys.stdout.write(st)
    return {}


#
global_dic = {}
user_set = {}
gps_dic = {}
mc = 0
error_counter = 0
# ------------------ running from here
for data in sys.stdin:
    data = data.strip()
    dic_data = []
    try:
        # PV 
        dic_data.append("1PV")
        f, ss = segments(data)
        if f:
            dic1 = notice_process01(ss[0]) # notice
            dic2 = query_process(ss[1]) # query
            dic3 = info_process01(ss[2]) # info
            # ---------------- GPS
            gps_ff01 = filter_gps01(dic2, dic3) # check the quality of GPS
            gps = 0             # check whether there is GPS
            if "ll" in dic2:
                gps = 1
            #
            if gps==1 and gps_ff01 and filter_gps(dic2, dic3):
                #sys.stdout.write("%s\t%s\n"%("S",1))
                cal_dis(dic1, dic3, dic_data)
                mc = mc + 1
        #       
        write_data(dic_data, global_dic, user_set, gps_dic)
        #if mc % 100 == 0:
            #gps_dic = print_user_gps(gps_dic)
    except:
        #print(data)
        #print(count_row)
        #sys.stdout.write("%s\t%s\n"%("error",1))
        #dic_data.append("error")
        error_counter = error_counter + 1

try:
    # write global_dic:
    #print_user_gps(global_dic)
    # gps_dic:
    print_user_gps(gps_dic)
except:
    #sys.stdout.write("")
    error_counter = error_counter + 1
#sys.stdout.write("mc: %s\n"%(mc))