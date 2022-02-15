select aggr.name from (
SELECT * FROM teams, matches where team_id=host_team_id
union
SELECT * FROM teams, matches where team_id=guest_team_id) as aggr group by aggr.name
having count(*)>3