from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse

app = FastAPI()

DB_TAREAS = []

CSS = """
<style>
    body { font-family: 'Segoe UI', sans-serif; background: #f0f2f5; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
    .card { background: white; padding: 2rem; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); width: 400px; }
    h1, h2 { color: #1a1a1a; text-align: center; }
    input, select { width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #ddd; border-radius: 5px; box-sizing: border-box; }
    button { width: 100%; padding: 10px; background: #007bff; color: white; border: none; border-radius: 5px; cursor: pointer; font-size: 16px; margin-top: 10px; }
    button:hover { background: #0056b3; }
    button.logout { background: #dc3545; margin-top: 20px; }
    button.logout:hover { background: #a71d2a; }
    .error { color: red; text-align: center; margin-bottom: 10px; }
    ul { list-style: none; padding: 0; }
    li { background: #f8f9fa; border-bottom: 1px solid #ddd; padding: 10px; display: flex; justify-content: space-between; }
    .badge { background: #28a745; color: white; padding: 2px 8px; border-radius: 10px; font-size: 12px; }
</style>
"""

@app.get("/", response_class=HTMLResponse)
def login_page(error: str = ""):
    error_msg = f'<div class="error">{error}</div>' if error else ""
    return f"""
    <!DOCTYPE html>
    <html>
    <head><title>Portal Seguro</title>{CSS}</head>
    <body>
        <div class="card">
            <h1>Bienvenido</h1>
            {error_msg}
            <form action="/login" method="post">
                <input type="text" id="username" name="username" placeholder="Usuario" required>
                <input type="password" id="password" name="password" placeholder="Contraseña" required>
                <button type="submit" id="btn-login">Iniciar Sesión</button>
            </form>
        </div>
    </body>
    </html>
    """

@app.post("/login", response_class=HTMLResponse)
def login(username: str = Form(...), password: str = Form(...)):
    if username == "admin" and password == "admin123":
        return RedirectResponse(url="/dashboard", status_code=303)
    return RedirectResponse(url="/?error=Credenciales Incorrectas", status_code=303)

@app.get("/dashboard", response_class=HTMLResponse)
def dashboard():
    lista_html = ""
    for tarea in DB_TAREAS:
        lista_html += f'<li class="task-item"><span>{tarea["nombre"]}</span> <span class="badge">{tarea["prioridad"]}</span></li>'
    
    return f"""
    <!DOCTYPE html>
    <html>
    <head><title>Dashboard</title>{CSS}</head>
    <body>
        <div class="card">
            <h2>Mis Tareas</h2>
            <ul id="lista-tareas">
                {lista_html}
            </ul>
            <hr>
            <h3>Nueva Tarea</h3>
            <form action="/add" method="post">
                <input type="text" id="task_name" name="task_name" placeholder="Descripción de la tarea" required>
                <select id="priority" name="priority">
                    <option value="Baja">Baja</option>
                    <option value="Media">Media</option>
                    <option value="Alta">Alta</option>
                </select>
                <button type="submit" id="btn-add">Agregar Tarea</button>
            </form>
            <form action="/logout" method="get">
                <button type="submit" id="btn-logout" class="logout">Cerrar Sesión</button>
            </form>
        </div>
    </body>
    </html>
    """

@app.post("/add", response_class=HTMLResponse)
def add_task(task_name: str = Form(...), priority: str = Form(...)):
    DB_TAREAS.append({"nombre": task_name, "prioridad": priority})
    return RedirectResponse(url="/dashboard", status_code=303)

@app.get("/logout")
def logout():
    DB_TAREAS.clear()
    return RedirectResponse(url="/", status_code=303)