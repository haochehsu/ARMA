import numpy as np
import pandas as pd
import warnings
from statsmodels.tsa.arima.model import ARIMA

warnings.filterwarnings("ignore")

filename = 'data.xlsx'
data = pd.read_excel(filename)

p_range = 4
q_range = 4

dict = {}

indicator = 0
list = ['a', 'b', 'c']
list_exit = ['e', 'x', 'q', 'quit', 'no', 'exit']

while indicator == 0:
    select = input("Please enter the time series (a, b, c or exit/q): ")

    if select.strip().lower() in list_exit:
        print(' - - - PROGRAM TERMINATED - - - ')
        print('')
        break
    if select.strip().lower() not in list:
        continue

    def arma_model(p_range, q_range, data):
        index = 0
        result = np.array([[]])
        for p in range(p_range):
            pi = []
            for q in range(q_range):
                try:
                    model = ARIMA(data, order=(p, 0, q))
                    model_fit = model.fit()
                except:
                    model_fit.bic = np.nan
                dict[index] = (p, q, model_fit.bic)
                pi.append(model_fit.bic)
                index = index + 1
            result = np.append(result, np.array(pi))
        # return result

    data_c = data[str(select).strip().lower()]
    result_c = arma_model(p_range, q_range, data_c)

    BIC = 1e13
    index = 0
    i = 0

    for element in dict.values():
        if element[2] != 'nan':
            if element[2] < BIC:
                BIC = element[2]
                index = index + 1

    for value in dict.values():
        if value[2] == BIC:
            index = i
        i = i + 1

    print('- - - - - - - - - -')
    print('The ARMA parameter triplet (p, q, BIC) is: ' + str(dict[index]))
    print('')
