# 어린 동물 찾기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59037
# 작성자: 김수인
# 작성일: 2026. 11. 25. 19:47:15

SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE NOT INTAKE_CONDITION = 'Aged'