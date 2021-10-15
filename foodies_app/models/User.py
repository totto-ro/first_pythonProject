from flask import flash
from foodies_app.config.MySQLConnection import connectToMySQL
import re
from foodies_app.models import Restaurant


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        #self.fav_restaurants = []

    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name,last_name,email,password) VALUES(%(first_name)s,%(last_name)s,%(email)s,%(password)s)"
        return connectToMySQL( 'foodies_db' ).query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL( 'foodies_db' ).query_db(query)
        users = []
        for row in results:
            users.append( cls(row))
        return users

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL( 'foodies_db' ).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL( 'foodies_db' ).query_db(query,data)
        return cls(results[0])

    @staticmethod
    def validate_register(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL( 'foodies_db' ).query_db(query,user)
        if len(results) >= 1:
            flash("Email already taken.","register")
            is_valid=False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address!","register")
            is_valid=False
        if len(user['first_name']) < 2:
            flash("First name must be at least 2 characters","register")
            is_valid= False
        if len(user['last_name']) < 2:
            flash("Last name must be at least 2 characters","register")
            is_valid= False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters","register")
            is_valid= False
        if user['password'] != user['confirm']:
            flash("Passwords don't match","register")
        return is_valid

    @staticmethod
    def validate_login( user ):
        is_valid = True
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!", "login")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters.", "login")
            is_valid = False
        return is_valid

    # @classmethod
    # def get_fav_list( cls, data ):
    #     query = "SELECT* FROM users LEFT JOIN favorites ON users.id = favorites.user_id LEFT JOIN restaurants ON restaurants.id = favorites.restaurant_id  WHERE users.id = %(id)s;"
    #     results = connectToMySQL( 'foodies_db' ).query_db( query, data )
    #     print (results, "helloooo")
    #     user = cls(results[0])
    #     for row in results:
    #         if row['restaurants.id'] == None:
    #             break
    #         data = {
    #             "id": row['restaurants.id'],
    #             "name": row['name'],
    #             "location": row['location'],
    #             "reason": row['reason'],
    #             "created_at": row['restaurants.created_at'],
    #             "updated_at": row['restaurants.updated_at'],
    #             "user_id": row['user_id']
    #         }
    #     user.fav_restaurants.append( Restaurant.Restaurant( data ) )
    #     print (user, "hellooo")  
    #     return user


    @classmethod
    def get_info_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL( 'foodies_db' ).query_db(query,data)
        users = []
        print(results, "pointinnnnnnnnnnnnng")
        for row in results:
            users.append( cls(row))
        return users


    @classmethod
    def update( cls, data ):
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, password=%(password)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL( 'foodies_db' ).query_db( query,data )