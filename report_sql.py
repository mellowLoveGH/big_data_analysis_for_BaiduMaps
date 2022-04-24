
# ---------------------------------------

# remove the empty lines by iteration
def report_preprocess(sample):
  sample = sample.strip()
  lines = sample.split("\n")
  new_lines = [] # remove empty lines
  for ln in lines:
    tmp = ln.strip()
    if len(tmp)>0:
      new_lines.append(tmp)
  return new_lines

# remove the empty lines by iteration
def report_preprocess01(lns):
  new_lines = [] # remove empty lines
  for ln in lns:
    tmp = ln.strip()
    if len(tmp)>0:
      new_lines.append(tmp)
  return new_lines


# get the date-time, usually, it should be the primary key for SQL table
def get_date(lines):
  dt = lines[-1][-12:-4]
  return dt[:4]+"-"+dt[4:6]+"-"+dt[6:]

# form SQL insert sentence
def form_sql(table_name, report_date, nums):
  st = "insert into " + table_name + " values ('" + report_date + "'"
  for n in nums:
    st = st + ", " + str(n)
  st = st + "); "
  return st

def form_sql_update01(table_name, report_date, category, city, nums):
  st = "insert into " + table_name + " values ('" + report_date + "', '" + category + "', '" + city + "'"
  for n in nums:
    st = st + ", " + str(n)
  st = st + "); "
  return st 

def get_quantity_ratio(ln):
  tmp = []
  pre = ""
  i = 0
  while i<len(ln):
    ch = ln[i]
    if ch >= '0' and ch <= '9':
      pre = ln[ max(0, i-1) ]
      if pre == ' ' or pre == '\t':
        tmp.append(i)
    i += 1
  assert len(tmp) == 2
  quantity = int(ln[tmp[0]: tmp[1]])
  ratio = float(ln[tmp[1]:].replace("%", ""))
  return quantity, ratio

def get_header_quantity_ratio(ln):
  tmp = []
  pre = ""
  i = 0
  while i<len(ln):
    ch = ln[i]
    if ch >= '0' and ch <= '9':
      pre = ln[ max(0, i-1) ]
      if pre == ' ' or pre == '\t':
        tmp.append(i)
    i += 1
  assert len(tmp) == 2
  header = ln[:tmp[0]].strip()
  quantity = int(ln[tmp[0]: tmp[1]])
  ratio = float(ln[tmp[1]:].replace("%", ""))
  return header, quantity, ratio


# table 1: date, PV, UV
def process_table01(lines):
  tmp = lines[1].split(":")
  if len(tmp)==2:
    uv = int(tmp[1].strip())
  #
  tmp = lines[2].split(":")
  if len(tmp)==2:
    pv = int(tmp[1].strip())
  return pv, uv
# table 1, form the sql
def table01_sql(report_date, pv, uv):
  st = "insert into " + "t01_pv_uv" + " values ('" + report_date + "', " + str(pv) + ", " + str(uv) + ");"
  return st

# table 2: date, nlp, map, op, pv
def process_table02(lines):
  nums = []
  for i in [4, 5, 6]:
    quantity, ratio = get_quantity_ratio(lines[i])
    nums.append(quantity)
    nums.append(ratio)
  return nums
# table 2, form the sql
def table02_sql(report_date, nums, pv):
  nums.append(pv)
  st = form_sql("t02_pv_source", report_date, nums)
  return st

# table 3: date, -1, 0, 1, 2, 3, pv
def process_table03(lines):
  nums = []
  i = 8
  while i<=12:
    quantity, ratio = get_quantity_ratio(lines[i])
    nums.append(quantity)
    nums.append(ratio)
    i = i + 1
  return nums
# table 3, form the sql
def table03_sql(report_date, nums, pv):
  nums.append(pv)
  st = form_sql("t03_pv_inout", report_date, nums)
  return st

# table 4: date, valid cell, invalid cell, pv
def process_table04(lines):
  nums = []
  i = 14
  while i<=15:
    quantity, ratio = get_quantity_ratio(lines[i])
    nums.append(quantity)
    nums.append(ratio)
    i = i + 1
  return nums
# table 4, form the sql
def table04_sql(report_date, nums, pv):
  nums.append(pv)
  st = form_sql("t04_pv_cell", report_date, nums)
  return st

