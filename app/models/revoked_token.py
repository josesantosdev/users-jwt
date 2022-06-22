from app import db 

class RevokedTokenModel(db.Model):
    
    __tablename__ = 'revoked_tokens'
    
    id_token = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(100), nullable=False)