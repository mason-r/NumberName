number = input("How many zeroes does your number have? ")
numZeroes = int(number)

if numZeroes < 3:

  shortScale = 0
  match numZeroes:
    case 0: print("Your number is in the ones.")
    case 1: print("Your number is in the tens.")
    case 2: print("Your number is in the hundreds.")
    case _: print("what") #if the input is negative

else: #this is where the fun begins

  import math
  shortScale = math.floor((numZeroes-3)/3) #gets short scale of a number; e.g. trillions (twelve through fourteen zeroes) is 3 from "tri"llion

  if 0 <= shortScale < 10: #thousands to nonillions

    match shortScale:
      case 0: ones = "thousands"
      case 1: ones = "millions"
      case 2: ones = "billions"
      case 3: ones = "trillions"
      case 4: ones = "quadrillions"
      case 5: ones = "quintillions"
      case 6: ones = "sextillions"
      case 7: ones = "septillions"
      case 8: ones = "octillions"
      case 9: ones = "nonillions"

    print("Your number is in the " + ones + ".")

  elif 10 <= shortScale < 100: #decillions to novemnonagintillions

    tensScale = math.floor(shortScale/10) #gets decillion, vigintillion, trigintillion, etc
    onesScale = shortScale - tensScale*10 #gets un-, duo-, tre-, quattuor-, etc

    match tensScale:
      case 1: tens = "decillions"
      case 2: tens = "vigintillions"
      case 3: tens = "trigintillions"
      case 4: tens = "quadragintillions"
      case 5: tens = "quinquagintillions"
      case 6: tens = "sexagintillions"
      case 7: tens = "septuagintillions"
      case 8: tens = "octogintillions"
      case 9: tens = "nonagintillions"

    match onesScale:
      case 0: ones = "" #empty string for when there is no ones prefix
      case 1: ones = "un"
      case 2: ones = "duo"
      case 3: ones = "tre"
      case 4: ones = "quattuor"
      case 5: ones = "quin"
      case 6: ones = "sex"
      case 7: ones = "septen"
      case 8: ones = "octo"
      case 9: ones = "novem"

    print(shortScale)
    print("Your number is in the " + ones + tens + ".")

  elif 100 <= shortScale < 1000: #centillions to novemnonagintinongentillions (SS 999)

    hundsScale = math.floor(shortScale/100) #gets centillion, ducentillion, trecentillion, etc
    tensScale = math.floor((shortScale - hundsScale*100)/10)
    onesScale = shortScale - (hundsScale*100 + tensScale*10)

    match hundsScale:
      case 1: hunds = "centillions"
      case 2: hunds = "ducentillions"
      case 3: hunds = "trecentillions"
      case 4: hunds = "quadringentillions"
      case 5: hunds = "quingentillions"
      case 6: hunds = "sescentillions"
      case 7: hunds = "septingentillions"
      case 8: hunds = "octingentillions"
      case 9: hunds = "nongentillions"

    match tensScale:
      case 0: tens = ""
      case 1: tens = "deci"
      case 2: tens = "viginti"
      case 3: tens = "triginti"
      case 4: tens = "quadraginti"
      case 5: tens = "quinquaginti"
      case 6: tens = "sexaginti"
      case 7: tens = "septuaginti"
      case 8: tens = "octoginti"
      case 9: tens = "nonaginti"

    match onesScale:
      case 0: ones = ""
      case 1: ones = "un"
      case 2: ones = "duo"
      case 3: ones = "tre"
      case 4: ones = "quattuor"
      case 5: ones = "quin"
      case 6: ones = "sex"
      case 7: ones = "septen"
      case 8: ones = "octo"
      case 9: ones = "novem"

    print("Your number is in the " + ones + tens + hunds + ".")

  elif 1000 <= shortScale < 1e6: #millillions to novemnonagintinongentimillinovemnonagintinongentillions. this is where the fun REALLY begins

    hundThousScale = math.floor(shortScale/100000)
    tenThousScale = math.floor((shortScale - hundThousScale*100000)/10000)
    thousScale = math.floor((shortScale - (hundThousScale*100000 + tenThousScale*10000))/1000)
    hundsScale = math.floor((shortScale - (hundThousScale*100000 + tenThousScale*10000 + thousScale*1000))/100)
    tensScale = math.floor((shortScale - (hundThousScale*100000 + tenThousScale*10000 + thousScale*1000 + hundsScale*100))/10)
    onesScale = shortScale - (hundThousScale*100000 + tenThousScale*10000 + thousScale*1000 + hundsScale*100 + tensScale*10)

    match hundThousScale:
      case 0: hundThous = ""
      case 1: hundThous = "centi"
      case 2: hundThous = "ducenti"
      case 3: hundThous = "trecenti"
      case 4: hundThous = "quadringenti"
      case 5: hundThous = "quingenti"
      case 6: hundThous = "sescenti"
      case 7: hundThous = "septingenti"
      case 8: hundThous = "octingenti"
      case 9: hundThous = "nongenti"

    match tenThousScale:
      case 0: tenThous = ""
      case 1: tenThous = "deci"
      case 2: tenThous = "viginti"
      case 3: tenThous = "triginti"
      case 4: tenThous = "quadraginti"
      case 5: tenThous = "quinquaginti"
      case 6: tenThous = "sexaginti"
      case 7: tenThous = "septuaginti"
      case 8: tenThous = "octoginti"
      case 9: tenThous = "nonaginti"

    if hundThousScale == 0 and tenThousScale == 0: #only for short scales less than 10,000

      match thousScale:
        case 1: thous = ""
        case 2: thous = "du"
        case 3: thous = "tre"
        case 4: thous = "quadri"
        case 5: thous = "quinti"
        case 6: thous = "sexti"
        case 7: thous = "septi"
        case 8: thous = "octi"
        case 9: thous = "noni"

    else:

      match thousScale:
        case 0: thous = ""
        case 1: thous = "un"
        case 2: thous = "duo"
        case 3: thous = "tre"
        case 4: thous = "quattuor"
        case 5: thous = "quin"
        case 6: thous = "sex"
        case 7: thous = "septen"
        case 8: thous = "octo"
        case 9: thous = "novem"

    match hundsScale:
      case 0: hunds = ""
      case 1: hunds = "centillions"
      case 2: hunds = "ducentillions"
      case 3: hunds = "trecentillions"
      case 4: hunds = "quadringentillions"
      case 5: hunds = "quingentillions"
      case 6: hunds = "sescentillions"
      case 7: hunds = "septingentillions"
      case 8: hunds = "octingentillions"
      case 9: hunds = "nongentillions"

    match tensScale:
      case 0: tens = ""
      case 1: tens = "deci"
      case 2: tens = "viginti"
      case 3: tens = "triginti"
      case 4: tens = "quadraginti"
      case 5: tens = "quinquaginti"
      case 6: tens = "sexaginti"
      case 7: tens = "septuaginti"
      case 8: tens = "octoginti"
      case 9: tens = "nonaginti"

    match onesScale:
      case 0: ones = ""
      case 1: ones = "un"
      case 2: ones = "duo"
      case 3: ones = "tre"
      case 4: ones = "quattuor"
      case 5: ones = "quin"
      case 6: ones = "sex"
      case 7: ones = "septen"
      case 8: ones = "octo"
      case 9: ones = "novem"

    if hundsScale == 0 and tensScale == 0: #short scale of 1000, 20007, 400009, etc

      print("Your number is in the " + tenThous + hundThous + thous + ones + "millillions.")

    elif hundsScale == 0:

      print("Your number is in the " + thous + tenThous + hundThous + "milli" + ones + tens + "llions.")

    else:

      print("Your number is in the " + thous + tenThous + hundThous + "milli" + ones + tens + hunds + ".")

  elif 1e6 <= shortScale < 1e9: #micrillions to *inhale* novemnonagintinongentimicrillinovemnonagintinongentimillinovemnonagintinongentillions.

    print("ooh the number gettin really big now!")

    hundMilScale = math.floor(shortScale/1e8)
    tenMilScale = math.floor((shortScale - hundMilScale*1e8)/1e7)
    milScale = math.floor((shortScale - (hundMilScale*1e8 + tenMilScale*1e7))/1e6)
    hundThousScale = math.floor((shortScale - (hundMilScale*1e8 + tenMilScale*1e7 + milScale*1e6))/100000)
    tenThousScale = math.floor((shortScale - (hundMilScale*1e8 + tenMilScale*1e7 + milScale*1e6 + hundThousScale*100000))/10000)
    thousScale = math.floor((shortScale - (hundMilScale*1e8 + tenMilScale*1e7 + milScale*1e6 + hundThousScale*100000 + tenThousScale*10000))/1000)
    hundsScale = math.floor((shortScale - (hundMilScale*1e8 + tenMilScale*1e7 + milScale*1e6 + hundThousScale*100000 + tenThousScale*10000 + thousScale*1000))/100)
    tensScale = math.floor((shortScale - (hundMilScale*1e8 + tenMilScale*1e7 + milScale*1e6 + hundThousScale*100000 + tenThousScale*10000 + thousScale*1000 + hundsScale*100))/10)
    onesScale = math.floor(shortScale - (hundMilScale*1e8 + tenMilScale*1e7 + milScale*1e6 + hundThousScale*100000 + tenThousScale*10000 + thousScale*1000 + hundsScale*100 + tensScale*10))
    #onesScale keeps returning a decimal so I have to use floor now

    print(shortScale, hundMilScale, tenMilScale, milScale, hundThousScale, tenThousScale, thousScale, hundsScale, tensScale, onesScale)

    match hundMilScale:
      case 0: hundMil = ""
      case 1: hundMil = "centi"
      case 2: hundMil = "ducenti"
      case 3: hundMil = "trecenti"
      case 4: hundMil = "quadringenti"
      case 5: hundMil = "quingenti"
      case 6: hundMil = "sescenti"
      case 7: hundMil = "septingenti"
      case 8: hundMil = "octingenti"
      case 9: hundMil = "nongenti"

    match tenMilScale:
      case 0: tenMil = ""
      case 1: tenMil = "deci"
      case 2: tenMil = "viginti"
      case 3: tenMil = "triginti"
      case 4: tenMil = "quadraginti"
      case 5: tenMil = "quinquaginti"
      case 6: tenMil = "sexaginti"
      case 7: tenMil = "septuaginti"
      case 8: tenMil = "octoginti"
      case 9: tenMil = "nonaginti"

    if tenMilScale == 0 and hundMilScale == 0:

      match milScale:
        case 1: mil = ""
        case 2: mil = "du"
        case 3: mil = "tre"
        case 4: mil = "quadri"
        case 5: mil = "quinti"
        case 6: mil = "sexti"
        case 7: mil = "septi"
        case 8: mil = "octi"
        case 9: mil = "noni"

    else:

      match milScale:
        case 0: mil = ""
        case 1: mil = "un"
        case 2: mil = "duo"
        case 3: mil = "tre"
        case 4: mil = "quattuor"
        case 5: mil = "quin"
        case 6: mil = "sex"
        case 7: mil = "septen"
        case 8: mil = "octo"
        case 9: mil = "novem"

    match hundThousScale:
      case 0: hundThous = ""
      case 1: hundThous = "centi"
      case 2: hundThous = "ducenti"
      case 3: hundThous = "trecenti"
      case 4: hundThous = "quadringenti"
      case 5: hundThous = "quingenti"
      case 6: hundThous = "sescenti"
      case 7: hundThous = "septingenti"
      case 8: hundThous = "octingenti"
      case 9: hundThous = "nongenti"

    match tenThousScale:
      case 0: tenThous = ""
      case 1: tenThous = "deci"
      case 2: tenThous = "viginti"
      case 3: tenThous = "triginti"
      case 4: tenThous = "quadraginti"
      case 5: tenThous = "quinquaginti"
      case 6: tenThous = "sexaginti"
      case 7: tenThous = "septuaginti"
      case 8: tenThous = "octoginti"
      case 9: tenThous = "nonaginti"

    if hundThousScale == 0 and tenThousScale == 0: #only for short scales less than 10,000

      match thousScale:
        case 1: thous = ""
        case 2: thous = "du"
        case 3: thous = "tre"
        case 4: thous = "quadri"
        case 5: thous = "quinti"
        case 6: thous = "sexti"
        case 7: thous = "septi"
        case 8: thous = "octi"
        case 9: thous = "noni"

    else:

      match thousScale:
        case 0: thous = ""
        case 1: thous = "un"
        case 2: thous = "duo"
        case 3: thous = "tre"
        case 4: thous = "quattuor"
        case 5: thous = "quin"
        case 6: thous = "sex"
        case 7: thous = "septen"
        case 8: thous = "octo"
        case 9: thous = "novem"

    match hundsScale:
      case 0: hunds = ""
      case 1: hunds = "centillions"
      case 2: hunds = "ducentillions"
      case 3: hunds = "trecentillions"
      case 4: hunds = "quadringentillions"
      case 5: hunds = "quingentillions"
      case 6: hunds = "sescentillions"
      case 7: hunds = "septingentillions"
      case 8: hunds = "octingentillions"
      case 9: hunds = "nongentillions"

    match tensScale:
      case 0: tens = ""
      case 1: tens = "deci"
      case 2: tens = "viginti"
      case 3: tens = "triginti"
      case 4: tens = "quadraginti"
      case 5: tens = "quinquaginti"
      case 6: tens = "sexaginti"
      case 7: tens = "septuaginti"
      case 8: tens = "octoginti"
      case 9: tens = "nonaginti"

    match onesScale:
      case 0: ones = ""
      case 1: ones = "un"
      case 2: ones = "duo"
      case 3: ones = "tre"
      case 4: ones = "quattuor"
      case 5: ones = "quin"
      case 6: ones = "sex"
      case 7: ones = "septen"
      case 8: ones = "octo"
      case 9: ones = "novem"

    if hundMilScale == 0 and tenMilScale == 0 and 

shortScale = str(shortScale)
print("That's " + shortScale + " in short scale.")
