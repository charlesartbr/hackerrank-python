from collections import namedtuple

n = int(input())

Student = namedtuple('Student', input())

marks = 0

for i in range(n):

    row = input().split()

    student = Student(row[0], row[1], row[2], row[3])

    marks += float(student.MARKS)

average = marks / n

print('%.2f' % average)
