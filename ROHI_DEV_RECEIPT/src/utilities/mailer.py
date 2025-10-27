import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

# === CARGAR VARIABLES DE ENTORNO ===
load_dotenv()

SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp-relay.brevo.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SMTP_USER = os.getenv("SMTP_USER")           # Login técnico de Brevo (ej: 99a936001@smtp-brevo.com)
SMTP_PASS = os.getenv("SMTP_PASS")           # Clave SMTP generada en Brevo
EMAIL_SENDER = os.getenv("SENDER_EMAIL")     # Correo verificado, visible para el usuario
STRIPE_URL = os.getenv("STRIPE_URL", "#")


def send_payment_email(email_receiver: str):
    """Envía un correo electrónico con el enlace de pago de Stripe usando Brevo SMTP."""

    if not all([SMTP_USER, SMTP_PASS, EMAIL_SENDER, email_receiver]):
        raise ValueError("❌ Faltan variables de entorno o parámetros para enviar el correo.")

    # === PLANTILLA HTML ===
    HTML_TEMPLATE = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pago de cita médica</title>
    <style>
      body {{
        font-family: 'Segoe UI', Arial, sans-serif;
        background-color: #f6f8fa;
        margin: 0;
        padding: 0;
      }}
      .container {{
        max-width: 600px;
        margin: 40px auto;
        background: white;
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
      }}
      .header {{
        background: linear-gradient(90deg, #1a73e8, #0a58ca);
        color: white;
        text-align: center;
        padding: 25px;
      }}
      .content {{
        padding: 25px;
        color: #333;
        line-height: 1.6;
      }}
      .button {{
        display: inline-block;
        background-color: #ff7a00;
        color: white;
        text-decoration: none;
        padding: 14px 28px;
        font-weight: bold;
        border-radius: 8px;
        transition: background 0.3s ease;
      }}
      .button:hover {{
        background-color: #e06b00;
      }}
      .footer {{
        text-align: center;
        padding: 15px;
        font-size: 13px;
        color: #777;
        background-color: #f0f0f0;
      }}
    </style>
    </head>
    <body>
      <div class="container">
        <div class="header">
          <h2>Confirmación de cita médica</h2>
        </div>
        <div class="content">
          <p>Estimado paciente,</p>
          <p>Para confirmar su cita médica, por favor realice el pago seguro haciendo clic en el siguiente botón:</p>
          <p style="text-align:center;">
            <a href="{STRIPE_URL}" class="button">Pagar cita médica</a>
          </p>
          <p>Este enlace lo llevará al portal de pagos de <strong>Stripe</strong>, donde podrá completar la transacción de forma segura.</p>
          <p>Gracias por confiar en nosotros.</p>
        </div>
        <div class="footer">
          © 2025 ROHI | Todos los derechos reservados
        </div>
      </div>
    </body>
    </html>
    """

    # === Versión texto plano ===
    texto_plano = f"""
    Confirmación de cita médica

    Estimado paciente,

    Para confirmar su cita médica, por favor realice el pago en el siguiente enlace:
    {STRIPE_URL}

    Gracias por confiar en nosotros.
    © 2025 ROHI | Todos los derechos reservados
    """

    # === CREAR MENSAJE ===
    msg = MIMEMultipart("alternative")
    msg["From"] = EMAIL_SENDER
    msg["To"] = email_receiver
    msg["Subject"] = "Pago pendiente - Cita médica ROHI"

    msg.attach(MIMEText(texto_plano, "plain"))
    msg.attach(MIMEText(HTML_TEMPLATE, "html"))

    # === ENVIAR CORREO ===
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=15) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASS)
            server.send_message(msg)
        return True
    except Exception as e:
        print(f"❌ Error al enviar correo: {e}")
        return False
