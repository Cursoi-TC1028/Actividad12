![Tec de Monterrey](../../images/logotecmty.png)
# Números primos
Ciclos - Números primos

Escribe un programa que reciba un entero y devuelva True si es un número primo y False si NO es un número primo.  
Para este ejercicio, vamos a asumir que los numeros primos inician en 2.

Modifica el programa que se encuentra en la carpeta `src` que se llama
`exercise.py` y que contiene el siguiente código:

```python
def main():
    num = int(input("Escribe un numero entero : "))
    #escribe tu código abajo de esta línea
    pass

if __name__ == '__main__':
    main()
```

La línea `#escribe tu código abajo de esta línea` es un comentario,
el programa la va a ignorar al ejecutarse.

La salida del programa debe de ser solamente un True o un False de la siguiente forma:

```
Escribe un numero entero : 1
False
```

```
Escribe un numero entero : -3
False
```

```
Escribe un numero entero : 5
True
```

**Nota:** No te preocupes por esta parte del código
`if __name__ == '__main__':` por el momento.
No la vamos a necesitar para este programa, pero es una buena práctica
incluirla y quedará más claro para que sirve en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con
`python -m pytest --tb=short -v`,
subela a tu repositorio en GitHub, con el proceso de commit + push.
