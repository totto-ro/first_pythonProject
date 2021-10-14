from flask import Flask
from foodies_app import app
from foodies_app.controllers import users_controller, restaurants_controller

if __name__ == "__main__":
    app.run( debug = True )