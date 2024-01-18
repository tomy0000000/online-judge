SELECT
  CASE
    WHEN mod(`id`, 2) = 0 THEN `id` -1
    WHEN mod(`id`, 2) = 1
    AND `id` + 1 not in(
      SELECT
        `id`
      FROM
        seat
    ) THEN `id`
    ELSE `id` + 1
  END AS `id`,
  `student`
FROM
  `seat`
ORDER BY
  `id`
