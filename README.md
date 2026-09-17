# Proyecto Urban Grocers

## Descripción
Este proyecto automatiza la lista de comprobación para el campo `name` en la
solicitud de creación de un kit de producto de la aplicación Urban Grocers.
Las pruebas están escritas en Python usando la librería `requests` para
enviar solicitudes HTTP y `pytest` como framework de pruebas.

## Estructura del proyecto
- `configuration.py`: contiene la URL del servicio y las rutas de los endpoints.
- `data.py`: contiene los cuerpos de solicitud (bodies) y los headers utilizados.
- `sender_stand_request.py`: contiene las funciones que envían las solicitudes HTTP.
- `create_kit_name_kit_test.py`: contiene las 9 pruebas automatizadas de la lista de comprobación.

## Cómo ejecutar las pruebas

1. Clona este repositorio en tu computadora.
2. Crea un entorno virtual e instala las dependencias necesarias:
```
pip install requests pytest
```
3. Inicia el servidor de Urban Grocers y copia la URL generada.
4. Abre el archivo `configuration.py` y actualiza la variable `URL_SERVICE`
   con la URL de tu servidor.
5. Ejecuta las pruebas desde la terminal, dentro de la carpeta del proyecto:
```
pytest create_kit_name_kit_test.py
```