# Proy_robotica_2025
## Diseño de robot manipulador de 7 grados de libertad tomando como referencia el robot ES200RDII

## 1 Descripción
El proyecto del curso consiste en dise ̃nar un robot manipulador serial con alguna estructura cinem ́atica
de al menos 6 grados de libertad. Se puede tomar como base la estructura de alg ́un robot existente,
brind ́andole algunas caracter ́ısticas distintivas, o se puede realizar un dise ̃no de cero. Este robot debe
ser luego modelado y controlado. Todo el sistema debe ser implementado usando ROS.

El proyecto ser ́a realizado en grupos de hasta m ́aximo 5 estudiantes. Asimismo, estar ́a compuesto de
dos partes: el reporte escrito (80%) y la presentaci ́on oral (20%).

## 2 Estructura del Reporte
Las partes que debe contener el reporte escrito, con su puntaje, son las siguientes:

### 2.1 Introducci ́on (1 pt)
Se debe indentificar una problem ́atica nacional, la cual debe ser debidamente justificada mediante datos
reales (estad ́ısticas, reportes, etc).

## 2.2 Proposici ́on (1 pt)
Se debe presentar de manera general el robot que se usar ́a, indicando sus caracter ́ısticas principales. Se
debe presentar la manera en que el robot ayudar ́ıa en la problem ́atica presentada. Esta parte deber ́a
ser apoyada por una imagen del robot terminado y de imagenes que representen el entorno en el que
trabajar ́ıa el robot.

### 2.3 Dise ̃no mecatr ́onico (2 pt)
Debe contener una descripci ́on detallada de qu ́e componentes utilizar ́ıa el robot si fuese implementado de
manera real. Debe incluirse la estructura mec ́anica, el sistema de percepci ́on, la actuaci ́on (y transmisi ́on,
de ser aplicable), as ́ı como los elementos que conformar ́ıan el sistema de control.

### 2.4 Modelo del Robot (3 pt)
Debe presentar el modelo del robot en RViz y Gazebo.

• Se debe visualizar el dise ̃no realizado (un boceto inicial mostrando el dimensionado del robot), y
el robot en URDF. Lo m ́ınimo necesario es usar figuras geom ́etricas b ́asicas de RViz, pero con los
par ́ametros de la cadena cinem ́atica dise ̃nada para el robot (1 punto).

• El incluir enmallado (mesh) para las partes del robot tiene un peso de 1 punto.

• La simulaci ́on con Gazebo tiene un peso de 1 punto. Para tener puntaje completo se debe demostrar
la funcionalidad del modelo (movimiento articular b ́asico) con im ́agenes o con alg ́un video.

### 2.5 Cinem ́atica Directa e Inversa (3 pt)

• Se debe mostrar el modelamiento cinem ́atico (usando el m ́etodo geom ́etrico o Denavit-Hartenberg),
as ́ı como algunas configuraciones esperadas y obtenidas a partir del modelo cinem ́atico. La verifi-
caci ́on debe, al menos, realizarse usando RViz (1 punto).

• Se puede utilizar cualquier m ́etodo para el c ́alculo de la cinem ́atica inversa. Se debe mostrar
c ́omo se implement ́o, verificando la validez para diferentes configuraciones (2 puntos). Para tener
puntaje completo, en el caso de usar un m ́etodo num ́erico, se debe incluir gr ́aficos que muestren la
convergencia del algoritmo en diferentes configuraciones.

### 2.6 Control Cinem ́atico (4 pt)

• Se debe obtener el modelo cinem ́atico diferencial del robot, mostrando claramente el procedimiento
seguido para el c ́alculo de los Jacobianos que sean relevantes. Se debe indicar matem ́aticamente
c ́omo se lleg ́o al Jacobiano (justificar el c ́alculo num ́erico con ecuaciones). Se debe, adem ́as, indicar
las posibles configuraciones singulares del robot (2 puntos).

• Se debe implementar control cinem ́atico verificando el movimiento con RViz a trav ́es de la visual-
izaci ́on y de gr ́aficos que muestren el funcionamiento adecuado para diferentes casos. Por facilidad,
se puede solo hacer control de posici ́on (2 puntos).

### 2.7 Din ́amica y Control Din ́amico (2 pt)
• Se debe mostrar de manera detallada el procedimiento seguido para el c ́alculo de la din ́amica
del robot. Se recomienda indicar un ejemplo de la matriz M, C, g obtenidas para al menos una
configuraci ́on particular, indicando dicha configuraci ́on. Se puede utilizar alg ́un paquete como
RBDL (1 punto).

• Debe implementarse dos esquemas de control din ́amico para el robot, mostrando la descripci ́on
te ́orica y pruebas de movimiento con RViz y/o Gazebo. Se debe, adem ́as, incluir figuras que
muestren el comportamiento del sistema sin control y con control (1 puntos).

### 2.8 Validaci ́on de la proposici ́on (2 pt)
Utilizando alguno de los esquemas de control, se deber ́a simular el robot realizando una o varias activi-
dades que demuestren que el robot podr ́a ayudar a resolver la problem ́atica planteada en la introducci ́on.
Aqu ́ı, se deber ́a incluir el entorno gr ́afico necesario para que la simulaci ́on sea comprensible.

### 2.9 Conclusiones y Recomendaciones (1 pt)
Debe contener las conclusiones finales del proyecto y recomendaciones para futuros trabajos.

### 2.10 Anexo: C ́odigo Implementado (1 pt)
Se debe incluir el c ́odigo comentado de las partes m ́as importantes implementadas (no de todos los
programas). De manera alternativa, se puede incluir el enlace de un repositorio de GitHub creado para
el proyecto (en este caso debe indicarse claramente qu ́e archivo implementa qu ́e parte).
2

## Consideraciones Generales

Para cada figura utilizada se debe tener alg ́un comentario pertinente: no basta con incluir la figura, sino
que hay que indicar qu ́e se muestra en dicha figura. Adem ́as, la adecuada redacci ́on, ortograf ́ıa y orden
ser ́an evaluados y se descontar ́a puntos en cada inciso en caso no se presente un trabajo adecuado. Cada
figura y tabla debe tener un t ́ıtulo y numeraci ́on (Tabla 1, Figura 1), y deben ser referenciadas desde el
texto. El reporte se puede presentar en cualquier formato: como reporte (en una sola columna) o como
art ́ıculo (en dos columnas).

## Presentaci ́on Oral
La presentaci ́on oral debe seguir un esquema similar al del reporte, mostrando las partes que se considere
m ́as importantes. La duraci ́on ser ́a de m ́aximo 15 minutos por grupo y todos los integrantes deben realizar
alguna parte de la presentaci ́on. Las presentaciones se realizar ́an durante la semana 15 y la semana 16.

## Evaluaci ́on Individual

Cada integrante de cada grupo llenar ́a una encuesta indicando el nivel de compromiso y trabajo de sus
dem ́as compa ̃neros de grupo, en una escala de 0 a 10, donde 0 es el m ́ınimo valor (no hizo nada) y 10 es
el m ́aximo valor (hizo todo lo requerido de la mejor manera posible). Esta evaluaci ́on no ser ́a revelada
a los dem ́as miembros del grupo y se utilizar ́a para ponderar la nota individual de cada integrante. La
modalidad de la encuesta ser ́a notificada d ́ıas antes de la presentaci ́on.
