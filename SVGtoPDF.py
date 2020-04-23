from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM


drawing = svg2rlg("./data/Panelists.svg")
renderPDF.drawToFile(drawing, "./data/Panelists2.pdf")
# drawing = svg2rlg("./data/Qos.svg")
# renderPDF.drawToFile(drawing, "./data/Qos.pdf")