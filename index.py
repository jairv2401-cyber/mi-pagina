<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bienvenido a mi página</title>
  <style>
    body {
      background: linear-gradient(135deg, #5a0dad, #8e2de2);
      color: #ffffff;
      font-family: Arial, sans-serif;
      text-align: center;
      margin: 0;
      padding: 0;
    }

    h1 {
      margin-top: 120px;
      font-size: 3em;
      text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.4);
    }

    .buttons {
      margin-top: 60px;
    }

    button {
      background-color: #ffffff;
      color: #5a0dad;
      border: none;
      padding: 15px 40px;
      margin: 15px;
      border-radius: 12px;
      font-size: 1.1em;
      font-weight: bold;
      cursor: pointer;
      box-shadow: 0 4px 10px rgba(0,0,0,0.3);
      transition: 0.3s;
    }

    button:hover {
      background-color: #d5b3ff;
      transform: scale(1.05);
    }

    footer {
      position: fixed;
      bottom: 20px;
      width: 100%;
      font-size: 1.2em;
      font-weight: bold;
      text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.3);
    }
  </style>
</head>
<body>

  <h1>✨ Bienvenido a mi página ✨</h1>

  <div class="buttons">
    <button onclick="window.open('https://wa.me/50761072304', '_blank')">📱 WhatsApp</button>
    <button onclick="window.open('https://www.instagram.com/', '_blank')">📸 Instagram</button>
  </div>

  <footer>
    📞 Teléfono: +507 6107-2304
  </footer>

</body>
</html>
