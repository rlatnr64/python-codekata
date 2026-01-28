# 삼각형의 완성조건 (1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120889
# 알고리즘: 기초
# 작성자: 김수인
# 작성일: 2026. 01. 29. 00:46:54

def solution(sides):
    sided = sorted(sides, reverse=True)
    if sided[0] < sided[1] + sided[2]:
        return 1
    else:
        return 2