from flask import Flask
from config import Config
from models import db
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    with app.app_context():
        # Create database tables
        db.create_all()
        
        # Auto-seed admin user for remote deployment
        from models import User
        if not User.query.filter_by(username='operator_01').first():
            hashed_pw = bcrypt.generate_password_hash('AdminPassword123!').decode('utf-8')
            new_admin = User(username='operator_01', password_hash=hashed_pw, clearance_level=4)
            db.session.add(new_admin)
            db.session.commit()

    from routes.auth import auth
    from routes.vault import vault

    app.register_blueprint(auth)
    app.register_blueprint(vault)

    return app


