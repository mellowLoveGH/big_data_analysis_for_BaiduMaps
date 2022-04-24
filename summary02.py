def ratio(num):
    return "\t"+str(round(num*100, 2)) + "%"


def printing01(s1, s2, s3):
    s2 = str(s2)
    s3 = str(s3)
    #
    i1 = 36 - len(s1)
    i  = 0
    while i<i1:
        s1 = s1 + " "
        i = i + 1
    #
    i2 = 16 - len(s2)
    i = 0
    while i<i2:
        s2 = s2 + " "
        i = i + 1
    #
    i3 = 16 - len(s3)
    i = 0
    while i<i3:
        s3 = s3 + " "
        i = i + 1    
    print(s1, s2, s3)
    return 

dic = {}
uv = 0
cnt = 0
f = open("/home/map/gh_internship/st03.txt", "r")
for ln in f:
    ln = ln.strip()
    ps = []
    if '\t' in ln:
        ps = ln.split('\t')
    else:
        ps = ln.split(' ')
    #ps = ln.split(' ')
    tmp = []
    for p in ps:
        if len(p)>0:
            tmp.append(p)
    ps = tmp
    #print(ln.split(' '))
    if len(ps)==2:
        h = ps[0].strip()
        n = int(ps[1])
        if "+1000" in h:
            h = h.replace("+1000", "1001")
        if h[0]=="S":
            print(h, n)
        dic[h] = n
        cnt = cnt + 1
    #elif len(ps)==1:
        #uv = int(ln[1:])
#print(dic)
try:
    uv = dic['U']
    print("uv", uv)
    dic['uv'] = uv - cnt - 1
    #pv = dic['1PV']
except:
    print("UV: cannot get the data")
    dic['uv'] = 0

print('--------------------------------------')

#
try:
    print('UV/PV: ')
    print('UV - unique visitor: \t', dic['uv'])
    pv = dic['1PV']
    print('PV - page view: \t', pv)
    print()
except:
    print("PV/UV: cannot get the data")
    pv = 1000 * 1000 * 1000 * 600
    if '2R11' in dic and '2R13' in dic and '2R*' in dic and '2N' in dic:
        pv = dic['2R11'] + dic['2R13'] + dic['2R*'] + dic['2N']
    print('PV: ', pv)
    print()

printing01("basic indicators", "quantity", "  ratio")

try:
    pv_nlp = dic['2R11']
    pv_map = dic['2R13']
    pv_op = dic['2R*']
    pv_n = dic['2N']
    printing01('nlp ', pv_nlp, ratio(pv_nlp/pv))
    printing01('map ', pv_map, ratio(pv_map/pv))
    printing01('op  ', pv_op, ratio(pv_op/pv))
    printing01('none', pv_n, ratio(pv_n/pv))
    print()
except:
    print("resid/prop: cannot get the data")

try:
    pv_io_1 = dic['3IO-1']
    pv_io0 = dic['3IO0']
    pv_io1 = dic['3IO1']
    pv_io2 = dic['3IO2']
    pv_io3 = dic['3IO3']
    pv_n = dic['3N']
    printing01('inout=-1', pv_io_1, ratio(pv_io_1/pv))
    printing01('inout=0 ', pv_io0, ratio(pv_io0/pv))
    printing01('inout=1 ', pv_io1, ratio(pv_io1/pv))
    printing01('inout=2 ', pv_io2, ratio(pv_io2/pv))
    printing01('inout=3 ', pv_io3, ratio(pv_io3/pv))
    printing01('none    ', pv_n, ratio(pv_n/pv))
    print()
except:
    print("IO: cannot get the data")

try:
    pv_cl1 = dic['4CL+']
    pv_cl0 = dic['4CL-']
    pv_n = dic['4N']
    printing01('valid cl   ', pv_cl1, ratio(pv_cl1/pv))
    printing01('invalid cl ', pv_cl0, ratio(pv_cl0/pv))
    printing01('none       ', pv_n, ratio(pv_n/pv))
    print()
except:
    print("CL: cannot get the data")

