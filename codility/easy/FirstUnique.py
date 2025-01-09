def solution(A):
    unique = set()
    notUnique = set()

    for num in A:
        if num in unique:
            notUnique.add(num)
        else:
            unique.add(num)

    unique = unique-notUnique
    for i, num in enumerate(A):
        if num in unique:
            return num

    return -1