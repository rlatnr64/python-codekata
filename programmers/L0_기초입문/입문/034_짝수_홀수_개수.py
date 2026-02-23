# 짝수 홀수 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120824
# 알고리즘: 기초
# 작성자: 김수인
# 작성일: 2026. 02. 23. 12:18:53

def solution(num_list):
    answer = []
    x = 0
    y = 0
    for i in num_list:
        if i % 2 == 0:
            x += 1
        else:
            y += 1
    answer = [x,y]
    return answer