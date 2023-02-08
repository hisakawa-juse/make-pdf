from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.platypus import Spacer
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
import sys
import random,string

def parse_option():
    option = {}
    for arg in sys.argv[1:]:
        if arg.startswith("--count="):
            option['count'] = int(arg[8:])
        option['filename'] = arg
    if 'filename' not in option:
        option['filename'] = 'sample.pdf'
    if 'count' not in option:
        option['count'] = 1
    return option

def random_string(n):
   randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
   return ''.join(randlst)

def make_pdf(option):
    doc = SimpleDocTemplate(option['filename'],pagesize=A4)
    fontname_g = "HeiseiKakuGo-W5"
    pdfmetrics.registerFont(UnicodeCIDFont(fontname_g))
    elements = []

    style = ParagraphStyle(
        name='Normal',
        fontName='HeiseiKakuGo-W5',
        fontSize=20,
    )

    for i in range(option['count']):
        elements.append(Paragraph(random_string(1280),style))
    doc.build(elements)

if __name__ == '__main__':
    option = parse_option()
    pdffile = make_pdf(option)

