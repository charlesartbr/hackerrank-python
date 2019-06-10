students = list()

for _ in range(int(input())):

    name = input()

    score = float(input())

    students.append([name, score])

# order by score
students.sort(key = lambda x: x[1])

# get the first lowest score
first = students[0][1]

# find the second lowest score
for student in students:
    if student[1] > first:
        second = student[1]
        break

# order by name
students.sort(key = lambda x: x[0])

for student in students:
    if student[1] == second:
        print(student[0])