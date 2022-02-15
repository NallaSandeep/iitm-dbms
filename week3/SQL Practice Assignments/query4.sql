select faculty_fname,faculty_lname from faculty
except
select faculty_fname,faculty_lname from faculty,members
where faculty.id=members.id and 
members.member_no in (select member_no from book_issue)