# table 5: date, wf, pv
def process_table05(lines):
  nums = []
  i = 17
  while i<=17:
    quantity, ratio = get_quantity_ratio(lines[i])
    nums.append(quantity)
    nums.append(ratio)
    i = i + 1
  return nums
# table 5, form the sql
def table05_sql(report_date, nums, pv):
  nums.append(pv)
  st = form_sql("t05_pv_wf", report_date, nums)
  return st

# table 6: date, gps, pv
def process_table06(lines):
  nums = []
  i = 19
  while i<=19:
    quantity, ratio = get_quantity_ratio(lines[i])
    nums.append(quantity)
    nums.append(ratio)
    i = i + 1
  return nums
# table 6, form the sql
def table06_sql(report_date, nums, pv):
  nums.append(pv)
  st = form_sql("t06_pv_gps", report_date, nums)
  return st

# table 7: date, main, other, pv
def process_table07(lines):
  nums = []
  i = 21
  while i<=22:
    quantity, ratio = get_quantity_ratio(lines[i])
    nums.append(quantity)
    nums.append(ratio)
    i = i + 1
  return nums
# table 7, form the sql
def table07_sql(report_date, nums, gps):
  nums.append(gps)
  st = form_sql("t07_gps_cities", report_date, nums)
  return st

# table 8: date, nlp, map, op, pv
def process_table08(lines):
  nums = []
  i = 23
  while i<=25:
    quantity, ratio = get_quantity_ratio(lines[i])
    nums.append(quantity)
    nums.append(ratio)
    i = i + 1
  return nums
# table 8, form the sql
def table08_sql(report_date, nums, gps):
  nums.append(gps)
  st = form_sql("t08_gps_source", report_date, nums)
  return st

# table 9: date, nlp, map, op, pv
def process_table09(lines):
  nums = []
  i = 27
  while i<=29:
    quantity, ratio = get_quantity_ratio(lines[i])
    nums.append(quantity)
    nums.append(ratio)
    i = i + 1
  return nums
# table 9, form the sql
def table09_sql(report_date, nums, main_gps):
  nums.append(main_gps)
  st = form_sql("t09_gps_main_source", report_date, nums)
  return st

# table 10: date, nlp, map, op, pv
def process_table10(lines):
  nums = []
  i = 31
  while i<=33:
    quantity, ratio = get_quantity_ratio(lines[i])
    nums.append(quantity)
    nums.append(ratio)
    i = i + 1
  return nums
# table 10, form the sql
def table10_sql(report_date, nums, other_gps):
  nums.append(other_gps)
  st = form_sql("t10_gps_other_source", report_date, nums)
  return st

# get main-cities gps, other-cities valid gps
def get_valid(lines):
  nums = []
  i = 35
  while i<=46:
    quantity, ratio = get_quantity_ratio(lines[i])
    nums.append(quantity)
    i = i + 1
  return sum(nums[:4]), sum(nums[4:8]), sum(nums[8:])

# table 11: date, nlp, map, op, pv
def process_table11(lines):
  nums = []
  i = 35
  while i<=37:
    quantity, ratio = get_quantity_ratio(lines[i])
    nums.append(quantity)
    nums.append(ratio)
    i = i + 1
  return nums
# table 11, form the sql
def table11_sql(report_date, nums, valid_gps):
  nums.append(valid_gps)
  st = form_sql("t11_gps_valid_source", report_date, nums)
  return st

# table 12: date, nlp, map, op, pv
def process_table12(lines):
  nums = []
  i = 39
  while i<=41:
    quantity, ratio = get_quantity_ratio(lines[i])
    nums.append(quantity)
    nums.append(ratio)
    i = i + 1
  return nums
# table 12, form the sql
def table12_sql(report_date, nums, valid_main_gps):
  nums.append(valid_main_gps)
  st = form_sql("t12_gps_valid_main_source", report_date, nums)
  return st

# table 13: date, nlp, map, op, pv
def process_table13(lines):
  nums = []
  i = 43
  while i<=45:
    quantity, ratio = get_quantity_ratio(lines[i])
    nums.append(quantity)
    nums.append(ratio)
    i = i + 1
  return nums
# table 13, form the sql
def table13_sql(report_date, nums, valid_other_gps):
  nums.append(valid_other_gps)
  st = form_sql("t13_gps_valid_other_source", report_date, nums)
  return st

