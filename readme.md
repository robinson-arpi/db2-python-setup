
# Proyecto de Conexión a Base de Datos con iSeries Access ODBC Driver

Este proyecto está diseñado para establecer una conexión con una base de datos utilizando el driver ODBC de iSeries Access, y realizar consultas a través de una conexión ODBC.

## Desarrollo

* VSCode
* Python 3.12.3

### Ejecución

Clone el repositorio

> ```
> https://github.com/robinson-arpi/db2-python-setup.git
> ```

Situese en la carpeta del proyecto e instale el requirements.txt

> Instale requirements.txt
>
> ```python
> pip install -r requirements.txt
> ```

> Ejecute la aplicación
>
> ```python
> test_connection.py
> ```
>

## Estructura del Proyecto

```
└── 📁config
    └── __init__.py
    └── constants.py
    └── database_config.ini
└── 📁db
    └── __init__.py
    └── connection.py
    └── queries.py
└── 📁resources
    └── configuring_the_iseries_access_odbc_driver.pdf
└── __init__.py
└── .gitignore
└── readme.md
└── requirements.txt
└── test_connection.py
```

### Descripción de las Carpetas y Archivos

* **config/** : Contiene archivos relacionados con la configuración de la base de datos y constantes necesarias para la conexión.
  * `constants.py`: Este archivo lee el archivo `database_config.ini` y almacena las constantes necesarias para la conexión a la base de datos.
  * `database_config.ini`: Archivo de configuración que contiene las credenciales de la base de datos y la información de conexión.
* **db/** : Contiene la lógica de conexión y consultas a la base de datos.
  * `connection.py`: Módulo responsable de manejar la conexión a la base de datos.
  * `queries.py`: Define las consultas que serán ejecutadas en la base de datos utilizando la conexión establecida.
* **resources/** : Contiene recursos adicionales, como documentación relacionada con la configuración del driver ODBC.
  * `configuring_the_iseries_access_odbc_driver.pdf`: Un documento que explica cómo configurar el driver ODBC para acceder a iSeries.
* **test_connection.py** : Script de prueba para verificar la conexión a la base de datos.



## Instalación del Driver ODBC de IBM para Windows 11

Para poder utilizar el driver ODBC de iSeries Access en Windows 11, sigue los siguientes pasos:

1. **Descargar ACS Windows App Pkg (64-bit):**

- Debes descargar el paquete `ACS Windows App Pkg English (64-bit)` desde la página de IBM o utilizando el archivo adjunto `IBMiAccess_v1r1_WindowsAP_English.zip`.

2. **Descomprimir y ejecutar el instalador:**

- Descomprime el archivo `IBMiAccess_v1r1_WindowsAP_English.zip`.
- Ejecuta el instalador desde la ruta: `IBMiAccess_v1r1_WindowsAP_English\Image64a\setup.exe`.

3. **Configurar el DNS (si es necesario):**

- Dirígete a **Panel de Control** > **Herramientas de Windows** > **ODBC Data Sources (64-bit)**.
- Desde allí puedes configurar los DNS para la conexión ODBC.
- Las configuraciones específicas para DNS están adjuntas en el archivo `configuring_the_iseries_access_odbc_driver.pdf`, que se encuentra en la carpeta `resources/`.

## Configuración de credenciales

1. Asegúrate de que el archivo `database_config.ini` en la carpeta `config/` contenga la información correcta para conectarse a tu base de datos. Aquí un ejemplo de cómo debe verse:

   ```
   [CREDENTIALS]
   UID = tu_usuario
   PWD = tu_contraseña

   [DATABASE]
   DRIVER = {iSeries Access ODBC Driver}
   HOST = xxx.xxx.xxx.xxx
   DATABASE = DATABASE_NAME
   ```

   Si es necesario, ajusta el archivo `constants.py` para asegurarte de que está leyendo correctamente el archivo de configuración. Se utiliza la librería `configparser` para leer este archivo.

## .gitignore

El archivo `.gitignore` está configurado para ignorar archivos temporales, como los generados por entornos virtuales de Python, así como cualquier archivo `.pyc` y `__pycache__/` que se genere durante la ejecución del código.


## Recursos Adicionales

Si necesitas más información sobre la configuración del driver ODBC para iSeries, consulta el archivo PDF ubicado en `resources/configuring_the_iseries_access_odbc_driver.pdf`.

---

¡Gracias por usar este proyecto! Si tienes algún problema o sugerencia, no dudes en abrir un issue o contribuir al proyecto.

<!-- Contact Information -->


<div align="center">
  <h3>Robinson Arpi</h3>
  <p>Computer Science Engineer | Full Stack Developer | Data Analyst</p>
  <h3>Contact Me</h3>
  <a href="https://www.linkedin.com/in/robinson-arpi-ayala-b258821b0">
    <img src="https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  <a href="https://wa.me/593998320642" target="_blank">
    <img src="https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp" />
  </a>
  <a href="mailto:robinson.arpi@gmail.com">
    <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="GMail" />
  </a>
</div>
