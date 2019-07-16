import operator

def person_lister(f):
    def inner(people):

        for p in xrange(len(people)):
            people[p][2] = int(people[p][2])

        people.sort(key = operator.itemgetter(2))

        return [f(p) for p in people]

    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [raw_input().split() for i in range(int(raw_input()))]
    print '\n'.join(name_format(people))