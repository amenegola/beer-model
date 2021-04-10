from fastapi import APIRouter, Depends
from starlette.requests import Request

from fastapi_skeleton.core import security
from fastapi_skeleton.models.payload import PredictionPayload
from fastapi_skeleton.models.prediction import PredictionResult
from fastapi_skeleton.services.models import BeerModel

router = APIRouter()


@router.post("/predict", response_model=PredictionResult, name="predict")
def post_predict(
    request: Request,
    authenticated: bool = Depends(security.validate_request),
    block_data: PredictionPayload = None
) -> PredictionResult:

    model: BeerModel = request.app.state.model
    prediction: PredictionResult = model.predict(block_data)

    return prediction
