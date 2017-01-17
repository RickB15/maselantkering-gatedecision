NAPRotterdam = 2.8
NAPDordrecht = 0

if NAPRotterdam == None:
    if NAPDordrecht == None:
        print('er zijn geen weerstations actief, allarm!')
    elif NAPDordrecht <= 2.64:
        kleurencode = 'Groen'
        print(kleurencode)
    elif NAPDordrecht >= 2.65 and NAPDordrecht <= 2.89:
        kleurencode = 'Geel'
        print('Sent mail naar waterbeheerders')
        print(kleurencode)
    elif NAPDordrecht >= 2.90 and NAPDordrecht <= 3.19:
        kleurencode = 'Oranje'
        print('Sent mail naar waterbeheerders')
        print('Ligt 4 uur van tevoren het scheepsvaartverkeer in')
        print('Leg 2 uur van tevoren het scheepsvaartverkeer stil')
        print('Sluit de deuren')
        sluisdeuren = 'dicht'
        print(kleurencode)
    elif NAPDordrecht >= 3.20:
        kleurencode = 'Rood'
        print('Sent mail naar waterbeheerders')
        print('Geef een landelijk allarm en evacueer bewooners')
        print('Ligt 4 uur van tevoren het scheepsvaartverkeer in')
        print('Leg 2 uur van tevoren het scheepsvaartverkeer stil')
        print('Sluit de deuren')
        sluisdeuren = 'dicht'
        print(kleurencode)
elif NAPRotterdam <= 2.74:
    kleurencode = 'Groen'
    print(kleurencode)
elif NAPRotterdam >= 2.75 and NAPRotterdam <= 2.99:
    kleurencode = 'Geel'
    print('Sent mail naar waterbeheerders')
    print(kleurencode)
elif NAPRotterdam >= 3.00 and NAPRotterdam <= 3.29:
    kleurencode = 'Oranje'
    print('Sent mail naar waterbeheerders')
    print('Ligt 4 uur van tevoren het scheepsvaartverkeer in')
    print('Leg 2 uur van tevoren het scheepsvaartverkeer stil')
    print('Sluit de deuren')
    sluisdeuren = 'dicht'
    print(kleurencode)
elif NAPRotterdam >= 3.30:
    kleurencode = 'Rood'
    print('Sent mail naar waterbeheerders')
    print('Geef een landelijk allarm en evacueer bewooners')
    print('Ligt 4 uur van tevoren het scheepsvaartverkeer in')
    print('Leg 2 uur van tevoren het scheepsvaartverkeer stil')
    print('Sluit de deuren')
    sluisdeuren = 'dicht'
    print(kleurencode)
if NAPRotterdam <= 2.74 and NAPDordrecht <= 2.63:
    print('sluit de deuren')
