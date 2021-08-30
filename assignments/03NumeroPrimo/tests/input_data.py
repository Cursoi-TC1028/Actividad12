# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
    (
        ["6"],
        ["","El número es perfecto"],
        "Debe salir: El número es perfecto"
    ),
    # Test case 2
    (
        ["28"],
        ["","El número es perfecto"],
        "Debe salir: El número es perfecto"
    ),
    # Test case 3
    (
        ["52"],
        ["","El NO es número perfecto"],
        "Debe salir: El NO es número perfecto"
    ),
    # Test case 4
    (
        ["8128"],
        ["","El número es perfecto"],
        "Debe salir: El número es perfecto"
    ),
    # Test case 5
    (
        ["1"],
        ["","El NO es número perfecto"],
        "Debe salir: El NO es número perfecto"
)
]
