import sys

frase = ' '.join(sys.argv[1:]).strip()

qntd_caracteres = len(frase) + 2

texto = f"""{qntd_caracteres*'_'} 
< {frase} >
 {qntd_caracteres*'-'}"""

semapinho = f""" {texto}
{qntd_caracteres*' '}\\    __
{qntd_caracteres*' '} \\  /,,)
{qntd_caracteres*' '}   <>   \\____
{qntd_caracteres*' '}    |  \\++>  ⟩
{qntd_caracteres*' '}     \\______/
{qntd_caracteres*' '}      _|_|
"""

print(semapinho)