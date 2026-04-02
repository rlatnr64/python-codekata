# 최댓값 만들기 (2)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120862
# 알고리즘: 기초
# 작성자: 김수인
# 작성일: 2026. 04. 02. 23:10:29

def solution(numbers):
    answer = 0
    numbers.sort()
    a = numbers[0] * numbers[1]
    b = numbers[-1] * numbers[-2]
    
    if a > b:
        answer = a
    else:
        answer =b
    return answer