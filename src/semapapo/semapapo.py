def semapapo ():
    import sys
    
    if len(sys.argv) <= 1:
        print("diga uma frase!")
        return

    frase = ' '.join(sys.argv[1:]).strip()

    qntd_caracteres = len(frase) + 2

    texto = f"""    {qntd_caracteres*'_'} 
    < {frase} >
     {qntd_caracteres*'-'}"""

    semapinho = f""" {texto}
    {qntd_caracteres*' '}\\
    {qntd_caracteres*' '} \\    __
    {qntd_caracteres*' '}   __/,,\\
    {qntd_caracteres*' '}  \\__|   \\___
    {qntd_caracteres*' '}    |  ___   ⟩
    {qntd_caracteres*' '}    |  \\__]  ⟩
    {qntd_caracteres*' '}     \\______/
    {qntd_caracteres*' '}      _| _|
    {qntd_caracteres*' '}      \/ \/
    """

    print(semapinho)