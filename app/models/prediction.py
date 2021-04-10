from pydantic import BaseModel


class PredictionResult(BaseModel):
    ibu: float
