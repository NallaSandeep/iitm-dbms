select faculty_fname,faculty_lname from faculty AS f,departments as d where f.department_code=d.department_code AND d.department_name='Computer Science'