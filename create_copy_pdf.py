from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, KeepTogether
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from reportlab.pdfgen.canvas import Canvas
import os

OUT = os.path.join('output', 'pdf', 'Copy_Site_Luanne_Vieira_ANTT.pdf')
os.makedirs(os.path.dirname(OUT), exist_ok=True)

font = r'C:\Windows\Fonts\arial.ttf'
font_bold = r'C:\Windows\Fonts\arialbd.ttf'
if os.path.exists(font):
    pdfmetrics.registerFont(TTFont('Arial', font))
    pdfmetrics.registerFont(TTFont('Arial-Bold', font_bold))
    F, FB = 'Arial', 'Arial-Bold'
else:
    F, FB = 'Helvetica', 'Helvetica-Bold'

navy = HexColor('#102A43')
blue = HexColor('#176B87')
gold = HexColor('#C99A3A')
light = HexColor('#F2F6F8')
muted = HexColor('#52606D')

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='CoverTitle', fontName=FB, fontSize=29, leading=34, textColor=colors.white, alignment=TA_LEFT, spaceAfter=12))
styles.add(ParagraphStyle(name='CoverSub', fontName=F, fontSize=14, leading=20, textColor=HexColor('#D9EAF0'), alignment=TA_LEFT))
styles.add(ParagraphStyle(name='H1x', fontName=FB, fontSize=20, leading=25, textColor=navy, spaceBefore=8, spaceAfter=10))
styles.add(ParagraphStyle(name='H2x', fontName=FB, fontSize=13, leading=17, textColor=blue, spaceBefore=10, spaceAfter=5))
styles.add(ParagraphStyle(name='Bodyx', fontName=F, fontSize=10.5, leading=16, textColor=HexColor('#243B53'), spaceAfter=7))
styles.add(ParagraphStyle(name='Smallx', fontName=F, fontSize=8.8, leading=12, textColor=muted, spaceAfter=4))
styles.add(ParagraphStyle(name='Quote', fontName=FB, fontSize=15, leading=21, textColor=navy, leftIndent=12, borderColor=gold, borderWidth=2, borderPadding=9, spaceBefore=8, spaceAfter=12))
styles.add(ParagraphStyle(name='Label', fontName=FB, fontSize=8.5, leading=11, textColor=gold, uppercase=True, spaceAfter=4))

def P(text, style='Bodyx'):
    return Paragraph(text.replace('\n', '<br/>'), styles[style])

def bullet(text):
    return Paragraph('• ' + text, styles['Bodyx'])

def header_footer(canvas: Canvas, doc):
    canvas.saveState()
    w, h = A4
    if doc.page > 1:
        canvas.setStrokeColor(HexColor('#D9E2EC'))
        canvas.line(18*mm, h-15*mm, w-18*mm, h-15*mm)
        canvas.setFont(F, 8)
        canvas.setFillColor(muted)
        canvas.drawString(18*mm, h-11*mm, 'Luanne Vieira Advocacia | Copy do novo site')
        canvas.drawRightString(w-18*mm, 12*mm, f'{doc.page}')
    canvas.restoreState()

story = []
# cover
story.append(Spacer(1, 25*mm))
story.append(P('COPY DO NOVO SITE', 'Label'))
story.append(P('Luanne Vieira<br/>Advocacia ANTT', 'CoverTitle'))
story.append(P('Posicionamento pessoal para empresas médias e grandes do transporte rodoviário interestadual de passageiros.', 'CoverSub'))
story.append(Spacer(1, 35*mm))
story.append(P('Direção estratégica', 'Label'))
story.append(P('Especialização, prevenção e defesa regulatória para empresas que precisam operar com segurança perante a ANTT.', 'CoverSub'))
story.append(Spacer(1, 55*mm))
story.append(P('Documento de copy e arquitetura de conteúdo<br/>Novembro de 2026', 'Smallx'))
story.append(PageBreak())

