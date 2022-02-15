select m.match_num,r.name from matches as m,match_referees as mr, referees as r
where m.match_date='2020-05-11' and m.match_num=mr.match_num
and mr.referee=r.referee_id