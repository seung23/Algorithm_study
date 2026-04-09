def solution(genres, plays):

    genre_total = {}
    for g, p in zip(genres, plays):
        genre_total[g] = genre_total.get(g, 0) + p
    
        genre_rank = {g: rank for rank, (g, _) in enumerate(sorted(genre_total.items(), key=lambda x: -x[1]))}
    
    songs = sorted(range(len(genres)), key=lambda i: (genre_rank[genres[i]], -plays[i], i))
    
    ans = []
    count = {}
    
    for i in songs:
        g = genres[i]
        if count.get(g, 0) < 2:
            ans.append(i)
            count[g] = count.get(g, 0) + 1
            
    
    return ans