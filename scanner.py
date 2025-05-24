import requests

# Configurações
url_base = "http://10.10.60.93/"
wordlist = ["admin", "login", "s3cr3t-area", "dashboard", "hidden", "backup", "private"]

def scan_paths():
    print(f"[+] Iniciando scan em {url_base}")
    
    for path in wordlist:
        url = url_base + path
        res = requests.get(url)
        
        if res.status_code == 200:
            print(f"[✓] Encontrado: {url}")
        elif res.status_code == 403:
            print(f"[!] Acesso proibido: {url}")
        else:
            print(f"[-] {path} não encontrado")

if __name__ == "__main__":
    scan_paths()
