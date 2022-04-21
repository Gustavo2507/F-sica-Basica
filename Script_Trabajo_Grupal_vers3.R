################################################################################
####################### TRABAJO GRUPAL - ESTADÍSTICA CON R #####################
#######################  INTEGRANTES:                 ##########################
#######################  Faride Altamirano Zevallos   ##########################
#######################  Myke Salazar Quispe           ##########################
#######################  Carlos Vidal Herrera          ##########################
#######################                                ##########################
#######################                               ##########################
#######################                               ##########################
################################################################################

######## I PRIMERA PARTE

#a)	Que es un vector.
#   Es un conjunto lineal de datos, esta colección de datos debe ser del mismo tipo.
#b)	Indicar que tipo de estructuras permiten los vector, listas y matriz.
#   Un vector permite: datos de tipo numérico, caracter, complejo o lógico, pero del mismo tipo.
#c)	Por qué se dice que Rstudio se trabaja en estructuras.
#   Porque presenta información estructurada en paquetes y librerías que permiten 
#   el manejo de bases de datos, el análisis estadístico y representaciones gráficas.
#d)	Para que sirven los data.frame.
#   Data.frame es una función que nos ayuda a crear data frames con distinto tipos de datos.

######## II SEGUNDA PARTE

#a)	Los 501 primeros pares, siendo un número que contenga igual cantidad de valores positivos y negativos.
a<-seq(from=-510, to= 510, length.out=501)
a
length(a)
# b) Un vector de 35 elementos quw contengan valores que van del -5 al -200.
b<-seq(-5,-200, length.out=35)  
b
length(b)
# c) Una serie que empiece en 12 con un intervalo de 1.35; esta serie debe contener 30 elementos.
c<-seq(12,52,by=1.35)
c
length (c)
#d)	Graficar las ventas del día por color. Las ventas fueron 
# (rojo, azul, verde, rojo, azul, blanco, naranja, verde, azul, rojo, naranja, blanco, amarillo, azul)

vec_color<-c("rojo", "azul", "verde", "rojo", "azul", "blanco", "naranja", "verde", 
         "azul", "rojo", "naranja", "blanco", "amarillo", "azul")

graf_01<-barplot(table(vec_color),xlab="Color",main="Ventas del día por color", 
                 col=c("yellow","blue","white","orange","red","green"))

#e)	La tangente de 35°.
e<-tan(35*pi/180)
e

#f) Sea la función

f<-function(x,y){(x^2+pi^x+y^8)/(pi+sin(58*pi/180))}
f(3,6)

#g)	Definir la ecuación general de orden 3:

g<-function(x,a,b,c,d){a*x^3+b*x^2+c*x+d}

g(3,5,2,3,1)
g(10,5,2,3,1)
g(12,5,2,3,1)
g(19,5,2,3,1)

vecg<-c(163,5231,8965,35075)
vecg
which.max(vecg) #Ubicación del valor máximo
which.min(vecg) #Ubicación del valor mínimo


######## III PARTE OPERATVA

# 1) Generando los vectores
genero<-c("h","m","m","h","m","h")
edad<-c(23,45,34,39,60,52)
colesterol<-c(230,241,190,150,201,278)
colesterolrango<-c("201-260","201-260","<=200","<=200","201-260",">260")

# 2) Generando el data frame

BD01<-data.frame(genero=genero,edad=edad,rango_coleterol=colesterolrango)
str(BD01)

# 3) Genera en resutlados separados la media de la edad y colesterol

media_edad<-mean(BD01$edad)
media_edad

media_colesterol<-mean(colesterol)
media_colesterol

# 4)	Generar la suma de los cuadrados de la edad

func_SC<-function(x){sum(x^2)}
suma_cuad_edad<-func_SC(BD01$edad)
suma_cuad_edad

# 5) Suma de datos de colesterol para hombres y mujeres

datos_colesterol_sexo<-aggregate(edad~genero,data = BD01,
                                    FUN=sum)
datos_colesterol_sexo

######## TERCERA PARTE

# Cargando el excel y las libreriras

setwd("C:\\Users\\cvida\\OneDrive\\CURSOS Y CAPACITACIONES\\CURSO_R\\EXAMEN")
getwd()

library("readxl")
library("dplyr")
BD_ventas_total<-read_excel("PRACTICA.xlsx",sheet="Hoja1")
View(BD_ventas_total)

# a) Generando un data.frame con las variables cargo, edad e ingreso

head(BD_ventas_total)

BD_ventas_01<-data.frame(BD_ventas_total$CARGO, BD_ventas_total$EDAD, BD_ventas_total$INGRESOS)
BD_ventas_01
head(BD_ventas_01)
names(BD_ventas_01)
BD_ventas_01<-rename(BD_ventas_01, Cargo=BD_ventas_total.CARGO, Edad=BD_ventas_total.EDAD, 
                     Ingresos=BD_ventas_total.INGRESOS)
names(BD_ventas_01)

# (a.a) Indicar la media de los ingresos y la edad
head(BD_ventas_01)
Media_Ingresos01<-mean(BD_ventas_01$Ingresos)
Media_Ingresos01

Media_Edad01<-mean(BD_ventas_01$Edad)
Media_Edad01

# (a.b) Indicar la suma de los ingresos y la edad

Suma_ingresos01<-sum(BD_ventas_01$Ingresos)
Suma_ingresos01

Suma_edad01<-sum(BD_ventas_01$Edad)
Suma_edad01

# (a.c) Indicar el rango de los ingresos y la edad

rango_ingresos<-range(BD_ventas_01$Ingresos)
rango_ingresos

rango_edad<-range(BD_ventas_01$Edad)
rango_edad

# (a.d) Graficar los ingresos y la edad

View(BD_ventas_01)
str(BD_ventas_01)
summary(BD_ventas_01)

grafica_Historgram_Ingresos<-hist(BD_ventas_01$Ingresos,
                                  col="mediumpurple1", 
                                  xlab="Ingresos (S/.)", 
                                  ylab = "Frecuencia", 
                                  main="Gráfico 1. Histograma de los Ingresos")

grafica_Historgram_Edad<-hist(BD_ventas_01$Edad, 
                              col="darkolivegreen1", 
                              xlab="Edad (años)",
                              ylab = "Frecuencia", main="Gráfico 2. Histograma de la Edad")

#b)	Generar una base que contenga los ingresos por cargos y edad.

names(BD_ventas_total)
BD_ingresos_cargos_edad<-select(BD_ventas_total, CARGO, INGRESOS, EDAD)
names(BD_ingresos_cargos_edad)
str(BD_ingresos_cargos_edad)
View(BD_ingresos_cargos_edad)

#c)	Generar una base que sólo muestre las zonas quienes tiene ingresos mayores a S/ 3500.
names(BD_ventas_total)
View (BD_ventas_total)
BD_ingresos_ciudad<-select(BD_ventas_total, INGRESOS, CIUDAD)
BD_ciudad_por_ingresos=subset(BD_ingresos_ciudad,INGRESOS>3500,)
BD_ciudad_por_ingresos
View(BD_ciudad_por_ingresos)

#d)	Generar un gráfico de dispersión de las edades e ingresos.

#Ambas variables son cuantitativas por lo que se realizará un diagrama de dispersión
grafica_dispersión<- plot(BD_ventas_01$Ingresos,BD_ventas_01$Edad, pch=20, cex=1, 
                          col="royalblue2", 
                          bg="darkblue", 
                          xlab="Ingresos S/.", 
                          ylab="Edad (años)", 
                          main="Gráfico 3. Diagrama de dispersión de los ingresos y la edad")




