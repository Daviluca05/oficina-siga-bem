from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def pagina_inicial():
    return """
    <html>
        <head>
            <title>Histórico de Serviços</title>
        </head>
        <body style="font-family:Arial;text-align:center;margin-top:50px;">
            <h1 style="color:blue;">Sistema de Histórico de Serviços</h1>
            <h2>Desenvolvido por: Seu Nome Aqui</h2>
            <p style="font-size:18px;">
                Este sistema foi criado para armazenar de forma segura e acessível remotamente
                os serviços realizados pela oficina. A solução utiliza tecnologias modernas,
                hospedadas na nuvem, garantindo proteção contra perda de dados.
            </p>
        </body>
    </html>
    """
