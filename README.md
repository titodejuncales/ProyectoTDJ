# ProyectoTDJ
## Creado por Titodejuncales

## Cómo instalar y ejecutar el proyecto

- Instalar Python
- Instalar Django
- Ejecutar las migraciones

  $python manage.py makemigrations
  
  $python manage.py migrate
  
- Ejecutar el proyecto

  $python manage.py runserver

## Acerca del proyecto
Se trata de una página web para la venta de camisetas de fútbol.
La página cuenta con tres secciones: camisetas nacionales, camisetas internacionales y camisetas de selecciones.
En cada una de estas secciones vas a encontrar dos botones para acceder, por un lado a la creación de nuevos artículos, 
y por otro a la búsqueda de artículos ya generados. 
En la subsección de creación de nuevos artículos se encuentra un formulario con todos los campos necesarios para dar
de alta nuevas camisetas. Una vez completo el formulario, presionamos el botón "guardar" y los datos ingresados quedan
registrados en nuestra base de datos.
Por otro lado, en la subsección de búsqueda de artículos, se encuentra un campo para completar con el nombre del club
del cual deseas buscar camisetas. Luego con el botón de buscar la página arroja los resultados que contienen el valor
ingresado.


