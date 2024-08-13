# Bruteforce Login Script

Este es un script en Python para intentar iniciar sesión en un servidor local usando un ataque de fuerza bruta con el archivo de contraseñas `rockyou.txt`.

## Requisitos

- Python 3.x
- Archivo de contraseñas `rockyou.txt`

### Descargar rockyou.txt
rockyou.txt es un archivo de contraseñas comúnmente usado en pruebas de seguridad y pentesting.

Puedes descargar rockyou.txt desde varios recursos en línea. Asegúrate de hacerlo desde una fuente confiable.

### Uso del Script
Clona o descarga este repositorio en tu máquina local.
Asegúrate de que el servidor en localhost esté corriendo en el puerto 6969.
Ejecuta el script:
* `python3 main.py`
#### Nota
El script intentará iniciar sesión en http://localhost:6969/client/login utilizando el nombre de usuario angelqui y todas las contraseñas de rockyou.txt.

El script mostrará el estado de cada intento y se detendrá cuando encuentre la contraseña correcta.

### Advertencia
Este script es solo para fines educativos. No uses este script para actividades no autorizadas. El uso no autorizado de este script puede ser ilegal.