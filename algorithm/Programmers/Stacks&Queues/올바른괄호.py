def solution(s):
    lefty = ['(']
    righty = [')']
    temp = []
    temp = []
    for char in s:
        if char in lefty:
            temp.append(char)
        elif char in righty:
            if not temp or temp.pop() != '(':
                return False
    return len(temp) == 0   

    