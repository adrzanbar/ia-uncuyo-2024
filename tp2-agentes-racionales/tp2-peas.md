# Ejercicio 1

### a) Jugar al CS (Counter-Strike) o cualquier otro 3D Shooter

**PEAS:**
- **Medida de Desempeño:** 
  - Ganar rondas y/o partidas.
  - Conseguir la mayor cantidad de eliminaciones.
  - Minimizar muertes.
  - Completar objetivos (por ejemplo, plantar/desactivar una bomba).
- **Entorno:** 
  - Mapa en 3D con distintos entornos y obstáculos.
  - Oponentes y compañeros de equipo controlados por otros jugadores o IA.
  - Diferentes armas y objetos disponibles.
- **Actuadores:** 
  - Movimientos del personaje (caminar, correr, agacharse, saltar).
  - Disparo de armas.
  - Uso de objetos (granadas, kits de desactivación).
- **Sensores:** 
  - Visión en 3D (pantalla).
  - Audio (sonidos del entorno y de los oponentes).
  - Indicadores en pantalla (munición, salud, etc.).
  
**Propiedades del Entorno:**
- **Observabilidad:** Parcialmente observable (el jugador no puede ver todo el mapa ni las intenciones de los oponentes).
- **Número de Agentes:** Multi-agente (otros jugadores y/o IA).
- **Determinismo:** Estocástico (las acciones de los oponentes son impredecibles).
- **Episódico vs. Secuencial:** Secuencial (cada acción afecta el desarrollo de la partida y el resultado final).
- **Dinámico vs. Estático:** Dinámico (el entorno cambia durante la partida).
- **Discreto vs. Continuo:** Discreto (acciones y estados del juego están bien definidos).
- **Conocido vs. Desconocido:** Conocido (reglas del juego son bien definidas, pero la estrategia del oponente puede ser desconocida).

### b) Explorar los océanos

**PEAS:**
- **Medida de Desempeño:** 
  - Mapeo de áreas nuevas.
  - Recolección de datos científicos (por ejemplo, fauna y flora marina).
  - Minimización de riesgos para el equipo y el vehículo.
- **Entorno:** 
  - Océanos con distintos hábitats y condiciones (profundidad, temperatura, corrientes).
  - Vida marina (peces, mamíferos marinos).
  - Condiciones meteorológicas y marítimas.
- **Actuadores:** 
  - Movimiento del vehículo (submarino o robot).
  - Manipuladores para recoger muestras.
- **Sensores:** 
  - Sonar para navegación y mapeo.
  - Cámaras para imágenes y video.
  - Sensores de temperatura y salinidad.
  - Sensores de profundidad.
  
**Propiedades del Entorno:**
- **Observabilidad:** Parcialmente observable (la visibilidad puede estar limitada y las condiciones pueden cambiar).
- **Número de Agentes:** Generalmente un solo agente (en exploración autónoma) o multi-agente (si hay varios vehículos o investigadores).
- **Determinismo:** Estocástico (el entorno marino es variable y difícil de predecir).
- **Episódico vs. Secuencial:** Secuencial (las decisiones afectan la exploración futura y la seguridad).
- **Dinámico vs. Estático:** Dinámico (las condiciones del océano cambian constantemente).
- **Discreto vs. Continuo:** Continuo (profundidad, temperatura, y ubicaciones están en rangos continuos).
- **Conocido vs. Desconocido:** Desconocido (gran parte del océano sigue sin explorar).

### c) Comprar y vender tokens crypto

**PEAS:**
- **Medida de Desempeño:** 
  - Maximizar ganancias.
  - Minimizar pérdidas.
  - Eficiencia en las transacciones.
- **Entorno:** 
  - Mercados de criptomonedas con diferentes tokens.
  - Fluctuaciones de precios y volúmenes de transacciones.
  - Noticias y eventos que afectan el mercado.
- **Actuadores:** 
  - Ejecución de órdenes de compra y venta.
  - Configuración de alertas y parámetros de trading.
- **Sensores:** 
  - Datos de precios en tiempo real.
  - Información de volumen de transacciones.
  - Noticias del mercado y análisis técnico.
  
