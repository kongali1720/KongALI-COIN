# whitepaper_professional.py
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle, Flowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
import urllib.request
from io import BytesIO
from reportlab.pdfgen import canvas

pdf_file = "whitepaper.pdf"
doc = SimpleDocTemplate(pdf_file, pagesize=A4,
                        rightMargin=40, leftMargin=40, topMargin=60, bottomMargin=60)

styles = getSampleStyleSheet()
story = []

# Custom styles
title_style = ParagraphStyle('title', parent=styles['Heading1'], fontSize=26, leading=28, alignment=1, spaceAfter=20)
subtitle_style = ParagraphStyle('subtitle', parent=styles['Heading2'], fontSize=16, leading=20, alignment=1, spaceAfter=20)
normal_center = ParagraphStyle('center', parent=styles['Normal'], alignment=1, spaceAfter=12)
normal_justify = ParagraphStyle('justify', parent=styles['Normal'], alignment=4, spaceAfter=12)

# Header / Footer
class HeaderFooterCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)

    def draw_header_footer(self):
        # Header
        self.setFont("Helvetica-Bold", 9)
        self.setFillColor(colors.HexColor('#4a90e2'))
        self.drawString(40, A4[1]-40, "KongaliCoin (KAC) Whitepaper")
        # Footer
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.grey)
        self.drawString(40, 20, f"Page {self._pageNumber}")
        self.drawRightString(A4[0]-40, 20, "https://kongali1720.com/kongalicoin/")

    def showPage(self):
        self.draw_header_footer()
        canvas.Canvas.showPage(self)

    def save(self):
        self.draw_header_footer()
        canvas.Canvas.save(self)

# Logo from GitHub
logo_url = "https://raw.githubusercontent.com/kongali1720/kongali1720.github.io/main/kongalicoin.png"
with urllib.request.urlopen(logo_url) as url:
    image_data = BytesIO(url.read())
logo = Image(image_data, width=150, height=150)
story.append(logo)

# Title
story.append(Paragraph("KongaliCoin (KAC) Whitepaper", title_style))
story.append(Paragraph("The Future of Digital Currency on Ethereum Mainnet", subtitle_style))
story.append(Spacer(1, 20))

# Token Info Table
token_data = [
    ["Token Name", "KongaliCoin"],
    ["Token Symbol", "KAC"],
    ["Contract Address", "0xe71185E2F039013993F2Bc7Da8e51B63E40B063D"],
    ["Decimals", "18"],
    ["Max Supply", "15,000,000,000 KAC"],
    ["Public Sale Allocation", "10,000,000 KAC (20% of total supply)"]
]
table = Table(token_data, colWidths=[150, 300])
table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#4a90e2')),
    ('TEXTCOLOR',(0,0),(-1,0),colors.white),
    ('ALIGN',(0,0),(-1,-1),'LEFT'),
    ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
    ('FONTSIZE', (0,0), (-1,-1), 10),
    ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ('BACKGROUND',(0,1),(-1,-1),colors.HexColor('#f0f0f0')),
    ('GRID', (0,0), (-1,-1), 0.5, colors.grey)
]))
story.append(table)
story.append(Spacer(1, 20))

# Project Description
story.append(Paragraph("Project Description", styles['Heading2']))
story.append(Paragraph("KongaliCoin (KAC) is a digital currency built on Ethereum blockchain, designed to provide fast, secure, and transparent transactions for users globally. Our mission is to enable seamless financial interactions and create value for holders, merchants, and the community.", normal_justify))
story.append(Spacer(1, 20))

# Team & Contact
story.append(PageBreak())
story.append(Paragraph("Team & Contact", styles['Heading2']))
story.append(Spacer(1, 12))
story.append(Paragraph("""
KongAli1720 - Founder & Lead Developer  
Email: <a href="mailto:admin@kongali1720.com">admin@kongali1720.com</a>
""", normal_center))

# Additional Information (Second Page)
story.append(PageBreak())
story.append(Paragraph("Additional Information", styles['Heading2']))
story.append(Spacer(1, 12))

# Tokenomics Detailed Table
tokenomics_data = [
    ["Category", "Amount", "Percentage"],
    ["Public Sale", "10,000,000 KAC", "20%"],
    ["Team Allocation", "3,000,000 KAC", "6%"],
    ["Reserve / Treasury", "2,000,000 KAC", "4%"],
    ["Circulating Supply", "500,000,000 KAC", "10%"],
    ["Others", "14,485,000,000 KAC", "60%"]
]
table2 = Table(tokenomics_data, colWidths=[150, 150, 150])
table2.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#ff9900')),
    ('TEXTCOLOR',(0,0),(-1,0),colors.white),
    ('ALIGN',(0,0),(-1,-1),'CENTER'),
    ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
    ('FONTSIZE', (0,0), (-1,-1), 10),
    ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ('GRID', (0,0), (-1,-1), 0.5, colors.grey)
]))
story.append(table2)
story.append(Spacer(1, 20))

# Roadmap
story.append(Paragraph("Roadmap", styles['Heading2']))
story.append(Paragraph("""
1. Launch of mainnet KAC token  
2. Listing on decentralized exchanges (DEX)  
3. Community building and marketing campaigns  
4. Integration with wallet platforms and merchant adoption  
5. Continuous development and ecosystem expansion
""", normal_justify))
story.append(Spacer(1, 20))

# ICO / Public Sale Info
story.append(Paragraph("Public Sale Information", styles['Heading2']))
story.append(Paragraph("""
Token Sale Address: 0xe71185E2F039013993F2Bc7Da8e51B63E40B063D  
Token Sale Start Date: 01/10/2025  
Token Sale End Date: 31/10/2025  
Token Price: 0.01 ETH per KAC  
Soft Cap / Hard Cap: 50,000 ETH / 150,000 ETH  
Amount Raised: Pending  
Token Distribution Date: 05/11/2025
""", normal_justify))
story.append(Spacer(1, 20))

# Social / Links
story.append(Paragraph("Social Media & Official Links", styles['Heading2']))
story.append(Paragraph("""
Website: https://kongali1720.com/kongalicoin/  
Whitepaper: https://kongali1720.com/kongalicoin/whitepaper.pdf  
Telegram: https://t.me/kongalicoin  
Twitter (X): https://twitter.com/kongalicoin  
GitHub: https://github.com/kongali1720
""", normal_justify))

# Build PDF
doc.build(story, canvasmaker=HeaderFooterCanvas)
print(f"Whitepaper successfully generated: {pdf_file}")
