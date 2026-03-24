#importo librerias para manejo de datos en formato simple y otros para conseguir rutas de archivos
import pandas as pd
from pathlib import Path
import os
import json

class SignalLoader:
    def __init__(self, csv_folder='Archivos/csv', cache_file='Archivos/.cache.json'):
        self.csv_folder = Path(csv_folder)
        self.cache_file = cache_file
        self.data = None
        self.filename = None

    def get_csv_files(self):
        if not os.path.exists(self.csv_folder):
            print(f"Error: El directorio '{self.csv_folder}' no existe.")
            return []

        csv_list = [f for f in os.listdir(self.csv_folder) if f.endswith('.CSV')]
        return csv_list

    def load_csv(self, filename):
        filepath = os.path.join(self.csv_folder, filename)
        try:
            self.data = pd.read_csv(filepath)
            self.filename = filename
            self._save_cache(filename)
            print(f"Archivo '{filename}' cargado exitosamente.")
        except Exception as e:
            print(f"Error al cargar el archivo '{filename}': {e}")
            self.data = None
            self.filename = None

    def _save_cache(self, filename):
        """Guarda el nombre del archivo en caché"""
        cache_data = {'last_file': filename}
        try:
            with open(self.cache_file, 'w') as f:
                json.dump(cache_data, f)
        except Exception as e:
            print(f"Advertencia: No se pudo guardar caché: {e}")

    def get_last_file(self):
        """Obtiene el último archivo cargado desde caché"""
        try:
            if os.path.exists(self.cache_file):
                with open(self.cache_file, 'r') as f:
                    cache_data = json.load(f)
                    return cache_data.get('last_file')
        except Exception as e:
            print(f"Advertencia: No se pudo leer caché: {e}")
        return None

    def get_data(self):
        if self.data is not None:
            print(f" adquiriendo datos del archivo '{self.filename}'")
            return self.data
        else:
            print("No se ha cargado ningún archivo CSV.")
            return None

    def csv_info(self):
        if self.data is None:
            print("No se ha cargado ningún archivo CSV.")
            return None

        stats = {
            'archivo': self.filename,
            'filas': len(self.data),
            'columnas': list(self.data.columns)
        }

        return stats