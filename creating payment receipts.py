from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
data=[
    ["ITEM NO.","DESCRIPTION","QTY","UNIT PRICE"],
    ["A11","Beakers","50","200"],
    ["B22","Test tubes","80","100"],
    ["C33","Bunsen burners","10","300"],
["DISCOUNT","","","1000"],
["TOTAL","","","20000"],]

pdf=SimpleDocTemplate("chemistrylab_receipt.pdf",pagesize=A4)
styles=getSampleStyleSheet()
title_style=styles["Heading2"]
title_style.alignment=1
title=Paragraph("Chemistry Lab Equipment",title_style)
style=TableStyle(
    [
        ("BOX",(0,0),(-1,-1),1,colors.blueviolet),
        ("GRID",(0,0),(4,4),1,colors.blueviolet),
        ("BACKGROUND",(0,0),(3,0),colors.cornflowerblue),
        ("TEXTCOLOR",(0,0),(-1,0),colors.black),
        ("ALIGN",(0,0),(-1,-1),"CENTER"),
        ("BACKGROUND",(0,1),(-1,-1),colors.lavender),
    ]
)
table=Table(data,style=style)
pdf.build([title,table])
