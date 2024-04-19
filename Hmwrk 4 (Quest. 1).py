




import math
import numpy as np
import matplotlib.pyplot as plt


drift = 0.00 
sigma = 0.01 
I_Price = 280

prices = np.zeros( ( 252, 1000 ) ) #Range is not inclusive on the end

for i in range( 0, 1000 ): 
    prices[ 0 ][ i ] = I_Price #Intial price is 280
    
for col in range( 0, 1000 ): # Calls each column (price path)
    for row in range( 1, 252 ): #Calls each row after initial price of each column
      
        prices[ row ][ col ] = prices[ row - 1 ][ col ] * math.exp( drift * 1 - 0.5 * 
                                                                   math.pow( sigma, 2 ) * 1 + sigma * np.random.normal( 0, 1, 1 ) ) 
        
plt.plot( prices ) 
plt.show() 
