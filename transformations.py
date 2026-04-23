from fetch_data import fetch
from transformation_impl import win_avg, exp_avg, crossAbove, constant_series, ROF, portfolio_simulation
def Fetch(datasource):
    return fetch(datasource).tolist()
def SimpleMovingAverage(window, datasource):
    return win_avg(datasource, window)
def ExponentialMovingAverage(datasource, window):
    return exp_avg(datasource, window)
def CrossAbove(A1,A2):
    return crossAbove(A1,A2)
def ConstantSeries(A,k):
    return constant_series(A,k)
def RateOfChange(period,datasource):
    return ROF(period,datasource)
def  PortfolioSimulation(balance, price, entry, exit):
    return portfolio_simulation(balance, price, entry, exit)