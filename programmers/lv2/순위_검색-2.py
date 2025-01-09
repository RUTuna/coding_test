import itertools
import bisect
from collections import defaultdict

def solution(infos, queries):
    dic = defaultdict(list)
    combs = []
    for i in range(1, 5):
        combs += itertools.combinations([0,1,2,3], i)

    for info in infos:
        info = info.split()
        dic[''.join(info[:4])].append(int(info[4]))
        for comb in combs:
            new_info = []
            for i in range(4):
                new_info.append('-' if i in comb else info[i])
            dic[''.join(new_info)].append(int(info[4]))
    
    for _, value in dic.items():
        value.sort()
    
    answer = []
    for query in queries:
        query = query.split()
        new_query = ''.join([query[i*2] for i in range(4)])
        result = dic[new_query]
        answer.append(len(result) - bisect.bisect_left(result, int(query[-1])))
    
    return answer