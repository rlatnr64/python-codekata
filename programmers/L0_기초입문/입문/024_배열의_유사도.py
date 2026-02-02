# 배열의 유사도
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120903
# 알고리즘: 기초
# 작성자: 김수인
# 작성일: 2026. 02. 02. 21:32:09

def solution(s1, s2):
    total = 0
    for i in s1:
        for j in s2:
            if i == j:
                total += 1
    return total