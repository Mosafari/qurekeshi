# pip install mysql-connector-python
import mysql.connector
import random

lsk = {}  # list sherkat konandegan -> {'idshakhs' : ('esm','shans')}


def shans(record):
    # +1 baraie shans bishtar va ger be samt bala
    shansq = (int(record[0])+1)//2
    lsk[record[2]] = (record[1], shansq)
    return lsk


mydb = mysql.connector.connect(
    host='localhost', user='root', password='yourpasword', database='yourdatabase')
mycursor = mydb.cursor()
# DB baiad customers(for names) and customerID columns dashte bashe

mycursor.execute("SELECT COUNT(customers),customers,customersID AS TKS FROM pytamrin group \
    by customers order by count(customers) DESC")  # TKS -> tedad kharid shakhs
myresult = mycursor.fetchall()
# qur e keshi ba shart hadghal kharid 2 bar va zarib n//2 baraie kharid bishtar az 2bar + 1 shans bra kharid aval
listqure = {}

for i in range(len(myresult)):
    listqure.update(shans(myresult[i]))
lras = []  # list random afrad be tedad shans

for v in listqure.values():
    for i in range(v[1]):
        lras.insert(random.choice([i
                    for i in range(len(lras)+1)]), v[0])


print(listqure, len(listqure))
print('_'*50)
print(lras, len(lras))
barande = random.choice(lras)
for k, v in listqure.items():
    if v[0] == barande:
        idbarande = k
print('Barande --> {} ba id {}'.format(barande, idbarande))
