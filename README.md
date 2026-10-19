# Buscador-Programas
Buscador de Programas Académicos por Prefijos

Descripción:

Este proyecto consiste en desarrollar un buscador de programas académicos utilizando Python. El sistema permite consultar un catálogo de programas mediante la búsqueda por prefijos, mostrando aquellos nombres que comienzan con el texto ingresado por el usuario aplicandose en un contexto real de medellin.

¿Entonces cual seria el objetivo?=
En si seria la aplicación de conceptos de estructuras de datos, yendo específicamente a las cadenas de caracteres(str),diccionarios(dict) y algoritmos de busqueda por preijos aplicandose a una transformacion de dato tipo csv obtenido a partir de una API de medellin, el cual seria medata.


Tecnologías

-Lenguaje: Python.

-Estructuras de datos: Cadenas, diccionarios, listas y tuplas.

-Tipo de dato: cadenas de caracteres (str).

-Métodos utilizados: items(), lower(), strip() y startswith().

-Librerías externas: pandas

Link de la api utilizada: https://medata.gov.co/search/?publisher__name=Medell%C3%8Dn%20en%20Cifras

#redaccion sobre el proceso e implementacion del problema:
Hola soy yojhan martinez al habla para explicar paso a paso (maomenos) el orden en el cual se fue estableciendo el proyecto,e indagar un poco en el contexto.
lo primero seria como la identificacion del problema, en si me base en un proyecto anterior de adquisicion en integracion de datos utilizando los mismos archivos csv, jason(en este caso no lo utilice) basado en un ODS, el 11
para la solucion al congestionamiento vehicular,en particular en este caso utilizaremos el archivo scv: velocidad_e_intensidad_vehicular_en_medellin (1) para transformarlo y leerlo mediante la libreria de pandas para asi obtener
un barrio en el que nos interezaria trabajar, el cual seria la candelaria (Mas que todo porq por ahi se hubica el itm fraternidad).

Una vez separado la localidad q nos intereza creamos otro archivo csv de la candelaria para empezar a trabajar en el(visto en el archivo Transormacion_dato.py).

Lo siguiente seria la utilizacion de cadenas para representar las columnas que yacen en el scv, obteniendo asi los corredores, avenidas  y calles(visto en representacion_cadenas.py).

lugo pasariamos directamente a un diccionario, teniendo ya la representacion de cada columna, que utilizariamos como llave solo quedaria agregarle el contenido de los renglones que nos intereza como la fecha,velocidad,hora,intensida y en
 que sentido proviene,mediante un append.(visto en el almacenamiento_diccionario.py).

y ya por ultimo nos quedaria la busqueda de su contenido , utilizando ya el diccionario previamente creado  ya simplemente podemos indagar en su contenido mediante un prefijo(visto en el buscador_trafico.py)

%to las busquedas posibles para la utilizacion del preijo son  las columnas establecidas en las cadenas que serian:
Avenida 33
Avenida El Poblado
Avenida Ferrocarril
Avenida Oriental
Calle 31
Calle 41 - Los Huesos
Calle 52 - La Playa
Calle 57 - Argentina
Carrera 37
Carrera 57 - Avenida Ferrocarril
San Juan

Y listo, eso seria mi proyecto actual, algo sencillito para facilitar la busqueda de congestionamiento vehicular y en que zona se muestra mas los intervalos de desplazamiento, tipo por si no quieres llegar tarde revisas si a X hora
en la zona Y el trafico esta demaciado lento, o que carrera es mejor tomar.




Autor :
Yojhan Martinez Betancourth

los resultados obtenidos lo puedes visualizar en el apartado de arribas junto a los archivos: trafico_nocturno y graico_velocidad, los cuales son el resultado visual del nivel de congestionamiento de la candelaria 
