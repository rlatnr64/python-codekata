# 주사위의 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120845
# 알고리즘: 기초
# 작성자: 김수인
# 작성일: 2026. 04. 01. 17:28:55

def solution(box, n):
    answer = 0
    
    a = int(box[0]) // n
    answer += a
    
    b = int(box[1]) // n
    answer *= b
    
    c = int(box[2]) // n
    answer *= c
    
    return answer