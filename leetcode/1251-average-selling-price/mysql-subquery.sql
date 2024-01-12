SELECT
  `product_id`,
  COALESCE(ROUND(SUM(`subtotal`) / SUM(`units`), 2), 0) AS `average_price`
FROM
  (
    SELECT
      p.`product_id`,
      u.`units`,
      u.`units` * p.`price` AS `subtotal`
    FROM
      `UnitsSold` u
      RIGHT JOIN `Prices` p ON u.`product_id` = p.`product_id`
      AND p.`start_date` <= u.`purchase_date`
      AND u.`purchase_date` <= p.`end_date`
  ) s
GROUP BY
  s.`product_id`
