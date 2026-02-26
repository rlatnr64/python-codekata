# 짝수는 싫어요
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120813
# 알고리즘: 기초
# 작성자: 김수인
# 작성일: 2026. 02. 26. 10:01:03

def solution(n):
    answer = []
    for i in range(1, n+1, 2):
        answer.append(i)
    return answer