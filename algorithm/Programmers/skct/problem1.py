# 1. Dart 점수 계산하기 

from collections import Counter

scores = [[4,9,8,10,10],[9,2,2,5,8],[5,10,5,3,4],[7,9,10,5,4],[4,4,10,1,4]]
darts = [4,9,14,19,24,12,23]
# result = 34

def solution(scores,darts):
    # expense 계산
    if len(darts) > 5:
        expense = 10 + 5*(len(darts)-5)
    else:
        expense = 10

    # row, column , score 계산
    score = 0
    row = []
    column = []
    unique_darts = list(set(darts)) #dart 중복 제거
    for dart in unique_darts:
        i = (dart-1) // 5
        j = (dart-1) % 5
        row.append(i)
        column.append(j)
        score += scores[i][j]
        
    # Bingo 찾기 
    sub_list = [0, 1, 2, 3, 4]

    # row 연속 0,1,2,3,4 , column 같은 숫자 5개
    bingo  = False
    if all(item in row for item in sub_list):
        c = Counter(column)
        for _ , count in c.items():
            if count == 5:
                bingo = True
    # column 연속 0,1,2,3,4  , row 같은 숫자 5개     
    if all(item in column for item in sub_list):
        r = Counter(row)
        for _ , count in r.items():
            if count == 5:
                bingo = True

    if bingo:
        fin_score = score - expense + 10
    else:
        fin_score = score - expense
    return fin_score 

print(solution(scores,darts))