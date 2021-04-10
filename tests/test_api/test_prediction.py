

from app.core import config


def test_prediction(test_client) -> None:
    response = test_client.post(
        "/api/model/predict",
        json={
            "abv": 6.7,
            "target_fg": 1013,
            "target_og": 1064.0,
            "ebc": 19.0,
            "srm": 9.5,
            "ph": 4.4},
        headers={"token": str(config.API_KEY)})
    assert response.status_code == 200
    assert "ibu" in response.json()


def test_prediction_nopayload(test_client) -> None:
    response = test_client.post(
        "/api/model/predict",
        json={},
        headers={"token": str(config.API_KEY)}
    )
    assert response.status_code == 422
