from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)


class AuthRequest(BaseModel):
    email: EmailStr
    password: str

@app.post("/api/v1/auth")
async def login(auth: AuthRequest):
    print(f"Tentative de connexion avec: {auth.email} / {auth.password}")
    if auth.email == "admin@example.com" and auth.password == "admin":
        return {"message": "Connexion réussie", "token": "fake-js-token"}
    else:
        raise HTTPException(status_code=401, detail="Email ou mot de passe incorrect")
