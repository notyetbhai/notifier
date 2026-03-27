import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-secret-key-please-change-in-prod'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'vault.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Session lifetime in seconds (15 minutes = 900 seconds)
    PERMANENT_SESSION_LIFETIME = 900

    # Encryption key for Vault passwords (AES). Must be securely stored in .env in production
    # Generated via cryptography.fernet.Fernet.generate_key()
    VAULT_ENCRYPTION_KEY = os.environ.get('VAULT_ENCRYPTION_KEY') or b'2P628X_KjTbz03y90R8XqM_2k62Tbx_4tPqM0T9Xbz8='
