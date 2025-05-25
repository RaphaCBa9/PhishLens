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
        "numbers_in_domain": hasDigits(url),
        "too_many_subdomains": tooManySubdomains(url),
        "special_characters": hasSpecialChars(url),
        "in_phishtank": checkUrlDatabase(url)
    }

    # Determina se qualquer fator suspeito foi identificado
    result["is_malicious"] = (
        result["numbers_in_domain"] or
        result["too_many_subdomains"] or
        result["special_characters"] or
        result["in_phishtank"]
    )

    return result
