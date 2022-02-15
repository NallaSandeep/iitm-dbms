select distinct faculty_fname,faculty_lname from faculty,members,book_issue
where faculty.department_code='ME' and 
faculty.id=members.id and 
members.member_no=book_issue.member_no