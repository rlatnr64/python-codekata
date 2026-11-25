# 상위 n개 레코드
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59405
# 작성자: 김수인
# 작성일: 2026. 11. 25. 19:22:50

SELECT NAME
FROM ANIMAL_INS
WHERE DATETIME = (SELECT MIN(DATETIME) FROM ANIMAL_INS)
ORDER BY NAME
LIMIT 1;