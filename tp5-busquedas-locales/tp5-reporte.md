# Trabajo Práctico N° 5. Reporte

## Introducción

El objetivo del problema de las 8 reinas es colocar ocho reinas en un tablero de ajedrez de forma que ninguna reina ataque a otra. (Una reina ataca a cualquier pieza de la misma fila, columna o diagonal).

Una formulación de estado completo comienza con las 8 reinas en el tablero y las mueve de un lado a otro.

## Marco Teórico

Los algoritmos de búsqueda que hemos visto hasta ahora están diseñados para explorar espacios de búsqueda de forma sistemática. Esta sistematicidad se consigue manteniendo uno o más caminos en la memoria y registrando qué alternativas se han explorado en cada punto del camino. Cuando se encuentra un objetivo, el camino hacia ese objetivo también constituye una solución al problema. En muchos problemas, sin embargo, el camino hacia la meta es irrelevante. Por ejemplo, en el problema de las 8 reinas lo que importa es la configuración final de las reinas, no el orden en que se añaden.

Si el camino a la meta no importa, podríamos considerar una clase diferente de algoritmos, los que no se preocupan por los caminos en absoluto. Los algoritmos de búsqueda local operan utilizando un único nodo actual (en lugar de múltiples caminos) y generalmente se mueven sólo a los vecinos de ese nodo. Normalmente, los caminos seguidos por la búsqueda no se conservan. Aunque los algoritmos de búsqueda local no son sistemáticos, tienen dos ventajas clave: (1) utilizan muy poca memoria, normalmente una cantidad constante; y (2) a menudo pueden encontrar soluciones razonables en espacios de estados grandes o infinitos (continuos) para los que los algoritmos sistemáticos son inadecuados.

Un paisaje tiene tanto «localización» (definida por el estado) como «elevación» (definida por el valor de la función de coste heurístico o función objetivo). Si la elevación corresponde al coste, el objetivo es encontrar el valle más bajo, un mínimo global; si la elevación corresponde a una función objetivo, el objetivo es encontrar el pico más alto, un máximo global. (Los algoritmos de búsqueda local exploran este paisaje). Un algoritmo de búsqueda local completo siempre encuentra un objetivo si existe; un algoritmo óptimo siempre encuentra un mínimo/máximo global.

El algoritmo «Hill Climbing» (versión de ascenso más pronunciado) es simplemente un bucle que se mueve continuamente en la dirección del valor creciente, es decir, cuesta arriba. Termina cuando alcanza un «pico» en el que ningún vecino tiene un valor superior. El algoritmo no mantiene un árbol de búsqueda, por lo que la estructura de datos del nodo actual sólo necesita registrar el estado y el valor de la función objetivo. El algoritmo no mira más allá de los vecinos inmediatos del estado actual.

Hill climbing se denomina a veces búsqueda local greedy porque agarra un buen estado vecino sin pensar con antelación a dónde ir a continuación. 

Máximos locales: un máximo local es un pico superior a cada uno de sus estados vecinos pero inferior al máximo global. Los algoritmos Hill Climbing que alcanzan las proximidades de un máximo local se ven arrastrados hacia arriba, hacia el pico, pero se quedan atascados y no tienen adónde ir.

Mesetas: una meseta es una zona plana del paisaje espacio-estatal. Puede ser un máximo local plano, desde el que no existe salida ascendente, o un hombro, desde el que es posible progresar. Una búsqueda Hill Climbing puede perderse en una meseta.

En cada caso, el algoritmo llega a un punto en el que no avanza. Partiendo de un estado de 8 reinas generado aleatoriamente, el algoritmo de ascenso más pronunciado se atasca el 86% de las veces y sólo resuelve el 14% de los problemas. Trabaja con rapidez, dando sólo 4 pasos de media cuando tiene éxito y 3 cuando se atasca, lo que no está nada mal para un espacio de estados con 88 ≈ 17 millones de estados.

Se han inventado muchas variantes de hill climbing. El hill climbing estocástico elige al azar entre los movimientos cuesta arriba; la probabilidad de selección puede variar con la inclinación del movimiento cuesta arriba.

Se garantiza que un algoritmo de ascenso que nunca realiza movimientos «cuesta abajo» hacia estados con menor valor (o mayor coste) es incompleto, porque puede quedarse atascado en un máximo local. Por el contrario, un recorrido puramente aleatorio, es decir, hacia un sucesor elegido uniformemente al azar del conjunto de sucesores, es completo pero extremadamente ineficiente. Por lo tanto, parece razonable intentar combinar la escalada con un recorrido aleatorio de forma que se consiga eficiencia y exhaustividad. El recocido simulado es un algoritmo de este tipo.

Se garantiza que un algoritmo de ascenso que nunca realiza movimientos «cuesta abajo» hacia estados con menor valor (o mayor coste) es incompleto, porque puede quedarse atascado en un máximo local. Por el contrario, un recorrido puramente aleatorio, es decir, hacia un sucesor elegido uniformemente al azar del conjunto de sucesores, es completo pero extremadamente ineficiente. Por lo tanto, parece razonable intentar combinar la escalada con un recorrido aleatorio de forma que se consiga eficiencia y exhaustividad. Simulated annealing es un algoritmo de este tipo.

