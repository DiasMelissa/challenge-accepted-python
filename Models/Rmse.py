import netCDF4, numpy

from typing import Union

class Rmse:
    INTERVAL: int = 6

    forecast: Union[numpy.ndarray, None] = None
    observation: Union[numpy.ndarray, None] = None

    intervals: Union[int, None] = None

    latitudeRange: Union[int, None] = None
    longitudeRange: Union[int, None] = None

    def __init__(self, forecast: netCDF4.Dataset, observation: netCDF4.Dataset) -> None:
        self.forecast = forecast.variables['t2m'][:]
        self.observation = observation.variables['temperatura'][:] + 273.15

        self.intervals = len(self.observation) // self.INTERVAL

        self.latitudeRange = self.forecast.shape[1]
        self.longitudeRange = self.forecast.shape[2]

    def calculate(self) -> numpy.ndarray:

        values: numpy.ndarray = numpy.zeros((self.intervals, self.latitudeRange, self.longitudeRange))

        for index in range(self.intervals):
            startIndex: int = index * self.INTERVAL
            finalIndex: int = startIndex + self.INTERVAL

            forecastInterval: numpy.ndarray = self.forecast[startIndex:finalIndex]
            observationInterval: numpy.ndarray = self.observation[startIndex:finalIndex]

            self.getRootMeanSquaredError(index, values, forecastInterval, observationInterval)

        return values

    def getRootMeanSquaredError(
        self,
        index: int,
        values: numpy.ndarray, 
        forecastInterval: numpy.ndarray,
        observationInterval: numpy.ndarray
    ) -> None:
        for latitude in range(self.latitudeRange):
            for longitude in range(self.longitudeRange):
                mask: numpy.ndarray = numpy.isnan(observationInterval[:, latitude, longitude])

                forecastMasked: numpy.ndarray = numpy.ma.array(
                    forecastInterval[:, latitude, longitude],
                    mask = mask
                )

                observedMasked: numpy.ndarray = numpy.ma.array(
                    observationInterval[:, latitude, longitude],
                    mask = mask
                )

                rootMeanSquaredError: float = numpy.sqrt(numpy.mean((observedMasked - forecastMasked) ** 2))
                values[index, latitude, longitude] = rootMeanSquaredError