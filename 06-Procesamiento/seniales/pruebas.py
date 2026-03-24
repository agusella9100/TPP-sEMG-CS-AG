#pruebas de algoritmos

#importo librerias necesarias
import numpy as np
import matplotlib.pyplot as plt
from Archivos.signal_loader import select_and_load_file, show_signal_analysis, loader

if __name__ == "__main__":
    # use_cache=True carga automáticamente el último archivo
    # use_cache=False abre siempre el selector
    select_and_load_file(use_cache=True)
    show_signal_analysis()

    datos = loader.get_data()

    print(datos.head(10))
    Channel_1 = datos['CH1']
    print(Channel_1.info())
    print(Channel_1.describe())


    print(Channel_1[1:10])
    Channel_1
V_ch1 = Channel_1[1:]
'''
figura1 = plt.figure(figsize=(10, 6))


plt.plot(Channel_1., label='CH1')
plt.title('Señal del Canal 1')
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.legend()
plt.grid()
plt.show()  
'''