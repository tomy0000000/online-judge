SELECT
  IF(COUNT(e.`salary`) = 1, NULL, MIN(e.`salary`)) AS `SecondHighestSalary`
FROM
  (
    SELECT
      `salary`
    FROM
      `Employee`
    GROUP BY
      `salary`
    ORDER BY
      `salary` DESC
    LIMIT
      2
  ) e
