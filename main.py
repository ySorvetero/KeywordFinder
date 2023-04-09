import requests
import urllib3
import threading
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Back, Style, init
init(autoreset=True)




tfind = []


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

lista = open('results.txt', 'r', encoding='utf-8').readlines()
lista = [linha.replace('\n',"") for linha in lista]

# end settings

print(Fore.RED + f"""
         ██╗ ██████╗  █████╗ ███╗   ██╗ █████╗     ██████╗   ██  █████╗ ██████╗  ██████╗
         ██║██╔═══██╗██╔══██╗████╗  ██║██╔══██╗    ██╔══██╗ ╚═╝  ██╔══██╗██╔══██╗██╔════╝
         ██║██║   ██║███████║██╔██╗ ██║███████║    ██║  ██║      ███████║██████╔╝██║     
    ██   ██║██║   ██║██╔══██║██║╚██╗██║██╔══██║    ██║  ██║      ██╔══██║██╔══██╗██║     
    ╚█████╔╝╚██████╔╝██║  ██║██║ ╚████║██║  ██║    ██████╔╝      ██║  ██║██║  ██║╚██████╗
     ╚════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝    ╚═════╝       ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝
                                                                           
         [!] DOES Nᴏᴛ Sᴜᴘᴘᴏʀᴛ Sɪᴛᴇs Cᴏɴᴛᴀɪɴɪɴɢ Tᴇxᴛ Iɴ CSS
         [!] Exemple: php css html
         [!] Supports multiple keywords
""")
th6 = input(Fore.LIGHTRED_EX + " [THREADS]: ")
executor = ThreadPoolExecutor(max_workers=int(th6))
r = input(Fore.LIGHTRED_EX + " [KEYWORD]: ")
x = r.split()
for i in x:
    tfind.append(i)

def chttp(url, tfind):
    curl = "http://" + url
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.51'}
    r = requests.get(curl, verify=False, timeout=10, headers=headers)
    listed = []
    for ftexts in tfind:
        if ftexts in r.text:
            listed.append(ftexts)
    for ftexts in tfind:
        if ftexts in listed:
            print(Fore.GREEN + f"       [+] {url} ~ Text: {listed} \r")
            with open('listed/live.txt', '+a') as f:
                f.write(f"[+] {url} ~ Text: {listed} \n")
            break

for url in lista:
    try:
        task2 = executor.submit(chttp,url, tfind)
    except:
        print("Failed - The discrepancy in the code or url")
        pass
