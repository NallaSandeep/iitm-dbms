select name from teams
except 
select name from teams where team_id in 
(select team_id from players where jersey_no=74)