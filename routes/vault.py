from flask import Blueprint, render_template, redirect, url_for, request, jsonify, current_app
from flask_login import login_required, current_user
from models import db, VaultEntry
from cryptography.fernet import Fernet
from datetime import datetime
import json

vault = Blueprint('vault', __name__)

def get_cipher_suite():
    return Fernet(current_app.config['VAULT_ENCRYPTION_KEY'])

@vault.route('/')
def index():
    return redirect(url_for('auth.login'))

@vault.route('/dashboard')
@login_required
def dashboard():
    entries = VaultEntry.query.filter_by(user_id=current_user.id).order_by(VaultEntry.expiry_date).all()
    # Calculate some stats
    total_records = len(entries)
    
    return render_template('dashboard.html', entries=entries, total_records=total_records)

@vault.route('/api/entries', methods=['POST'])
@login_required
def add_entry():
    data = request.get_json()
    
    # Encrypt password
    cipher_suite = get_cipher_suite()
    encrypted_pass = cipher_suite.encrypt(data.get('password', '').encode()).decode('utf-8')
    
    # Expiry logic
    expiry_date_str = data.get('expiry_date')
    if expiry_date_str:
        expiry_date = datetime.strptime(expiry_date_str, '%Y-%m-%d')
    else:
        # Default 30 days
        from datetime import timedelta
        expiry_date = datetime.utcnow() + timedelta(days=30)
        
    entry = VaultEntry(
        title=data.get('title'),
        url=data.get('url'),
        category=data.get('category', 'OTHER'),
        identifier=data.get('identifier'),
        password_encrypted=encrypted_pass,
        full_name=data.get('full_name'),
        terminal_loc=data.get('terminal_loc'),
        card_info=data.get('card_info'),
        card_expiry=data.get('card_expiry'),
        notes=data.get('notes'),
        expiry_date=expiry_date,
        owner=current_user
    )
    db.session.add(entry)
    db.session.commit()
    
    return jsonify({"message": "Entry added successfully"}), 201

@vault.route('/api/entries/<int:entry_id>/reveal', methods=['POST'])
@login_required
def reveal_entry(entry_id):
    entry = VaultEntry.query.get_or_404(entry_id)
    if entry.owner != current_user:
        return jsonify({"message": "Unauthorized"}), 401
        
    cipher_suite = get_cipher_suite()
    try:
        decrypted_pass = cipher_suite.decrypt(entry.password_encrypted.encode()).decode('utf-8')
        return jsonify({"password": decrypted_pass})
    except Exception as e:
        return jsonify({"message": "Decryption failed"}), 500

@vault.route('/api/entries/<int:entry_id>', methods=['DELETE'])
@login_required
def delete_entry(entry_id):
    entry = VaultEntry.query.get_or_404(entry_id)
    if entry.owner != current_user:
        return jsonify({"message": "Unauthorized"}), 401
        
    db.session.delete(entry)
    db.session.commit()
    return jsonify({"message": "Entry deleted successfully"}), 200
