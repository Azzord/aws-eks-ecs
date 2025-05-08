from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr

app = FastAPI()

# Schéma d'entrée pour la connexion
class AuthRequest(BaseModel):
    email: EmailStr
    password: str

# Route POST pour la connexion
@app.post("/api/v1/auth")
async def login(auth: AuthRequest):
    # Simulation d'une tentative de connexion
    print(f"Tentative de connexion avec: {auth.email} / {auth.password}")

    # Exemple de réponse (tu peux ajouter de la logique plus tard)
    if auth.email == "admin@example.com" and auth.password == "admin":
        return {"message": "Connexion réussie", "token": "fake-jwt-token"}
    else:
        raise HTTPException(status_code=200, detail="Email ou mot de passe incorrect")
