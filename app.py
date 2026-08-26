from datetime import datetime, timezone

from flask import Flask, jsonify, render_template


app = Flask(__name__)


# ============================================================
# Página principal
# ============================================================

@app.route("/")
def index():
    """
    Renderiza a página principal da disciplina.
    """
    return render_template("index.html")


# ============================================================
# API de verificação do serviço
# ============================================================

@app.route("/api/health")
def health():
    """
    Retorna informações sobre o estado da aplicação.

    Esta rota será utilizada para demonstrar uma requisição
    HTTP a uma API executando na instância EC2.
    """

    return jsonify({
        "status": "online",
        "service": "Desenvolvimento de Sistemas Distribuídos",
        "course": "Ciência da Computação - UNIP",
        "semester": "6º semestre",
        "professor": "Prof. Dr. André Lourenço",
        "server": "AWS EC2",
        "framework": "Flask",
        "timestamp": datetime.now(timezone.utc).isoformat()
    })


# ============================================================
# Informações sobre a disciplina
# ============================================================

@app.route("/about")
def about():
    """
    Retorna informações básicas sobre a disciplina.
    """

    return jsonify({
        "discipline": "Desenvolvimento de Sistemas Distribuídos",
        "course": "Ciência da Computação",
        "institution": "UNIP",
        "semester": "6º semestre",
        "workload": "60 horas-aula",
        "professor": "Prof. Dr. André Lourenço"
    })


# ============================================================
# Execução da aplicação
# ============================================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )