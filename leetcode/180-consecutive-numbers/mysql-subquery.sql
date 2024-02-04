SELECT
  l1.`num` AS `ConsecutiveNums`
FROM
  `Logs` l1
  JOIN (
    SELECT
      `id` - 1 AS `id`,
      `num`
    FROM
      `Logs`
  ) l2 USING (`id`)
  JOIN (
    SELECT
      `id` - 2 AS `id`,
      `num`
    FROM
      `Logs`
  ) l3 USING (`id`)
WHERE
  l1.`num` = l2.`num`
  AND l2.`num` = l3.`num`
GROUP BY
  l1.`num`
