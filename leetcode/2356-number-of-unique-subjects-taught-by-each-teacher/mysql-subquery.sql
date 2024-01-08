SELECT
  `teacher_id`,
  COUNT(*) AS `cnt`
FROM
  (
    SELECT
      *
    FROM
      `Teacher`
    GROUP BY
      `teacher_id`,
      `subject_id`
  ) c
GROUP BY
  `teacher_id`
