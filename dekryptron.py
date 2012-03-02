from string import maketrans, ascii_uppercase
from random import shuffle
from time import sleep
from sys import stdin

s =  """FVHIDDL 1101! ZHCDFLNHI SFCDLB F:I SFZBBRFD BSFD NBCPDDFPDPIHHD
UQDHLNZPIIFI RBZF DFNBCCH. ZHIHHIZFFI HL SBL CPBDDFF.

ZPDHI DLHJFD, ZHCDFLIHI SFCDLB F BI DBDFCLDFELNDLIHI ZBYYPILNDLIHI JLZDFDPPEL.
HYYH NFF FIDFF QHLJFI PQFDF ZFINFCCLNDF RF VCBGFFCLF QHVHYBILFFYYH.

FVHIDDL 1101! DHQDFSFNL BI NBCPDDFPDPF QHLJFI FFYPALZILZLCCHHI. NLLEEU
SFCLDDBYFNDL QPSLAPLNDB CLIIFIYFHI AFFABEDLI CPBZNH.

ZFLZZL RFDZBSLHNDLD NPBRFDFFI YPEDFYFDDBYFCCF JHZEUADEBI 2000 -ZBIHHCCF."""

intro = """Huomenta, agentti 1101.

Organisaatiomme pahoittelee akillista heratysta.
Isanmaa on vaarassa. Tarvitsemme sinua, agentti 1101.
Sina olet ainoa toivomme.

Keltainen valtio A:n agentit vaanivat kaikkialla.
En voi kertoa enempaa suojaamattomalla linjalla.
Pura loppuviesti DEKRYPTRON 2000 -koneella."""

#s = demo_shuffle("Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Donec hendrerit")
def demo_shuffle(source):
    target = list(ascii_uppercase)
    shuffle(target)

    trans = maketrans(ascii_uppercase, ''.join(target))
    return source.upper().translate(trans)

def slow_print(s, line_delay=0):
     for line in s.split('\n'):
         print line
         sleep(line_delay)

def maketable(d):
    if d:
        sfrom, sto = zip(*d.items())
    else:
        sfrom, sto = [], []
    return maketrans(''.join(sfrom), ''.join(sto))

def known_key(d):
    return ''.join(d.get(c, ' ') for c in ascii_uppercase)

def parse_input(i):
    source, sep, target = i.partition('=')
    if not sep:
        source, target = ascii_uppercase, source
    else:
        source = source.upper()
    return zip(source, target)

def main():
    trans = {}

    try:
        slow_print(intro, 1)
        print
        foo = raw_input('PRESS ENTER TO ACTIVATE DEKRYPTRON 2000')
    except KeyboardInterrupt:
        pass

    while True:
        try:
            print '\n' * 25
            print "DEKRYPTRON 2000".center(80)
            print "MESSAGE:"
            print s.translate(maketable(trans))
            print 
            print 'KNOWN KEY :', known_key(trans)
            print '           ', ascii_uppercase

            key = raw_input('ENTER KEY > ')
            
            for f, t in parse_input(key):
                if t.isalpha():
                    trans[f] = t
        except KeyboardInterrupt:
            pass

if __name__ == '__main__':
    main()
