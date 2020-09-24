import webbrowser
import os
import time
os.system("color a")
os.system("cls")
while(True):
    soru = input("""
    
 d888888P                   dP                 .d888888                      dP   
    88                      88                d8'    88                      88   
    88    dP    dP 88d888b. 88  .dP           88aaaaa88a 88d888b. .d8888b. d8888P 
    88    88    88 88'  `88 88888"   88888888 88     88  88'  `88 88'  `88   88   
    88    88.  .88 88       88  `8b.          88     88  88       88.  .88   88   
    dP    `88888P' dP       dP   `YP          88     88  dP       `88888P8   dP   
    ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
    @alismsk234 ooo @alismsk234 ooo @alismsk234 ooo @alismsk234 ooo @alismsk234 ooooo  
    ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
                                                                                    
        1)Site hakkında dosyalar bul
        2)Site sunucusundaki siteler
        3)Whois Sorgusu
        4)Çık

    >> """)
    

    if soru=="1":

        sr = input("Sayfanın urlsini gir>> ")
        arat = "inurl:"+sr + " ext:pdf"
        url = "https://www.google.com/search?q="+arat
        webbrowser.get().open(url)
    elif soru=="2":
        sr1 = input("(https'siz) Sayfanın alan adını gir>> ")
        urls = "https://viewdns.info/reverseip/?host="+sr1+"&t=1"
        webbrowser.get().open(urls)
        time.sleep(2)

    elif soru=="3":
        sr2 = input("Sayfanın urlsini gir>> ")
        urlss = "https://www.hosting.com.tr/domain/whois-sorgulama/"+sr2
        webbrowser.get().open(urlss)

    elif soru=="4":
        break

    else:
        print("Hata")

    

