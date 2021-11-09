def start():
    print("Hi, welkom bij dit keuzeverhaal.")
    name = input('Wat is je naam? >>')

    print (f"{name} welk land kies je?")
    print("A Nederland")
    print("B Irak")
    print("C Afghanistan")

    afkomst = input('>>')

    if afkomst.lower() == 'a':
        print("Je heb hebt Nederland gekozen. De regering daar probeert nu de grootse machtstaat van Europa te worden, daarvoor indoctrineren ze de bevolking ook bepalen ze nu wat je doet en kiest hun verkozen geloof voor jou wat doe je?")
        print("A Je accepteert het besluit van de overheid en nu kiezen zij een geloof vor je")
        print("B Je accepteert het besluit van de overheid niet en gaat er tegen in.")

        keuze_a = input('>>')

        if keuze_a.lower() == 'a':
            print("Je hebt het geloof dat je regering voor je gekozen heb aangenomen.")
            print("De overheid heeft besloten dat geen  eigen mening meer hebt. Je moet het altijd met hun eens zijn, zoniet treden ze hard op.")
            print("Wat ga je doen?")
            print("A Je accepteer het niet en gaat tegen het besluit van de overheid in.")
            print("B Je vlucht weg van de overheid omdat je, je mening wilt uiten hoe jij dat wilt.")

            keuze_a1 = input('>>')

            if keuze_a1.lower() == 'a':
                print("Je bent tegen de overheid in gegaan, en nu kiezen je om je op te pakken wegens niet doen wat je overheid doet. Je moet uit het land vluchten. Waar ga je naartoe vluchten?")
                print("A Parijs")
                print("B Los Angeles")

                keuze_a2 = input('>>')

                if keuze_a2.lower() == 'a':
                    print("Je heb gekozen om naar Parijs te vluchten. Helaas heeft iemand je veraden en ben je onderweg vermoord.")
                    print("GAME OVER!")
                elif keuze_a2.lower() == 'b':
                    print("Je bent naar Los Angeles gevlucht. Je bent veilig, goed gedaan!")

        elif keuze_a.lower() == 'b':
            print("Je hebt het geloof niet aangenomen, en je hebt een slecht artikel over de overheid geschreven.")
            print("De overheid heeft je opgepakt en proberen hun je te overtuigen van hun mening via marteling. Wat doe je?")
            print("A Je geeft toe aan de overheid en neemt hun mening aan.")
            print("B Je geeft niet toe aan de overheid en blijft bij je eigen standpunt.")

            keuze_a3 = input('>>')

            if keuze_a3.lower() == 'a':
                print("Je neemt de mening aan van de overheid en ze laten je vrij. Wat doe je?")
                print("A Je vlucht")
                print("B Je blijft in Nederland.")

                keuze_a4 = input('>>')

                if keuze_a4.lower() == 'a':
                    print("Je bent veilig gevlucht uit Nederland en je leeft gellukig verder.")
                elif keuze_a4.lower() == 'b':
                    print("Je bent in Nederland gebleven en je bent alsnog doodgemaakt door de overheid.")
                    print("GAME OVER!")

            if keuze_a3.lower() == 'b':
                print("Je geeft niet toe aan de mening van de overheid en je word doodgemaakt door middel van marteling.")
                print("GAME OVER!")

    elif afkomst.lower() == 'b':
        print("Je bent in Irak. Er is een oorlog uitgebroken tegen de corrupte staat. Wat ga je doen?")
        print("A Je kiest ervoor om mee te vechten.")
        print("B Je vlucht naar een ander land van oorlog is te gevaarkijk voor je.")

        keuze_b = input('>>')

        if keuze_b.lower() == 'a':
            print("Je gaat vecht mee, maar wordt neergeschoten")
            print("GAME OVER!")

        elif keuze_b.lower() == 'b':
            print("Je bent gevlucht, naar welk land ga je?")
            print("A Duitsland")
            print("B Turkijë")

            keuze_b2 = input('>>')

            if keuze_b2.lower() == 'a':
                print("Je probeert te vluchten naar Duitsland, om naar Duitsland te gaan moet je eerst via buurland Turkije. Maak een keuze :")
                print("1")
                print("2")

                keuze_b3 = input('>>')

                if keuze_b3.lower() == '1':
                    print("Je bent veilig in Turkije aangekomen.")
                    print("Je stapt op een vliegtuig naar Duitsland, en leeft daar lang en gellukig.")
                elif keuze_b3.lower() == '2':
                    print("Dat was een domme keuze, je wordt neergeschoten en overleid")
                    print("GAME OVER!")

            elif keuze_b2.lower() == 'b':
                print("Je vlucht naar Turkije.")
                print("Je bent veilig in Turkijë gekomen en je leeft lang en gelukkig.")

    elif afkomst.lower() == 'c':
        print("Je bent in Afghanistan. De taliban zit in het land.De Verenigde Staten valt binnen. Wat doe je?")
        print("A Je helpt de Verenigde Staten helpen om de taliban weg te krijgen uit Afghanistan.")
        print("B Je vlucht weg van de oorlog.")

        keuze_c = input('>>')

        if keuze_c.lower() == 'a':
            print("Je gaat de Verenigde Staten helpen de taliban weg te krijgen uit Afghanistan.")
            print("vecht je mee met de Verenigde staten?")
            print("A Ja")
            print("B Nee")

            keuze_c1 = input('>>')

            if keuze_c1.lower() == 'a':
                print("Je word doodgeschoten door de taliban.")
                print("GAME OVER!")
            elif keuze_c1.lower() == 'b':
                print("Je bent veilig weggevlucht en je leeft lang en gelukkig.")

        elif keuze_c.lower() == 'b':
            print("Je vlucht weg van de oorlog.")
            print("Je leeft lang en gelukkig.")
    else:
        print("Dit is  keuze.")
        print(f"{name} wil je het nog een keer proberen?\n type Y/N")

        option = input('>>')

        if option.lower() == 'y':
            start()
        else:
            exit()



start()
