# -*- coding: utf-8 -*-
from sqlalchemy import Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine





Base = declarative_base()
class Restaurant(Base):
  __tablename__ = 'restaurant'
  id = Column(Integer, primary_key = True)
  restaurant_name = Column(String)
  restaurant_address = Column(String)
  restaurant_image = Column(String)
  
  
  
  @property
  def serialize(self):
    return {
      'restaurant_name': self.restaurant_name,
      'restaurant_address': self.restaurant_address,
      'restaurant_image' : self.restaurant_image,
      'id' : self.id
      
      }

engine = create_engine('sqlite:///restaurants.db')
 

Base.metadata.create_all(engine)
GET | 302 | 255 ms | GitHub.com
GET | 200 | 216 ms