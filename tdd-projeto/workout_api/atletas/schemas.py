from pydantic import BaseModel, Field, PositiveFloat

class Athlete(BaseModel):
    nome: str = Field(..., description="Nome do atleta", example="João Silva")
    cpf: str = Field(..., description="CPF único", example="12345678900")
    idade: int = Field(..., description="Idade", example=25)
    peso: PositiveFloat = Field(..., description="Peso", example=75.5)
    altura: PositiveFloat = Field(..., description="Altura", example=1.75)
    sexo: str = Field(..., description="Sexo (M/F)", example="M")

class AthleteOut(Athlete):
    id: str  # Esse campo só aparece na resposta, vindo do MongoDB