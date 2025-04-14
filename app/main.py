from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

USUARIO = "admin"
SENHA = "1234"

@app.get("/", response_class=HTMLResponse)
async def pagina_login():
    return """
    <html>
        <head>
            <title>Oficina Mecânica - Login</title>
        </head>
        <body>
            <h1 style='color:blue;'>Bem-vindo à Oficina Siga Bem</h1>
            <h2 style='color:red;'>Login</h2>
            <form method="post">
                <input name="nome" placeholder="Seu nome" /><br><br>
                <input name="usuario" placeholder="Usuário" /><br><br>
                <input name="senha" type="password" placeholder="Senha" /><br><br>
                <button type="submit">Entrar</button>
            </form>
        </body>
    </html>
    """

@app.post("/", response_class=HTMLResponse)
async def autenticar(nome: str = Form(...), usuario: str = Form(...), senha: str = Form(...)):
    if usuario == USUARIO and senha == SENHA:
        return f"""
        <html>
            <body>
                <h2 style='color:green;'>Login realizado com sucesso!</h2>
                <p>Olá, <strong>{nome}</strong>! Bem-vindo(a) de volta.</p>
                <a href='/'>Sair</a>
            </body>
        </html>
        """
    return """
    <html>
        <body>
            <h2 style='color:red;'>Usuário ou senha incorretos!</h2>
            <a href='/'>Tentar novamente</a>
        </body>
    </html>
    """
