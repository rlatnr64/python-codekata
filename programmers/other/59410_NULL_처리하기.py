# NULL 처리하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59410
# 작성자: 김수인
# 작성일: 2026. 11. 26. 16:02:45

SELECT 
    ANIMAL_TYPE, 
    CASE WHEN NAME IS NULL THEN 'No name' ELSE NAME END, 
    SEX_UPON_INTAKE
FROM ANIMAL_INS
