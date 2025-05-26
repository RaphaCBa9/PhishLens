# PhishLens — Verificador de Phishing

> Desenvolvido por **Raphael Banov**

**PhishLens** é uma plataforma simples desenvolvida em Python para detectar potenciais URLs de phishing. O projeto está em desenvolvimento incremental e atualmente implementa as funcionalidades do conceito **C**, com uma análise básica de risco e uma interface web funcional.

## 📚 Índice

- [Funcionamento](#funcionamento)
- [Como Utilizar a Plataforma](#como-utilizar-a-plataforma)
  - [Requisitos](#1-requisitos)
  - [Instalação](#2-instalação)
  - [Execute o Servidor](#4-execute-o-servidor)
  - [Use a Interface](#5-use-a-interface)

---

## Funcionamento

A plataforma realiza uma análise básica de URLs submetidas pelo usuário com base em quatro critérios:

1. **Presença de números no domínio**  
2. **Excesso de subdomínios** (mais de 3 níveis)
3. **Caracteres especiais incomuns** na URL
4. **Verificação contra base de dados do PhishTank**  
   Utiliza a base de dados baixável da PhishTank `online-valid.json`, contendo URLs verificadas e ainda ativas.

Com base nesses critérios, cada URL recebe um **nível de risco**:

| Nível de Risco | Cor     | Critérios                                            |
|----------------|----------|------------------------------------------------------|
| `safe`         | 🟢 Verde  | Nenhuma flag levantada                              |
| `attention`    | 🟡 Amarelo| Exatamente 1 ou 2 flags levantadas                  |
| `unsafe`       | 🔴 Vermelho| Mais de 2 flags **ou** encontrada na base PhishTank |

---

## Como Utilizar a Plataforma

### 1. Requisitos

- Python 3.7+
- `pip` instalado
- Módulo `Flask` instalado

### 2. Instalação

Clone o projeto ou copie os arquivos para uma pasta local:

```
git clone https://github.com/RaphaCBa9/PhishLens
cd Phishlens
```

#### (Opcional) Utilizando um ambiente virtual:

Crie um ambiente virtual dentro do diretório:

```bash
python3 -m venv env
```

**Ative o Ambiente**
Para Windows

```bash
env/scripts/activate.bash #activate.ps1 caso esteja no Windows PowerShell
```

Para sistemas POSIX

```bash
source env/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```


### 4. Execute o Servidor

Execute o script principal:

```
python app.py
```

Abra seu navegador e acesse:

```
http://localhost:5000
```

### 5. Use a Interface

- Insira uma ou mais URLs (uma por linha).
- Clique em **"Analisar"**.
- Visualize os resultados com coloração e indicadores de risco.

---

