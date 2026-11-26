# 경기도에 위치한 식품창고 목록 출력하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131114
# 작성자: 김수인
# 작성일: 2026. 11. 26. 16:24:52

SELECT 
    WAREHOUSE_ID,
    WAREHOUSE_NAME,
    ADDRESS,
    CASE WHEN FREEZER_YN IS NULL THEN 'N' ELSE FREEZER_YN END AS FREEZER_YN
FROM FOOD_WAREHOUSE
WHERE WAREHOUSE_NAME LIKE '%경기%'
ORDER BY WAREHOUSE_ID;