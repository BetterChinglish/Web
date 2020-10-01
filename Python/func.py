# def my_abs(x):
#     if x>0:
#         return x
#     elif x<=0:
#         return -x
#     else:
#         return "false"
        
# while True:
#     print (my_abs(int(input("enter your number"))))


#可变参数
def calc(*number):
    sum=0
    for i in number:
        sum+=i**2
    return sum

print(calc(1,2,3,4,9))


    