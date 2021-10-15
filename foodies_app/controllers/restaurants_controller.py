from flask import render_template,redirect,session,request, flash
from foodies_app import app
from foodies_app.models.Restaurant import Restaurant
from foodies_app.models.User import User



@app.route('/new/restaurant', methods=['GET'])
def new_restaurant():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    user = User.get_by_id(data)
    return render_template('new_restaurant.html', user=user)

@app.route( '/create/restaurant', methods=['POST'] )
def save_restaurant():
    if 'user_id' not in session:
        return redirect( '/logout' )

    if not Restaurant.validation_restaurant( request.form ):
        return redirect( '/new/restaurant' )

    data = {
        "name": request.form["name"],
        "location": request.form["location"],
        "reason": request.form["reason"],
        "user_id": session["user_id"]
    }

    results = Restaurant.save( data )
    print( results )
    return redirect( '/new/restaurant' )

@app.route('/dashboard', methods=['GET'])
def getrestaurants():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id'],
    }
    user = User.get_by_id(data)

    restaurant = Restaurant.allRestaurants_by_userID(data)
    
    #fav_restaurant=Restaurant.get_fav_list(data)
    #print(fav_restaurant, "nnnnnooooooooooooooooo")

    return render_template('dashboard.html', user=user, restaurant=restaurant)#, fav_restaurant=fav_restaurant)










# @app.route('/account', methods=['GET'])
# def show_account():
#     if 'user_id' not in session:
#         return redirect('/logout')
#     data = {
#         "id":session['user_id'],
#     }
#     user = User.get_by_id(data)
#     restaurant = Restaurant.allRestaurants_by_userID(data)
#     print(Restaurant)
#     return render_template('account.html', user=user, restaurant=restaurant)


# @app.route('/edit/<int:id>', methods=['GET'] )
# def edit_restaurant(id):
#     if 'user_id' not in session:
#         return redirect('/logout')
#     user_data = {
#         "id":session['user_id']
#     }

#     data = {
#         "id":id
#     }
#     user = User.get_by_id(user_data)

#     edit_restaurant = Restaurant.get_userID(data)
#     print (edit_restaurant)
    
#     return render_template("edit.html", user=user, restaurant=edit_restaurant)


# @app.route('/update/restaurant',methods=['POST'])
# def update_restaurant():
#     if 'user_id' not in session:
#         return redirect('/logout')

#     if not Restaurant.validation_restaurant( request.form ):
#         return redirect(f"/edit/{request.form['id']}")

#     data = {
#         "name": request.form["name"],
#         "location": request.form["location"],
#         "reason": request.form["reason"],
#         "date_planted": request.form["date_planted"],
#         "id": request.form['id']
#     }
#     results = Restaurant.update( data )
#     print( results )
#     return redirect( '/dashboard' )

# @app.route('/show/<int:id>', methods=['GET'] )
# def show_restaurant(id):
#     if 'user_id' not in session:
#         return redirect('/logout')
#     user_data = {
#         "id":session['user_id']
#     }

#     data = {
#         "id":id
#     }
#     user = User.get_by_id(user_data)

#     edit_restaurant = Restaurant.get_userID(data)
#     print (edit_restaurant)
    
#     return render_template("show.html", user=user, restaurant=edit_restaurant)

# @app.route('/destroy/<int:id>', methods=['GET'] )
# def destroy(id):
#     if 'user_id' not in session:
#         return redirect('/logout')
#     user_data = {
#         "id":session['user_id']
#     }

#     data = {
#         "id":id
#     }
#     User.get_by_id(user_data)

#     Restaurant.destroy(data)
    
#     return redirect( '/account' )