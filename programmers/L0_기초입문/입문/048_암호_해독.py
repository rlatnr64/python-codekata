# 암호 해독
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120892
# 알고리즘: 기초
# 작성자: 김수인
# 작성일: 2026. 04. 03. 11:38:23

def solution(cipher, code):
    return cipher[code-1::code]