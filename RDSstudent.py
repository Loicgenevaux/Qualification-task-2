import numpy as np
from student import TUstudent
import matplotlib.pyplot as plt

class RobustDataScienceStudent (TUstudent):

    @classmethod
    def integral_compute(cls,x,xstat,plot_derivative=False):
        try:
                if not isinstance(x, list) or len(x) != 2:
                        raise ValueError("x should be a list of two elements.")
                if not isinstance(xstat, list) or len(xstat) != 2:
                        raise ValueError("xstat should be a list of two elements.")

                x=np.linspace(x[0],x[1],100)
                cls.y=np.exp(-x)*np.cos(x)
                plt.figure(figsize=(10, 6))
                plt.plot(x, cls.y, label="y(x)")
                plt.title("Function y = e^(-x)cos(x)")
                plt.xlabel("x")
                plt.ylabel("y")
                plt.legend()
                plt.grid()
                plt.show()
                range = (x >= xstat[0]) & (x <= xstat[1])
                ystat = cls.y[range]
                mean = np.mean(ystat)
                var = np.var(ystat)
                std = np.std(ystat)
                threshold = np.percentile(ystat, 70)   
                dy=np.gradient(cls.y,x)
                if plot_derivative:
                        plt.figure(figsize=(10, 6))
                        plt.plot(x, dy, label="derivative of y", color="orange")
                        plt.title("Derivative of y")
                        plt.xlabel("x")
                        plt.ylabel("dy/dx")
                        plt.legend()
                        plt.grid()
                        plt.show()
                zeros=np.argmin(np.abs(dy))
                print(f"Mean of y between x={xstat}: {mean}")
                print(f"Variance of between x={xstat}: {var}")
                print(f"Standard deviation of y between x={xstat}: {std}")
                print(f"Threshold y 70%: {threshold}")
                print(f"dy/dx=0 for x={x[zeros]}")

        except Exception as error:
                print(f"error when computing the function: {error}")



    
rdss1=RobustDataScienceStudent("David Dupond",21,"11-11-2011","Elektrotechnik und Informationstechnik",1234567,["e","m","p","t","h"],"e")
rdss1.integral_compute([0,100],[4,7],plot_derivative=True)


