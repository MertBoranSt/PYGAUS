import numpy as np
import matplotlib.pyplot as plt
from lmfit import Model

# Define the model function as a sum of two Gaussians and an exponential
def model_function(x, g1_center, g1_amplitude, g1_sigma, g2_center, g2_amplitude, g2_sigma, exp_amplitude, exp_decay):
    gaussian1 = g1_amplitude * np.exp(-(x - g1_center)**2 / (2 * g1_sigma**2))
    gaussian2 = g2_amplitude * np.exp(-(x - g2_center)**2 / (2 * g2_sigma**2))
    exponential = exp_amplitude * np.exp(-exp_decay * x)
    return gaussian1 + gaussian2 + exponential

# Read the data file
file_path = "----------------------"  # Replace with the actual path to your data file
data = np.loadtxt(file_path)

# Select the columns to be read for X and Y data
x_data = data[:, 0]
y_data = data[:, 1]

# Create an lmfit Model
model = Model(model_function)

# Set initial parameter values
params = model.make_params(
    g1_center=np.mean(x_data),
    g1_amplitude=np.max(y_data),
    g1_sigma=3,
    g2_center=np.mean(x_data),
    g2_amplitude=np.max(y_data),
    g2_sigma=4,
    exp_amplitude=np.min(y_data),
    exp_decay=0.1
)

# Fit the data using lmfit
result = model.fit(y_data, params, x=x_data)

# Show fit results
print(result.fit_report(min_correl=0.5))

# Plotting a graph
plt.scatter(x_data, y_data, label='data')
plt.plot(x_data, result.best_fit, 'r-', label='fit')
plt.legend()
plt.xlabel('Spectral Type')
plt.ylabel('Avg. Vsini')
plt.title('ST-Vsini')
plt.show()
