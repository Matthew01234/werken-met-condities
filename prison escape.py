import time
loop = True
def gameover():
    print('        ░██████╗░░█████╗░███╗░░░███╗███████╗  ░█████╗░██╗░░░██╗███████╗██████╗░')
    print('        ██╔════╝░██╔══██╗████╗░████║██╔════╝  ██╔══██╗██║░░░██║██╔════╝██╔══██╗')
    print('        ██║░░██╗░███████║██╔████╔██║█████╗░░  ██║░░██║╚██╗░██╔╝█████╗░░██████╔╝')
    print('        ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░  ██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗')
    print('        ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗  ╚█████╔╝░░╚██╔╝░░███████╗██║░░██║')
    print('        ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝  ░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝')
    time.sleep(10)

while loop == True:

    print ('██████ ██████ ██████ ██████ ██████ ██████ ██████ ██████ ██████ ██████ ██████ █████ █████ █████ \n')

    print ('██████╗░██████╗░██╗░██████╗░█████╗░███╗░░██╗  ███████╗░██████╗░█████╗░░█████╗░██████╗░███████╗')
    print ('██╔══██╗██╔══██╗██║██╔════╝██╔══██╗████╗░██║  ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝')
    print ('██████╔╝██████╔╝██║╚█████╗░██║░░██║██╔██╗██║  █████╗░░╚█████╗░██║░░╚═╝███████║██████╔╝█████╗░░')
    print ('██╔═══╝░██╔══██╗██║░╚═══██╗██║░░██║██║╚████║  ██╔══╝░░░╚═══██╗██║░░██╗██╔══██║██╔═══╝░██╔══╝░░')
    print ('██║░░░░░██║░░██║██║██████╔╝╚█████╔╝██║░╚███║  ███████╗██████╔╝╚█████╔╝██║░░██║██║░░░░░███████╗')
    print ('╚═╝░░░░░╚═╝░░╚═╝╚═╝╚═════╝░░╚════╝░╚═╝░░╚══╝  ╚══════╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚══════╝ \n')
    print ('██████ ██████ ██████ ██████ ██████ ██████ ██████ ██████ ██████ ██████ ██████ █████ █████ █████ \n')
    print ('Welkom bij dit spel, Hierbij een makkelijke uitleg. Je moet ontsnappen door een voorwerp / optie te kiezen, \ntyp de optie / voorwerp precies zoals aangegeven in het bericht! \n')
    print ('██████ ██████ ██████ ██████ ██████ ██████ ██████ ██████ ██████ ██████ ██████ █████ █████ █████ \n')
    optie1= input ('Je zit vast in de gevangenis wat gebruik je? kernbom, portalgun, kaas: ')
    if (optie1 == 'secret'):
        secret = input ('train of flyhack: ')
        if (secret == 'train'):
            optiontrain = input ('Meer trainen? ja/nee: ')
            if (optiontrain == 'nee'):
               print('Je bent zo sterk je slaat gwn de muur deruit! goed gedaan!!!')

            if (optiontrain == 'ja'):
              print('Je bent nu zo sterk je slaat gwn de muur deruit! goed gedaan!!!')

        if secret == ('flyhack'):
            optionfly = input ('Wanneer vlieg je weg ochtend, avond: ')
            if (optionfly == 'ochtend'):
                print ('Iedereen ziet je weg vliegen... je word uit de lucht geschoten')
                gameover()

            if optionfly == 'avond':
                print ('Goed gedaan je bent ongezien weg gevlogen!') 

    if (optie1 == 'kernbom'):
        print ('Je hebt niet alleen de cell opgeblazen maar ook jezelf...')
        gameover()
      

    if optie1 == ('portalgun'):
        optiedak= input ('Je beland op het dak wat doe / gebruik je? springen, fortniteglider, enderdragon: ')
        if optiedak == ('springen'):
            print ('Je valt dood, Wat dacht je....')
            gameover()

        if optiedak == ('fortniteglider'):
            print ('Je wordt uit de lucht gesniped door een 9 jarig kind...')
            gameover()

        if optiedak ==('enderdragon'):
            print ('Je wordt opgegeten net als je broer steve...')
            gameover()      

    if optie1 == ('kaas'):
        optiekaas= input ('Wat doe je met de kaas? omkopen, eten: ')
        if optiekaas == ('omkopen'):
           print ('Dacht je echt een agent om te kopen met een stukje kaas?')
           gameover()

        if optiekaas == ('eten'):
           print ('Door het eten van de kaas kreeg je 100+ HP!')
           optiekaas2 = input ('Na het eten van de kaas ga je verder, je kiest tussen trainen of vechten: ')
           if optiekaas2 == ('trainen'):
              optiepower = input ('Je kreeg +100 power door het trainen, kies tussen vechten of trainen: ')
              if optiepower == ('vechten'):
                 ontsnapoptie = input ('Je won het gevegt van de agent, je hebt ze sleutels via welke deur ontsnap je? voor of achter: ')
                 if ontsnapoptie == ('voor'):
                     print ('Dacht je echt via voor te ontsnappen?')
                     gameover()

                 if ontsnapoptie == ('achter'):
                     print ('Goed gedaan je ben ontsnapt!!')

              if optiepower == ('trainen'):
                 print ('Je kreeg ruzie tijdens het trainen en belande in de isoleercell')
                 gameover()



           if optiekaas2 == ('vechten'):
              print ('Je verliest in het gevech had moeten trainen ')
              gameover()