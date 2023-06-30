import numpy

from Models.Rmse import Rmse
from Models.Data import Data
from Models.Plot import Plot

rmse: Rmse = Rmse(Data.forecast, Data.observation)
rmseValues: numpy.ndarray = rmse.calculate()

plot: Plot = Plot(rmseValues)

plot.temporalPoint()
plot.maps()