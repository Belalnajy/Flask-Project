from flask import Blueprint
from flask import render_template, redirect, url_for, flash,request
from app.auth.forms import RegisterForm, LoginForm
from app import db
from app.models import User
from flask_login import login_user, logout_user, login_required

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    error=[]
    form = RegisterForm()
    if form.validate_on_submit():
        print("Form submitted and validated!")  # Debugging
        new_user = User(username=form.username.data, email=form.email.data)
        new_user.set_password(form.password.data) 
        new_user.save_to_db()
        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('auth.login'))
    else:
        print("Form validation failed:", form.errors)  # Debugging

    return render_template('auth/register.html', form=form ,error=error)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    errors=[]
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash(f'Login successful! Welcome {user.username}', 'success')
            next_page= request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('main.book_page'))
        else:
            flash('Invalid username or password.', 'danger')

    return render_template('auth/login.html', form=form, errors=errors)


@auth.route('/logout')
@login_required
def logout():
    logout_user() 
    flash('You have been logged out.', 'success')
    return redirect(url_for('auth.login'))

@auth.route('/profile')
@login_required
def profile():
    return render_template('auth/profile.html')