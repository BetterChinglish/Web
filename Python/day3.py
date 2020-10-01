# 1
# import random

# def func(sum):
#     sum=sum
#     random_num=random.randint(1,100)
#     print "let's play the game"
#     print"you have ",sum, " chances"
#     while sum>0:
        
#         getnum=int(input("enter your number[0~100)："))
#         if getnum==random_num:
#             print("you are right")
#             return 
#         elif getnum>random_num:
#             print("bigger! try again")
#             sum-=1
#             print"you have ",sum, " chances"
#         elif getnum<random_num:
#             print("smaller! try again")   
#             sum-=1
#             print"you have ",sum, " chances"      
            
# func(5)




# 2

# import math

# #最大公因数
# def function_1(x, y):
#     m = max(x, y)
#     n = min(x, y)
#     while m%n:
#         m, n = n, m%n
#     return n

# #或：
# print(math.gcd(10,15))

# #最小公倍数
# def function_2(x,y):
#      m = max(x, y)
#     n = min(x, y)
#     while m%n:
#         m, n = n, m%n
#     return x*y//n

# 3

# def function(dict_a):
#     dict_b=[]
#     for i in dict_a:
#         if i not in dict_b:
#             dict_b.append(i)
    