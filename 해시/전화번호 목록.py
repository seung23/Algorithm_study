def solution(phone_book):
    phone_book.sort()
    
    for i in range(len(phone_book) - 1):
        a = phone_book[i]
        b = phone_book[i+1]
        if b.startswith(a): # 이런 내장함수가 있는지도 몰랐넹 x.startswith(y)
            return False
       
    return True
