from flask import render_template,redirect,session,request, flash
from foodies_app import app
#from foodies_app.models import 
from foodies_app.models.User import User






# @app.route('/new/tree', methods=['GET'])
# def new_tree():
#     if 'user_id' not in session:
#         return redirect('/logout')
#     data = {
#         "id":session['user_id']
#     }
#     user = User.get_by_id(data)
#     return render_template('new_tree.html', user=user)

# @app.route( '/create/tree', methods=['POST'] )
# def save_tree():
#     if 'user_id' not in session:
#         return redirect( '/logout' )

#     if not Tree.validation_tree( request.form ):
#         return redirect( '/new/tree' )

#     data = {
#         "name": request.form["name"],
#         "location": request.form["location"],
#         "reason": request.form["reason"],
#         "date_planted": request.form["date_planted"],
#         "user_id": session["user_id"]
#     }

#     results = Tree.save( data )
#     print( results )
#     return redirect( '/new/tree' )


# @app.route('/account', methods=['GET'])
# def show_account():
#     if 'user_id' not in session:
#         return redirect('/logout')
#     data = {
#         "id":session['user_id'],
#     }
#     user = User.get_by_id(data)
#     tree = Tree.allTrees_by_userID(data)
#     print(tree)
#     return render_template('account.html', user=user, tree=tree)


# @app.route('/edit/<int:id>', methods=['GET'] )
# def edit_tree(id):
#     if 'user_id' not in session:
#         return redirect('/logout')
#     user_data = {
#         "id":session['user_id']
#     }

#     data = {
#         "id":id
#     }
#     user = User.get_by_id(user_data)

#     edit_tree = Tree.get_userID(data)
#     print (edit_tree)
    
#     return render_template("edit.html", user=user, tree=edit_tree)


# @app.route('/update/tree',methods=['POST'])
# def update_tree():
#     if 'user_id' not in session:
#         return redirect('/logout')

#     if not Tree.validation_tree( request.form ):
#         return redirect(f"/edit/{request.form['id']}")

#     data = {
#         "name": request.form["name"],
#         "location": request.form["location"],
#         "reason": request.form["reason"],
#         "date_planted": request.form["date_planted"],
#         "id": request.form['id']
#     }
#     results = Tree.update( data )
#     print( results )
#     return redirect( '/dashboard' )

# @app.route('/show/<int:id>', methods=['GET'] )
# def show_tree(id):
#     if 'user_id' not in session:
#         return redirect('/logout')
#     user_data = {
#         "id":session['user_id']
#     }

#     data = {
#         "id":id
#     }
#     user = User.get_by_id(user_data)

#     edit_tree = Tree.get_userID(data)
#     print (edit_tree)
    
#     return render_template("show.html", user=user, tree=edit_tree)

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

#     Tree.destroy(data)
    
#     return redirect( '/account' )