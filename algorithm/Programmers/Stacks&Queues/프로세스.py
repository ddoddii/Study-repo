from collections import deque
def solution(priorities, location):
    priorities_dict = {}
    start = deque([])
    idx_sequence = []
    for i in range(len(priorities)):
        priorities_dict[i] = priorities[i]
        start.append(i)
    while start:
        maxval = max(priorities)
        if priorities_dict[start[0]] < maxval:
            start.append(start.popleft())
        else:
            idx_sequence.append(start[0])
            priorities.remove(priorities_dict[start.popleft()])
    return idx_sequence.index(location) + 1
    