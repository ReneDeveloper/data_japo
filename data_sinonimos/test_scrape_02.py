#test_scrape_02.py

import requests
from bs4 import BeautifulSoup
import sqlite3

class GeneradorSinonimos:
    def __init__(self, db_name='sinonimos.db'):
        # URL base de Sinonimos.com
        self.base_url = 'https://www.sinonimos.com/sinonimo.php?palabra='
        # Inicializa la conexión a la base de datos
        self.conn = sqlite3.connect(db_name)
        self.crear_tabla()
    
    def crear_tabla(self):
        # Crea la tabla si no existe
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS sinonimos (
                    palabra TEXT PRIMARY KEY,
                    sinonimos TEXT
                )
            ''')

    def obtener_sinonimos_web(self, palabra):
        """Obtiene los sinónimos de la palabra desde Sinonimos.com"""
        url = f"{self.base_url}{palabra}"
        response = requests.get(url)
        
        if response.status_code != 200:
            print("Error al obtener datos de la página")
            return []
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Selector CSS para extraer sinónimos en defbox > ol > a
        sinonimos = [elem.text.strip() for elem in soup.select('.defbox ol li a')]
        return sinonimos

    def guardar_sinonimos(self, palabra, sinonimos):
        """Guarda los sinónimos en la base de datos"""
        sinonimos_str = ','.join(sinonimos)
        with self.conn:
            self.conn.execute('''
                INSERT OR REPLACE INTO sinonimos (palabra, sinonimos)
                VALUES (?, ?)
            ''', (palabra, sinonimos_str))

    def obtener_sinonimos_db(self, palabra):
        """Obtiene los sinónimos de la base de datos"""
        cursor = self.conn.execute('SELECT sinonimos FROM sinonimos WHERE palabra = ?', (palabra,))
        row = cursor.fetchone()
        if row:
            return row[0].split(',')
        return []

    def obtener_sinonimos(self, palabra):
        """Obtiene los sinónimos desde la base de datos o, si no están, desde la web"""
        # Primero intenta obtener los sinónimos desde la base de datos
        sinonimos = self.obtener_sinonimos_db(palabra)
        
        # Si no se encuentran en la base de datos, realiza el scraping
        if not sinonimos:
            sinonimos = self.obtener_sinonimos_web(palabra)
            if sinonimos:
                # Guarda los sinónimos en la base de datos para futuras consultas
                self.guardar_sinonimos(palabra, sinonimos)
        
        return sinonimos

# Ejemplo de uso
generador = GeneradorSinonimos()
palabra = "sabroso"
sinonimos = generador.obtener_sinonimos(palabra)
print(f"Sinónimos de '{palabra}': {sinonimos}")
