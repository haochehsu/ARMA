import statsmodels.tsa.arima_process as sm
import numpy as np
import matplotlib.pyplot as plt

AR = np.array([1, -0.9])
MA = np.array([1, 1.2])

arma_process = sm.arma_impulse_response(AR, MA, leads=20)

x = [1*i for i in range(len(arma_process))]
print(x)
print(arma_process)

plt.scatter(x, arma_process)
plt.plot(x, arma_process)
plt.xlabel("Future Periods (h)")
plt.ylabel("Implus Responses")
plt.show()
