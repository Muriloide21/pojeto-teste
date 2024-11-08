from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    html_content = """
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Enquetes - Página Inicial</title>
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
        <style>
            body {
                font-family: 'Poppins', sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f7fa;
                color: #333;
            }

            header {
                background-color: #007bff;
                color: white;
                padding: 20px;
                text-align: center;
            }

            header h1 {
                margin: 0;
                font-size: 3em;
            }

            .hero {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 60vh;
                background: linear-gradient(135deg, #007bff, #0056b3);
                color: white;
                text-align: center;
            }

            .hero h2 {
                font-size: 2.5em;
                margin: 0;
            }

            .cta-button {
                background-color: #ff6f61;
                color: white;
                padding: 15px 30px;
                font-size: 1.2em;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                margin-top: 20px;
                text-decoration: none;
            }

            .cta-button:hover {
                background-color: #e55d4e;
            }

            .content {
                padding: 40px;
                background-color: white;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                margin: 30px auto;
                max-width: 1200px;
                border-radius: 8px;
            }

            .features {
                display: flex;
                justify-content: space-around;
                margin-top: 30px;
            }

            .feature {
                width: 30%;
                text-align: center;
            }

            .feature img {
                max-width: 100%;
                border-radius: 8px;
            }

            .footer {
                background-color: #333;
                color: white;
                text-align: center;
                padding: 20px;
                position: fixed;
                bottom: 0;
                width: 100%;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Enquetes</h1>
            <p>Crie, compartilhe e analise enquetes facilmente</p>
        </header>

        <section class="hero">
            <div>
                <h2>Faça sua opinião ser ouvida</h2>
                <p>Participe de enquetes e obtenha insights valiosos</p>
                <a href="#" class="cta-button">Criar Enquete</a>
            </div>
        </section>

        <section class="content">
            <h2>Como Funciona?</h2>
            <p>Com nossa plataforma, você pode criar enquetes rápidas e fáceis. Compartilhe com sua audiência e veja os resultados em tempo real.</p>
            
            <div class="features">
                <div class="feature">
                    <h3>Rápido e Simples</h3>
                    <p>Crie enquetes em minutos e compartilhe com o mundo.</p>
                </div>
                <div class="feature">
                    <h3>Resultados em Tempo Real</h3>
                    <p>Veja os resultados enquanto a enquete está ativa.</p>
                </div>
                <div class="feature">
                    <h3>Compartilhe com Facilidade</h3>
                    <p>Envie suas enquetes diretamente para suas redes sociais.</p>
                </div>
            </div>
        </section>

    </body>
    </html>
    """
    return HttpResponse(html_content)
