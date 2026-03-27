from app import create_app
from models import db, User
from app import bcrypt
import getpass
from cryptography.fernet import Fernet

def init_db():
    app = create_app()
    with app.app_context():
        print("Creating database tables...")
        db.create_all()

        # Check if admin user exists
        admin = User.query.filter_by(username='operator_01').first()
        if not admin:
            print("No 'operator_01' found. Creating default admin account...")
            password = 'AdminPassword123!'
            hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')
            new_admin = User(username='operator_01', password_hash=hashed_pw, clearance_level=4)
            db.session.add(new_admin)
            db.session.commit()
            print("Admin account created successfully!")
        else:
            print("Admin account already exists.")

        print("\n--- Encryption Setup ---")
        print("Here is a newly generated AES encryption key for vault passwords:")
        print(Fernet.generate_key().decode('utf-8'))
        print("Ensure this matches the VAULT_ENCRYPTION_KEY in your config.py/.env")
        print("Initialization complete.")

if __name__ == '__main__':
    init_db()
