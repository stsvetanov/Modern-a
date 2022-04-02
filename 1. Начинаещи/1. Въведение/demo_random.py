import numpy as np
import matplotlib.pyplot as plt

mu,sigma,n = 0.,1.,1000

def normal(x,mu,sigma):
    return ( 2.*np.pi*sigma**2. )**-.5 * np.exp( -.5 * (x-mu)**2. / sigma**2. )

x = np.random.normal(mu,sigma,n)
y = normal(x,mu,sigma)


plt.plot(x,y)
plt.show()