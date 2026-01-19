# 인기있는 아이스크림
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/133024
# 작성자: 김수인
# 작성일: 2026. 01. 19. 10:27:54

SELECT
    FLAVOR
FROM FIRST_HALF
ORDER BY TOTAL_ORDER DESC, SHIPMENT_ID ASC;