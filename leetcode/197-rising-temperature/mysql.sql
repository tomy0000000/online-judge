SELECT
  w1.`id` AS `Id`
FROM
  `Weather` w1
  INNER JOIN `Weather` w2 ON DATE_SUB(w1.`recordDate`, INTERVAL 1 DAY) = w2.`recordDate`
WHERE
  w1.`temperature` > w2.`temperature`
