![Tec de Monterrey](../../images/logotecmty.png)
# Suma de dígitos
Ciclos - Suma de digitos

Escribe un programa que muestre la suma de los dígitos de un número entero, el número puede ser positivo o negativo, la suma siempre será positiva.

Modifica el programa que se encuentra en la carpeta `src` que se llama
`exercise.py` y que contiene el siguiente código:

```python
def main():
    num = int(input("Escribe un numero entero: "))
    #escribe tu código abajo de esta línea
    pass

if __name__ == '__main__':
    main()
```

La línea `#escribe tu código abajo de esta línea` es un comentario,
el programa la va a ignorar al ejecutarse.

La salida del programa debe de ser solamente el resultado, sin leyendas ni mensajes, debe ser de la siguiente forma:

```
Escribe un numero entero: 2975
23
```

```
Escribe un numero entero: -517
13
```



**Nota:** No te preocupes por esta parte del código
`if __name__ == '__main__':` por el momento.
No la vamos a necesitar para este programa, pero es una buena práctica
incluirla y quedará más claro para que sirve en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con
`python -m pytest --tb=short -v`,
subela a tu repositorio en GitHub, con el proceso de commit + push.
