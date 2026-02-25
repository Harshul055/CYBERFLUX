# 🔥 CYBERFLUX

CYBERFLUX is a modular URL intelligence and phishing detection framework built with Python and a modern web interface.

It analyzes URLs using multiple security checks, evaluates risk indicators, and generates a structured risk score to help detect suspicious or malicious links.

Designed with a scalable architecture, CYBERFLUX separates routing, analysis logic, scoring, and services for clean maintainability and future expansion.

---

## 🚀 Features

- 🔍 Multi-layer URL analysis engine
- 🧠 Modular check-based architecture
- 📊 Risk scoring system
- 🌍 Geo & ISP lookup
- 🔐 HTTPS & domain validation checks
- 🧪 Unit testing support
- 🎨 Clean frontend interface
- 🗄 SQLite database integration

---

## 🧠 Security Checks Implementation

The system performs multiple phishing and suspicious pattern checks:

- `@` Symbol detection
- Domain age verification
- IP-based URL detection
- HTTPS validation
- Hyphen usage check
- URL length analysis
- Subdomain analysis
- Typosquatting detection
- Unicode character detection
- URL shortener detection
- Keyword-based phishing detection
- IP resolution
- Geo lookup
- ISP lookup

Each check is modular and located inside:
## 🛠 Installation Guide

CYBERFLUX can be installed on **Kali Linux, Windows, Ubuntu/Linux, and macOS**.

---

# 🐉 Kali Linux Installation

### 1️⃣ Update System
```bash 
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip python3-venv git -y
git clone https://github.com/Harshul055/CYBERFLUX.git
cd CYBERFLUX
```
### 2️⃣ Virtual Environment creation
```bash
python3 -m venv venv
source venv/bin/activate
```
### 3️⃣ Requirements Installation
```bash
pip install -r requirements.txt
```
### 4️⃣ Run Application
```bash
python run.py
```

# 🐧 Ubuntu / Linux Installation

### 1️⃣ Install Dependencies
```
sudo apt update
sudo apt install python3 python3-pip python3-venv git sqlite3 -y
```
### 2️⃣ Clone Repository
```
git clone https://github.com/Harshul055/CYBERFLUX.git
cd CYBERFLUX
```
### 3️⃣ Create Virtual Environment
```
python3 -m venv venv
source venv/bin/activate
```
### 4️⃣ Install Requirements
```
pip install -r requirements.txt
```
### 5️⃣ Start Server
```
python run.py
```
# 🪟 Windows Installation

### 1️⃣ Install Python

Download and install Python 3.x from:
https://www.python.org/downloads/

Download github from: https://git-scm.com/install/windows:

✔ Make sure to check "Add Python to PATH" during installation.

### 2️⃣ Install Git & Clone Repository (Command Prompt or PowerShell)
```
git clone https://github.com/Harshul055/CYBERFLUX.git
cd CYBERFLUX
```
### 3️⃣ Install Dependencies
```
pip install -r requirements.txt
```
# 4️⃣ Run Application
```
python run.py
```

# 🍎 macOS Installation
### 1️⃣ Install Homebrew (if not installed)
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
### 2️⃣ Install Python & Git
```
brew install python git sqlite
```
### 3️⃣ Clone Repository
```
git clone https://github.com/Harshul055/CYBERFLUX.git
cd CYBERFLUX
```
### 4️⃣ Create Virtual Environment
```
python3 -m venv venv
source venv/bin/activate
```
### 5️⃣ Install Requirements
```
pip install -r requirements.txt
```
### 6️⃣ Run Application
```
python run.py
```
## ⚠️ Troubleshooting

- Ensure Python version is 3.8+

- Ensure virtual environment is activated

- If port 5000 is in use, modify port **inside app.py**
## 📊 How It Works

1. User submits a URL via the frontend.

2. Backend routes handle the request.

3. **analyzer_core.py** executes all checks inside **checks/**.

4. Each check returns structured results.

5. **scoring.py** calculates a risk score.

6. Final analysis report is returned to the user.

## 👨‍💻 Author
- Harshul Agarwal
-  Anmol Kumar
-  Ayush Varshney
-  Mounil Gautam
