from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime, timedelta

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False) # e.g., operator_01
    password_hash = db.Column(db.String(150), nullable=False)
    clearance_level = db.Column(db.Integer, default=4)
    entries = db.relationship('VaultEntry', backref='owner', lazy=True)

class VaultEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False) # e.g., Neo-Zurich Global
    url = db.Column(db.String(255)) # e.g., banking.nzg.ch
    category = db.Column(db.String(50)) # e.g., BANKING
    identifier = db.Column(db.String(150), nullable=False) # Username/Email
    password_encrypted = db.Column(db.Text, nullable=False) # AES encrypted
    
    # Extra Info
    full_name = db.Column(db.String(150))
    terminal_loc = db.Column(db.String(150))
    card_info = db.Column(db.String(50))
    card_expiry = db.Column(db.String(10))
    notes = db.Column(db.Text)
    
    # Expiry Timer Logic
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    expiry_date = db.Column(db.DateTime, nullable=False) 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    @property
    def is_expired(self):
        return datetime.utcnow() > self.expiry_date

    def time_remaining(self):
        if self.is_expired:
            return "EXPIRED"
        delta = self.expiry_date - datetime.utcnow()
        days = delta.days
        hours, remainder = divmod(delta.seconds, 3600)
        minutes, _ = divmod(remainder, 60)
        return f"{days}d {hours}h {minutes}m"
