from fastapi import FastAPI,Depends
from Schemas.schemas import User
from Models.models import UserModel
from database import get_mysql_db,get_snf_db,conn
from sqlalchemy.orm import Session
import uvicorn
app = FastAPI()

@app.get('/')
def home():
    sql = 'select * from USERS'
    cursor = conn.cursor()
    df = cursor.execute(sql)
    return df


@app.post('/adduser')
def add_user(req:User,mysql_db:Session = Depends(get_mysql_db)):
    mysql_user = mysql_db.query(UserModel).filter(UserModel.Email == req.Email).first()
    if not mysql_user:
        newUser = UserModel(Name= req.Name,Email = req.Email,Location = req.Location,Company= req.Company)
        mysql_db.add(newUser)
        mysql_db.commit()
        return 'Added'


    return "User already Exists"
