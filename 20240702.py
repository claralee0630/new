#2024.07.02 점프투파이썬 for문 p.138 부터

#p.138
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

    
a = [(1,2),(3,4),(5,6)]
for (first, last) in a:
    print(first + last)


#marks1.py
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." %number)
    else:
        print("%d번 학생은 불합격입니다." %number)


#marks2.py
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark < 60: continue
    print("%d번 학생 축하합니다. 합격입니다. " %number)


a = range(10)

a = range(1,11)


add = 0
for i in range(1,11):
    add = add + i
    
print(add)


#marks3. py
marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60: continue
    print("%d번 학생 축하합니다. 합격입니다." %(number + 1))


add = 0
for number in range(1,101):
    add = add + i

print(add)


for i in range(2,10):
    for j in range(1,10):
        print(i * j, end = " ")
    print(' ')


for i in range(2,10):
    for j in range(1,10):
        print(i*j)

  
for i in range(2,10):
    for j in range(1,10):
        print(i*j, end = " ")

               
for i in range(2,10):
    for j in range(1,10):
        print(i * j, end = " ")
    print(' ')


#p.144
a = [1,2,3,4]          
result = []           
for num in a:
    result. append(num * 3)
print(result)      

a = [1,2,3,4]          
result = [num * 3 for num in a]            
print(result)
               
a = [1,2,3,4] 
result = [num * 3 for num in a if num % 2 == 0]         
print(result)

a = [1,2,3,4]          
result = [num * 3 for num in a]       
print(result)
               
a = [1,2,3,4]    
result = [num * 3 for num in a if num % 2 == 0]
print(result)


#p.145
result = [x * y for x in range(2,10)
          for y in range(1,10)]
print(result)

#3장 연습문제

#1번
a = "Life is too short, you need python"
if "wife" in a : print("wife")
elif "python"