# 이름에 el이 들어가는 동물 찾기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59047
# 작성자: 김수인
# 작성일: 2026. 11. 26. 15:37:08

SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE 
    NAME LIKE '%el%' 
    AND ANIMAL_TYPE = 'Dog'
ORDER BY NAME, ANIMAL_ID;