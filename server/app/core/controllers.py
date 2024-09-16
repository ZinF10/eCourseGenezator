from flask_login import login_user
from flask import request, flash, redirect, url_for

from .dao import auth_user


def auth_admin():
    email = request.form.get('email')
    password = request.form.get('password')
    user = auth_user(email=email, password=password)

    if user and user.is_admin:
        flash(f"Welcome to {user.username} comeback!", category="success")
        login_user(user=user)
        return redirect(url_for('admin.index'))

    flash("Invalid email or password. Please try again.", category="warning")
    return redirect(url_for('admin.index'))