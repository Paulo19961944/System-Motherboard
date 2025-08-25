# 🖥️ System Motherboard

Este projeto coleta informações detalhadas do seu dispositivo:
💻 CPU | 🎮 GPU | 🧠 RAM | 💽 Disco | 🛠️ Placa-mãe


# ✅ REQUISITOS
1️⃣ Python 3.8+ instalado no computador  
2️⃣ Variáveis de ambiente configuradas (Python e pip no terminal)  
3️⃣ Git instalado (opcional, para clonar o projeto)  


# ⚙️ INSTALAÇÃO (Windows)
📥 1. Clone este repositório  
   `git clone https://github.com/Paulo19961944/System-Motherboard.git  `

📂 2. Entre na pasta do projeto  
   `cd System-Motherboard`  

🌐 3. Crie um ambiente virtual  
   `python -m venv venv`

🚀 4. Ative o ambiente virtual  
   `venv\Scripts\activate`

📦 5. Instale as dependências  
   `pip install -r requirements.txt`

# ▶️ EXECUÇÃO

🔹 Rode o programa:  
   `python main.py` ou então `python3 main.py`


# ℹ️ OBSERVAÇÕES
- 🪟 Windows → usa o comando interno "wmic" para informações da placa-mãe  
- 🐧 Linux → usa o comando "dmidecode" (precisa de sudo)  
- 🎮 Se não houver GPU → mostrará "Nenhuma GPU detectada"  
