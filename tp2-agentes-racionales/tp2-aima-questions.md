Considere una versión modificada del entorno de la aspiradora en la que el agente es penalizado con un punto por cada movimiento.

## ¿Puede un agente reflejo simple ser perfectamente racional para este entorno? Explíquelo.

Un agente reflejo simple no puede ser perfectamente racional en este entorno modificado de manera porque necesita realizar un seguimiento del estado del entorno que no puede sensar para detenerse. En este nuevo entorno siempre obtendrá la menor medida de desempeño, ya que no se detendrá cuando el mundo esté limpio.

## ¿Y un agente reflejo con estado? Diseñe un agente de este tipo.

Un agente reflejo con estado sí puede ser perfectamente racional en este nuevo entorno, ya que puede determinar cuándo el mundo está limpio y detenerse.

## ¿Cómo cambian tus respuestas si las percepciones del agente le dan el estado limpio/sucio de cada cuadrado del entorno?

En este caso ambos agentes son perfectamente racionales. Dado que el agente puede conocer que ha cumplido su objetivo a través de sus sensores no es necesario un modelo del entorno para que pueda decidir cuando detenerse.