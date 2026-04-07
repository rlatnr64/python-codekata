# 숫자 찾기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120904
# 알고리즘: 기초
# 작성자: 김수인
# 작성일: 2026. 04. 07. 16:51:45

def solution(num, k):
    num = str(num)
    return num.index(str(k)) + 1 if str(k) in num else -1