try:
    pv_wf = dic['5WF']
    pv_n = dic['5N']
    printing01('wf  ', pv_wf, ratio(pv_wf/pv))
    printing01('none', pv_n, ratio(pv_n/pv))
    print()
except:
    print("wifi: cannot get the data")

try:
    pv_g0 = dic['6G0']
    pv_g1 = dic['6G1']
    pv_n = dic['6N']
    printing01('GPS=0', pv_g0, ratio(pv_g0/pv))
    printing01('GPS=1', pv_g1, ratio(pv_g1/pv))
    printing01('none ', pv_n, ratio(pv_n/pv))
    print()
except:
    pv_g = dic['6G']
    pv_n = dic['6N']
    printing01('GPS ', pv_g, ratio(pv_g/pv))
    printing01('none', pv_n, ratio(pv_n/pv))
    #print("G: cannot get the data")   
    print()
    mncity = dic['6MN']
    printing01('main cities GPS ', mncity, ratio(mncity/pv_g))
    otcity = dic['6OT']
    printing01('other cities GPS ', otcity, ratio(otcity/pv_g))
     
    pv_g1 = pv_g
    print()

try:
    g_nlp = dic['7GR11']
    g_map = dic['7GR13']
    g_op = dic['7GR*']
    g_n = dic['7N']
    gps = g_nlp + g_map + g_op
    gps_sum = gps + g_n
    printing01('GPS-nlp ', g_nlp, ratio(g_nlp/pv_g1))
    printing01('GPS-map ', g_map, ratio(g_map/pv_g1))
    printing01('GPS-op  ', g_op, ratio(g_op/pv_g1))
    printing01('GPS-none', g_n, ratio(g_n/pv_g1))
    print()
    #
    g_nlp_mn = dic['7MN11']
    g_map_mn = dic['7MN13']
    g_op_mn = dic['7MN*']
    g_n_mn = dic['7MNN']
    gps_mn = g_nlp_mn + g_map_mn + g_op_mn
    gps_sum_mn = gps_mn + g_n_mn
    printing01('main cities GPS-nlp ', g_nlp_mn, ratio(g_nlp_mn/gps_sum_mn))
    printing01('main cities GPS-map ', g_map_mn, ratio(g_map_mn/gps_sum_mn))
    printing01('main cities GPS-op  ', g_op_mn, ratio(g_op_mn/gps_sum_mn))
    printing01('main cities GPS-none', g_n_mn, ratio(g_n_mn/gps_sum_mn))
    print() 
    #
    g_nlp_ot = dic['7OT11']
    g_map_ot = dic['7OT13']
    g_op_ot = dic['7OT*']
    g_n_ot = dic['7OTN']
    gps_ot = g_nlp_ot + g_map_ot + g_op_ot
    gps_sum_ot = gps_ot + g_n_ot
    printing01('other cities GPS-nlp ', g_nlp_ot, ratio(g_nlp_ot/gps_sum_ot))
    printing01('other cities GPS-map ', g_map_ot, ratio(g_map_ot/gps_sum_ot))
    printing01('other cities GPS-op  ', g_op_ot, ratio(g_op_ot/gps_sum_ot))
    printing01('other cities GPS-none', g_n_ot, ratio(g_n_ot/gps_sum_ot))
    print()  
except:
    print("G-resid: cannot get the data")

