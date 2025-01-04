def solution(phone_book):
    phone_book = sorted(phone_book)
    prev = '-'
    
    for phone in phone_book:
        if len(prev) <= len(phone) and prev == phone[:len(prev)]:
            return False
        else:
            prev = phone
    
    return True