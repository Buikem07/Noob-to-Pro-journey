#Resume generator 
from fpdf import FPDF
import os
import webbrowser

# Debugging: Check if the font files exist
font_path_regular = "DejaVuSans.ttf"
font_path_bold = "DejaVuSans-Bold.ttf"
font_path_italic = "DejaVuSans-Oblique.ttf"
font_path_bold_italic = "DejaVuSans-BoldOblique.ttf"

if not all(os.path.exists(path) for path in [font_path_regular, font_path_bold, font_path_italic, font_path_bold_italic]):
    print("One or more font files are missing. Please ensure all required .ttf files are in the script's directory.")
    exit(1)

# Initialize PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Add Unicode-compatible fonts
try:
    pdf.add_font("DejaVu", "", font_path_regular, uni=True)       # Regular
    pdf.add_font("DejaVu", "B", font_path_bold, uni=True)         # Bold
    pdf.add_font("DejaVu", "I", font_path_italic, uni=True)       # Italic
    pdf.add_font("DejaVu", "BI", font_path_bold_italic, uni=True) # Bold Italic
    print("All font variants loaded successfully!")
except RuntimeError as e:
    print(f"Error loading font: {e}")
    exit(1)

# Set the font
pdf.set_font("DejaVu", size=12)

# Title Section
pdf.set_font("DejaVu", style="B", size=16)  # Bold title
pdf.cell(200, 10, "Chibuikem Madueke", ln=True, align="C")
pdf.set_font("DejaVu", size=12)  # Regular font
pdf.cell(200, 8, "Calgary, AB T3P1S2 | 587-439-8554 | chibuikem.e.madueke@gmail.com", ln=True, align="C")
pdf.cell(200, 8, "LinkedIn: http://linkedin.com/in/chibuikem-madueke-843233283", ln=True, align="C")
pdf.ln(10)

# Section Headers
def add_section(title):
    pdf.set_font("DejaVu", style="B", size=14)  # Bold section headers
    pdf.cell(0, 8, title, ln=True)
    pdf.ln(2)

# Content Sections
pdf.set_font("DejaVu", size=12)

# Professional Summary
add_section("Professional Summary")
summary = """Driven and results-oriented Software Development Intern with a strong analytical mindset, problem-solving expertise, 
and a passion for backend development, automation, and AI-driven applications. Adept at leveraging Python, Flask, and Django 
to build web applications and automate workflows. Thrives in fast-paced environments, demonstrating exceptional attention 
to detail, time management, and adaptability. Currently expanding expertise in database management, software engineering, 
and artificial intelligence, with a keen interest in optimizing systems and processes for maximum efficiency."""
pdf.multi_cell(0, 6, summary)
pdf.ln(5)

# Skills
add_section("Technical & Professional Skills")
skills = """- Programming & Software Development: Python (Backend Development, Automation), Flask, Django (learning), Git, SQL (SQLite, PostgreSQL)
- AI & Data Analytics: Proficient in AI-driven tools, automation scripts, and data analysis techniques
- Problem Solving & Critical Thinking: Strong analytical and mathematical skills to optimize processes and improve efficiency
- Project Management & Collaboration: Team-oriented with excellent communication, leadership, and time management abilities
- Content Creation & Design: Experienced in graphic design, content development, and digital media strategies
- Tools & Technologies: Google Workspace, Basic Computer Networking, Version Control Systems"""
pdf.multi_cell(0, 6, skills)
pdf.ln(5)

# Experience
add_section("Experience")
experience = """Reality AI | Software Development Intern (Voluntary) | March 2024 - Present
- Developed backend solutions using Python, Flask, and Django, enhancing automation and web applications.
- Wrote Python scripts that automated 50+ manual tasks, reducing processing time by 30%.
- Assisted in the development of internal tools, contributing to AI-driven projects and database optimizations.
- Gained hands-on experience in API integrations, backend system architecture, and workflow automation.

Olivecaeli Global Service Ltd. | Data & Sales Analyst | Jan 2024 - Sept 2024
- Analyzed customer and sales data, optimizing sales strategies and increasing efficiency by 20%.
- Maintained precise financial records, reducing record discrepancies by 15% and improving decision-making.
- Applied data analytics to track trends and improve inventory planning and operational efficiency."""
pdf.multi_cell(0, 6, experience)
pdf.ln(5)

# Projects Section
add_section("Projects")
projects = """- Automated Data Processing Script – Developed a Python-based automation tool that processed and cleaned large datasets, reducing manual effort by 40%.
- Flask-Based API for Internal Tool – Designed a Flask API that handled 1,000+ requests per hour, improving system efficiency and scalability.
- AI Chatbot Prototype – Built a chatbot using Python and NLP models, automating customer support tasks."""
pdf.multi_cell(0, 6, projects)
pdf.ln(5)

# Education
add_section("Education")
education = """- University of Calgary - Open Studies Student (January 2025 - Present)
- Pan Atlantic University - Electrical/Electronics Engineering (2023 - 2024)
- Eucharistic Heart of Jesus Model College - Secondary School Leaving Certificate & GCE (WASSCE Certified)"""
pdf.multi_cell(0, 6, education)
pdf.ln(5)

# Certifications
add_section("Certifications")
pdf.cell(0, 6, "- Google Workspace Proficiency", ln=True)
pdf.ln(5)

# Languages
add_section("Languages")
pdf.cell(0, 6, "- English - Fluent (Professional Proficiency)", ln=True)

# Save PDF
pdf_filename = "Chibuikem_Madueke_Resume_Updated.pdf"
pdf.output(pdf_filename)

# Automatically open the PDF
webbrowser.open(pdf_filename)

print(f"Resume saved as {pdf_filename}")