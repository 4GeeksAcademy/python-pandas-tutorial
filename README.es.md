# Pandas for machine learning

Pandas es la mejor y más popular biblioteca de [Python](https://4geeks.com/es/lesson/que-es-python-tutorial) para machine learning. Esta biblioteca ofrece una amplia variedad de funciones que te ayudarán a manipular datos, optimizar tu algoritmo de machine learning y mucho más. Este tutorial te ayudará a familiarizarte con esta biblioteca y dominar las funcionalidades más utilizadas con ejemplos de código y tutoriales en video que te ayudarán a crear tu primer marco de datos (data frame), limpiar un dataset de información, leer archivos CSV, entre otras cosas...

Los ejercicios en este tutorial han sido creados en aproximadamente 60 horas de desarrollo por expertos en machine learning y revisados cuidadosamente por nuestros [colaboradores](https://github.com/4GeeksAcademy/python-functions-programming-exercises/graphs/contributors) para asegurarnos de que tengas la información más precisa e importante que te ayudará a comenzar tu carrera en machine learning.

## Tabla de Contenidos

En este tutorial, veremos las funciones más importantes y básicas proporcionadas por Pandas que te ayudarán a trabajar con datos en machine learning. A continuación, algunos de los temas que se cubrirán en este tutorial son:

| Ejercicio     | Descripción del tema                                                                                                    |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
|Instalar Pandas | Estos ejercicios cubren cómo instalar Pandas, cómo importar la biblioteca Pandas en un archivo de Python, y cómo crear tu primer script en Python.          |
|DataSets       | Estos ejercicios explican qué son los conjuntos de datos y cómo trabajar con ellos.                                                                                |
|Series         | Estos ejercicios explican qué son las series en Pandas y cómo usarlas.                                                                    |
|DataFrames     | Estos ejercicios explican cómo crear un DataFrame de información y qué funciones se pueden usar para trabajar con ellos.                                    |
|Clean DataSets | Esta clase cubre qué es la limpieza de datos, las funciones que Pandas ofrece para limpiar un DataSet, y las mejores prácticas para limpiar un DataSet. |

## Tutorial de Instalación

Hay dos formas de iniciar este tutorial, la primera y más fácil es abrir el tutorial en un entorno en la nube como **Codespaces** o **Gitpod**, y la segunda es clonar este repositorio en tu entorno local.

> Recomendamos que utilices **Codespaces**, ya que es la forma más fácil y rápida de comenzar el tutorial.

### 1. Abrir el tutorial en un entorno en la nube

Puedes iniciar este tutorial en tan solo unos segundos con Codespaces haciendo clic en el siguiente enlace: [abrir en codespaces](https://codespaces.new/?repo=4GeeksAcademy/python-pandas-tutorial) (recomendado) o puedes usar **Gitpod** haciendo clic en: [abrir en gitpod](https://gitpod.io#https://github.com/4GeeksAcademy/python-pandas-tutorial).

> Una vez que hayas abierto el entorno en la nube, ya sea **Codespaces** o **Gitpod**, los ejercicios de LearnPack deberían comenzar automáticamente. Si los ejercicios no comienzan automáticamente, puedes abrir una terminal y escribir el siguiente comando: `learnpack start`.

### 2. Abrir el tutorial en tu entorno local

Para iniciar este tutorial en tu entorno local, sigue los siguientes pasos:

1.  Abre una terminal y clona este repositorio en tu entorno local usando el siguiente comando:

```bash
git clone https://github.com/4GeeksAcademy/python-pandas-tutorial.git 
```

2. Asegúrate de tener instalada una versión de Node.js igual o superior a `12.01.1`:

```bash
node --version
```

3. Instala LearnPack, el gestor de paquetes para tutoriales de aprendizaje, y también ejecuta el complemento del compilador de Python para LearnPack con los siguientes comandos:
 
```bash
> npm i learnpack -g
> learnpack plugins:install learnpack-python
```

4. Por último, instala Jest para realizar las pruebas necesarias a lo largo del tutorial y comienza los ejercicios con los siguientes comandos:

```bash
> npm i jest@24.8.0 -g
> learnpack start
```

## Colaboradores

Queremos expresar nuestro más profundo agradecimiento a los siguientes colaboradores por su valioso apoyo en la creación de este tutorial.

| Colaborador       | Cuenta de GitHub                                  |
|-------------------|-----------------------------------------------------|
| Alejandro Sanchez | [alesanchezr](https://github.com/alesanchezr)       |
| Martín Suárez     | [kiddopro](https://github.com/kiddopro)             |
| Lorena Gubaira    | [Lorenagubaira](https://github.com/Lorenagubaira)   |
| Tomas Gonzalez    | [tommygonzaleza](https://github.com/tommygonzaleza) |
| Hernán García     | [hernanjkd](https://github.com/hernanjkd)           |
| Ernesto Gonzalez  | [UmiKami](https://github.com/UmiKami)               |
| Hector Chocobar   | [hchocobar](https://github.com/hchocobar)           |
| Charly Chacón     | [Charlytoc](https://github.com/Charlytoc)           |
| Agustín Fernández | [Dasher83](https://github.com/Dasher83)             |
| Ignacio Cordoba   | [nachovz](https://github.com/nachovz)               |

Este tutorial y muchos otros ejercicios están diseñados para estudiantes como parte del [Bootcamp de Programación](https://4geeksacademy.com/us/coding-bootcamp) de 4Geeks Academy. Actualmente, tenemos dos cursos disponibles. El primero es el Curso de [Desarrollador Full Stack](https://4geeksacademy.com/us/coding-bootcamps/part-time-full-stack-developer), en este curso aprenderás tecnologías como HTML5, CSS3, JavaScript, Python, Flask, SQL y muchas otras. El segundo es el [Bootcamp de Data Science](https://4geeksacademy.com/us/coding-bootcamps/datascience-machine-learning) donde aprenderás tecnologías como Python, fundamentos de algoritmos, Pandas, bases de datos SQL y muchas otras tecnologías. Puedes encontrar más información sobre estos cursos y el próximo curso de Blockchain y Web3 en la página web oficial de [4Geeks Academy](http://4geeksacademy.com/).

