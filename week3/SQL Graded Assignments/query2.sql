select p.name from players as p, teams as t
where t.team_id=p.team_id and t.name='All Stars' order by p.dob desc limit 1