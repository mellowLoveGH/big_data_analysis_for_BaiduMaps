import sys

# for UV, calculate the number of distinct users
# for accuracy rate, calculate them as to cell, wifi, prop, fp

def add_dic(k, data_dic):
    if k not in data_dic:
        data_dic[k] = 1
    else:
        data_dic[k] = data_dic[k] + 1

    return

#
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
    xl, xr = v[0][0], v[1][0]
    yl, yr = v[0][1], v[1][1]
    if llx >= xl and llx <= xr and lly >= yl and lly <= yr:
      return k
    #print(xl, xr, yl ,yr, k)
  return "UN"


def get_xy(p0):
    ps = p0.split("&")
    llx, lly = ps[2], ps[3]
    grid_len=10
    return float(llx)*grid_len/100000, float(lly)*grid_len/100000

def gps_sample(p0, gps, data_dic):
    #sys.stdout.write("%s\t%s\n"%("S",1))
    llx, lly = get_xy(p0)
    city = find_city(llx, lly)
    #
    accs = gps.split("&")
    if len(accs)==4:
        cl = int(accs[0])
        wf = int(accs[1])
        pp = int(accs[2])
        fp = int(accs[3])
        #
        if cl<0:
            #sys.stdout.write("%s\t%s\n"%("9CN", 1))
            k = "9CN"
            add_dic(k, data_dic)
            k = "9-" + city + "-CN"
            add_dic(k, data_dic)
        else:
            #sys.stdout.write("%s\t%s\n"%("9C"+str(cl), 1))
            k = "9C"+str(cl)
            add_dic(k, data_dic)
            k = "9-" + city + "-C" + str(cl)
            add_dic(k, data_dic)
        #
        if wf<0:
            #sys.stdout.write("%s\t%s\n"%("9WN", 1))
            k = "9WN"
            add_dic(k, data_dic)
            k = "9-" + city + "-WN"
            add_dic(k, data_dic)
        else:   
            #sys.stdout.write("%s\t%s\n"%("9W"+str(wf), 1)) 
            k = "9W"+str(wf)
            add_dic(k, data_dic)
            k = "9-" + city + "-W" + str(wf)
            add_dic(k, data_dic)
        #
        if pp<0:
            #sys.stdout.write("%s\t%s\n"%("9PN", 1))
            k = "9PN"
            add_dic(k, data_dic)
            k = "9-" + city + "-PN"
            add_dic(k, data_dic)
        else:   
            #sys.stdout.write("%s\t%s\n"%("9P"+str(pp), 1))
            k = "9P"+str(pp)
            add_dic(k, data_dic)
            k = "9-" + city + "-P" + str(pp)
            add_dic(k, data_dic)
        #
        if fp<0:
            #sys.stdout.write("%s\t%s\n"%("9FN", 1))
            k = "9FN"
            add_dic(k, data_dic)
            k = "9-" + city + "-FN"
            add_dic(k, data_dic)
        else:   
            #sys.stdout.write("%s\t%s\n"%("9F"+str(fp), 1))
            k = "9F"+str(fp)
            add_dic(k, data_dic)
            k = "9-" + city + "-F" + str(fp)
            add_dic(k, data_dic)
    else:
        #sys.stdout.write("%s\t%s\n"%("9N"+str(len(ps)), 1))
        data_dic["exception2"] = 1
    return 

# ------------------ running from here 
fg = True
data_dic = {"U":0, "S":0}

for data in sys.stdin:
    data = data.strip()
    if data[-2]=="#":
        data = data[:-2]
    try:
        #record = data.split('\t', 1)
        record = data.split('\t')
        p0 = record[0]
        p1 = record[1]
        if p0[0]=="U":
            #sys.stdout.write("%s\t%s\n"%("U",1))
            data_dic["U"] = data_dic["U"] + 1
        elif p0[0]=="S":
            #sys.stdout.write("%s\t%s\n"%("S",1))
            data_dic["S"] = data_dic["S"] + 1
            gps_sample(p0, p1, data_dic)
        else:
            #key = int(record[1])
            sys.stdout.write("%s\t%s\n"%(p0,p1))
    except:
        #sys.stdout.write("%s\t%s\n"%("exception",1))
        data_dic["exception1"] = 1


for k, v in data_dic.items():
    sys.stdout.write("%s\t%s\n"%(k,v))
