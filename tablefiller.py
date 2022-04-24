# pip install mysql-connector-python
import mysql.connector
import random


mydb = mysql.connector.connect(
    host='localhost', user='root', password='yourpasword', database='yourdatabase')
mycursor = mydb.cursor()

customersl = {'ali': 1, 'reza': 2, 'mohamad': 3, 'dariush': 4, 'hasn': 5, 'mohsen': 6, 'zahra': 7, 'sara': 8, 'masoud': 9, 'sami': 10, 'maryam': 11,
              'rayan': 12, 'jamshid': 21, 'mostafa': 13, 'kamran': 14, 'sadegh': 15, 'shayan': 16, 'pari': 17, 'parham': 18, 'masih': 19, 'nahid': 20}

mahsooll = {'guitar': 2500, 'cd': 5, 'mesvak': 9, 'ketab': 45, 'sim': 90, 'daftar': 20,
            'medad': 2, 'A4': 60, 'airbud': 300, 'iphone13': 40000, 'asus': 26000, 'havij': 1, 'sib': 3, 'hulu': 8, 'karafs': 4}

n = 0
while n != 50:
    custid = int(random.choice([v for k, v in customersl.items()]))
    custnam = [k for k, v in customersl.items() if v == custid]
    custname = custnam[0]
    gheimat = int(random.choice([v for k, v in mahsooll.items()]))
    mahsoo = [k for k, v in mahsooll.items() if v == gheimat]
    mahsool = mahsoo[0]
    val = (custname, mahsool, str(gheimat), str(custid))
    sql = "insert into pytamrin (customers,mahsool,gheimat,customersID) values (%s,%s,%s,%s)"
    mycursor.execute(sql, val)
    mydb.commit()
    n += 1
