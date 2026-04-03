# 인덱스 바꾸기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120895
# 알고리즘: 기초
# 작성자: 김수인
# 작성일: 2026. 04. 03. 11:56:05

def solution(my_string, num1, num2):
    a = list(my_string)
    a[num1], a[num2] = a[num2], a[num1]
    return ''.join(a)