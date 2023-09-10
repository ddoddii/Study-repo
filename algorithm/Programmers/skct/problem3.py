#3. page 이동(0), 뒤로 가기(-1), 앞으로 가기(1) 구현
# 페이지 이동시 idx += 1. 이동 시 current idx 페이지로 이동하고, 뒤로가기 stack 에 현재 페이지 추가, 앞 stack 삭제
# 뒤로 가기 시, 뒤로가기 stack 의 마지막 페이지로 이동 , 현재 페이지는 앞 stack 에 추가. 뒤로가기 stack 이 없을 시 명령 무시
# 앞으로 가기 시, 앞 stack 의 마지막 페이지로 이동, 현재 페이지는 뒤 stack 에 추가. 앞 stack 이 없을 시 명령 무시

acts = [[0,2],[-1,1],[0,1],[1,1],[-1,2],[1,1]]

def solution(acts):
    answer = []
    back = []
    front = []
    curr = 0
    idx = 0
    for act in acts:
        # 페이지 이동
        if act[0] == 0:
            while act[1] > 0:
                idx += 1
                back.append(curr)
                curr = idx
                act[1] -= 1
            front = []
            answer.append(curr)
            
        # 뒤로 가기
        if act[0] == -1:
            while act[1] > 0:
                if back:
                    front.append(curr)
                    curr = back.pop()
                    act[1] -= 1
                else:
                    act[1] -= 1        
            answer.append(curr)
            
        # 앞으로 가기
        if act[0] == 1:
            while act[1] > 0:
                if front:
                    back.append(curr)
                    curr = front.pop()
                    act[1] -= 1
                else:
                    act[1] -= 1
            answer.append(curr)
    return answer

print(solution(acts))
            
            
    
            
            