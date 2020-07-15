denglu={}
username=[]
password=[]
a=0
x=1
while x==1:
    username.append(input('请输入账号:'))
    if len(username[a])<5 or len(username[a])>8:
        print('账号长度为5-8位，请重新输入')
        exit()
    elif username[a][0] not in 'qwertyuiopasdfghjklzxcvbnm':
        print('账号首字母必须为小写')
        exit()
    password.append(input('请输入密码:'))
    if len(password[a])<6 or len(password[a])>12:
        print('密码长度为6-12位，请重新输入')
        exit()
    a=a+1
    x=int(input('是否继续注册，继续请输入1，停止请输入0：'))
print('注册用户数量:',a)
for i in range(a):
    denglu[username[i]]=password[i]
print(denglu)