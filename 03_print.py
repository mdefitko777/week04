print("hello world")

name = 'bowen'
print(name)

print(f'My name is {name}.')
print('My name is',  name , '.')
print('My name is ' + name + '.')
print('My name is %s.' %(name))

width = 10
precision = 4
value = 12.24567
print(f'result = {value : {width}.{precision}}') # 4개의 유효 숫자
print(f'result = {value : {width}.{precision}f}') # 소수점 4개
print(f'result = {value : {width}.2f}') #
print(f'result = {value : {width}.3f}') #
print(f'result = {value : {width}.4f}') #  소수점 {}f개




