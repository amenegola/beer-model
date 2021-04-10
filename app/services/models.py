from typing import List

import joblib
import numpy as np
from loguru import logger
import boto3

from fastapi_skeleton.core.config import BUCKET_MODEL_ARTIFACTS, MODEL_FILENAME
from fastapi_skeleton.core.messages import NO_VALID_PAYLOAD
from fastapi_skeleton.models.payload import (PredictionPayload,
                                             payload_to_list)
from fastapi_skeleton.models.prediction import PredictionResult


class BeerModel():

    def __init__(self):
        self._load_local_model()

    def _load_model(self):
        s3 = boto3.client('s3')
        s3.download_file(BUCKET_MODEL_ARTIFACTS, MODEL_FILENAME, MODEL_FILENAME)
        self.model = joblib.load(MODEL_FILENAME)

    def _pre_process(self, payload: PredictionPayload) -> List:
        logger.debug("Pre-processing payload.")
        result = np.asarray(payload_to_list(payload)).reshape(1, -1)
        return result

    def _post_process(self, prediction: np.ndarray) -> PredictionResult:
        logger.debug("Post-processing prediction.")
        result = prediction.tolist()
        hpp = PredictionResult(ibu=result[0])
        return hpp

    def _predict(self, features: List) -> np.ndarray:
        logger.debug("Predicting.")
        prediction_result = self.model.predict(features)
        return prediction_result

    def predict(self, payload: PredictionPayload):
        if payload is None:
            raise ValueError(NO_VALID_PAYLOAD.format(payload))

        pre_processed_payload = self._pre_process(payload)
        prediction = self._predict(pre_processed_payload)
        logger.info(prediction)
        post_processed_result = self._post_process(prediction)

        return post_processed_result
