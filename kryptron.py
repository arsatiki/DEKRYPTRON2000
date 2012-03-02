from string import maketrans, ascii_uppercase

key = "POLTRABENDFIXSCUHJVWYGZQMK"

def maketable(d):
    if d:
        sfrom, sto = zip(*d.items())
    else:
        sfrom, sto = [], []
    return maketrans(''.join(sfrom), ''.join(sto))

message = """Agentti 1101! Keltaisen valtio A:n vakoojat ovat soluttautuneet
yhteiskunnan joka tasolle. Keneenkaan ei voi luottaa.

Kuten tiedat, Keltainen valtio A on totalitaristinen kommunistinen diktatuuri.
Emme saa antaa heidan uhata kansallista ja globaalia hegemoniaamme.

Agentti 1101! Tehtavasi on soluttautua heidan aamupiknikilleen. Siirry
valittomasti huvipuisto Linnanmaen paaportin luokse.

Kaikki jatkoviestit suojataan murtamattomalla DEKRYPTRON 2000 -koneella."""


print message.upper().translate(maketrans(key, ascii_uppercase))