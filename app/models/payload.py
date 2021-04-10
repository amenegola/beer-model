from typing import List
from pydantic import BaseModel


class PredictionPayload(BaseModel):
    abv: float
    target_fg: int
    target_og: float
    ebc: float
    srm: float
    ph: float


def payload_to_list(hpp: PredictionPayload) -> List:
    return [
        hpp.abv,
        hpp.target_fg,
        hpp.target_og,
        hpp.ebc,
        hpp.srm,
        hpp.ph]
