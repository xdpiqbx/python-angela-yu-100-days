from pathlib import PurePath
from flask import render_template, request, send_from_directory, redirect, url_for, flash
from auth.DTO import UserDTO
from auth.repositories import auth_repo
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash


def home():
    return render_template("index.html")


def register():
    if request.method == 'POST':
        user = auth_repo.register(
            UserDTO(
                name=request.form['name'],
                email=request.form['email'],
                password=request.form['password'],
            )
        )
        if not user:
            flash("You already signed up. Try to log in.")
            return redirect(url_for('auth.register'))
        login_user(user)
        return render_template("secrets.html")
    return render_template("register.html")


def login():
    if request.method == 'POST':
        user = auth_repo.get_user(
            email=request.form['email']
        )
        if not user:
            flash("That email does not exists, please try again.")
            return redirect(url_for('auth.login'))
        if check_password_hash(user.password, request.form['password']):
            login_user(user)
            return redirect(url_for('auth.secrets'))
        else:
            flash("Password incorrect, please try again.")
            return redirect(url_for('auth.login'))
    return render_template("login.html")


def secrets():
    return render_template("secrets.html")


def logout():
    logout_user()
    return redirect(url_for('auth.home'))


def download():
    return send_from_directory(
        PurePath('auth', 'static', 'files'),
        'cheat_sheet.pdf',
        as_attachment=True
    )
