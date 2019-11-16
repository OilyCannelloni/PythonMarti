from datetime import date

d, m, y = [int(input("Podaj {} urodzenia:".format(i))) for i in ["dzień", "miesiąc", "rok"]]
bd = date(y, m, d)
today = date.today()
this_year_bd = date(today.year, m, d)

if today > this_year_bd:
    print("Urodziny w przyszlym roku")

elif this_year_bd != today:
    days_to_next_bd = (this_year_bd - today).days
    print("Do tegorocznych urodzin zostalo {} dni".format(days_to_next_bd))
    gifts = ["pilkę", "komputer", "gitarę"]
    print("Wybierz twoj wymarzony prezent odpowiadając 'tak':")

    for gift in gifts:
        answer = input("Czy chcesz {}?".format(gift))
        if answer.lower() == 'tak':
            print("Za {0} dni dostaniesz {1}".format(days_to_next_bd, gift))
            print("WYCZAROWUJĘ {}!".format(gift.upper()))
            break

else:
    age = today.year - bd.year
    print("Dzisiaj są twoje {} urodziny".format(age))
    print("BALONIKI!")
