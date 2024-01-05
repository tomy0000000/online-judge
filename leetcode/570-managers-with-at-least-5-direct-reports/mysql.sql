SELECT
  E2.`name`
FROM
  `Employee` AS E1
  JOIN `Employee` AS E2 ON E1.`managerId` = E2.`id`
GROUP BY
  E1.`managerId`
HAVING
  COUNT(*) >= 5
