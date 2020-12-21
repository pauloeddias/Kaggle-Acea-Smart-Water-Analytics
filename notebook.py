# In[]:
from helpers import read_data

# In[]:
Aquifer_Auser = read_data('Aquifer_Auser.csv')
Aquifer_Doganella = read_data('Aquifer_Doganella.csv')
Aquifer_Luco = read_data('Aquifer_Luco.csv')
Aquifer_Petrignano = read_data('Aquifer_Petrignano.csv')
Lake_Bilancino = read_data('Lake_Bilancino.csv')
River_Arno = read_data('River_Arno.csv')
Water_Spring_Amiata = read_data('Water_Spring_Amiata.csv')
Water_Spring_Lupa = read_data('Water_Spring_Lupa.csv')
Water_Spring_Madonna_di_Canneto = read_data('Water_Spring_Madonna_di_Canneto.csv')

# In[]:
River_Arno.head().T

# In[]:
print('Gabriel was here')