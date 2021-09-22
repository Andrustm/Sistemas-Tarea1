# Sistemas-Tarea1
Integrantes:
Andrés Daille, Marcelo Luengo, Diego Venegas


El objetivo de esta tarea trata de poner en practica los conceptos RPC y Cache. Por consiguiente se ocupo el lenguaje de python y redis para dar solucion a la problematica de la tarea.



# Instrucciones para la ejecucion de codigo
Para ejecutar la aplicación se debe ejecutar: server.py, cliente_app.py y el servidor de redis previamente instalado, luego en su navegador de preferencia ir a la ruta http://127.0.0.1:5000/inventory/search?q= <- y aqui insertar el producto que desea buscar, cabe destacar que el nombre debe iniciar con mayuscula y que para buscar por más de una palabra poner _ en los espacios.

# Tecnologias ocupadas
Redis
gRPC
Flask


# Configuracion de Redis utilizada
20 mb de ram y protocolo lru, basicamente para que al sobrepasar esta cantidad de almacenamiento, redis elimine el elemento más antiguo.
