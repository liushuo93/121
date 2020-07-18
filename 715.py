# denglu={}
# username=[]
# password=[]
# a=0
# x=1
# while x==1:
#     username.append(input('请输入账号:'))
#     if len(username[a])<5 or len(username[a])>8:
#         print('账号长度为5-8位，请重新输入')
#         exit()
#     elif username[a][0] not in 'qwertyuiopasdfghjklzxcvbnm':
#         print('账号首字母必须为小写')
#         exit()
#     password.append(input('请输入密码:'))
#     if len(password[a])<6 or len(password[a])>12:
#         print('密码长度为6-12位，请重新输入')
#         exit()
#     a=a+1
#     x=int(input('是否继续注册，继续请输入1，停止请输入0：'))
# print('注册用户数量:',a)
# for i in range(a):
#     denglu[username[i]]=password[i]
# print(denglu)




# light={'红灯':50,'绿灯':35,'黄灯':3}
# for i in light:
#     for j in range(light[i]):
#         print('距离',i,'结束还有',light[i]-j,'秒')


# for i in range(10):
#     if i==4:
#         break
#     print(i)

# def checkname(username):

# def plus(a,b):
#     '''
#     实现两个数字相加
#     '''
#     if type(a) is int and type(b) is int:
#         # print(a+b)
#         return a+b
#     else:
#         # print('输入的数据类型不正确')
#         return '输入的数据类型不正确'
# x=int(input())
# y=int(input())
# print(plus(x,y))



# 异常类hui
# try:
#     print(1+s32)
# except Exception as e:
#     print('上面的代码错了',e)



# import time
# for i in range(10):
#     time.sleep(1)
#     print(i)


# import random
# a=random.randint(12,3244)
# print(a)

import pymysql

