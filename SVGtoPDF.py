from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM


drawing = svg2rlg("./data/visualization1.svg")
renderPDF.drawToFile(drawing, "./data/Panelists3.pdf")
# drawing = svg2rlg("./data/Qos.svg")
# renderPDF.drawToFile(drawing, "./data/Qos.pdf")