story.append(P('1. Direção de posicionamento', 'H1x'))
story.append(P('A nova comunicação deve colocar Luanne Vieira no centro da marca. O site não será apresentado como uma banca com sócios, mas como a presença profissional de uma advogada com 9 anos de experiência na área e atuação especializada em ANTT.', 'Bodyx'))
story.append(P('Posicionamento principal', 'H2x'))
story.append(P('Advocacia especializada em ANTT e transporte rodoviário interestadual de passageiros.', 'Quote'))
story.append(P('Promessa de valor', 'H2x'))
story.append(P('Luanne Vieira orienta empresas médias e grandes do setor na regularização, expansão e proteção de suas operações perante a ANTT.', 'Quote'))
story.append(P('Tom de voz', 'H2x'))
for t in ['técnico, sem ser excessivamente burocrático', 'seguro, sem prometer resultados', 'estratégico e orientado à continuidade da operação', 'pessoal: a autoridade é a própria Luanne', 'voltado a gestores, diretores e responsáveis regulatórios']:
    story.append(bullet(t))

story.append(PageBreak())
story.append(P('2. Estrutura recomendada do site', 'H1x'))
tbl = Table([[P('<b>Página</b>','Smallx'), P('<b>Função</b>','Smallx')],
             [P('Início','Bodyx'), P('Apresentar posicionamento, autoridade, serviços e CTA principal.','Bodyx')],
             [P('Atuação em ANTT','Bodyx'), P('Explicar a atuação completa para empresas de transporte de passageiros.','Bodyx')],
             [P('Regularização e autorizações','Bodyx'), P('Detalhar habilitação, TAR, LOP, mercados e alterações operacionais.','Bodyx')],
             [P('Fiscalização e defesa','Bodyx'), P('Mostrar atuação em autos, notificações, recursos, suspensões e cassações.','Bodyx')],
             [P('Conformidade regulatória','Bodyx'), P('Vender prevenção, diagnóstico e acompanhamento contínuo.','Bodyx')],
             [P('Sobre Luanne','Bodyx'), P('Construir confiança na experiência pessoal de 9 anos.','Bodyx')],
             [P('Radar ANTT','Bodyx'), P('Publicar análises e fortalecer autoridade orgânica.','Bodyx')],
             [P('Contato','Bodyx'), P('Converter empresas qualificadas em conversas estratégicas.','Bodyx')]], colWidths=[50*mm, 115*mm])
tbl.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),light),('GRID',(0,0),(-1,-1),0.3,HexColor('#D9E2EC')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]))
story.append(tbl)
story.append(PageBreak())

story.append(P('3. Copy da página inicial', 'H1x'))
story.append(P('PRIMEIRA DOBRA', 'Label'))
story.append(P('Advocacia especializada em ANTT e transporte rodoviário interestadual de passageiros.', 'H1x'))
story.append(P('Atuação jurídica estratégica para empresas médias e grandes que precisam regularizar, expandir e proteger suas operações perante a Agência Nacional de Transportes Terrestres.', 'Bodyx'))
story.append(P('[ Falar sobre minha empresa ]    [ Recebi uma autuação ]', 'Quote'))
story.append(P('9 anos de experiência na área | Atendimento para empresas em todo o Brasil', 'Smallx'))

story.append(P('SEÇÃO: A regulação pode impactar toda a operação', 'Label'))
story.append(P('No transporte interestadual de passageiros, uma decisão regulatória pode afetar mercados, linhas, investimentos, frota, contratos e a continuidade do serviço.', 'H2x'))
story.append(P('Por isso, a atuação jurídica precisa ir além da resposta a uma multa. É necessário compreender a operação da empresa, acompanhar as mudanças da ANTT e agir com estratégia antes que um risco regulatório se transforme em prejuízo.', 'Bodyx'))

story.append(P('SEÇÃO: Como Luanne Vieira pode ajudar sua empresa', 'Label'))
cards = [
('Regularização e autorizações','Habilitação, TAR, LOP, mercados, documentação e alterações operacionais para empresas que desejam operar ou expandir no transporte interestadual.'),
('Fiscalização e defesa administrativa','Análise de autos de infração, notificações, defesas, recursos e processos que possam resultar em multas, suspensão ou cassação.'),
('Conformidade regulatória','Diagnóstico preventivo da operação, revisão de documentos e orientação para reduzir vulnerabilidades perante a fiscalização.'),
('Assessoria regulatória contínua','Acompanhamento de normas, comunicados, prazos e decisões que possam afetar a estratégia da empresa.'),
('Mercados e expansão','Orientação em janelas, requerimentos, novos mercados e planejamento regulatório para crescimento seguro.')]
for title, body in cards:
    story.append(P(title, 'H2x')); story.append(P(body, 'Bodyx'))

