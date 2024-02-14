SELECT
  `student_id`,
  `student_name`,
  `subject_name`,
  COALESCE(`attended_exams`, 0) AS `attended_exams`
FROM
  `Students` st
  CROSS JOIN `Subjects` sj
  LEFT JOIN (
    SELECT
      *,
      COUNT(*) AS `attended_exams`
    FROM
      `Examinations`
    GROUP BY
      `student_id`,
      `subject_name`
  ) c USING (`student_id`, `subject_name`)
ORDER BY
  `student_id`,
  `subject_name`
