from foodies_app import app
from flask import render_template,redirect,request,session,flash
from foodies_app.models.User import User
from foodies_app.models.Restaurant import Restaurant
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register',methods=['POST'])
def register():

    if not User.validate_register(request.form):
        return redirect('/')

    data ={ 
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    userID = User.save(data)
    session['user_id'] = userID

    return redirect('/dashboard')

@app.route('/login',methods=['POST'])
def login():
    user = User.get_by_email(request.form)

    if not user:
        flash("Invalid Email","login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Password","login")
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/dashboard')

@app.route('/dashboard2')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    user=User.get_by_id(data)

    #fav_restaurant=Restaurant.get_fav_list(data)
    
    return render_template("dashboard.html", user=user)#, fav_restaurant=fav_restaurant)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


@app.route('/account', methods=['GET'])
def show_account():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id'],
    }
    user = User.get_info_by_id(data)

    return render_template('account.html', user=user)



@app.route('/edit',methods=['GET'])
def editAccount():

    if 'user_id' not in session:
        return redirect('/logout')
    user_data = {
        "id":session['user_id']
    }

    user = User.get_by_id(user_data)

    data ={ 
        "id":id
    }

    edit_user = User.get_info_by_id(data)
    print(edit_user, "heeeeeerrrrrrreeeeeeeee")

    return render_template("edit_account.html", user=user, edit_user=edit_user)



@app.route('/update/account',methods=['POST'])
def update_restaurant():
    if 'user_id' not in session:
        return redirect('/logout')

    if not User.validate_register( request.form ):
        return redirect(f"/edit/{request.form['id']}")

    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password']),
        "id": request.form['id']
    }
    results = User.update( data )
    print( results )
    return redirect( '/account' )