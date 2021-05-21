import matplotlib.pyplot as plt 
import numpy as np 

data = ['SQL', 'PHP', 'Assembly language', 'JavaScript', 'Visual Basic', 'C#', 'C++', 'Java', 'Python', 'C']
x = np.arange(len(data))
score = [1.71, 1.86, 2.43, 2.45, 4.02, 4.41, 7.81, 11.74, 11.87, 13.38]
plt.barh(x, score, align = 'center', alpha = 0.5)
plt.yticks(x, data)

plt.xlabel('Ratings')
plt.title('Most Popular Programming Languages')
plt.show()