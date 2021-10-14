from foodies_app.config.MySQLConnection import connectToMySQL
from flask import flash

class Restaurant:
    def __init__( self, data ):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.reason = data['reason']
        self.date_planted = data['date_planted']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        

    @classmethod
    def get_all( cls ):
        query = "SELECT* FROM trees LEFT JOIN users ON users.id = trees.user_id;"
        results =  connectToMySQL('arbortrary_db').query_db(query)
        all_trees = []
        for row in results:
            print(row['first_name'], row['last_name'])
            all_trees.append( cls(row) )
        return all_trees


    @classmethod
    def save( cls, data ):
        query = "INSERT INTO trees(name, location, reason, date_planted, user_id) VALUES(%(name)s, %(location)s, %(reason)s, %(date_planted)s, %(user_id)s);"
        results = connectToMySQL( 'arbortrary_db' ).query_db( query, data )
        print( results )
        return results

    @staticmethod
    def validation_tree( tree ):
        is_valid = True
        if len(tree['name']) < 5:
            is_valid = False
            flash("Name must be at least 5 characters","tree")
        if len(tree['location']) < 2:
            is_valid = False
            flash("Location must be at least 2 characters","tree")
        if len(tree['reason']) >= 50:
            is_valid = False
            flash("Reason can't surpass 50 characters","tree")
        if tree['date_planted'] == "":
            is_valid = False
            flash("You most enter a date","tree")
        return is_valid

    @classmethod
    def allTrees_by_userID( cls, data ):
        query = "SELECT * FROM trees WHERE user_id = %(id)s;"
        results = connectToMySQL( 'arbortrary_db' ).query_db( query, data )
        print(results)
        trees = []
        for row in results:
            trees.append( cls(row) )
        return trees

    @classmethod
    def get_userID( cls,data ):
        query = "SELECT * FROM trees WHERE trees.id = %(id)s;"
        results = connectToMySQL( 'arbortrary_db' ).query_db(query,data)
        print(results)
        return cls( results[0] )

    @classmethod
    def update( cls, data ):
        query = "UPDATE trees SET name=%(name)s, location=%(location)s, reason=%(reason)s, date_planted=%(date_planted)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL( 'arbortrary_db' ).query_db( query,data )

    @classmethod
    def destroy( cls, data ):
        query = "DELETE FROM trees WHERE trees.id = %(id)s;"
        return connectToMySQL( 'arbortrary_db' ).query_db( query,data )
        

    