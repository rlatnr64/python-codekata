# 개미 군단
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120837
# 알고리즘: 기초
# 작성자: 김수인
# 작성일: 2026. 03. 16. 16:44:07

def solution(hp):
    answer = 0
    
    answer += hp // 5
    hp %= 5
    answer += hp // 3
    hp %= 3
    answer += hp // 1
    hp %= 1
    
    return answer