import sqlalchemy
import pymysql


engine = sqlalchemy.create_engine('mysql+pymysql://root:admin@34.121.209.148')

engine.execute(sqlalchemy.schema.CreateSchema('Stock'))