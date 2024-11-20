import numpy as np
from student import TUstudent
import matplotlib.pyplot as plt
from scipy import stats


class RobustDataScienceStudent(TUstudent):
    @classmethod
    def integral_compute(cls, x, xstat, plot_derivative=False):
        try:
            if not isinstance(x, list) or len(x) != 2:
                raise ValueError("x should be a list of two elements.")
            if not isinstance(xstat, list) or len(xstat) != 2:
                raise ValueError("xstat should be a list of two elements.")

            x = np.linspace(x[0], x[1], 100)
            cls.y = np.exp(-x) * np.cos(x)

            # Plot the function
            plt.figure(figsize=(10, 6))
            plt.plot(x, cls.y, label="y(x)")
            plt.title("Function y = e^(-x)cos(x)")
            plt.xlabel("x")
            plt.ylabel("y")
            plt.legend()
            plt.grid()
            plt.show()

            # Compute statistics
            range_mask = (x >= xstat[0]) & (x <= xstat[1])
            ystat = cls.y[range_mask]
            mean = np.mean(ystat)
            var = np.var(ystat)
            std = np.std(ystat)
            threshold = np.percentile(ystat, 70)

            # Compute derivative
            dy = np.gradient(cls.y, x)
            if plot_derivative:
                plt.figure(figsize=(10, 6))
                plt.plot(x, dy, label="derivative of y", color="orange")
                plt.title("Derivative of y")
                plt.xlabel("x")
                plt.ylabel("dy/dx")
                plt.legend()
                plt.grid()
                plt.show()

            zeros = np.argmin(np.abs(dy))

            # Print results
            print(f"Mean of y between x={xstat}: {mean}")
            print(f"Variance of y between x={xstat}: {var}")
            print(f"Standard deviation of y between x={xstat}: {std}")
            print(f"Threshold y 70%: {threshold}")
            print(f"dy/dx=0 for x={x[zeros]}")

            return cls.y
        except Exception as error:
            print(f"Error when computing the function: {error}")

    @classmethod
    def linear_algebra_compute(cls, matrix, vector):
        try:
            if not isinstance(matrix, np.ndarray) or not isinstance(vector, np.ndarray):
                raise TypeError("Matrix and Vector should be NumPy arrays.")
            if matrix.shape[0] != matrix.shape[1]:
                raise ValueError("Matrix should have the same i and j.")
            if matrix.shape[0] != vector.size:
                raise ValueError("The number of rows in matrix should match the size of vector.")

            x = np.linalg.solve(matrix, vector)

            # Print results
            print("\nLinear System Solution:\n")
            print(f"System Matrix:\n{matrix}\n")
            print(f"Solution Vector:\n{vector}\n")
            print(f"Solution:\n{x}\n")

            return x
        except Exception as error:
            print(f"Error when computing the function: {error}")

    @classmethod
    def least_squares(cls, y, X, verbose=True):
        try:
            if not isinstance(X, np.ndarray) or not isinstance(y, np.ndarray):
                raise TypeError("X and y should be NumPy arrays.")
            if X.shape[0] <= X.shape[1]:
                raise ValueError("The number of observations should always exceed the number of variables.")
            if y.shape[0] != X.shape[0]:
                raise ValueError("y should have the same number of observations as X.")

            beta, residuals = np.linalg.lstsq(X, y, rcond=None)[:2]

            # Compute residuals and statistical values
            ym = X @ beta
            residual = y - ym
            n, k = X.shape
            residual_var = np.sum(residuals**2) / (n - k)
            XtX_inv = np.linalg.inv(X.T @ X)
            beta_std_errors = np.sqrt(np.diagonal(XtX_inv) * residual_var)

            t = beta / beta_std_errors
            p = 2 * (1 - stats.t.cdf(np.abs(t), df=n - k))

            if verbose:
                print("\nMultivariate least-squares linear regression solution:\n")
                print(f"Vector coefficient β:\n{beta}\n")
                print(f"Standard error of vector coefficient β:\n{beta_std_errors}\n")
                print(f"t statistical value:\n{t}\n")
                print(f"p statistical value:\n{p}\n")

            return beta, t, p
        except Exception as error:
            print(f"Error when computing the function: {error}")


# Main program
x = []
y = []

rdss1 = RobustDataScienceStudent(
    "David Dupond", 21, "11-11-2011", "Elektrotechnik und Informationstechnik", 1234567, ["e", "m", "p", "t", "h"], "e"
)

y = rdss1.integral_compute([0, 12], [4, 7], plot_derivative=True)

A = np.array([[3, 2, 3, 10], [2, -2, 5, 8], [3, 3, 4, 9], [3, 4, -3, -7]])
b = np.array([4, 1, 3, 2])
X = rdss1.linear_algebra_compute(A, b)

rdss1.least_squares(y, X, verbose=True)
