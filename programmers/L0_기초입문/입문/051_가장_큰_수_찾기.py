# 가장 큰 수 찾기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120899
# 알고리즘: 기초
# 작성자: 김수인
# 작성일: 2026. 04. 07. 12:57:31

def solution(array):
    answer = []
    
    a = max(array)
    b = array.index(max(array))
    answer = a,b
    
    return answer