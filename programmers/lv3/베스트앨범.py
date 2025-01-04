import heapq

def solution(genres, plays):
    song = {}
    n = len(genres)
    
    for i in range(n):
        if genres[i] in song:
            song[genres[i]][0] += plays[i]
            heapq.heappush(song[genres[i]][1], (-plays[i], i))
        else:
            song[genres[i]] = [plays[i], [(-plays[i], i)]]
    
    keys = sorted(song.keys(), key = lambda k: song[k][0], reverse = True)
    
    answer = []
    for key in keys:
        for i in range(2):
            heap = song[key][1]
            if len(heap):
                answer.append(heapq.heappop(heap)[1])
        
    return answer