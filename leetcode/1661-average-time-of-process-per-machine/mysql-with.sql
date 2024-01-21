WITH
  a2 AS (
    SELECT
      `machine_id`,
      SUM(`timestamp`) AS 'end'
    FROM
      `Activity`
    WHERE
      `activity_type` = 'end'
    GROUP BY
      `machine_id`
  )
SELECT
  `machine_id`,
  ROUND((a2.`end` - SUM(`timestamp`)) / COUNT(*), 3) AS `processing_time`
FROM
  `Activity`
  JOIN a2 USING (`machine_id`)
WHERE
  `activity_type` = 'start'
GROUP BY
  `machine_id`
