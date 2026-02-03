# 순서쌍의 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120836
# 알고리즘: 기초
# 작성자: 김수인
# 작성일: 2026. 02. 03. 23:02:10

def solution(n):
    answer = 0
    i = 1
    
    while i * i <= n:
        if n % i == 0:
            if i == n // i:
                answer += 1
            else:
                answer += 2
        i += 1
        
    return answer