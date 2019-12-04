from findARestaurant import findARestaurant
from models import Base, Restaurant
from flask import Flask, jsonify, request
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)




#foursquare_client_id = ''

#foursquare_client_secret = ''

#google_api_key = ''

engine = create_engine('sqlite:///restaurants.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
app = Flask(__name__)

@app.route('/restaurants', methods = ['GET', 'POST'])
def all_restaurants_handler():
  if request.method == 'GET':
    return getAllRestaurants()
  elif request.method == 'POST':
    restaurant_name = request.args.get('restaurant_name', '')
    restaurant_address = request.args.get('restaurant_address', '')
    restaurant_image = request.args.get('restaurant_image', '')
    return addANewRestaurant(restaurant_name, restaurant_address, restaurant_image)

@app.route('/restaurants/<int:id>', methods = ['GET','PUT', 'DELETE'])
def restaurant_handler(id):
    if request.method == 'GET':
        return getRestaurant(id)
    elif request.method == 'PUT':
        restaurant_name = request.args.get('restaurant_name', '')
        restaurant_address = request.args.get('restaurant_address', '')
        restaurant_image = request.args.get('restaurant_image', '')
        return updateRestaurant(id, restaurant_name, restaurant_address. restaurant_image)
    elif request.method == 'DELETE'
        return deleteRestaurant(id)

def getAllRestaurants():
    restaurants = session.query(Restaurant).all()
    return jsonify(Restaurant=[i.serialize for i in restaurants])

def addANewRestaurant(restaurant_name, restaurant_address, restaurant_image):
    restaurant = Restaurant(restaurant_name = restaurant_name, restaurant_address = restaurant_address, restaurant_image = restaurant_image)
    session.add(restaurant)
    session.commit()
    return jsonify(Restaurant=restaurant.serialize)

def getRestaurant(id):
    restaurant = session.query(Restaurant).filter_by(id=id).one()
    return jsonify(restaurant=restaurant.serialize)

def updateRestaurant(id, restaurant_name, restaurant_address, restaurant_image):
    restaurant = session.query(Restaurant).filter_by(id=id).one()
    if restaurant_name:
        restaurant.restaurant_name = restaurant_name
    if restaurant_address:
        restaurant.restaurant_address = restaurant_address
    if restaurant_image:
        restaurant.restaurant_image = restaurant_image
    session.add(restaurant)
    session.commit()
    return "Updated a Restaurant with an id %s" % id        

def deleteRestaurant(id):
    restaurant = session.query(Restaurant).filter_by(id=id).one()
    session.delete(restaurant)
    session.commit()
    return "Removed a Restaurant with an id %s" % id

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
  
GET | 302 | 257 ms | GitHub.com
GET | 200 | 233 ms