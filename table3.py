import csv
import MySQLdb
import re
import string

db = MySQLdb.connect("localhost","root","root","GenomicsProject")

cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS HUMANLIKESDOG")

# Create table as per requirement
sql = """CREATE TABLE HUMANLIKESDOG(
    ensemble_human varchar(500),
    dog_ID varchar(500),
    ensemble_dog varchar(500),
    RefSeq_ID varchar(500))"""
cursor.execute(sql)

sql1 = "SELECT human.EnsemblgeneID, dog.EnsemblgeneID, dog.RefSeqDOG, human.RefSeqmRNAID FROM human human INNER JOIN dog dog ON dog.RefSeqDog = human.EnsemblgeneID"
cursor.execute(sql1)
rows= cursor.fetchall()

for row in rows:
    q = 'insert into HUMANLIKESDOG(ensemble_human, dog_id, ensemble_dog, RefSeq_ID) values ("%s", "%s","%s", "%s")' % (row[0], row[1], row[2], row[3])
    print(q)
    cursor.execute(q)

# Commit your changes in the database
db.commit()
#except:
# Rollback in case there is any error
db.rollback()


