from functools import wraps
from flask import abort
from flask_login import current_user

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Check if the user is authenticated and is an admin
        if not current_user.is_authenticated or not current_user.is_admin():
            abort(403)  # Forbidden access
        return f(*args, **kwargs)
    return decorated_function