import os
import boto3
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, Spacer, SimpleDocTemplate, Image, Table, TableStyle

# === Parámetros fijos de AWS S3 ===
BUCKET_NAME = "rohi-ips-dev"
AWS_REGION = "us-east-1"

def generate_clinical_report(datos_paciente, output_dir="reports"):
    os.makedirs(output_dir, exist_ok=True)

    # === Nombre y ruta local del PDF ===
    safe_name = datos_paciente.get("nombre", "Paciente").replace(" ", "_")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"Reporte_{safe_name}_{timestamp}.pdf"
    local_path = os.path.join(output_dir, filename)

    # === Crear documento PDF ===
    pdf = SimpleDocTemplate(
        local_path,
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=2*cm,
        bottomMargin=2*cm
    )

    fecha = datetime.now()
    hora = fecha.strftime("%H:%M:%S")
    diaMesAno = fecha.strftime("%d/%m/%Y")

    # === Estilos con fuente estándar ===
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name='Titulo',
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        alignment=1,
        textColor=colors.HexColor("#000000")
    ))
    styles.add(ParagraphStyle(
        name='Subtitulo',
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        spaceAfter=10
    ))
    styles.add(ParagraphStyle(
        name='Normal2',
        fontName='Helvetica',
        fontSize=11,
        leading=15
    ))

    contenido = []

    # === Logo (opcional) ===
    try:
        logo = Image("logo.jpg", width=10*cm, height=4*cm)
        logo.hAlign = 'CENTER'
        contenido.append(logo)
    except Exception:
        contenido.append(Paragraph("<b>Clínica CEDIMEC</b>", styles["Titulo"]))

    contenido.append(Spacer(1, 12))
    contenido.append(Paragraph("REPORTE CLÍNICO DEL PACIENTE", styles["Titulo"]))
    contenido.append(Spacer(1, 12))

    # === Tabla de datos del paciente ===
    tabla_datos = [
        ["Nombre del Paciente:", datos_paciente.get("nombre", "N/A")],
        ["Dirección:", datos_paciente.get("direccion", "N/A")],
        ["Diagnóstico:", datos_paciente.get("diagnostico", "N/A")],
        ["Profesional:", datos_paciente.get("profesional", "N/A")],
        ["Valor a Cobrar:", datos_paciente.get("valor", "N/A")],
    ]

    tabla = Table(tabla_datos, colWidths=[5*cm, 10*cm])
    tabla.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#d2af6e")),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('BOX', (0, 0), (-1, -1), 1, colors.grey),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')
    ]))

    contenido.append(tabla)
    contenido.append(Spacer(1, 24))

    # === Firma ===
    contenido.append(Paragraph("<b>Firma del profesional:</b>", styles["Subtitulo"]))
    try:
        firma = Image("Firma.jpg", width=5*cm, height=3*cm)
        firma.hAlign = 'LEFT'
        contenido.append(firma)
    except Exception:
        contenido.append(Spacer(1, 36))
        contenido.append(Paragraph(datos_paciente.get("profesional", ""), styles["Normal2"]))
        contenido.append(Paragraph("Cédula Profesional: 123456789", styles["Normal2"]))
        contenido.append(Spacer(1, 24))

    contenido.append(Paragraph("<i>Este documento es de carácter confidencial y solo puede ser usado con fines médicos autorizados.</i>", styles["Normal2"]))
    contenido.append(Spacer(1, 12))
    contenido.append(Paragraph(f"Generado el {diaMesAno} a las {hora}", styles["Normal2"]))

    # === Generar PDF local ===
    pdf.build(contenido)
    print(f"✅ PDF generado correctamente: {local_path}")

    # === Subir a S3 ===
    s3 = boto3.client('s3', region_name=AWS_REGION)

    s3_key = f"reportes/{filename}"
    s3.upload_file(
        local_path,
        BUCKET_NAME,
        s3_key,
        ExtraArgs={'ContentType': 'application/pdf', 'ACL': 'public-read'}
    )

    # === Construir URL pública ===
    s3_url = f"https://{BUCKET_NAME}.s3.{AWS_REGION}.amazonaws.com/{s3_key}"

    print(f"☁️ PDF subido a S3: {s3_url}")
    return s3_url
