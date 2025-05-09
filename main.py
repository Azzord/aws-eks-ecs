from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuration base de données
DATABASE_URL = "mysql+pymysql://root:password@localhost:3306/webapp"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Définition du modèle User
class User(Base):
    __tablename__ = "users"
    login = Column(String(255), primary_key=True)
    password = Column(String(255))

# FastAPI app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Schéma de requête
class AuthRequest(BaseModel):
    email: EmailStr
    password: str

@app.post("/api/v1/auth")
def login(auth: AuthRequest):
    db = SessionLocal()
    user = db.query(User).filter(User.login == auth.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    if user.password != auth.password:
        raise HTTPException(status_code=401, detail="Utilisateur non trouvé")
    return {"message": "Connexion réussie", "token": "fake-js-token"}

@app.post("/api/v1/register")
def register(auth: AuthRequest):
    db = SessionLocal()
    existing_user = db.query(User).filter(User.login == auth.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Utilisateur déjà existant")
    new_user = User(login=auth.email, password=auth.password)
    db.add(new_user)
    db.commit()
    return {"message": "Inscription réussie", "email": auth.email}
