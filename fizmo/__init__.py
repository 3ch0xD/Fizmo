from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_login import LoginManager
import os

# Initialize extensions
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    # App Declaration
    app = Flask(__name__, static_folder='static')
    
    # Use /tmp directory for instance path
    app.instance_path = '/tmp'
    
    app.config.from_object(Config)
    
    # Initialize extensions with the app
    db.init_app(app)
    login_manager.init_app(app)

    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path, exist_ok=True)
    except OSError as e:
        app.logger.error(f"Failed to create instance path: {e}")

    # Correctly calculate the path to the static directory

    # Add Whitenoise middleware
    
    # Import blueprints locally to avoid circular imports
    from .auth import auth as auth_blueprint
    from .views import views as views_blueprint

    # Register blueprints
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(views_blueprint)

    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        from .models import User
        return User.query.get(int(user_id))

    # Error Pages
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('/errors/404.html', style="sign_up.css"), 404

    return app
