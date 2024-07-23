from flask import Flask, Blueprint, render_template, abort, flash, redirect, url_for, request
from flask_login import login_required, login_user, logout_user, current_user
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash


auth = Blueprint("auth", __name__)

@auth.route("/")
def landing_page():
    if current_user.is_authenticated:
        return redirect(url_for('views.home'))
    return render_template('/auth/landing_page.html')

@auth.route("/login/", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('views.home'))
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                flash('Logged In Sucessfully!', category='success')
                return redirect(url_for('views.home'))
            else:
                flash('Password is incorrect, try again.', category='danger')
        else:
            flash('A user by that email doesnot exist, please sign up', category='danger')
    return render_template('/auth/login.html', style='login.css')

@auth.route("/sign-up/", methods=['GET', 'POST'])
def sign_up():
    if current_user.is_authenticated:
        return redirect(url_for('views.home'))
    if request.method == 'POST':
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")
        password_c = request.form.get("password_c")

        user = User.query.filter_by(email=email).first()

        if user:
            flash("user with that email already exists!", category='danger')
        if len(email) < 3:
            flash("Invalid Email!", category='danger')
        elif len(username) < 4:
            flash("Username must be greater than 4 characters!", category='danger')
        elif password != password_c:
            flash("Passwords donot match!", category='danger')
        elif len(password) < 5:
            flash("Insecure password!", category='danger')
        else:
            flash("Account Was Created Successfully!", category="success")
            new_user = User(first_name=first_name, last_name=last_name, email=email, username=username, password=generate_password_hash(password))
            from . import db
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('auth.login'))
    return render_template('/auth/sign_up.html', style='sign_up.css')

@auth.route("/logout/")
def logout():
    flash("Successfully Logged Out!", category='success')
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route("/forgot-password", methods=['GET', 'POST'])
def forgot_password():
    return render_template('/auth/forgot_password.html')

@auth.route("/forgot-password/<token>", methods=['GET', 'POST'])
def reset_password():
    return render_template('/auth/set_new_password.html')
