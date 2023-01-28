import json
import os
import requests
import colorama
import urllib.request
from urllib.request import Request, urlopen
from urllib.error import URLError
from dotenv import load_dotenv
from colorama import Fore, Back, Style
colorama.init()


load_dotenv()

def hetrixtools(ip_address):    

    BASE_URL = 'https://api.hetrixtools.com/v2/'
    API_TOKEN = os.environ.get('API_TOKEN')
    endpoint = '/blacklist-check/ipv4/'
    
    params = ip_address + '/'  

    response = requests.request("GET", BASE_URL + API_TOKEN + endpoint + params).json()
    bl = response['blacklisted_on']

    for item in bl:
        listed_on = item['rbl']
        delist = item['delist']
        resp = {"rbl_list": listed_on, "url_delist": delist}
        print()
        print(f'The IP Address {ip_address} is listed ON: {resp.get("rbl_list")}\nGo to following address: {resp.get("url_delist")} to apply for delist!\n')

    res = response['status']
    if res == 'ERROR':
        print('Invalid API Call')
    else:
      exit

def proofpoint(IP):
       
    try:
        req = Request('https://support.proofpoint.com/rbl-lookup.cgi?ip=' + IP)
        response = urlopen(req)
        data = urllib.request.urlopen(req).read()
    except URLError as e:
        print ("Proofpoint rejected for reason: " + str(e.code))
        return
    
    res = 'This IP address is not blocked'

    if b'res' in data:
        print ('The IP Address ' + IP + ' was checked on RBL: :Proofpoint: and the current ' + 'status is: ' + Fore.GREEN +'NOT LISTED')
        print(Fore.RESET)
    else:
        print ('The IP Address ' + IP + ' was checked on RBL: :Proofpoint: and the current ' + 'status is: ' + Fore.RED +'LISTED')
        print(Fore.RESET)

def honey_pot_project(IP):
       
    try:
        url = 'https://www.projecthoneypot.org/ip_' + IP
        request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        data = urlopen(request).read()        
    except URLError as e:
        print ("MultiDNSBL rejected for reason: " + str(e.code))
        return

    res = ("The Project Honey Pot system has detected behavior from the IP address").encode()
    if res in data:
        print ('The IP Address ' + IP + ' was checked on RBL: :ProjectHoneyPot: and the current ' + 'status is: ' + Fore.RED +'LISTED')
    else:
        print ('The IP Address ' + IP + ' was checked on RBL: :ProjectHoneyPot: and the current ' + 'status is: ' + Fore.GREEN +'NOT LISTED')

def multi_dnsbl(IP):
       
    try:
        url = 'https://zy0.de/q/' + IP
        request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        data = urlopen(request).read()        
    except URLError as e:
        print ("MultiDNSBL rejected for reason: " + str(e.code))
        return

    res = ("listed").encode()
    if res in data:
        print ('The IP Address ' + IP + ' was checked on RBL: :MultiDNSBL: and the current ' + 'status is: ' + Fore.RED +'LISTED')
    else:
        print ('The IP Address ' + IP + ' was checked on RBL: :MultiDNSBL: and the current ' + 'status is: ' + Fore.GREEN +'NOT LISTED')

def zyde(IP):
       
    try:
        url = 'https://zy0.de/q/' + IP
        request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        data = urlopen(request).read()        
    except URLError as e:
        print ("ZyDe rejected for reason: " + str(e.code))
        return

    res = ("Listed").encode()
    if res in data:
        print ('The IP Address ' + IP + ' was checked on RBL: :ZyDe: and the current ' + 'status is: ' + Fore.RED +'LISTED')
    else:
        print ('The IP Address ' + IP + ' was checked on RBL: :ZyDe: and the current ' + 'status is: ' + Fore.GREEN +'NOT LISTED')

def abusix(IP):
       
    try:
        url = 'https://lookup.abusix.com/search?q=' + IP
        request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        data = urlopen(request).read()        
    except URLError as e:
        print ("Abusix rejected for reason: " + str(e.code))
        return

    res = ("listed").encode()
    if res in data:
        print ('The IP Address ' + IP + ': was checked on RBL: :Abusix: and the current ' + 'status is: ' + Fore.RED +'LISTED')
    else:
        print ('The IP Address ' + IP + ': was checked on RBL: :Abusix: and the current ' + 'status is: ' + Fore.GREEN +'NOT LISTED')


def spfbl(IP):
       
    try:
        url = 'https://matrix.spfbl.net/pt/' + IP
        request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        data = urlopen(request).read()        
    except URLError as e:
        print ("SPFBL rejected for reason: " + str(e.code))
        return

    res = ("Este endereço de email abuse está desinscrito da nossa plataforma").encode()
    if res in data:
        print ('The IP Address ' + IP + ' was checked on RBL: :SPFBL: and the current ' + 'status is: ' + Fore.GREEN +'NOT LISTED')
    else:
        print ('The IP Address ' + IP + ' was checked on RBL: :SPFBL: and the current ' + 'status is: ' + Fore.RED +'LISTED')


def spamcop(IP):
       
    try:
        url = 'https://www.spamcop.net/w3m?action=checkblock&ip=' + IP
        request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        data = urlopen(request).read()        
    except URLError as e:
        print ("Spamcop rejected for reason: " + str(e.code))
        return

    res = ("not listed").encode()
    if res in data:
        print ('The IP Address ' + IP + ' was checked on RBL: :Spamcop: and the current ' + 'status is: ' + Fore.GREEN +'NOT LISTED')
    else:
        print ('The IP Address ' + IP + ' was checked on RBL: :Spamcop: and the current ' + 'status is: ' + Fore.RED +'LISTED')

def barracuda(IP):

    url = "https://www.barracudacentral.org/lookups/lookup-reputation"

    payload={'submit': 'Check+Reputation',
    'cid': 'ccc27e3296991116723134870e3b13fd',
    'lookup_entry': IP}
    files=[

    ]
    headers = {
    'content-type': 'application/x-www-form-urlencoded',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.125 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }

    data = requests.post(url, headers=headers, data=payload, files=files).text

    res = "poor"
    if res in data:
        print ('The IP Address ' + IP + ' was checked on RBL: :MultiDNSBL: and the current ' + 'status is: ' + Fore.RED +'LISTED')
    else:
        print ('The IP Address ' + IP + ' was checked on RBL: :MultiDNSBL: and the current ' + 'status is: ' + Fore.GREEN +'NOT LISTED')