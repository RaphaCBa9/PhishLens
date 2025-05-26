import json
import os
from urllib.parse import urlparse
import re

# Caminho para o arquivo do PhishTank
PHISHTANK_FILE = "data/online-valid.json"

# Carrega os dados verificados e online do PhishTank
def loadDatabase():
    if not os.path.exists(PHISHTANK_FILE):
        return set()

    with open(PHISHTANK_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

    phishing_urls = {
        entry["url"].strip()
        for entry in data
        if entry.get("verified") == "yes" and entry.get("online") == "yes"
    }

    return phishing_urls

# Inicializa conjunto de URLs phishing
PHISHTANK_URLS = loadDatabase()

# Verifica se URL está na lista do PhishTank
def checkUrlDatabase(url):
    return url.strip() in PHISHTANK_URLS

# Verifica se há números no domínio
def hasDigits(url):
    try:
        domain = urlparse(url).netloc
        return any(char.isdigit() for char in domain)
    except:
        return False

# Verifica excesso de subdomínios
def tooManySubdomains(url, limit=3):
    try:
        domain = urlparse(url).netloc
        parts = domain.split('.')
        return len(parts) > limit
    except:
        return False

# Verifica presença de caracteres especiais
def hasSpecialChars(url):
    return bool(re.search(r"[^a-zA-Z0-9:/._\-]", url))

# Função principal de análise
def checkUrl(url):
    url = url.strip()

    result = {
        "url": url,
        "hasDigits": hasDigits(url),
        "subdomainCount": tooManySubdomains(url),
        "specialChars": hasSpecialChars(url),
        "inDatabase": checkUrlDatabase(url)
    }

    flags = sum(
        [result["hasDigits"], result["subdomainCount"], result["specialChars"], result["inDatabase"]]
    )

    if result["inDatabase"] or flags > 2:
        result["riskLevel"] = "unsafe"

    elif flags <= 2 and flags > 0:
        result["riskLevel"] = "attention"

    else:
        result["riskLevel"] = "safe"

    

    return result