try:
    vg_nlp = dic['8GR11']
    vg_map = dic['8GR13']
    vg_op = dic['8GR*']
    vg_n = dic['8N']
    vgps = vg_nlp + vg_map + vg_op
    vgps_sum = vgps + vg_n
    printing01('valid GPS-nlp ', vg_nlp, ratio(vg_nlp/vgps_sum))
    printing01('valid GPS-map ', vg_map, ratio(vg_map/vgps_sum))
    printing01('valid GPS-op  ', vg_op, ratio(vg_op/vgps_sum))
    printing01('valid GPS-none', vg_n, ratio(vg_n/vgps_sum))
    print()
    #
    vg_nlp_mn = dic['8MN11']
    vg_map_mn = dic['8MN13']
    vg_op_mn = dic['8MN*']
    vg_n_mn = dic['8MNN']
    vgps_mn = vg_nlp_mn + vg_map_mn + vg_op_mn 
    vgps_sum_mn = vgps_mn + vg_n_mn
    printing01('valid main cities GPS-nlp ', vg_nlp_mn, ratio(vg_nlp_mn/vgps_sum_mn))
    printing01('valid main cities GPS-map ', vg_map_mn, ratio(vg_map_mn/vgps_sum_mn))
    printing01('valid main cities GPS-op  ', vg_op_mn, ratio(vg_op_mn/vgps_sum_mn))
    printing01('valid main cities GPS-none', vg_n_mn, ratio(vg_n_mn/vgps_sum_mn))
    print() 
    #
    vg_nlp_ot = dic['8OT11']
    vg_map_ot = dic['8OT13']
    vg_op_ot = dic['8OT*']
    vg_n_ot = dic['8OTN']
    vgps_ot = vg_nlp_ot + vg_map_ot + vg_op_ot 
    vgps_sum_ot = vgps_ot + vg_n_ot
    printing01('valid other cities GPS-nlp ', vg_nlp_ot, ratio(vg_nlp_ot/vgps_sum_ot))
    printing01('valid other cities GPS-map ', vg_map_ot, ratio(vg_map_ot/vgps_sum_ot))
    printing01('valid other cities GPS-op  ', vg_op_ot, ratio(vg_op_ot/vgps_sum_ot))
    printing01('valid other cities GPS-none', vg_n_ot, ratio(vg_n_ot/vgps_sum_ot))
    print()   
except:
    print("valid G-resid: cannot get the data")


#
try:
    printing01('success rate - localization by ', "quantity", "  ratio")
    cellflag1 = dic['A+']
    cellflag0 = dic['A-']
    cn = dic['AN']
    cb = dic['B']
    printing01('cell loc', cellflag1, ratio(cellflag1/cb))
    wf = pv_wf
    wfflag = dic['C+']
    printing01('wifi loc', wfflag, ratio(wfflag/wf))
    ppflag = dic['D+']
    printing01('prop loc', ppflag, ratio(ppflag/wf))
    fpflag = dic['E+']
    printing01('fp loc  ', fpflag, ratio(fpflag/wf))
    clsflag = dic['F+']
    printing01('cls loc ', clsflag, ratio(clsflag/wf))
    #
    printing01('in=2/1 loc ', dic['T2'], ratio( float(dic['T2'])/dic['T1'] ))
    print()
except:
    print("success: cannot get the data")

#
printing01('accuracy rate - localization error ', "quantity", "  ratio")
prefix = "9"

import sys
try:
    prefix = sys.argv[1]
    print("------------------ mode: ", prefix)
except:
    prefix = "9"

cities = ['BJ','SH','GZ','SZ','DG','XA','CD','ZZ','HE','UN']

cell30 = dic[prefix+'C30']
cell50 = dic[prefix+'C50'] + cell30
cell100 = dic[prefix+'C100'] + cell50
cell500 = dic[prefix+'C500'] + cell100
cell1000 = dic[prefix+'C1000'] + cell500
cell1000_ = dic[prefix+'C1001']
s = cell1000_ + cell1000
printing01('cell loc error <30  ', cell30, ratio(cell30/s))
printing01('cell loc error <50  ', cell50, ratio(cell50/s))
printing01('cell loc error <100 ', cell100, ratio(cell100/s))
printing01('cell loc error <500 ', cell500, ratio(cell500/s))
printing01('cell loc error <1000', cell1000, ratio(cell1000/s))
printing01('cell loc error >1000', cell1000_, ratio(cell1000_/s))
print()

