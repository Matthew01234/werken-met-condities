kaasgeel = input('Is de kaas geel? Ja/Nee: ')
if (kaasgeel == 'Ja'):
    gaten = input ('Zitten er gaten in? Ja/Nee: ')
    if (gaten == 'Ja'):
        duur = input('Is de kaas duur? Ja/Nee')
        if (duur == 'Ja'):
            print ('Emmenthaler')


        if (duur == 'Nee'):
            print('Leerdammer')
    


    if (gaten == 'Nee'):
        hard_als_steen = input ('Is het net zo hard als steen? Ja/Nee: ')
        if (hard_als_steen == 'Ja'):
            print ('Pamigiano Reggiano')


        if (hard_als_steen == 'Nee'):
            print ('Goudse Kaas')
         
 

   


if (kaasgeel == 'Nee'):
    blauweschimmel = input ('Heeft de kaas blauwe schimmel? Ja/Nee: ')
    if (blauweschimmel == 'Ja'):
        korst = input ('Heeft de kaas een korst? Ja/Nee: ')
        if (korst == 'Ja'):
              print ('blue de rochbaron')

        if  (korst == 'Nee'):  
              print ('Foumme d ambert') 

        
    if (blauweschimmel == 'Nee'):
        korstgeenschimmel = input ('Heeft de kaas een korst? Ja/Nee: ')
        if (korstgeenschimmel == 'Ja'):
             print ('camabert')


    if (korstgeenschimmel == 'Nee'):
            print ('mozzarella')
    
