SELECT
  e.`employee_id`
FROM
  (
    SELECT
      `employee_id`,
      `manager_id`
    FROM
      `Employees`
    WHERE
      `salary` < 30000
      AND `manager_id` IS NOT NULL
  ) e
  LEFT JOIN `Employees` m ON e.`manager_id` = m.`employee_id`
WHERE
  m.`employee_id` IS NULL
ORDER BY
  e.`employee_id` ASC
