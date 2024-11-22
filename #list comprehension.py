#list comprehension

squares = []
for i in range(1,11):
    squares.append(i*i)
print(squares)

#now using list comprehension

squares = [i * i for i in range(1,11)]
print(squares)

# selecting passed students

students = [100,90,80,70,60,30,20,10]

passed_students = [i if i >= 60 else "failed" for i in students ]
print(passed_students)

