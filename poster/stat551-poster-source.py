"""Render the portfolio summary poster. Requires reportlab; no research data required."""
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
import sys
out=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_name('stat551-poster.pdf')
W,H=2592,1728 # 36 x 24 inches
c=canvas.Canvas(str(out),pagesize=(W,H))
c.setTitle('Alcohol & Health Outcomes - STAT 551 Research Summary')
c.setAuthor('James Riggs | Team STAT 551 project')
paper='#f5f4ed';ink='#23352e';green='#193f35';muted='#536257';accent='#c9e4ae';line='#d7dbd1'
def rect(x,y,w,h,color):c.setFillColor(HexColor(color));c.rect(x,y,w,h,stroke=0,fill=1)
def text(x,y,t,size=24,font='Helvetica',color=ink):
 c.setFillColor(HexColor(color));c.setFont(font,size);c.drawString(x,y,t)
def para(x,top,w,t,size=26,color=muted,leading=None):
 st=ParagraphStyle('body',fontName='Helvetica',fontSize=size,leading=leading or size*1.4,textColor=HexColor(color))
 p=Paragraph(t,st);_,h=p.wrap(w,1400);p.drawOn(c,x,top-h);return top-h

def section(x,top,num,title,w):
 rect(x,top-4,w,2,line);text(x,top-52,num,20,'Helvetica-Bold',green);text(x+48,top-53,title,35,'Times-Roman');return top-88
rect(0,0,W,H,paper);rect(0,H-334,W,334,green)
text(90,H-70,'CAL POLY STATISTICS  /  STAT 551  /  APPLIED STATISTICAL RESEARCH',20,'Helvetica-Bold',accent)
text(90,H-172,'Alcohol & Health Outcomes',82,'Times-Roman',paper)
text(94,H-234,'Statistical learning with BRFSS and U.S. Chronic Disease Indicators',31,'Helvetica',paper)
text(94,H-290,'James Riggs  |  Team course project; teammate analysis preserved as Jose.qmd',23,'Helvetica',accent)
margin=90;gap=62;col=(W-2*margin-2*gap)/3;xs=[margin,margin+col+gap,margin+2*(col+gap)]
x=xs[0];t=H-390
t=section(x,t,'01','Research question',col)
t=para(x,t,col,'How do demographic, socioeconomic, and health characteristics relate to binge drinking? Separately, how do state-level health and income patterns relate to alcohol-related outcomes?')
t-=56;t=section(x,t,'02','Data & scope',col)
text(x,t-45,'50,000',66,'Times-Roman',green);t-=81
t=para(x,t-12,col,'BRFSS input survey rows, before cleaning.',24)
t=para(x,t-34,col,'<b>USCDI:</b> state-level alcohol/liver indicators. The project summary describes approximately 21,500 analysis records.',26)
t=para(x,t-28,col,'The saved USCDI extract has 50,000 rows; the exact filtering stage for the reported 21,500-record scope is unverified. Neither count is a final model sample size.',21)
t=para(x,t-34,col,'Individual survey responses and aggregate state indicators are separate units of analysis.',24)
x=xs[1];t=H-390
t=section(x,t,'03','Methods',col)
t=para(x,t,col,'<b>R / tidymodels / Quarto</b><br/>Regularized logistic regression (glmnet) and teammate random-forest work (ranger). Sources specify five-fold cross-validation and ROC AUC tuning.',26)
t-=42
for label,desc in [('Prepare','Recode survey responses and prepare predictors'),('Model','Fit and tune classification workflows'),('Compare','Explore individual and state-level associations')]:
 rect(x,t-105,col,105,'#e9ece2');text(x+22,t-34,label,28,'Times-Roman',green);para(x+22,t-49,col-44,desc,20);t-=133
para(x,t-3,col,'State-level workflow: aggregate BRFSS measures by state, then join to USCDI indicators.',24)
x=xs[2];t=H-390
t=section(x,t,'04','Reported findings',col)
t=para(x,t,col,'<b>Younger adults</b><br/>The project reported higher odds of binge drinking among younger adults.',29)
t=para(x,t-34,col,'<b>State-level patterns</b><br/>The project reported associations between poorer general health, lower income, and alcohol-related deaths.',29)
t=para(x,t-28,col,'Qualitative findings are from the supplied project summary. Final effect sizes, uncertainty intervals, and held-out metrics were unavailable for verification.',21)
t-=43;t=section(x,t,'05','Presentation & limits',col)
t=para(x,t,col,'Presented by James Riggs to Cal Poly Statistics faculty. The work connected data preparation, statistical learning, and communicating limitations.',25)
t=para(x,t-25,col,'Observational associations do not establish causation. State-level patterns do not establish individual risk. Chronic liver disease mortality is broader than alcohol-attributable mortality.',23)
t=para(x,t-25,col,'Saved sources require coding and evaluation review, including missing-value handling, outcome labels, an undefined recipe, and target leakage in one state-level workflow.',21)
# Footer is deliberately separate from the three reading columns.
rect(90,190,W-180,2,line)
para(90,153,1520,'<b>Sources:</b> Classification_project(James).qmd; Jose.qmd; project summary supplied by James Riggs. Source audit and reproduction notes are in the project repository.',20)
text(90,57,'NEW PORTFOLIO SUMMARY  |  Prepared October 27, 2026  |  Original faculty presentation not available',16,'Helvetica',muted)
text(1745,145,'Case study, sources & poster',21,'Helvetica-Bold',green)
text(1745,107,'jriggs03.github.io/stat551.html',23,'Helvetica',green)
c.linkURL('https://jriggs03.github.io/stat551.html',(1735,95,2500,160),relative=0)
c.showPage();c.save();print(out)