El bucle más interno del algoritmo de simulated annealing es bastante similar al de hill climbing. Sin embargo, en lugar de elegir el mejor movimiento, elige un movimiento aleatorio. Si el movimiento mejora la situación, siempre se acepta. En caso contrario, el algoritmo acepta el movimiento con una probabilidad menor que 1. La probabilidad disminuye exponencialmente con la «maldad» del movimiento, es decir, la cantidad ΔE en la que empeora la evaluación. La probabilidad también disminuye a medida que baja la «temperatura» T: Los movimientos «malos» tienen más probabilidades de ser permitidos al principio cuando T es alta, y se vuelven más improbables a medida que T disminuye. Si el programa disminuye T lo suficiente, el algoritmo encontrará un óptimo global con una probabilidad cercana a 1.

Mantener sólo un nodo en memoria podría parecer una reacción extrema al problema de las limitaciones de memoria. El algoritmo de búsqueda local beam mantiene un registro de k estados en lugar de sólo uno. Comienza con k estados generados aleatoriamente. En cada paso, se generan todos los sucesores de los k estados. Si alguno es un objetivo, el algoritmo se detiene.

En su forma más simple, la búsqueda local de haces puede adolecer de falta de diversidad entre los k estados, que pueden concentrarse rápidamente en una pequeña región del espacio de estados, lo que convierte la búsqueda en poco más que una costosa versión de hill climbing. Una variante llamada búsqueda beam estocástica, análoga a la hill climbing estocástico, ayuda a paliar este problema. En lugar de elegir el mejor k del conjunto de sucesores candidatos, la búsqueda estocástica en haz elige k sucesores al azar, siendo la probabilidad de elegir un sucesor determinado una función creciente de su valor.

Un algoritmo genético es una variante de la búsqueda estocástica beam en la que los estados sucesores se generan combinando dos estados padres en lugar de modificando un único estado.

Para cada pareja a aparear, se elige aleatoriamente un punto de cruce. Por último, cada lugar se somete a una mutación aleatoria con una pequeña probabilidad independiente.

## Diseño experimental

Se ejecuta 30 veces cada algoritmo para problemas de 4, 8 y 10 reinas. 

Para el hill climbing no se establece un límite de estados. 

Para simulated annealing se elige una función de enfriamiento exponencial $T(t) = k \cdot e^{-\lambda t}$ con k=100 y $\lambda$=0.005. El límite se establece en 1000 iteraciones. La probabilidad de que se acepte un movimento hacia abajo es de $p = e^{\Delta E/T}$.

Para el algoritmo genetico se utiliza una población $n = 50$ aleatoria y una probabilidad de mutación $p = 0.1$ y un límite de 1000 generaciones.

## Análisis y discusión de resultados

Para hill climbing la cantidad de estados es variable pero en general menor que el resto de los algoritmos. Dado que se detiene al encontrar un máximo (local o global). Es también de los más rápidos, la mayoría de las ejecuciones no superan los 0.03 segundos. Para problemas pequeños (N=4) es completo, pero se pierde en máximos locales la mayoría de las veces para problemas más grandes.

Dado que en la descripción formal de simulated annealing no se establece una prueba de detención temprana, el algoritmo utilizará todas las iteraciones (recorrerá todos los estados hasta llegar al límite, en este caso de 1000). Por esta razón también sus tiempos de ejecución son mayores que los de hill climbing, llegando a superar el segundo. Tiene una taza de éxito mucho mejor que hill climbing, pero aún así no llega a ser completo.

El algoritmo genético sí tiene una prueba de detención temprana, por lo tanto la cantidad de estados varía en función de su éxito para encontrar una solución. Para problemas más pequeños realiza pocas iteraciones comparables a las de hill climbing, pero escala rápidamente con el tamaño del problema llegando al máximo de generaciones establecido. Cada iteración es también más compleja que los anteriores algoritmos por lo que un aumento en la cantidad de estados causa un aumento también en el tiempo de ejecución, siendo el más lento para problemas más grandes superando los 15 segundos. Para problemas más grandes su efectividad disminuye a 0.

## Conclusiones

En general los 3 algoritmos no parecen ser la mejor opción para problemas que no sean de optimización (como es el caso de N reinas). Hill climbing tiene falencias ya mencionadas que no pueden ser corregidas. 

Simulated annealing puede mejorarse con una prueba de detención temprana. También se requiere un buen etnendimiento del problema y experimentación para idear una buena función de enfriamiento, ya que esta tiene un gran impacto en la tasa de éxtios.

De forma análoga, el algoritmo genético puede ser muy efectivo si se le proporciona una población inicial elegida inteligentemente. Pero eligiendo una población inicial aleatoria no llega a tener una buena tasa de éxitos, y por lo tanto tampoco es rápido (llega al límite de generaciones facilmente)