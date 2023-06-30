import os

class Constants:
    __DIR__: str = os.getcwd()

    FORECAST: str = os.path.join(__DIR__, "Data", "forecast.nc")
    OBSERVATION: str = os.path.join(__DIR__, "Data", "observation.nc")