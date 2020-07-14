studentlist=['刘大','王二','张三','李四','周五']
a=0
jige={}
bujige={}
while a<len(studentlist):
    print(studentlist[a]+'的成绩：')
    grade=int(input())
    if grade>=60:
        jige[studentlist[a]]=grade
    else:
        bujige[studentlist[a]]=grade
    a=a+1
print('及格学生成绩单:',jige)
print('不及格学生成绩单:',bujige)