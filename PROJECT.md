Calculating Root Mean Square Error (RMSE) for Air Surface Temperature. 

It's a way to express the accuracy of the weather forecast. In this case, it is used to calculate the RMSE every 6 hours and the RMSE is obtained for the city of São Paulo.

Requirements

For this project, it is necessary to have Python 3.X version installed. Here is the necessary library and instruction on how to install it:

pip install netCDF4

Or if you have a conda environment:

conda install -c conda-forge netcdf4

The files need to be in the same directory as the code.

Information about the data:

Forecast Data

Property	                          Description
File     	                          forecast.nc
Number of times steps	              72
Reference Date   	                  2018/04/14
Time Frequency                        Hourly
Temperature Variable Name             t2m
Temperature Variable Unity       	  Kelvin

Observed Data

Property	                          Description
File     	                          observation.nc
Number of times steps                 72
Reference Date   	                  2018/04/14
Time Frequency                        Hourly
Temperature Variable Name             temperatura
Temperature Variable Unit       	  Degree Celsius

Functionality

The code is divided into sections:

* main.py contains the main logic and coordinates the program execution;
* Constants.py contains constant or global variables used in the project;
* Data.py reads the data;
* Rmse.py calculates the RMSE index for each 6-hour interval in the time series at all points of the matrix;
* Plot.py plots two-dimensional maps of the index for each period and a time series graph of the same index for São Paulo (Latitude -23.5489 and Longitude -46.6388, corresponding to the Y: 8 and X: 26 point in the data matrix grid).

Execution

python main.py