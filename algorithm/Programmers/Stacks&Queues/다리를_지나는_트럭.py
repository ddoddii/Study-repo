from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    cur_weight = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    while truck_weights:
        answer += 1
        cur_weight -= bridge.popleft()
        w = truck_weights.popleft() if cur_weight + truck_weights[0] <= weight else 0
        cur_weight += w
        bridge.append(w)
    
    return answer + len(bridge)

bridge_length = 3
weight = 10
truck_weights = [7,4,5,3]

ans = solution(bridge_length,weight,truck_weights)
print(ans)
