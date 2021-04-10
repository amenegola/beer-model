
import pytest

from app.models.payload import PredictionPayload
from app.models.prediction import PredictionResult
from app.services.models import BeerModel


def test_prediction(test_client) -> None:
    hpp = PredictionPayload.parse_obj({
        "abv": 6.7,
        "target_fg": 1013,
        "target_og": 1064.0,
        "ebc": 19.0,
        "srm": 9.5,
        "ph": 4.4})

    hpm = BeerModel()
    result = hpm.predict(hpp)
    assert isinstance(result, PredictionResult)


def test_prediction_no_payload(test_client) -> None:
    hpm = BeerModel()
    with pytest.raises(ValueError):
        result = hpm.predict(None)
        assert isinstance(result, PredictionResult)
