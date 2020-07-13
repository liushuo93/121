#元组
# a=(1212,31232,"哈哈","哈哈","哈哈","哈哈","哈哈","哈哈",True,False)   #空元组
# print(a)
# print(a[4])
# print(a.index("哈哈"))
# print(a.count("哈哈"))
# b=(a,"是否是否是","ewrwerewe")
# print(b[0])
# print(b[0][4])
# print(a[4:9])
# print(a[5:])
# a=[1212,31232,"哈哈","哈哈",True,False]

# a.append("dhsjadhkashdk")
a.insert(0,"dadhajkdakdadshaskdad")
print(a)
b=[31312,4342,"fsdfsdf",'erw','y65y5g']
a.extend(b)
print(a)
a.remove(4342)
# print(a)
# a={"name":"张三",0:'232',321:'qwew'}
# print(a['name'])
# a['high']=180
# print(a)
# b=a.get('name')
# print(b)
# c=a.pop(0)
# print(c)
# print(a)
# a.update(name=3123213)
# print(a)
# a.update(na234me=3123213)
# print(a)
a=input('name:')
b=input('age:')
c=input('sex:')
print({'name':a,'age':b,'sex':c})

