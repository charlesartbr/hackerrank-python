class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        s = sorted(self.__elements)
        self.maximumDifference = s[len(s) - 1] - s[0]

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)