**Propiedades del Entorno:**
- **Observabilidad:** Parcialmente observable (la información de mercado puede ser incompleta y cambiante).
- **Número de Agentes:** Multi-agente (otros traders y algoritmos de trading).
- **Determinismo:** Estocástico (los movimientos de precios son impredecibles).
- **Episódico vs. Secuencial:** Secuencial (las decisiones de trading afectan el saldo y las oportunidades futuras).
- **Dinámico vs. Estático:** Dinámico (los precios y la información del mercado cambian rápidamente).
- **Discreto vs. Continuo:** Discreto (transacciones y precios son manejados en intervalos).
- **Conocido vs. Desconocido:** Conocido (las reglas del mercado son conocidas, pero la dinámica es incierta).

### d) Practicar tenis contra una pared

**PEAS:**
- **Medida de Desempeño:** 
  - Precisión y consistencia de los golpes.
  - Mejora de habilidades técnicas (por ejemplo, el control del saque).
- **Entorno:** 
  - Una pared para devolver las pelotas.
  - El área de juego.
- **Actuadores:** 
  - Golpes de raqueta.
  - Movimiento del jugador.
- **Sensores:** 
  - Vista del entorno (pelota, pared, líneas del campo).
  - Sensación táctil de la raqueta y la pelota.
  
**Propiedades del Entorno:**
- **Observabilidad:** Totalmente observable (el entorno es completamente visible).
- **Número de Agentes:** Un solo agente (el jugador).
- **Determinismo:** Determinístico (la pared devuelve la pelota de manera predecible).
- **Episódico vs. Secuencial:** Secuencial (el golpe actual determina la trayectoria de la pelota para el golpe siguiente).
- **Dinámico vs. Estático:** Estático (la pared no cambia y el entorno permanece constante).
- **Discreto vs. Continuo:** Discreto (los golpes son eventos individuales).
- **Conocido vs. Desconocido:** Conocido (las reglas y el comportamiento de la pared son bien entendidos).

### e) Realizar un salto de altura

**PEAS:**
- **Medida de Desempeño:** 
  - Altura alcanzada.
  - Técnica del salto (estilo y forma).
- **Entorno:** 
  - Área de salto.
  - Barra de altura ajustable.
- **Actuadores:** 
  - Movimiento del cuerpo durante el salto.
- **Sensores:** 
  - Visión de la barra y el área de aterrizaje.
  - Sensación táctil del cuerpo y el suelo.
  
**Propiedades del Entorno:**
- **Observabilidad:** Totalmente observable (el área y la barra son visibles).
- **Número de Agentes:** Un solo agente (el atleta).
- **Determinismo:** Determinístico (el salto sigue principios físicos predecibles).
- **Episódico vs. Secuencial:** Episódico (cada salto es una acción independiente).
- **Dinámico vs. Estático:** Estático (el entorno de salto no cambia).
- **Discreto vs. Continuo:** Discreto (cada intento de salto es un evento separado).
- **Conocido vs. Desconocido:** Conocido (las reglas del salto de altura y los principios físicos son bien conocidos).

### f) Pujar por un artículo en una subasta

**PEAS:**
- **Medida de Desempeño:** 
  - Ganar el artículo al menor precio posible.
  - Maximizar el valor recibido en relación con el precio pagado.
- **Entorno:** 
  - Subasta con otros pujadores.
  - Artículo en subasta.
  - Información sobre el artículo y las pujas actuales.
- **Actuadores:** 
  - Realización de pujas.
  - Estrategias de puja (modificación de la oferta).
- **Sensores:** 
  - Información sobre el artículo (descripción, precio inicial).
  - Información sobre las pujas actuales y los pujadores.
  
**Propiedades del Entorno:**
- **Observabilidad:** Parcialmente observable (puede no conocer las intenciones de otros pujadores).
- **Número de Agentes:** Multi-agente (otros pujadores están involucrados).
- **Determinismo:** Estocástico (las decisiones de otros pujadores son impredecibles).
- **Episódico vs. Secuencial:** Secuencial (las pujas afectan el resultado final y pueden depender de pujas anteriores).
- **Dinámico vs. Estático:** Dinámico (las pujas y el estado de la subasta cambian en tiempo real).
- **Discreto vs. Continuo:** Discreto (las pujas se realizan en incrementos específicos).
- **Conocido vs. Desconocido:** Conocido (las reglas de la subasta son establecidas, pero las estrategias de otros pujadores pueden ser desconocidas).
