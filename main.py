from pydantic import BaseModel, Field
from typing import (List, Optional)
from fastapi import FastAPI
from mangum import Mangum

app = FastAPI(title='Model API', description='Model API')

class out_response(BaseModel):
    str_id:str

class in_response_suficiencia(BaseModel):
    ls_lista_cnes:List[str]
    num_vidas:int         
    num_agenda:int       
    num_cenario:int        
    str_uf:str              
    ls_mun:List[str] 
    
class in_response_vidas(BaseModel):
    ls_mun:List[str] 
    str_uf:str

@app.get('/health')
def health():
    return {'health_status': 'ok'}

#@app.post("/predict", response_model=out_response)
#def read_calculadora(entrada:in_response_suficiencia):
@app.get("/predict")
def read_root():
    return {"Hello Medium Reader": "from FastAPI & API Gateway"}

handler = Mangum(app)