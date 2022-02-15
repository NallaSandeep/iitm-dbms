import os
import sys
import psycopg2
import math

f = open('parameter.txt')
a = f.read()
# print(a)
# os.environ['PGUSER'] = "postgres"
# os.environ['PGPASSWORD'] = "S@ndeep056"
# os.environ['PGHOST'] = "localhost"
# os.environ['PGPORT'] = "5432"
database = sys.argv[1]  # name of the database is obtained from the command line argument
user = os.environ.get('PGUSER')
password = os.environ.get('PGPASSWORD')
host = os.environ.get('PGHOST')
port = os.environ.get('PGPORT')
conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
cur = conn.cursor()
stat = '''
select sum(host_team_score) from matches 
where host_team_score > guest_team_score and 
host_team_id in (select team_id from teams where name like '{}%')
'''.format(a)
cur.execute(stat)
S = cur.fetchone()
X = S[0] * 10
X_deg = X * (math.pi/180)
c = round(math.cos(X_deg), 2)
print(c)
cur.close()
conn.close()
