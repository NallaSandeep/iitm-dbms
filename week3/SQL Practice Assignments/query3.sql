select count(*) from book_catalogue as bc, book_copies as bcs, book_issue as bi
where bc.ISBN_no=bcs.ISBN_no and bcs.accession_no=bi.accession_no and
bi.doi='2021-08-11'