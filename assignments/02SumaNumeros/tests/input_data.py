# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
    (
        ["100","200","3000"],
        ["","","","suma = 3300","cantidad de números = 3"],
        "Debe salir\n3300"
    ),
    (
        ["100","200","50","430","250"]
        ["","","","","","suma = 1030","cantidad de números = 5"],
        "Debe salir\n1030"
    ),
    (
        ["100","2000"],
        ["","","suma =2100","cantidad de números = 2"],
        "Debe salir\n2100"
    ),
    (
        ["150","256","500","55","100"],
        ["","","","","","suma =1061","cantidad de números = 5"],
        "Debe salir\n1061"
    )
]
