from collections import namedtuple

n = int(raw_input())

colummns = raw_input()

Student = namedtuple('Student', colummns)

marks = 0

for i in xrange(n):

    row = raw_input().split()

    student = Student(row[0], row[1], row[2], row[3])

    marks += float(student.MARKS)

average = marks / n

print '{0:.2f}'.format(average)
