from func_check_rbl import *
from time import sleep

while True:

    print('=' * 52)
    print(Fore.GREEN + '[AUTHOR: FAGNER OLIVEIRA]\n' + '[CONTACT E-MAIL: fagner.mendes22@gmail.com]\n' '[LICENSE: MIT]\n' + '[VERSION: 1.0]\n\n' + 
    'WELCOME TO THE REAL TIME BLACKLIST SYSTEM ANALYSER\n' + 'PLEASE, TO START SELECT THE FOLLOWING RBL BELOW.')
    print(Fore.RESET + '=' * 52)
    print()
    print("OPTIONS:")
    print()
    print(Fore.WHITE + "1. " + Fore.RED + "(RBL - HETRIXTOOLS)")
    print(Fore.WHITE + "2. " + Fore.RED + "(RBL - PROOFPOINT)")
    print(Fore.WHITE + "3. " + Fore.RED + "(RBL - HONEYPOT PROJECT)")
    print(Fore.WHITE + "4. " + Fore.RED + "(RBL - MULTI DNSBL)")
    print(Fore.WHITE + "5. " + Fore.RED + "(RBL - ZYDE)")
    print(Fore.WHITE + "6. " + Fore.RED + "(RBL - ABUSIX)")
    print(Fore.WHITE + "7. " + Fore.RED + "(RBL - SPFBL)")
    print(Fore.WHITE + "8. " + Fore.RED + "(RBL - BARRACUDA)")
    print(Fore.WHITE + "9. " + Fore.RED + "(RBL - SPAMCOP)")
    print(Fore.WHITE + "10. " + Fore.RED + "(CHECK ALL RBL'S)")
    print(Fore.WHITE + "11. " + Fore.RED + "(EXIT)")
    print(Fore.RESET)
    option = int(input("ENTER YOUR OPTION!: "))
    if option == 1:
        print()
        hetrixtools(input('Enter the IP address to be queried in HetrixTools: '))
    elif option == 2:
        proofpoint(input('Enter the IP address to be queried in ProofPoint: '))
    elif option == 3:
        honey_pot_project(input('Enter the IP address to be queried in HoneyPot '))
    elif option == 4:
        multi_dnsbl(input('Enter the IP address to be queried in MultiDNSBL '))
    elif option == 5:
        zyde(input('Enter the IP address to be queried in ZyDe: '))
    elif option == 6:
        abusix(input('Enter the IP address to be queried in Abusix: '))
    elif option == 7:
        spfbl(input('Enter the IP address to be queried in SPFBL: '))
    elif option == 8:
        barracuda(input('Enter the IP address to be queried in Barracuda: '))
    elif option == 9:
        spamcop(input('Enter the IP address to be queried in Spamcop: '))
    elif option == 10:               
        ip_request = (input('Enter your IP Address: '))
        hetrixtools(ip_request)
        sleep(5)
        print()
        proofpoint(ip_request)
        sleep(5)
        print()
        honey_pot_project(ip_request)
        sleep(5)
        print()
        multi_dnsbl(ip_request)
        sleep(5)
        print()
        abusix(ip_request)
        sleep(5)
        print()
        spfbl(ip_request)
        sleep(5)
        print()
        barracuda(ip_request)
        sleep(5)
        print()
        spamcop(ip_request)
    elif option == 11:
        exit()
    else:
        os.system('cls') or None
        wrong_option = "Wrong Option!!!"
        print(Fore.RED + wrong_option)
