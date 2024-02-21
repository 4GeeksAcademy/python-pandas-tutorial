# `01.2` Pipenv

Antes de empezar cualquier proyecto de Python, siempre es buena idea crear un nuevo environment (*entorno*). Los entornos aislados de Python previenen errores y hacen que tu aplicación sea independiente.
 
Estamos utilizando `pipenv` como nuestro administrador de paquetes y entornos.

## 📝 Instrucciones:

1. Crea un nuevo entorno. Escribe lo siguiente en tu terminal:

```bash
$ pipenv shell
```

## 💻 Resultado Esperado:

Lee la línea de comando resultante, debería de decir "Lanching subshell..." y ningún error debería ser visible.

![pipenv](../../assets/pipenv.png)

## 💡 Pistas:

+ No incluyas el símbolo `$`.

+ Cada vez que abres un nuevo terminal (también conocido como línea de comando), vas a tener que entrar de nuevo en el entorno escribiendo `pipenv shell`.
