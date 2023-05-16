from reportlab.lib import colors
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT

from fastapi import FastAPI, Response
from reportlab.lib.utils import ImageReader
from fpdf import FPDF
from reportlab.platypus import Image

app = FastAPI()

@app.get("/weather-report")
async def generate_pdf():
    # Weather report data
    weather_data = [
        ["State", "Temperature", "Humidity", "Wind speed"],
        ["Andhra Pradesh", "60°F", "70%", "15mph"],
        ["Telangana", "50°F", "60%", "10mph"],
        ["Tamil Nadu", "70°F", "50%", "20mph"],
        ["Karnataka", "40°F", "80%", "5mph"],
    ]

    # Creating a new PDF
    pdf = SimpleDocTemplate("weather-report.pdf", pagesize=landscape(letter))

    title = Paragraph("South India Weather Report", ParagraphStyle(
        "title",
        fontSize=20,
        textColor=colors.black,
        alignment=TA_CENTER,
        spaceAfter=20,
    ))

# Andhra
    place1 = Paragraph("Andhra Pradesh: Mostly Sunny", ParagraphStyle(
        "place1",
        fontSize=16,
        textColor=colors.black,
        alignment=TA_LEFT,
        spaceAfter=16,
    ))
    p1 = Paragraph("94°F|°C", ParagraphStyle(
        "p1",
        fontSize=25,
        textColor=colors.black,
        alignment=TA_LEFT,
        spaceAfter=16,
    ))
    image1 = Image("C:\\Users\\Anandini\\fpdf\\fulls.jpg")
    image1.drawHeight = 1*inch*image1.drawHeight/image1.drawWidth
    image1.drawWidth = 1*inch

# Telangana 
    place2 = Paragraph("Telangana: Mostly Sunny", ParagraphStyle(
        "place2",
        fontSize=16,
        textColor=colors.black,
        alignment=TA_LEFT,
        spaceAfter=16,
    ))
    p2 = Paragraph("92°F|°C", ParagraphStyle(
        "p2",
        fontSize=25,
        textColor=colors.black,
        alignment=TA_LEFT,
        spaceAfter=16,
    ))
    image2 = Image("C:\\Users\\Anandini\\fpdf\\sunny.png")
    image2.drawHeight = 1.5*inch*image2.drawHeight/image2.drawWidth
    image2.drawWidth = 1.5*inch

# Karnataka
    place3 = Paragraph("Karnataka: Partly Cloudy", ParagraphStyle(
        "place3",
        fontSize=16,
        textColor=colors.black,
        alignment=TA_LEFT,
        spaceAfter=16,
    ))
    p3 = Paragraph("83°F|°C", ParagraphStyle(
        "p3",
        fontSize=25,
        textColor=colors.black,
        alignment=TA_LEFT,
        spaceAfter=16,
    ))
    image3 = Image("C:\\Users\\Anandini\\fpdf\\images.jpg")
    image3.drawHeight = 1.2*inch*image3.drawHeight/image3.drawWidth
    image3.drawWidth = 1.2*inch

# Tamil Nadu
    place4 = Paragraph("Tamil Nadu: Mostly Sunny", ParagraphStyle(
        "place4",
        fontSize=16,
        textColor=colors.black,
        alignment=TA_LEFT,
        spaceAfter=16,
    ))
    p4 = Paragraph("93°F|°C", ParagraphStyle(
        "p4",
        fontSize=25,
        textColor=colors.black,
        alignment=TA_LEFT,
        spaceAfter=16,
    ))
    image4 = Image("C:\\Users\\Anandini\\fpdf\\fulls.jpg")
    image4.drawHeight = 1.5*inch*image4.drawHeight/image4.drawWidth
    image4.drawWidth = 1.5*inch