# table 14: date, cell, r, wf, r, prop, r, fp, r, cls, r
def process_table14(lines):
  nums = []
  i = 48
  while i<=52:
    quantity, ratio = get_quantity_ratio(lines[i])
    nums.append(quantity)
    nums.append(ratio)
    i = i + 1
  return nums
# table 14, form the sql
def table14_sql(report_date, nums):
  st = form_sql("t14_success_rate", report_date, nums)
  return st


def get_category_city(header):
  category = ["cell", "wifi", "prop", "fp", "cls"]
  city = ["all", "other", "BJ", "SH", "GZ", "SZ", "DG", "XA", "CD", "ZZ", "HEB"]
  hs = header.strip().split(" ")
  if hs[0].strip() in category:
    return hs[0].strip(), "all"
  else:
    return hs[1].strip(), hs[0].strip() 


# table 15: date, cell, r, wf, r, prop, r, fp, r, cls, r
def process_table15(lines):
  info = []
  i = 54
  while i<= len(lines)-2:
    ln = lines[i]
    if "---" in ln:
      i += 1
      continue
    header, quantity, ratio = get_header_quantity_ratio(ln)
    tmp = ( header, quantity, ratio )
    info.append(tmp)
    i = i + 1
  return info
# table 15, form the sql
def table15_sql(report_date, info):
  st = ""
  category = ""
  city = ""
  nums = []
  i = 0
  while i<len(info):
    h, q, r = info[i]
    category, city = get_category_city(h)
    nums.append( q )
    nums.append( r )
    #
    if (i+1)%6 == 0:
      ln = form_sql_update("t15_accuracy_rate", report_date, category, city, nums)
      nums = []
      st = st + ln + "\n"
    i += 1
  return st

def form_sql_update(table_name, report_date, att01, att02, nums):
  st = "insert into " + table_name + " values ('" + report_date + "', '" + att01 + "', '" + att02 + "'"
  for n in nums:
    st = st + ", " + str(n)
  st = st + "); "
  return st 

def get_table01(lines, idx_col):
  nums = []
  # pv - uv
  pv, uv = 0, 0
  tmp = lines[idx_col[0]].split(":")
  if len(tmp)==2:
    uv = int(tmp[1].strip())
  tmp = lines[idx_col[1]].split(":")
  if len(tmp)==2:
    pv = int(tmp[1].strip())
  nums.append(pv)
  nums.append(uv)
  # other info
  for i in idx_col[2:]:
    quantity, ratio = get_quantity_ratio(lines[i])
    nums.append(quantity)
    nums.append(ratio)
  return nums

def table01_insert(report_date, nums):
  st = form_sql("t01_pv_uv", report_date, nums)
  return st

def get_table02(lines, idx_col):
  nums = []
  for i in idx_col:
    quantity, ratio = get_quantity_ratio(lines[i])
    nums.append(quantity)
    nums.append(ratio)
  return nums

def table02_insert(report_date, nums, city="", scope=""):
  st = form_sql_update("t02_gps_source", report_date, city, scope, nums)
  return st

def get_valid_gps(lines, idx_col):
  ttl = 0
  for i in idx_col:
    quantity, ratio = get_quantity_ratio(lines[i])
    ttl += quantity
  return ttl

def get_table03(lines, idx_col):
  nums = []
  for i in idx_col:
    quantity, ratio = get_quantity_ratio(lines[i])
    nums.append(quantity)
    nums.append(ratio)
  return nums

def table03_insert(report_date, nums):
  st = form_sql("t03_success_rate", report_date, nums)
  return st

# table 15: date, cell, r, wf, r, prop, r, fp, r, cls, r
def get_table04(lines):
  info = []
  i = 54+1
  while i<= len(lines)-2:
    ln = lines[i]
    if "---" in ln:
      i += 1
      continue
    header, quantity, ratio = get_header_quantity_ratio(ln)
    tmp = ( header, quantity, ratio )
    info.append(tmp)
    i = i + 1
  return info
# table 15, form the sql
def table04_insert(report_date, info):
  st = ""
  category = ""
  city = ""
  nums = []
  i = 0
  while i<len(info):
    h, q, r = info[i]
    category, city = get_category_city(h)
    nums.append( q )
    nums.append( r )
    #
    if (i+1)%6 == 0:
      ln = form_sql_update("t04_accuracy_rate", report_date, category, city, nums)
      nums = []
      st = st + ln + "\n"
    i += 1
  return st

