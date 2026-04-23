import math
import pandas as pd
def win_avg(A, window):
    B = []
    for t in range(len(A)):
        if t < window - 1:
            B.append(math.nan)
        else:
            window_slice = A[t - window + 1 : t + 1]
            B.append(sum(window_slice) / window)
    return B

def exp_avg (A, alpha):
    B = [A[0]]
    for t in range (1,len(A)):
        B.append(alpha*A[t]+(1-alpha)*B[t-1])
    return B

def crossAbove(A1,A2):
    B= [0]
    for t in range(1,len(A1)):
        if (A1[t-1]<A2[t-1] and A1[t] >A2[t]):
            B.append(1)
        else:
            B.append(0)
    return B

def constant_series(A, k):
    return [k] * len(A)
def ROF(period, A):
    B = []
    for t in range(len(A)):
        if (t-period >= 0):
            difference= A[t] - A[t-period]
            B.append(difference/ A[t])
        else:
            B.append(math.nan)  
    return B
def portfolio_simulation(balance, price, entry, exit):
    n = len(price)
    positions_held = 0
    portfolio = [0.0] * n
    for i in range(n):
        if exit[i] == 1:
            balance += positions_held * price[i]
            positions_held = 0
        elif entry[i] == 1:
            positions_held += 1
            balance -= price[i]
        portfolio[i] = balance + positions_held * price[i]  # updated every step
    return portfolio

def rules():
    with open("rules.txt", "r") as f:
        return f.read()