# Kerala
    place5 = Paragraph("Kerala: Partly cloudy", ParagraphStyle(
        "place5",
        fontSize=16,
        textColor=colors.black,
        alignment=TA_LEFT,
        spaceAfter=16,
    ))
    p5 = Paragraph("91°F|°C", ParagraphStyle(
        "p5",
        fontSize=25,
        textColor=colors.black,
        alignment=TA_LEFT,
        spaceAfter=16,
    ))
    image5 = Image("C:\\Users\\Anandini\\fpdf\\part.png")
    image5.drawHeight = 1.5*inch*image4.drawHeight/image4.drawWidth
    image5.drawWidth = 1.5*inch


    


    # Adding the image
    image = Image("C:\\Users\\Anandini\\fpdf\\unt.png")
    image.drawHeight = 10.5*inch*image.drawHeight/image.drawWidth
    image.drawWidth = 10*inch

    # Creating a side heading for the forecast text
    forecast_heading = Paragraph("<b>Forecast:</b>", ParagraphStyle(
        "forecast_heading",
        fontSize=14,
        textColor=colors.black,
        alignment=TA_LEFT,
        spaceAfter=10,
        leading=14,
    ))

    # Creating the forecast text
    forecast_text = Paragraph(
        "Despite being in the thick of the Indian summer months, many parts of South India have been relishing in dipping temperatures. "
        "Prominent cities such as Bengaluru, Hyderabad and Kochi faced inclement weather over the past week, leaving residents wondering whether summer might've departed too soon this year.",
        ParagraphStyle(
            "forecast_text",
            fontSize=11,
            textColor=colors.black,
            alignment=TA_LEFT,
            spaceAfter=10,
            leading=14,
        )
    )

    # Adding the image
    map = Image("C:\\Users\\Anandini\\fpdf\\map.png")
    map.drawHeight = 7.5*inch*map.drawHeight/map.drawWidth
    map.drawWidth = 7*inch
    

    # Creating the table from the weather data
    table = Table(weather_data)

    # Defining the style options for the table cells
    table_style = TableStyle([
        ("GRID", (0, 0), (-1, -1), 1, colors.black),  # Add borders to all cells
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),  # Add grey background to header row
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),  # Change text color of header row
        ("ALIGN", (0, 0), (-1, 0), "CENTER"),  # Center align header row
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),  # Change font of header row
    ])

    # Applying the style options to the table
    table.setStyle(table_style)

    # Creating a title for the air
    ti = Paragraph("Air Quality based on timings in India: ", ParagraphStyle(
        "ti",
        fontSize=17,
        textColor=colors.black,
        alignment=TA_LEFT,
        spaceAfter=20,
    ))

    # Creating the forecast text
    ti_text = Paragraph(
        "An air quality index is used by government agencies to communicate to the public how polluted the air currently is or how polluted it is forecast to become. AQI information is obtained by averaging readings from an air quality sensor, which can increase due to vehicle traffic, forest fires, or anything that can increase air pollution. Pollutants tested include ozone, nitrogen dioxide, sulphur dioxide, among others.",
        ParagraphStyle(
            "ti_text",
            fontSize=11,
            textColor=colors.black,
            alignment=TA_LEFT,
            spaceAfter=10,
            leading=14,
        )
    )

    # Adding the image
    air = Image("C:\\Users\\Anandini\\fpdf\\air.png")
    air.drawHeight = 9.5*inch*air.drawHeight/air.drawWidth
    air.drawWidth = 7*inch

    # Creating a title for the table
    tit = Paragraph("Table: ", ParagraphStyle(
        "tit",
        fontSize=17,
        textColor=colors.black,
        alignment=TA_LEFT,
        spaceAfter=20,
    ))

    


    # Adding the title, forecast heading, forecast text, image, and table to the PDF
    elements = [title, place1,p1,image1,place2,p2,image2,place3,p3,image3,place4,p4,image4,place5,p5,image5,image,forecast_heading, forecast_text, tit, map, table, ti, ti_text, air, Spacer(1,20)]
    pdf.build(elements)

    # Returning the PDF as a response
    with open("weather-report.pdf", "rb") as f:
        pdf_bytes = f.read()
    return Response(content=pdf_bytes, media_type='application/pdf')

