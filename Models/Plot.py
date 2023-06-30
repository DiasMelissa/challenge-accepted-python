import numpy
import matplotlib.pyplot as pyplot

from matplotlib.image import AxesImage

class Plot:
    LATITUDE_INDEX: int = 8
    LONGITUDE_INDEX: int = 26

    TEMPORAL_POINT_TITLE_LABEL: str = 'RMSE Time Series - São Paulo (lat: 23.5489° S and lon: 46.6388° W)'
    TEMPORAL_POINT_X_LABEL: str = '6 hours Interval'
    TEMPORAL_POINT_Y_LABEL: str = 'RMSE'

    MAPS_TITLE_LABEL: str = 'RMSE - Interval'
    MAPS_X_LABEL: str = 'Longitude (W)'
    MAPS_Y_LABEL: str = 'Latitude (S)'

    rmseValues: numpy.ndarray

    def __init__(self, rmseValues: numpy.ndarray) -> None:
        self.rmseValues = rmseValues

    def maps(self) -> None :
        times: int = self.rmseValues.shape[0]

        for interval in range(times):
            fig, ax = pyplot.subplots()

            im: AxesImage = ax.imshow(
                self.rmseValues[interval, :, :],
                cmap = 'hot',
                vmin = 0,
                vmax = 10
            )

            ax.set_title(f'{self.MAPS_TITLE_LABEL} {interval + 1}')
            ax.set_xlabel(self.MAPS_X_LABEL)
            ax.set_ylabel(self.MAPS_Y_LABEL)

            fig.colorbar(im, ax = ax)

            pyplot.show()

    def temporalPoint(self) -> None :
        fig, ax = pyplot.subplots()

        time: numpy.ndarray = numpy.arange(len(self.rmseValues)) * 6
        rmsePoint: numpy.ndarray = self.rmseValues[:, self.LATITUDE_INDEX, self.LONGITUDE_INDEX]

        ax.plot(time, rmsePoint, marker = 'o', linestyle = '-', color = 'b')

        ax.set_title(self.TEMPORAL_POINT_TITLE_LABEL)
        ax.set_xlabel(self.TEMPORAL_POINT_X_LABEL)
        ax.set_ylabel(self.TEMPORAL_POINT_Y_LABEL)

        pyplot.show()