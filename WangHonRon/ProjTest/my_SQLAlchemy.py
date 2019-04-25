from sqlalchemy import Column,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

base_class = declarative_base() #创建对象的基类

# 定义windfarm类