############################################
report_file = open("email.txt","r")
lns = report_file.readlines()
lns = lns[3:]

sample = "\n"
for ln in lns:
    sample = sample + ln + "\n"

lines = report_preprocess(sample)
report_date = get_date(lines)

"""
pv, uv = process_table01(lines) # get pv
st = table01_sql(report_date, pv, uv)
print(st)

nums = process_table02(lines)
st = table02_sql(report_date, nums, pv)
print(st)

nums = process_table03(lines)
st = table03_sql(report_date, nums, pv)
print(st)

nums = process_table04(lines)
st = table04_sql(report_date, nums, pv)
print(st)

nums = process_table05(lines)
st = table05_sql(report_date, nums, pv)
print(st)

nums = process_table06(lines)
st = table06_sql(report_date, nums, pv)
print(st)

gps = nums[0] # get gps 

nums = process_table07(lines)
st = table07_sql(report_date, nums, gps)
print(st)

main_gps, other_gps = nums[0], nums[2] # get main-cities gps, other-cities gps

nums = process_table08(lines)
st = table08_sql(report_date, nums, gps)
print(st)

nums = process_table09(lines)
st = table09_sql(report_date, nums, main_gps)
print(st)

nums = process_table10(lines)
st = table10_sql(report_date, nums, other_gps)
print(st)

valid_gps, valid_main_gps, valid_other_gps = get_valid(lines) # get main-cities gps, other-cities valid gps

nums = process_table11(lines)
st = table11_sql(report_date, nums, valid_gps)
print(st)

nums = process_table12(lines)
st = table12_sql(report_date, nums, valid_main_gps)
print(st)

nums = process_table13(lines)
st = table13_sql(report_date, nums, valid_other_gps)
print(st)

# -------------------------------- success rate
nums = process_table14(lines)
st = table14_sql(report_date, nums)
print(st)

# -------------------------------- accuracy rate
info = process_table15(lines)
st = table15_sql(report_date, info)
print(st)
"""


# table 01: pv, uv, nlp, map, op, -1, 0, 1, 2, 3, valid cell, invalid cell, wifi, gps
idx_col = [1, 2, 4, 5, 6, 8, 9, 10, 11, 12, 14, 15, 17, 19]
nums = get_table01(lines, idx_col)
st = table01_insert(report_date, nums)
print(st)

# table 02: city, scope, nlp, map, op, total
idx_col = [23, 24, 25, 19]
nums = get_table02(lines, idx_col)
st = table02_insert(report_date, nums[:-1], "all", "all")
print(st)
idx_col = [27, 28, 29, 21]
nums = get_table02(lines, idx_col)
st = table02_insert(report_date, nums[:-1], "main", "all")
print(st)
idx_col = [31, 32, 33, 22]
nums = get_table02(lines, idx_col)
st = table02_insert(report_date, nums[:-1], "other", "all")
print(st)
valid_gps = get_valid_gps(lines, [35, 36, 37, 38])# get valid GPS
idx_col = [35, 36, 37]
nums = get_table02(lines, idx_col)
nums.append( valid_gps )
st = table02_insert(report_date, nums, "all", "valid")
print(st)
valid_main_gps = get_valid_gps(lines, [39, 40, 41, 42])# get valid main GPS
idx_col = [39, 40, 41]
nums = get_table02(lines, idx_col)
nums.append( valid_main_gps )
st = table02_insert(report_date, nums, "main", "valid")
print(st)
valid_other_gps = get_valid_gps(lines, [43, 44, 45, 46])# get valid other GPS
idx_col = [43, 44, 45]
nums = get_table02(lines, idx_col)
nums.append( valid_other_gps )
st = table02_insert(report_date, nums, "other", "valid")
print(st)

# table 03: cell, wifi, prop, fp, cls, indoor
idx_col = [48, 49, 50, 51, 52, 53]
nums = get_table03(lines, idx_col)
st = table03_insert(report_date, nums)
print(st)

# table 04: category, city, <30, <50, <100, <500, <1000, >1000
info = get_table04(lines)
st = table04_insert(report_date, info)
print(st)