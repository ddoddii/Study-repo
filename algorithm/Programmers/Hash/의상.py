from collections import Counter

def solution(clothes):
    ans = 1
    clodict = Counter([kind for name,kind in clothes])
    for h in clodict.values():
        ans = (h+1) * ans
    return ans-1

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))
