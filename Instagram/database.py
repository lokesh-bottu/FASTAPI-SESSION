from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import snowflake.connector

mysql_db_url = "mysql+pymysql://root:50aAA50$@localhost:3306/Instagram_db"
mysql_engine = create_engine(mysql_db_url)
SessionLocal_mysql = sessionmaker(autocommit=False, autoflush=False, bind=mysql_engine)


# snf_db_url = snf_db_url = "snowflake://LokiBo:50aAA50%24@jywcqdc-vp95088.snowflakecomputing.com/INSTAGRAM_DB/INSTA?warehouse=COMPUTE_WH"
# snf_engine = create_engine(snf_db_url)
# SessionLocal_snf = sessionmaker(autocommit=False, autoflush=False, bind=snf_engine)

conn = snowflake.connector.connect(
    user='LokiBo',
    password='50aAA50$',
    account='jywcqdc-vp95088.snowflakecomputing.com',
    warehouse='COMPUTE_WH',
    database='INSTAGRAM_DB',
    schema='INSTA'
    )


def get_mysql_db():
    mysql_db = SessionLocal_mysql()
    try:
        yield mysql_db
    finally:
        mysql_db.close()


# def get_snf_db():
#     snf_db = SessionLocal_snf()
#     try:
#         yield snf_db
#     finally:
#         snf_db.close()
    