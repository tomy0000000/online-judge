SELECT
  `project_id`,
  ROUND(SUM(`experience_years`) / COUNT(`employee_id`), 2) AS `average_years`
FROM
  `Project`
  JOIN `Employee` USING (`employee_id`)
WHERE
  `experience_years` IS NOT NULL
GROUP BY
  `project_id`
