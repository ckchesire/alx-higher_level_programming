# Python and MySQL Guide

## 1. Connect to a MySQL Database
Use the `mysql-connector-python` library:

```python
import mysql.connector

connection = mysql.connector.connect(
    host="your_host",
    user="your_username",
    password="your_password",
    database="your_database"
)

if connection.is_connected():
    print("Connected to MySQL database")
connection.close()
```
Install the library:
```bash
pip install mysql-connector-python
```

---

## 2. SELECT Rows from a MySQL Table
Retrieve rows using a query:

```python
cursor = connection.cursor()
cursor.execute("SELECT * FROM your_table")

for row in cursor.fetchall():
    print(row)

cursor.close()
connection.close()
```

---

## 3. INSERT Rows into a MySQL Table
Add rows using an SQL query:

```python
query = "INSERT INTO your_table (column1, column2) VALUES (%s, %s)"
cursor.execute(query, ("value1", "value2"))
connection.commit()
print(f"{cursor.rowcount} record inserted.")

cursor.close()
connection.close()
```

---

## 4. What is ORM?
**Object-Relational Mapping (ORM)** allows database interaction using objects. Popular Python ORMs include:
- **SQLAlchemy**
- **Django ORM**

---

## 5. Map a Python Class to a MySQL Table
Use SQLAlchemy:

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(100))

engine = create_engine("mysql+pymysql://username:password@localhost/your_database")
Base.metadata.create_all(engine)
```

---

## 6. Create a Python Virtual Environment
1. **Create**:
   ```bash
   python -m venv myenv
   ```
2. **Activate**:
   - Windows: `myenv\Scripts\activate`
   - macOS/Linux: `source myenv/bin/activate`
3. **Deactivate**:
   ```bash
   deactivate
   ```

