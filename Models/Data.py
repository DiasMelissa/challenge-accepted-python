import netCDF4

from Models.Constants import Constants

class Data:
    forecast: netCDF4.Dataset = netCDF4.Dataset(Constants.FORECAST)
    observation: netCDF4.Dataset = netCDF4.Dataset(Constants.OBSERVATION)