story.append(P('SEÇÃO: Uma atuação próxima da decisão empresarial', 'Label'))
story.append(P('Luanne Vieira atua pessoalmente na análise das demandas e na construção da estratégia jurídica de cada empresa.', 'H2x'))
story.append(P('Com 9 anos de experiência na área, sua atuação combina conhecimento técnico da regulação com uma visão prática dos impactos que uma decisão da ANTT pode causar na rotina, nos investimentos e na continuidade da operação.', 'Bodyx'))
story.append(P('O objetivo é traduzir a complexidade regulatória em decisões mais claras para diretores, gestores e responsáveis pela operação.', 'Bodyx'))

story.append(P('SEÇÃO: Para empresas que não podem operar no improviso', 'Label'))
story.append(P('A assessoria é direcionada a empresas médias e grandes do transporte rodoviário interestadual de passageiros que buscam segurança jurídica para operar, crescer e responder às exigências regulatórias.', 'Bodyx'))
story.append(P('Se a sua empresa está iniciando uma operação, buscando novos mercados, passando por fiscalização ou enfrentando um processo administrativo, o primeiro passo é entender exatamente o risco e as alternativas disponíveis.', 'Bodyx'))
story.append(P('[ Solicitar uma análise inicial ]', 'Quote'))
story.append(PageBreak())

story.append(P('4. Copy das páginas de serviço', 'H1x'))
services = [
('Atuação em ANTT','Decisões regulatórias exigem conhecimento da norma e compreensão da operação. Luanne Vieira presta assessoria jurídica para empresas de transporte rodoviário interestadual de passageiros em demandas administrativas, regulatórias e judiciais relacionadas à ANTT.','A atuação pode envolver regularização, autorizações, mercados, fiscalização, autos de infração, recursos, medidas administrativas e acompanhamento de mudanças que afetam o setor.'),
('Regularização e autorizações','Sua empresa precisa estar preparada para cumprir os requisitos regulatórios antes de iniciar ou ampliar uma operação.','A assessoria inclui análise documental, habilitação, autorização, TAR, LOP, mercados, alterações operacionais e orientação sobre os procedimentos aplicáveis ao serviço prestado.'),
('Fiscalização e defesa administrativa','Receber um auto de infração ou uma notificação exige resposta técnica e atenção aos prazos.','Luanne analisa os fatos, os documentos, o enquadramento e o processo administrativo para definir a estratégia adequada de defesa, recurso ou manifestação perante a ANTT.'),
('Conformidade regulatória','A prevenção começa antes da fiscalização.','O diagnóstico regulatório permite identificar inconsistências em documentos, autorizações, cadastros, operação e procedimentos internos, reduzindo o risco de autuações e interrupções.'),
('Mercados e expansão','Crescer no transporte interestadual exige planejamento regulatório.','A assessoria orienta empresas em janelas, requerimentos, novos mercados e decisões que envolvam a expansão da operação, sempre considerando prazos, documentos e riscos.'),
('Assessoria contínua','A regulação muda, e a empresa precisa acompanhar essas mudanças para tomar decisões com segurança.','O acompanhamento contínuo pode incluir monitoramento de normas, comunicados, decisões, prazos e impactos regulatórios relevantes para a operação.')]
for title, intro, body in services:
    story.append(P(title, 'H2x')); story.append(P(intro, 'Quote')); story.append(P(body, 'Bodyx')); story.append(P('[ Conversar sobre esta demanda ]', 'Smallx'))
story.append(PageBreak())

story.append(P('5. Página “Sobre Luanne Vieira”', 'H1x'))
story.append(P('Conhecimento técnico com atuação pessoal e estratégica.', 'H1x'))
story.append(P('Luanne Vieira é advogada com 9 anos de experiência na área e atuação voltada à regulação do transporte rodoviário interestadual de passageiros.', 'Bodyx'))
story.append(P('Seu trabalho é direcionado a empresas médias e grandes que precisam lidar com a complexidade da ANTT com mais segurança, clareza e planejamento.', 'Bodyx'))
story.append(P('A atuação é pessoal. Isso significa que cada demanda é analisada de perto, com compreensão do contexto da empresa, dos riscos envolvidos e dos objetivos da operação.', 'Bodyx'))
story.append(P('Mais do que elaborar uma resposta pontual, Luanne busca construir estratégias jurídicas que ajudem a empresa a preservar sua operação, cumprir as exigências regulatórias e tomar decisões melhores diante de um ambiente em constante transformação.', 'Bodyx'))
story.append(P('Princípios de atuação', 'H2x'))
for t in ['especialização no setor de transporte de passageiros', 'análise individualizada de cada empresa', 'comunicação clara com gestores e responsáveis pela operação', 'atuação preventiva sempre que possível', 'estratégia jurídica alinhada à realidade operacional']:
    story.append(bullet(t))
