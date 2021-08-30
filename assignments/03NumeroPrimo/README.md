![Tec de Monterrey](../../images/logotecmty.png)
# Numero Perfecto

Modifica el programa que se encuentra en la carpeta `src` que se llama
`exercise.py` y que contiene el siguiente código:

```python
def main():
  #escribe tu código abajo de esta línea

if __name__ == '__main__':
    main()
```
La línea `#escribe tu código abajo de esta línea` es un comentario,
el programa la va a ignorar al ejecutarse.

Los divisores propios de un número n son aquellos divisores positivos menores que n.
Un número entero positivo n se dice que es perfecto si la suma de sus divisores propios es igual a n.
Realiza un programa que lea un número y muestre un mensaje indicando si es perfecto o no.


### Entrada
<br>un números que es el numero a verificar  

### Salida
<br>la leyenda "El número es perfecto" o "El NO es némero perfecto"  dependiendo del caso

## Ejemplos de ejecución del programa
<br>Si se teclea
<br>6
<br>El programa mostrará
<br>El número es perfecto
#### NOTA IMPORTANTE:
Tu programa NO debe incluir ningún mensaje para pedir los datos y la salida debe coincidir exactamente con el formato y/o tipo de dato que se te pide como salida.

**Nota:** No te preocupes por esta parte del código
`if __name__ == '__main__':` por el momento.
No la vamos a necesitar para este programa, pero es una buena práctica
incluirla y quedará más claro para que sirve en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con
`python -m pytest --tb=short -v`, subela a tu repositorio en GitHub,
con el proceso de commit + push.