for city in cities: 
    prefix01 = prefix + "-" + city + "-C"
    cell30 = 0
    if prefix01+'30' in dic: 
        cell30 = dic[prefix01+'30']
    cell50 = cell30
    if prefix01+'50' in dic: 
        cell50 = dic[prefix01+'50'] + cell30
    cell100 = cell50
    if prefix01+'100' in dic: 
        cell100 = dic[prefix01+'100'] + cell50
    cell500 = cell100
    if prefix01+'500' in dic: 
        cell500 = dic[prefix01+'500'] + cell100 
    cell1000 = cell500
    if prefix01+'1000' in dic: 
        cell1000 = dic[prefix01+'1000'] + cell500 
    cell1000_ = 0
    if prefix01+'1001' in dic: 
        cell1000_ = dic[prefix01+'1001']    
    s = cell1000_ + cell1000
    if s==0:
        continue
    if city=="UN":
        city = "other"
    if city=="HE":
        city = "HEB" 
    printing01(city + ' cell loc error <30  ', cell30, ratio(cell30/s))
    printing01(city + ' cell loc error <50  ', cell50, ratio(cell50/s))
    printing01(city + ' cell loc error <100 ', cell100, ratio(cell100/s))
    printing01(city + ' cell loc error <500 ', cell500, ratio(cell500/s))
    printing01(city + ' cell loc error <1000', cell1000, ratio(cell1000/s))
    printing01(city + ' cell loc error >1000', cell1000_, ratio(cell1000_/s))
    print() 
print("----------------------------------")

wf30 = dic[prefix+'F30']
wf50 = dic[prefix+'F50'] + wf30
wf100 = dic[prefix+'F100'] + wf50
wf500 = dic[prefix+'F500'] + wf100 
wf1000 = dic[prefix+'F1000'] + wf500 
wf1000_ = dic[prefix+'F1001']
s = wf1000_ + wf1000
printing01('wifi loc error <30  ', wf30, ratio(wf30/s))
printing01('wifi loc error <50  ', wf50, ratio(wf50/s))
printing01('wifi loc error <100 ', wf100, ratio(wf100/s))
printing01('wifi loc error <500 ', wf500, ratio(wf500/s))
printing01('wifi loc error <1000', wf1000, ratio(wf1000/s))
printing01('wifi loc error >1000', wf1000_, ratio(wf1000_/s))
print()

for city in cities: 
    prefix01 = prefix + "-" + city + "-F"
    wf30 = 0
    if prefix01+'30' in dic: 
        wf30 = dic[prefix01+'30']
    wf50 = wf30
    if prefix01+'50' in dic: 
        wf50 = dic[prefix01+'50'] + wf30
    wf100 = wf50
    if prefix01+'100' in dic: 
        wf100 = dic[prefix01+'100'] + wf50
    wf500 = wf100
    if prefix01+'500' in dic: 
        wf500 = dic[prefix01+'500'] + wf100 
    wf1000 = wf500
    if prefix01+'1000' in dic: 
        wf1000 = dic[prefix01+'1000'] + wf500 
    wf1000_ = 0
    if prefix01+'1001' in dic: 
        wf1000_ = dic[prefix01+'1001']    
    s = wf1000_ + wf1000
    if s==0:
        continue
    if city=="UN":
        city = "other"
    if city=="HE":
        city = "HEB"  
    printing01(city + ' wifi loc error <30  ', wf30, ratio(wf30/s))
    printing01(city + ' wifi loc error <50  ', wf50, ratio(wf50/s))
    printing01(city + ' wifi loc error <100 ', wf100, ratio(wf100/s))
    printing01(city + ' wifi loc error <500 ', wf500, ratio(wf500/s))
    printing01(city + ' wifi loc error <1000', wf1000, ratio(wf1000/s))
    printing01(city + ' wifi loc error >1000', wf1000_, ratio(wf1000_/s))
    print() 
print("----------------------------------")

pp30 = dic[prefix+'P30']
pp50 = dic[prefix+'P50'] + pp30
pp100 = dic[prefix+'P100'] + pp50
pp500 = dic[prefix+'P500'] + pp100    
pp1000 = dic[prefix+'P1000'] + pp500    
pp1000_ = dic[prefix+'P1001']
s = pp1000_ + pp1000
printing01('prop loc error <30  ', pp30, ratio(pp30/s))
printing01('prop loc error <50  ', pp50, ratio(pp50/s))
printing01('prop loc error <100 ', pp100, ratio(pp100/s))
printing01('prop loc error <500 ', pp500, ratio(pp500/s))
printing01('prop loc error <1000', pp1000, ratio(pp1000/s))
printing01('prop loc error >1000', pp1000_, ratio(pp1000_/s))
print()

