from django.shortcuts import HttpResponse
from datetime import datetime
from django.shortcuts import redirect
import random

def saludo(request):

    documento = """
<!DOCTYPE html>
<html>
<head>
    <title>ParkeyMy - Iniciar Sesión</title>
    <style>
        body {
            margin: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background: linear-gradient(135deg, #39A900, #0f3d0f);
            font-family: Arial, sans-serif;
        }

        .login-container {
            background: white;
            padding: 40px;
            border-radius: 15px;
            width: 350px;
            box-shadow: 0 0 25px rgba(0,0,0,0.3);
            text-align: center;
            animation: aparecer 0.8s ease;
        }

        .logo {
            font-size: 30px;
            font-weight: bold;
            color: #39A900;
            margin-bottom: 10px;
        }

        .subtitle {
            font-size: 14px;
            color: #555;
            margin-bottom: 25px;
        }

        input {
            width: 100%;
            padding: 12px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 8px;
            font-size: 14px;
            transition: 0.3s;
        }

        input:focus {
            border-color: #39A900;
            outline: none;
            box-shadow: 0 0 5px #39A900;
        }

        button {
            width: 100%;
            padding: 12px;
            margin-top: 15px;
            background: #39A900;
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            cursor: pointer;
            transition: 0.3s;
        }

        button:hover {
            background: #2d7d00;
        }

        .footer {
            margin-top: 15px;
            font-size: 12px;
            color: #777;
        }

        @keyframes aparecer {
            from {transform: translateY(-20px); opacity: 0;}
            to {transform: translateY(0); opacity: 1;}
        }

    </style>
</head>
<body>

    <div class="login-container">
        <div class="logo">ParkeyMy</div>
        <div class="subtitle">Sistema de Registro y Control</div>

        <form action="/dameFecha/" method = "get">
            <input type="text" placeholder="Usuario" name = "usuario" required>
            <input type="password" placeholder="Contraseña" required>
            <button type="submit">Iniciar Sesión</button>
        </form>

        <div class="footer">
            © 2026 ParkeyMy - Todos los derechos reservados
        </div>
    </div>

</body>
</html>
"""
    
    return HttpResponse(documento)


def dameFecha(request):
    
    usuario = request.GET.get("usuario")

    if usuario == "kenner":
        return redirect("/panel_kenner/")

    # Si NO es kenner, continúa aquí
    fecha = datetime.now()

    documento = """
<!DOCTYPE html>
<html>
<head>
    <title>Fecha Actual</title>
    <style>
        body {{
            margin: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background: linear-gradient(45deg, #ff00cc, #3333ff, #00ffcc);
            background-size: 400% 400%;
            animation: fondo 6s ease infinite;
            font-family: Arial, sans-serif;
        }}

        h1 {{
            color: white;
            font-size: 60px;
            text-transform: uppercase;
            text-shadow: 0 0 10px #fff,
                         0 0 20px #ff00cc,
                         0 0 40px #ff00cc,
                         0 0 80px #ff00cc;
            animation: rebote 1s infinite alternate;
        }}

        @keyframes fondo {{
            0% {{background-position: 0% 150%;}}
            50% {{background-position: 100% 50%;}}
            100% {{background-position: 0% 350%;}}
        }}

        @keyframes rebote {{
            from {{transform: scale(1);}}
            to {{transform: scale(1.1);}}
        }}
    </style>
</head>
<body>
    <h1>
        Usuario incorrecto ❌ <br>
        Fecha y hora actual: {}
    </h1>
</body>
</html>
""".format(fecha)

    return HttpResponse(documento)



def panel_kenner(request):

    animales = ["Lobo 🐺", "Zorro 🦊", "Tigre 🐯", "Águila 🦅", "Pantera 🐆", "Dragón 🐉"]
    animal_elegido = random.choice(animales)

    documento = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Panel Kenner</title>
    <style>
        body {{
            margin: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background: linear-gradient(90deg, red, orange, yellow, green, blue, indigo, violet);
            background-size: 400% 400%;
            animation: fondo 8s ease infinite;
            font-family: Arial, sans-serif;
            text-align: center;
            color: white;
        }}

        .card {{
            background: rgba(0,0,0,0.7);
            padding: 50px;
            border-radius: 20px;
            box-shadow: 0 0 30px white;
            animation: flotar 3s ease-in-out infinite alternate;
        }}

        h1 {{
            font-size: 45px;
            margin-bottom: 20px;
        }}

        h2 {{
            font-size: 30px;
            margin-top: 10px;
        }}

        @keyframes fondo {{
            0% {{background-position: 0% 50%;}}
            50% {{background-position: 100% 50%;}}
            100% {{background-position: 0% 50%;}}
        }}

        @keyframes flotar {{
            from {{transform: translateY(0px);}}
            to {{transform: translateY(-15px);}}
        }}
    </style>
</head>
<body>

    <div class="card">
        <h1>🌈 Bienvenido Kenner 🌈</h1>
        <h2>🐾 Eres parte de la manada 🐾</h2>
        <h2>Tu espíritu animal es: {animal_elegido}</h2>
    </div>

</body>
</html>
"""

    return HttpResponse(documento)