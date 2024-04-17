SELECT
  `x`,
  `y`,
  `z`,
  IF(
    GREATEST(`x`, `y`, `z`) < (`x` + `y` + `z`) / 2,
    "Yes",
    "No"
  ) AS `triangle`
FROM
  `Triangle`
