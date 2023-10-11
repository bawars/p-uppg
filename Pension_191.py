# Vår klass Pension med attribut beskrivandes den information vi söker
# om en person och dess sparande.
class Pension:
    def __init__(self, name,age,savings,growth):
        self.name = name
        self.age = age
        self.savings = savings
        self.growth = growth

# Syfte: Vår metod 'result' beräknar den pension vi söker. Detta görs genom att nyttja några av klassens attribut.
# Pensionen räknas ut som en geometrisk summa (variabel a). Kapital sparas till och med pensionsåldern 65.
    def result(self):
        amount=self.savings
        rate=1+(self.growth/100)
        years=65-self.age
        if years < 0:
            return 0

        a=(amount * (1 - pow(rate, years))) / (1 - rate)
        return int(a)

#dundermetoder för att printa klassinstansers tilldelade värden och sortera/jämföra dem med varandra.
#då namn och pensionssparande är av intresse är det dem som printas.
    def __str__(self):
        return " {}: {}".format(self.name, self.result())

    def __gt__(self, other):
        return self.result() < other.result()



#Syfte: konvertera sifferelement i en sträng. (str)-->(str); str(int) --> float
def convert(elem: str):
    if not elem.isdigit():
        return elem
    return float(elem)

#vi tillämpar ovanstående funktion på en hel rad av strängar.
def convert_row(r: list) -> list:
   return [convert(e) for e in r]


#Syfte: att behandla datan i textfilen för att erhålla den i önskat format.
#Namn förblir i (str) format medan ålder och sparande konverteras till floats.
#Detta görs dels med hjälp av ovan definierade funktioner.
def process_data(filepath):
    with open(filepath, encoding="utf-8") as f:
        raw_data = f.readlines()
        data = [row[:-1].split("/") for row in raw_data]
        data = [convert_row(row) for row in data]
    return data

#Syfte: Inhämtande av tillväxttakt
def get_growth(msg: str = "Enter growth rate: "):
    return float((input(msg).strip()))


def main():

    data=process_data('personer.txt')
    pensions = [Pension(*i, get_growth()) for i in data]
    pensions=sorted(pensions)

    for p in pensions:
        print(p)

main()