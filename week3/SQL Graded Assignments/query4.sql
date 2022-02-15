select student_fname, student_lname from students
where roll_no in (select roll_no from members natural join book_issue)