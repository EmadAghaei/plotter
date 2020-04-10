from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM


drawing = svg2rlg("./data/visualization_1.svg")
renderPDF.drawToFile(drawing, "./data/QuestionVisualized.pdf")