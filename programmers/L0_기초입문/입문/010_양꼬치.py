# 양꼬치
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120830
# 알고리즘: 기초
# 작성자: 김수인
# 작성일: 2026. 01. 20. 13:53:52

def solution(n, k):
    free_drink =  n // 10 
    pay_drink = k - free_drink
        
    n_cost = n * 12000
    k_cost = pay_drink * 2000
    
    total =  n_cost + k_cost
    return total