from fastapi import APIRouter, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import HTTPException
from models.user import Token # Defina um modelo Pydantic para o Token
from services.auth import create_access_token, verify_password

router = APIRouter(
    prefix="/auth",
    tags=["Autenticação"]
)

USERS_DB = {
    "admin": {
        "username": "admin", 
        "hashed_password": "$2b$12$bL5KkQ12B/5.O.I3D1N.lO0Dq9y2vC3lT1d2tH5q8uG/p3z.E6L9S" 
    }
}

@router.post(
    "/token", 
    response_model=Token,
    summary="Login de Usuário",
    description="Gera um JWT Bearer Token para acessar endpoints protegidos."
)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = USERS_DB.get(form_data.username)
    
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Nome de usuário ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
    access_token = create_access_token(data={"sub": user["username"]})
    
    return {"access_token": access_token, "token_type": "bearer"}