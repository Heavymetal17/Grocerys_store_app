from app import app, db
from app.forms import RegistrationForm, LoginForm
from app.models import User
from app.helpers import hash_password, verify_password
from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = hash_password(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password=hashed_password, role_id=2)  # Regular user role ID is 2
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully. You can now login.', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html', title='Sign Up', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and verify_password(form.password.data, user.password):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('dashboard'))  # Replace 'dashboard' with the desired route
        else:
            flash('Login unsuccessful. Please check your email and password.', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
