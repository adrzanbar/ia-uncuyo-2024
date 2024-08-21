# Agentes Racionales: Reporte

## Introducción

### Mundo de la aspiradora

Este mundo es tan sencillo que podemos describir todo lo que ocurre; también es un mundo inventado, por lo que podemos inventar muchas variaciones. Este mundo en particular sólo tiene dos lugares: las casillas A y B. El agente de la aspiradora percibe en qué casilla se encuentra y si hay suciedad en ella. Puede elegir entre moverse a la izquierda, a la derecha, aspirar la suciedad o no hacer nada. 

### Descripción general del problema

- Implementar un simulador que determine la medida de rendimiento para el entorno del mundo de la aspiradora según las siguientes especificaciones:
    1. La medida de rendimiento premia con un punto al agente por cada recuadro que limpia (aspira) en un periodo de tiempo concreto, a lo largo de una ≪vida≫ de 1000 acciones.
    2. La ≪dimensión≫ de la grilla se conoce a priori pero la distribución de la suciedad y la localización inicial del agente no se conocen (aleatorio).
    3. Las cuadrículas se mantienen limpias y al aspirar se limpia la cuadrícula en la que se encuentra el agente.
    4. Las acciones permitidas son:
        - Arriba
        - Abajo
        - Izquierda
        - Derecha
        - Limpiar (aspirar)
        - NoHacerNada
    5. Las acciones Izquierda, Derecha, Arriba, Abajo mueven al agente en dichas direcciones, excepto en el caso en que lo puedan llevar fuera de la grilla.
    6. El agente percibe su locación y si esta contiene suciedad.
- Implementar un agente reflexivo simple para el entorno de la aspiradora del ejercicio anterior.

## Marco teórico

### Agentes y entornos

Un **agente** es todo aquello que percibe su entorno a través de sensores y actúa sobre él a través de actuadores.

Utilizamos el término **percepción** para referirnos a las entradas perceptivas del agente en un instante dado. La **secuencia perceptiva** de un agente es la historia completa de todo lo que el agente ha percibido alguna vez.

Decimos que el comportamiento de un agente está descrito por la **función agente** que mapea cualquier secuencia de percepción dada a una acción.

Internamente, la función de agente para un agente artificial será implementada por un **programa de agente**.

Podemos imaginarnos tabulando la función agente que describe a cualquier agente dado.

### Buen comportamiento: el concepto de racionalidad

Un agente **racional** es aquel que hace lo correcto; conceptualmente hablando, todas las entradas de la tabla de la función del agente se rellenan correctamente.

La secuencia de acciones del agente hace que el entorno pase por una secuencia de estados. Si la secuencia es *deseable*, entonces el agente ha actuado bien. Esta noción de deseabilidad se recoge en una **medida de rendimiento** que evalúa cualquier secuencia dada de estados del entorno.

#### Definición de agente racional

> Para cada posible secuencia de percepciones, un agente racional debe seleccionar una acción que se espera que maximice su medida de rendimiento, dada la evidencia proporcionada por la secuencia de percepciones y cualquier conocimiento incorporado que tenga el agente.

### La estructura de los agentes

####  Agentes reflejos simples

Estos agentes seleccionan las acciones de la percepción actual, ignorando el resto de la historia de la percepción.

Los bucles infinitos suelen ser inevitables para los agentes reflejos simples que operan en entornos parcialmente observables. Es posible escapar de los bucles infinitos si el agente puede aleatorizar sus acciones.

####  Agentes reflejos basados en modelos

La forma más eficaz de gestionar la observabilidad parcial es que el agente lleve un registro de la parte del mundo que ahora no puede ver. Es decir, el agente debe mantener algún tipo de **estado interno** que dependa del historial de percepciones y que, por tanto, refleje al menos algunos de los aspectos no observados del estado actual.

Actualizar esta información de estado interno a medida que pasa el tiempo requiere codificar dos tipos de conocimiento en el programa del agente. En primer lugar, necesitamos información sobre cómo evoluciona el mundo independientemente del agente. En segundo lugar, necesitamos información sobre cómo las acciones del agente afectan al mundo.
Este conocimiento sobre «cómo funciona el mundo» -ya sea implementado en circuitos booleanos simples o en teorías científicas completas- se denomina modelo del mundo. Un agente que utiliza un modelo de este tipo se denomina agente basado en un modelo.

## Diseño experimental

Evaluar el desempeño del agente reflexivo, esto es medida de desempeño y unidades de tiempo consumidas, para:

- Entornos de: 2 × 2, 4 × 4, 8 × 8, 16 × 16, 32 × 32, 64 × 64, 128 × 128.
- Porcentaje de suciedad en el ambiente: 0.1, 0.2, 0.4, 0.8

Repetir 10 veces cada combinación.

## Análisis y discusión de resultados

### Agente reflexivo simple



