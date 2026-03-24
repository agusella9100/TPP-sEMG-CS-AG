
# Script para seleccionar en ventana emergente el archivo que quiero cargar y luego cargarlo
# para obtener los datos de la señal, con la clase SignalLoader que creé en csv_loader.py

import numpy as np
import matplotlib.pyplot as plt
from Archivos.csv_loader import SignalLoader
import tkinter as tk
from tkinter import ttk

loader = SignalLoader()

def select_and_load_file(use_cache=True):
    """Interfaz simple para seleccionar archivo con opción de caché"""
    files = loader.get_csv_files()

    if not files:
        print("No hay archivos CSV disponibles en Archivos/csv")
        return False

    # Intenta usar caché si está habilitado
    if use_cache:
        last_file = loader.get_last_file()
        if last_file and last_file in files:
            loader.load_csv(last_file)
            print(f"Se cargó desde caché: '{last_file}'")
            return True

    # Crea ventana de selección
    root = tk.Tk()
    root.title("Seleccionar archivo CSV")
    root.geometry("300x150")

    ttk.Label(root, text="Elige un archivo:").pack(pady=10)

    file_var = tk.StringVar(value=files[0])
    combo = ttk.Combobox(root, textvariable=file_var, values=files, state="readonly")
    combo.pack(pady=10, padx=20, fill="x")

    result = [False]

    def load():
        filename = file_var.get()
        loader.load_csv(filename)
        result[0] = True
        root.destroy()

    ttk.Button(root, text="Cargar", command=load).pack(pady=10)
    root.mainloop()

    return result[0]

def show_signal_analysis():
    """Muestra análisis básico de la señal cargada"""
    if loader.data is None:
        print("Primero debes cargar un archivo")
        return

    stats = loader.csv_info()

    print(f"\n{'='*50}")
    print(f"Archivo: {stats['archivo']}")
    print(f"Filas: {stats['filas']}")
    print(f"Columnas: {stats['columnas']}")
    print(f"{'='*50}\n")