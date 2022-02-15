select bc.title from book_catalogue as bc, book_copies as bcs, book_issue as bi, members as m
where bc.ISBN_no=bcs.ISBN_no and bcs.accession_no=bi.accession_no and 
m.member_no=bi.member_no and m.member_type='PG'
except
select distinct bc.title from book_catalogue as bc, book_copies as bcs, book_issue as bi, members as m
where bc.ISBN_no=bcs.ISBN_no and bcs.accession_no=bi.accession_no and 
m.member_no=bi.member_no and m.member_type='UG'
