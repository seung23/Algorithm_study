def solution(brown, yellow):
    s = (brown + 4) / 2              # W + H (합)
    p = brown + yellow                # W * H (곱)
    d = (s**2 - 4*p) ** 0.5           # 판별식의 √
    w = (s + d) / 2                   # 큰 근 → 가로
    h = (s - d) / 2                   # 작은 근 → 세로
    return [int(w), int(h)]