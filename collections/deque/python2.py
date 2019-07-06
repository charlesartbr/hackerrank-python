from collections import deque

d = deque()

n = int(raw_input())

for _ in xrange(n):

    cmd = raw_input().split()

    if cmd[0] == 'append':
        d.append(cmd[1])
    elif cmd[0] == 'appendleft':
        d.appendleft(cmd[1])
    elif cmd[0] == 'pop':
        d.pop()
    elif cmd[0] == 'popleft':
        d.popleft()

print str.join(' ', d)