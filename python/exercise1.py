#############################
#### FUNCTION EXERCISES #####
#############################

###############
## Problem 1 ##
###############

# Given the string:
s = 'django'

# ใช้ indexing เพื่อ print out ให้ได้ผลดังต่อไปนี้:
# 'd'

# 'o'

# 'djan'

# 'jan'

# 'go'

# Bonus: ลองใช้ index จากท้าย
print(s[0])
print(s[-1])
print(s[:4])
print(s[1:4])
print(s[-2:])

###############
## Problem 2 ##
###############

# Given this nested list:
l = [3,7,[1,4,'hello']]
# จงแก้ค่า hello เป็น goodbye
l[2][2]="goodbye"
print(l)

###############
## Problem 3 ##
###############

# จง print out ค่า hello ออกมาจาก dicitionry ด้านล่าง:

d1 = {'simple_key':'hello'}

d2 = {'k1':{'k2':'hello'}}

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}

print(d1['simple_key'])
print(d2['k1']['k2'])
print(d3['k1'][0]['nest_key'][1][0])
#####################
## -- PROBLEM 4 -- ##
#####################

# เขียนฟังก์ชั่นที่รับ list ของเลข integer โดยจะ return True ถ้ามี list ของเลข 1, 2, 3 อยู่ใน list ที่รับเข้ามา

# For example:


# arrayCheck([1, 1, 2, 4, 1]) → False
# arrayCheck([1, 1, 2, 1, 2, 3]) → True

def arrayCheck(nums):
  for index,x in enumerate(nums):
    if nums[index]==1 and nums[index+1]==2 and nums[index+2] == 3:
      return True
  return False
    # CODE GOES HERE
print(arrayCheck([1, 1, 2, 3, 1]))
print(arrayCheck([1, 1, 2, 4, 3]))
print(arrayCheck([1, 1, 2, 1, 2, 3]))

#####################
## -- PROBLEM 5 -- ##
#####################

# เขียนฟังก์ชั่นที่รับ string เข้ามา แล้ว return string ที่แสดงตัวอักษร ตัว-เว้น-ตัว จาก string ที่รับเข้ามา

# For example:

# stringBits('Hello') → 'Hlo'
# stringBits('Hi') → 'H'
# stringBits('Heeololeo') → 'Hello'

def stringBits(str):
  print(str[::2])

  # CODE GOES HERE
stringBits('Hello')
stringBits('Hi')
stringBits('Heeololeo')
#####################
## -- PROBLEM 6 -- ##
#####################

# จง return จำนวนเลขคู่ใน list ที่ส่งเข้ามาในฟังก์ชั่น
#
# Examples:
#
# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0

def count_evens(args):
  a=0
  for i in args:
    if i %2 ==0:
      a+=1
  print(a)
  # CODE GOES HERE
count_evens([1, 3, 5])
count_evens([2, 2, 0])
