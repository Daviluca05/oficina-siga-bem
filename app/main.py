from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def dados_form():
    return """
    <html>
        <head>
            <title>Dados - Oficina</title>
        </head>
        <body style="font-family: Arial; margin: 40px;">
            <h1 style="color: blue;">📋 Dados da Oficina</h1>
            <form action="/enviar" method="post">
                <label for="titulo">Título:</label><br>
                <input type="text" id="titulo" name="titulo" required style="width: 300px;"><br><br>

                <label for="descricao">Descrição:</label><br>
                <textarea id="descricao" name="descricao" rows="4" cols="50" required></textarea><br><br>

                <input type="submit" value="Enviar">
            </form>
        </body>
    </html>
    """

@app.post("/enviar", response_class=HTMLResponse)
async def enviar_dados(titulo: str = Form(...), descricao: str = Form(...)):
    return f"""
    <html>
        <head><title>Enviado</title></head>
        <body style="font-family: Arial; margin: 40px;">
            <h1 style="color: green;">✅ Enviado com sucesso!</h1>
            <p><strong>Título:</strong> {titulo}</p>
            <p><strong>Descrição:</strong> {descricao}</p>
            <a href="/">🔙 Voltar</a>
        </body>
    </html>
    """
