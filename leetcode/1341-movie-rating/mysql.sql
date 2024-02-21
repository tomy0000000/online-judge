(
  SELECT
    `name` AS `results`
  FROM
    Users
    JOIN `MovieRating` USING (`user_id`)
  GROUP BY
    `user_id`
  ORDER BY
    COUNT(*) DESC,
    `name` ASC
  LIMIT
    1
)
UNION ALL
(
  SELECT
    `title` AS `results`
  FROM
    `MovieRating`
    JOIN `Movies` USING (`movie_id`)
  WHERE
    YEAR(`created_at`) = 2020
    AND MONTH(`created_at`) = 2
  GROUP BY
    `movie_id`
  ORDER BY
    AVG(`rating`) DESC,
    `title` ASC
  LIMIT
    1
)
