# studentlist=['刘大','王二','张三','李四','周五']
# a=0
# jige={}
# bujige={}
# while a<len(studentlist):
#     print(studentlist[a]+'的成绩：')
#     grade=int(input())
#     if grade>=60:
#         jige[studentlist[a]]=grade
#     else:
#         bujige[studentlist[a]]=grade
#     a=a+1
# print('及格学生成绩单:',jige)
# print('不及格学生成绩单:',bujige)



# a=['刘大','王二','张三','李四','周五']
# for i in a:
#     print(i)


# b=list(range(0,10))
# print(b)
# b=range(0,10,3)

# for i in b:
#     print(i)


# studentlist=['刘大','王二','张三','李四','周五']
# a=0
# jige={}
# bujige={}

# for i in range(len(studentlist)):
#     print(studentlist[a]+'的成绩：')
#     grade=int(input())
#     if grade>=60:
#         jige[studentlist[a]]=grade
#     else:
#         bujige[studentlist[a]]=grade
#     a=a+1
# print('及格学生成绩单:',jige)
# print('不及格学生成绩单:',bujige)



# studentlist=['刘大','王二','张三','李四','周五']
# jige={}
# bujige={}

# for i in studentlist:
#     print(i+'的成绩：')
#     grade=int(input())
#     if grade>=60:
#         jige[i]=grade
#     else:
#         bujige[i]=grade
# print('及格学生成绩单:',jige)
# print('不及格学生成绩单:',bujige)

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(i,'*',j,'=',i*j,' ',end='')
#     print()  




# for j in range(5):
#     for i in range(30):
#         print('距离红灯结束还有',30-i,'秒')
#     for i in range(35):
#         print('距离绿灯结束还有',35-i,'秒')
#     for i in range(5):
#         print('距离黄灯结束还有',5-i,'秒')



#初稿
# denglu={}
# username=[]
# password=[]
# a=0
# while x==1:
#     username[a]=input('请输入账号:')
#     if len(username[a])<5 or len(username[a])>8:
#         print('账号长度为5-8位，请重新输入')
#         exit()
#     elif username[a][0] not in 'qwertyuiopasdfghjklzxcvbnm':
#         print('账号首字母必须为小写')
#         exit()
#     password[a]=input('请输入密码:')
#     if len(password[a])<6 or len(password[a])>12:
#         print('密码长度为6-12位，请重新输入')
#         exit()
#     a=a+1

