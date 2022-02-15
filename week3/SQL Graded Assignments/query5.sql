select title,count(title) from book_copies as bcs, book_catalogue as bc where 
bcs.ISBN_no = bc.ISBN_no and title like '%Database%' group by title