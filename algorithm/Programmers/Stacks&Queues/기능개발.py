import math

def solution(progresses, speeds):
    answer = []
    days = []
    length = 1
    for i,progress in enumerate(progresses):
        days.append(math.ceil((100-progress) / speeds[i]))
    max_value = days[0]
    for i in range(1,len(days)):
        if days[i] > max_value:
            max_value = days[i]
            answer.append(length)
            length = 1
        else:
            length += 1
    answer.append(length)
    return answer