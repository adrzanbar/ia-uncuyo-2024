# Reporte de trabajos prácticos 3 y 4

## Introducción

Frozen lake consiste en cruzar un lago helado desde la salida hasta la meta sin caer en ningún agujero caminando sobre el lago helado.

El juego comienza con el jugador en una posición aleatoria del mundo cuadriculado del lago helado al igual que la meta.

Los agujeros en el hielo se distribuyen en ubicaciones ubicaciones aleatorias y el jugador no puede caminar sobre ellos.

El jugador realiza movimientos hasta alcanzar la meta o quedarse sin vidas.

Los mundos generados aleatoriamente no siempre tendrán un camino hacia la meta.

El jugador puede moverse en cuatro direcciones: izquierda, abajo, derecha y arriba.

## Marco teórico

Se utiliza un tipo de agente basado en objetivos llamado agente de resolución de problemas.
Los agentes de resolución de problemas utilizan representaciones atómicas, es decir, los estados del mundo se consideran enteros, sin estructura interna visible para los algoritmos de resolución de problemas.

La formulación de objetivos, basada en la situación actual y en la medida del rendimiento del agente, es el primer paso en la resolución de problemas.

La formulación del problema es el proceso de decidir qué acciones y estados a considerar, dado un objetivo.

El proceso de buscar una secuencia de acciones que alcance el objetivo se denomina búsqueda. Un algoritmo de búsqueda toma un problema como entrada y devuelve una solución en forma de secuencia de acciones

Una vez encontrada una solución, pueden llevarse a cabo las acciones que recomienda. Esto se denomina fase de ejecución.

Un problema puede definirse formalmente mediante cinco componentes:

- El estado inicial en el que comienza el agente
- Una descripción de las posibles acciones disponibles para el agente.
- Una descripción de lo que hace cada acción; el nombre formal de esto es el modelo de transición.
- La prueba de objetivo, que determina si un estado dado es un estado objetivo.
- Una función de coste del camino que asigna un coste numérico a cada camino. El agente que resuelve el problema elige una función de coste que refleje su propia medida de rendimiento.

Una solución a un problema es una secuencia de acciones que lleva del estado inicial a un estado objetivo. La calidad de la solución se mide por la función de coste del camino, y una solución óptima tiene el coste del camino más bajo entre todas las soluciones.

Los algoritmos de búsqueda se juzgan en función de su completitud, optimalidad, complejidad temporal y complejidad espacial. La complejidad depende de b, el factor de ramificación en el espacio de estados, y d, la profundidad de la solución más superficial.

Los métodos de búsqueda no informada sólo tienen acceso a la definición del problema. Algunos de los algoritmos básicos son los siguientes:
- La búsqueda por amplitud expande primero los nodos menos profundos; es completa, óptima para costes de paso unitarios, pero tiene una complejidad espacial exponencial.
- La búsqueda de coste uniforme expande el nodo con el menor coste de camino, g(n), y es óptima para costes de paso generales.
para costes de paso generales.
- La búsqueda por profundidad expande primero el nodo no expandido más profundo. No es completa ni óptima, pero tiene una complejidad espacial lineal. La búsqueda limitada en profundidad añade un límite de profundidad.

Los métodos de búsqueda informada pueden tener acceso a una función heurística h(n) que estima
el coste de una solución a partir de n.
- La búsqueda A* expande los nodos con un mínimo de f (n) = g(n) + h(n). A* es completo y óptimo, siempre que h(n) sea consistente. La complejidad espacial de A* sigue siendo prohibitiva.

Una heurística h(n) es consistente si, para cada nodo n y cada sucesor n' de n generado por cualquier acción a, el coste estimado de alcanzar la meta desde n no es mayor que el coste de paso de llegar a n' más el coste estimado de alcanzar la meta desde n'.

## Diseño experimental

Se generan 30 entornos aleatorios de FrozenLake de tamaño 100x100 con proabilidad de hoyos de 0.08.

Se evalúa el desempeño de agentes con una vida de 1000 acciones.

Se evalúan dos funciones de costo:

1. Costo constante de 1 por acción
2. El costo de cada acción es es su representación numérica (1 a 4) + 1

El agente utiliza distintos algoritmos para buscar la solución estos son:

- Búsqueda en Anchura
- Búsqueda en Profundidad
- Búsqueda en Profundidad Limitada (límite = 10)
- Búsqueda de Costo Uniforme
- Búsqueda A* con heurística de distancia de Manhattan
- Acciones aleatorias

De cada experimento se registra:

- Cantidad de estados hasta encontrar la solución
- Costo del camino encontrado
- Tiempo de ejecución de la búsqueda

## Análisis y discusión de los resultados

Se adjuntan los gráficos de cajas y extensiones en la carpeta images.

Se observa la búsqueda en profundidad limitada no encuentra soluciones. En general los caminos son más largos que 10.
El agente aleatorio también falla en encontrar soluciones consistentemente debido al límite de vidas.
La búsqueda en profundidad encuentra soluciones pero casi nunca son óptimas.
El algoritmo de búsqueda en anchura y los de tipo de búsqueda óptima (best-first search) visitan la misma cantidad de estados porque encuentran la solución óptima.

En cuanto a los costos de las soluciones encontradas, se observa que la segunda función de costo afecta negativamente el desmpeño de todos los algoritmos. El costo de la búsqueda en profundida es también más elevado debido a que encuentra soluciones con caminos más largos.

Los tiempos de ejecución correlativos con la complejidad del algoritmo y la longitud de la solución, con la excepción de A* para el entorno 1, con un tiempo de ejecución notable por su rapidez.

## Conclusiones

Para este problema una simple búsqueda en profundiad proporciona los mejores desempeños teniendo en cuenta el tiempo de ejecución y no varía mucho con los entornos. A* encuentra la solución óptima con los menores tiempos de ejecución para el primer entorno pero es superado en este aspecto por la búsqueda en profundidad para el segundo.