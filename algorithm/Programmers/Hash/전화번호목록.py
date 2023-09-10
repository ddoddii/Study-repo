# 전화번호 목록에서 접두사 확인 

def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
    return True

phone_book =["119", "97674223", "1195524421"]
print(solution(phone_book))