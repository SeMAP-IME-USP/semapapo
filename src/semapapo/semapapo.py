from pathlib import Path

MARCADOR_INICIO = "# >>> semapapo >>>"
MARCADOR_FINAL  = "# <<< semapapo <<<"

def configurar ():
    bashrc = Path.home() / ".bashrc"
    config_dir = Path.home() / ".semapapo"
    config_file = config_dir / "bashrc"
    
    config_dir.mkdir(exist_ok=True)

    config_file.write_text("""
hora=$(date +%H)
hora=$((10#$hora))
frase="agora são $(date '+%H:%M')"

if (( hora >= 4 && hora < 11 )); then
    msg="bom dia! $frase"
elif (( hora >= 11 && hora < 13 )); then
    msg="já pode? $frase"
elif (( hora >= 13 && hora < 15 )); then
    msg="café? $frase"
elif (( hora >= 15 && hora < 18 )); then
    msg="boa tarde! $frase"
elif (( hora >= 18 && hora < 20 )); then
    msg="boa noite! $frase"
elif (( hora >= 20 )); then
    msg="sextou! $frase"
else
    msg="tá acordado pq? $frase"
fi

semapapo $msg
""")

    source_block = f"""{MARCADOR_INICIO}
source "{config_file}"
{MARCADOR_FINAL}
"""

    conteudo = bashrc.read_text() if bashrc.exists() else ""

    if MARCADOR_INICIO not in conteudo:
        with bashrc.open("a") as f:
            f.write("\n" + source_block)

def desconfigurar ():
    bashrc = Path.home() / ".bashrc"
    config_dir = Path.home() / ".semapapo"
    config_file = config_dir / "bashrc"

    # removendo a saudacao
    if bashrc.exists():
        conteudo = bashrc.read_text()

        inicio = conteudo.find(MARCADOR_INICIO)
        final  = conteudo.find(MARCADOR_FINAL)

        if inicio != -1 and final != -1:
            final += len(MARCADOR_FINAL)
            conteudo = conteudo[:inicio] + conteudo[final:]
            bashrc.write_text(conteudo)
    
    # remove o bashrc personalizado
    if config_file.exists():
        config_file.unlink()
    
    # remove a pasta se estiver vazia
    if config_dir.exists() and not any(config_dir.iterdir()):
        config_dir.rmdir()


def semapapo ():
    import sys
    
    if len(sys.argv) <= 1:
        print("diga uma semafrase!")
        return

    frase = ' '.join(sys.argv[1:]).strip()

    if frase[0] == "-":
        if sys.argv[1] == "-c" or sys.argv[1] == "--configurar":
            configurar()
        elif sys.argv[1] == "-d" or sys.argv[1] == "--desconfigurar":
            desconfigurar()
        else:
            print("semacomando não identificado! use:")
            print("\t -c, --configurar: para configurar o bash")
            print("\t -d, --desconfigurar: para desconfigurar o bash")
        return

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
