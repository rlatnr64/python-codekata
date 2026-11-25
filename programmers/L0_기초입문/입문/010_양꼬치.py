# 양꼬치
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120830
# 알고리즘: 기초
# 작성자: 김수인
# 작성일: 2026. 11. 26. 00:04:33

def solution(n, k):
    n1 = n * 12000
    k1 = (k - (n // 10)) * 2000
    answer = n1 + k1
    return answer