story.append(P('Atendimento em todo o Brasil', 'H2x'))
story.append(P('A atuação é realizada de forma remota e estratégica para empresas de transporte localizadas em diferentes regiões do país.', 'Bodyx'))

story.append(P('6. Copy para a página de contato', 'H1x'))
story.append(P('Vamos entender o cenário regulatório da sua empresa?', 'H1x'))
story.append(P('Envie uma breve descrição da sua demanda. Luanne Vieira analisará as informações iniciais para entender se a situação envolve autorização, regularização, fiscalização, defesa administrativa ou conformidade regulatória.', 'Bodyx'))
story.append(P('Campos sugeridos', 'H2x'))
for t in ['Nome', 'Empresa', 'Cargo ou função', 'E-mail corporativo', 'Telefone ou WhatsApp', 'Tipo de demanda', 'Mensagem']:
    story.append(bullet(t))
story.append(P('[ Solicitar contato ]', 'Quote'))
story.append(P('Mensagem de apoio: “As informações enviadas serão utilizadas exclusivamente para o contato inicial sobre a demanda jurídica.”', 'Smallx'))

story.append(P('7. CTAs recomendados', 'H1x'))
for t in ['Falar sobre minha empresa', 'Solicitar uma análise inicial', 'Recebi uma autuação da ANTT', 'Avaliar minha situação regulatória', 'Conversar sobre regularização', 'Entender os riscos da minha operação', 'Acompanhar uma mudança regulatória']:
    story.append(bullet(t))

story.append(P('8. Frases a evitar e substituições', 'H1x'))
table2 = Table([[P('<b>Evitar</b>','Smallx'), P('<b>Usar</b>','Smallx')],
 [P('As melhores soluções jurídicas','Bodyx'),P('Atuação estratégica em ANTT e transporte interestadual de passageiros','Bodyx')],
 [P('Soluções completas para todos','Bodyx'),P('Assessoria para empresas médias e grandes do setor de transporte','Bodyx')],
 [P('Garantimos o cancelamento da multa','Bodyx'),P('Analisamos o auto e definimos a estratégia administrativa adequada','Bodyx')],
 [P('Advocacia para pessoas e empresas','Bodyx'),P('Advocacia especializada para empresas de transporte de passageiros','Bodyx')],
 [P('Atendimento jurídico em diversas áreas','Bodyx'),P('Regularização, conformidade, fiscalização e defesa perante a ANTT','Bodyx')]], colWidths=[78*mm, 87*mm])
table2.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),light),('GRID',(0,0),(-1,-1),0.3,HexColor('#D9E2EC')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]))
story.append(table2)
story.append(Spacer(1, 8))
story.append(P('Observação estratégica', 'H2x'))
story.append(P('Antes da publicação, revisar a redação final com a própria advogada, confirmar a forma correta de apresentar os 9 anos de experiência e validar informações profissionais obrigatórias, como número da OAB e dados de contato.', 'Smallx'))

doc = SimpleDocTemplate(OUT, pagesize=A4, rightMargin=18*mm, leftMargin=18*mm, topMargin=22*mm, bottomMargin=18*mm, title='Copy do novo site - Luanne Vieira Advocacia ANTT', author='')
def first_page(canvas, doc):
    canvas.saveState(); w,h=A4
    canvas.setFillColor(navy); canvas.rect(0,0,w,h,fill=1,stroke=0)
    canvas.setFillColor(blue); canvas.rect(0,h-45*mm,w,45*mm,fill=1,stroke=0)
    canvas.setFillColor(gold); canvas.rect(18*mm,h-48*mm,28*mm,3*mm,fill=1,stroke=0)
    canvas.restoreState()
doc.build(story, onFirstPage=first_page, onLaterPages=header_footer)
print(OUT)