for city in cities: 
    prefix01 = prefix + "-" + city + "-P"
    pp30 = 0
    if prefix01+'30' in dic: 
        pp30 = dic[prefix01+'30']
    pp50 = pp30
    if prefix01+'50' in dic: 
        pp50 = dic[prefix01+'50'] + pp30
    pp100 = pp50
    if prefix01+'100' in dic: 
        pp100 = dic[prefix01+'100'] + pp50
    pp500 = pp100
    if prefix01+'500' in dic: 
        pp500 = dic[prefix01+'500'] + pp100 
    pp1000 = pp500
    if prefix01+'1000' in dic: 
        pp1000 = dic[prefix01+'1000'] + pp500 
    pp1000_ = 0
    if prefix01+'1001' in dic: 
        pp1000_ = dic[prefix01+'1001']    
    s = pp1000_ + pp1000
    if s==0:
        continue
    if city=="UN":
        city = "other"
    if city=="HE":
        city = "HEB"  
    printing01(city + ' prop loc error <30  ', pp30, ratio(pp30/s))
    printing01(city + ' prop loc error <50  ', pp50, ratio(pp50/s))
    printing01(city + ' prop loc error <100 ', pp100, ratio(pp100/s))
    printing01(city + ' prop loc error <500 ', pp500, ratio(pp500/s))
    printing01(city + ' prop loc error <1000', pp1000, ratio(pp1000/s))
    printing01(city + ' prop loc error >1000', pp1000_, ratio(pp1000_/s))
    print() 
print("----------------------------------")


fp30 = dic[prefix+'W30']
fp50 = dic[prefix+'W50'] + fp30
fp100 = dic[prefix+'W100'] + fp50
fp500 = dic[prefix+'W500'] + fp100    
fp1000 = dic[prefix+'W1000'] + fp500    
fp1000_ = dic[prefix+'W1001']
s = fp1000_ + fp1000
printing01('fp loc error <30  ', fp30, ratio(fp30/s))
printing01('fp loc error <50  ', fp50, ratio(fp50/s))
printing01('fp loc error <100 ', fp100, ratio(fp100/s))
printing01('fp loc error <500 ', fp500, ratio(fp500/s))
printing01('fp loc error <1000', fp1000, ratio(fp1000/s))
printing01('fp loc error >1000', fp1000_, ratio(fp1000_/s))
print()

for city in cities:
    prefix01 = prefix + "-" + city + "-W"
    fp30 = 0
    if prefix01+'30' in dic:
        fp30 = dic[prefix01+'30']
    fp50 = fp30
    if prefix01+'50' in dic:
        fp50 = dic[prefix01+'50'] + fp30
    fp100 = fp50
    if prefix01+'100' in dic:
        fp100 = dic[prefix01+'100'] + fp50
    fp500 = fp100
    if prefix01+'500' in dic:
        fp500 = dic[prefix01+'500'] + fp100 
    fp1000 = fp500
    if prefix01+'1000' in dic:
        fp1000 = dic[prefix01+'1000'] + fp500 
    fp1000_ = 0
    if prefix01+'1001' in dic:
        fp1000_ = dic[prefix01+'1001']    
    s = fp1000_ + fp1000
    if s==0:
        continue
    if city=="UN":
        city = "other"
    if city=="HE":
        city = "HEB" 
    printing01(city + ' fp loc error <30  ', fp30, ratio(fp30/s))
    printing01(city + ' fp loc error <50  ', fp50, ratio(fp50/s))
    printing01(city + ' fp loc error <100 ', fp100, ratio(fp100/s))
    printing01(city + ' fp loc error <500 ', fp500, ratio(fp500/s))
    printing01(city + ' fp loc error <1000', fp1000, ratio(fp1000/s))
    printing01(city + ' fp loc error >1000', fp1000_, ratio(fp1000_/s))
    print() 





