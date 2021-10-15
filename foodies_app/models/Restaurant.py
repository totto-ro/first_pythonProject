from foodies_app.config.MySQLConnection import connectToMySQL
from flask import flash

class Restaurant:
    def __init__( self, data ):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.reason = data['reason']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.first_name = data ['first_name']
        self.fav_restaurants = []


        

    # @classmethod
    # def get_all( cls ):
    #     query = "SELECT* FROM restaurants LEFT JOIN users ON users.id = restaurants.user_id;"
    #     results =  connectToMySQL('foodies_db').query_db(query)
    #     all_trees = []
    #     for row in results:
    #         print(row['first_name'], row['last_name'])
    #         all_trees.append( cls(row) )
    #     return all_trees


    @classmethod
    def save( cls, data ):
        query = "INSERT INTO restaurants(name, location, reason, user_id) VALUES(%(name)s, %(location)s, %(reason)s, %(user_id)s);"
        results = connectToMySQL( 'foodies_db' ).query_db( query, data )
        print( results )
        return results

    @staticmethod
    def validation_restaurant( restaurant ):
        is_valid = True
        if len(restaurant['name']) < 3:
            is_valid = False
            flash("Name must be at least 3 characters","restaurant")
        if len(restaurant['location']) < 2:
            is_valid = False
            flash("Location must be at least 2 characters","restaurant")
        if len(restaurant['reason']) >= 50:
            is_valid = False
            flash("Reason can't surpass 50 characters","restaurant")
        return is_valid

    @classmethod
    def allRestaurants_by_userID( cls, data ):
        query = "SELECT* FROM restaurants LEFT JOIN users ON users.id = restaurants.user_id WHERE restaurants.id NOT IN  ( SELECT restaurants.id FROM restaurants WHERE restaurants.user_id = %(id)s ) GROUP BY users.id ORDER BY restaurants.created_at;"
        results = connectToMySQL( 'foodies_db' ).query_db( query, data )
        restaurants = []
        for row in results:
            restaurants.append( cls(row) )
        return restaurants

    @classmethod
    def get_fav_list( cls, data ):
        query = "SELECT* FROM restaurants LEFT JOIN favorites ON restaurants.id = favorites.restaurant_id LEFT JOIN users ON users.id = favorites.user_id  WHERE users.id = %(id)s;"
        results = connectToMySQL( 'foodies_db' ).query_db( query, data )
        print (results, "helloooo")
        restaurant = cls(results[0])
        print (restaurant, "pointttttttingHereeeeeeeeeeeeeeeee")

        for row in results:
            if row['users.id'] == None:
                break
            data = {
                "id": row['id'],
                "first_name": row['first_name'],
                "last_name" : row['last_name'],
                "email": row['email'],
                "password" : row['password'],
                "created_at" : row['created_at'],
                "updated_at" : row['updated_at']
            }

        restaurant.fav_restaurants.append( Restaurant( data ) )
        print ("herrreeeeeeeeeeeeeeeeeee")  
        return restaurant
    

    






    # @classmethod
    # def allRestaurants_by_userID( cls, data ):
    #     query = "SELECT * FROM restaurants WHERE user_id = %(id)s;"
    #     results = connectToMySQL( 'foodies_db' ).query_db( query, data )
    #     print(results)
    #     restaurants = []
    #     for row in results:
    #         restaurants.append( cls(row) )
    #     return restaurants

    # @classmethod
    # def get_userID( cls,data ):
    #     query = "SELECT * FROM restaurants WHERE restaurants.id = %(id)s;"
    #     results = connectToMySQL( 'foodies_db' ).query_db(query,data)
    #     print(results)
    #     return cls( results[0] )

    # @classmethod
    # def update( cls, data ):
    #     query = "UPDATE restaurants SET name=%(name)s, location=%(location)s, reason=%(reason)s, updated_at=NOW() WHERE id = %(id)s;"
    #     return connectToMySQL( 'foodies_db' ).query_db( query,data )

    # @classmethod
    # def destroy( cls, data ):
    #     query = "DELETE FROM restaurants WHERE restaurants.id = %(id)s;"
    #     return connectToMySQL( 'foodies_db' ).query_db( query,data )
        

    