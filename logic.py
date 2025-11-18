failai = {
    "failas1.txt": [None, "Egzistuoja toks 'skambutis.txt', tačiau jam reikia slaptažodžio. Jo slaptažodis yra MIDI2026."],
    "skambutis.txt": ["MIDI2026",
"""
> ATIDAROMAS FAILAS: stotis/irasai/skambutis.txt
> STATUSAS: 84% ATKURTA
> 2025/11/13 SKAMBUČIO ĮRAŠO TRANSKRIPCIJA

[00:00:02] Antulė Gintarytė: Ei, daktare, durys vėl užsidarė. Atidaryk.
[00:00:05] Dr. Gėlė Saulytė: Ir vėl? ████... Primink durų kodą, prašau?
[00:00:08] Antulė Gintarytė: Ugh, kas darosi šitoj ████████ stoty... Durų kodas yra D67.
[00:00:11] Dr. Gėlė Saulytė: Tuojau atidarysiu. 
[00:00:33] Antulė Gintarytė: [Girdima, kaip atsidaro durys.]
[00:00:38] Antulė Gintarytė: Pagaliau.
[00:00:40] Dr. Gėlė Saulytė: Nežinau... Čia jau apie ██ dienas gličina. Aš klausiau elektriko - jis galvoja, kad kažkas iš vidaus gadina sistemas, bet aš manau, kad čia nesamonė.
[00:00:46] Antulė Gintarytė: Na, man ██████, išsaiškinkit dėl savęs. Tu stoties vadovė, aš tik kartais užsuku.
[00:00:51] Dr. Gėlė Saulytė: Gerai, gerai... Beje, šių durų slaptažodis šiaip yra B3H74, jei vėl užstrigs.
[00:00:57] Antulė Gintarytė: Ačiū. Tikiuosi nereikės naudot, vis tiek ██████ planuoju grįžti atgal į stotį B.I.U.R.A.S. Iki.
[00:01:02] Dr. Gėlė Saulytė: Viso.

> FAILO PABAIGA"""]
}

durys_sarasas = {
    "D67": ["B3H74", True],
    "D29": [None, True],
    "D84": [None, True],
    "D01": [None, True],
    "D09": [None, True],
    "D46": [None, True]
}


def komandos():
    viesi_failai = [f for f, (pw, _) in failai.items() if pw is None]
    viesos_durys = ", ".join(durys_sarasas.keys())
    return f"""
 KKOMANDŲ SĄRAŠAS:

.komandos       : Parodo šias komandas.
.skaityti       : Atidaro failą. Šiuo metu egzistuojantys vieši failai: {", ".join(viesi_failai)}.
.atidaryti_duris: Atidaro duris stotyje. Kai kurios durys reikalauja slaptažodžio. Šiuo metu prieinamos durys: {viesos_durys}
"""


def skaityti(failas):
    if failas not in failai:
        return "> Error 68: Neegzistuoja toks failas."

    pw, content = failai[failas]

    if pw is not None:
        return {
            "ask": f"> ĮVESKITE SLAPTAŽODĮ failui {failas}:",
            "type": "file_pw",
            "target": failas
        }

    return content


def skaityti_su_pw(failas, entered):
    pw, content = failai[failas]
    if entered != pw:
        return "> Neteisingas slaptažodis."
    return content


def atidaryti(durys):
    if durys not in durys_sarasas:
        return "> Error 68: Neegzistuoja tokios durys."

    pw, closed = durys_sarasas[durys]

    if pw is not None:
        return {
            "ask": f"> ĮVESKITE SLAPTAŽODĮ durims {durys}:",
            "type": "door_pw",
            "target": durys
        }

    return flip_durys(durys)


def flip_durys(durys):
    pw, closed = durys_sarasas[durys]

    # invert state
    durys_sarasas[durys][1] = not closed

    if closed:
        return "Durys atidarytos."
    else:
        return "Durys uždarytos."



def atidaryti_su_pw(durys, entered):
    pw, closed = durys_sarasas[durys]
    if entered != pw:
        return "> Neteisingas slaptažodis."
    return flip_durys(durys)


def process_command(cmd):
    parts = cmd.split()
    if not parts:
        return ""

    c = parts[0]
    arg = " ".join(parts[1:])

    if c == ".komandos":
        return komandos()

    if c == ".skaityti":
        if not arg:
            return "> Error 69: Nėra failo pavadinimo."
        return skaityti(arg)

    if c == ".skaityti_pw":
        split = arg.split()
        if len(split) != 2:
            return "> Klaida: reikia nurodyti failą ir slaptažodį."
        failas, pw = split
        return skaityti_su_pw(failas, pw)

    if c == ".atidaryti_duris":
        if not arg:
            return "> Error 69: Nėra durų kodo."
        return atidaryti(arg)

    if c == ".atidaryti_pw":
        split = arg.split()
        if len(split) != 2:
            return "> Klaida: reikia nurodyti durų kodą ir slaptažodį."
        kodas, pw = split
        return atidaryti_su_pw(kodas, pw)

    return "> Error 67: rasyt ismok"
