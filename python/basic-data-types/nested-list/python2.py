students = list()

for _ in range(int(raw_input())):

    name = raw_input()

    score = float(raw_input())

    students.append([name, score])

# order by score
students.sort(lambda x,y: cmp(x[1], y[1]))

# get the second lowest score
second = students[1][1]

# order by name
students.sort(lambda x,y: cmp(x[0], y[0]))

for student in students:
    if student[1] == second:
        print student[0]