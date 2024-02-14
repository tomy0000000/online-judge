SELECT
  `student_id`,
  `student_name`,
  `subject_name`,
  COUNT(e.`subject_name`) AS `attended_exams`
FROM
  `Students` st
  CROSS JOIN `Subjects` sj
  LEFT JOIN `Examinations` e USING (`student_id`, `subject_name`)
GROUP BY
  `student_id`,
  `subject_name`
ORDER BY
  `student_id`,
  `subject_name`
