# 입양 시각 구하기(2)
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59413
# 작성자: 김수인
# 작성일: 2026. 04. 10. 17:47:57

WITH RECURSIVE ETC AS (
    SELECT 0 AS HOUR
UNION ALL
    SELECT HOUR + 1 FROM ETC WHERE HOUR < 23
)
SELECT 
    E.HOUR AS HOUR,
    COUNT(A.ANIMAL_ID) AS COUNT
FROM ETC AS E
LEFT JOIN ANIMAL_OUTS AS A
    ON E.HOUR = HOUR(A.DATETIME)
GROUP BY E.HOUR
ORDER BY HOUR ASC;

-- 모든 시간의 값이 없어서 추가해서 0을 채워 넣어야한다는것 -> CTE를 해야한다는 것
