from flask import Flask, render_template

# Initialize the Flask app
app = Flask(__name__)

# --- Your Portfolio Data ---
# All data is populated from the resume you provided.

YOUR_INFO = {
    "name": "Balamanoj Reddy Kommareddy",
    "headline": "Aviation Data Analytics Professional",
    "linkedin": "https://in.linkedin.com/in/balamanoj",
    "email": "bkommar1@kent.edu",
    "phone": "+1 (330) 554-1998",
    # This is the quote for the contact section
    "funny_quote": "P.S. I worked as a reliability engineer. You can be 99.9% confident this contact form works.",
    "bio": "Data Analytics professional with 4+ years of experience applying data-driven solutions in aviation, reliability engineering, and aftermarket support. Skilled in SQL, Oracle, Power BI, and ETL pipelines."
}

YOUR_SKILLS = [
    "Python",
    "SQL",
    "Oracle SQL Server",
    "MySQL",
    "Power BI",
    "ETL Pipelines",
    "Predictive Modeling",
    "Reliability Analysis",
    "Airtable",
    "Component Control Quantum",
    "Power Automate",
    "SAP",
    "CRM",
    "MS Excel",
    "FAA/EASA Regulations",
    "Root Cause Analysis",
    "Data Visualization",
    "Forecasting",
]

# These projects are based on the job descriptions in your resume
YOUR_PROJECTS = [
    {
        "id": "proj-1",
        "title": "Component Reliability Dashboard",
        "short_desc": "A Power BI dashboard to analyze component reliability and failure trends.",
        "goal": "The engineering team needed to prioritize reverse engineering efforts but lacked data on which parts were failing most often in the field.",
        "process": [
            "Built ETL pipelines to extract and load data from Oracle databases and Component Control Quantum ERP.",
            "Cleaned and transformed raw maintenance records and failure reports using SQL queries.",
            "Designed interactive Power BI dashboards to visualize Failure Trends, MTBF, and component attrition rates.",
            "Added filters for aircraft type, part number, and date range."
        ],
        "result": "The dashboard provided clear, data-driven insights that allowed the engineering team to prioritize critical parts for reverse engineering.",
        "github_link": "https://github.com/manojkommareddy/reliability-dashboard" # Update this link
    },
    {
        "id": "proj-2",
        "title": "Aerospace Technical Data App",
        "short_desc": "An application to create and compile Technical Data Packages (TDPs) for PMA parts.",
        "goal": "The manual process for compiling Technical Data Packages (TDPs) for airline and MRO customers was slow and prone to errors.",
        "process": [
            "Developed a web-based tool to centralize all part specifications, FAA regulations, and Airworthiness Review Certificates (ARC).",
            "Engineered a database schema to store complex relationships between parts, regulations, and maintenance requirements.",
            "Built a feature to export the final, formatted TDP to support regulatory compliance and informed purchasing decisions.",
        ],
        "result": "Streamlined the creation of comprehensive TDPs, ensuring accuracy and regulatory compliance for all MRO and airline customers.",
        "github_link": "https://github.com/manojkommareddy/tdp-generator" # Update this link
    },
    {
        "id": "proj-3",
        "title": "Inventory & Task Flow Automation",
        "short_desc": "An automation tool to proactively track parts shortages and inventory levels.",
        "goal": "The supply chain team needed a proactive way to manage inventory levels and be alerted to potential shortages before they caused delays.",
        "process": [
            "Used Power Automate to monitor the MAXQPROD inventory database (Oracle SQL).",
            "Created automated alerts triggered by specific data thresholds (e.g., inventory < 10 units).",
            "Integrated with Airtable to create and assign tasks to the procurement team when a shortage was detected.",
        ],
        "result": "Created a proactive inventory tracking system that reduced manual effort, prevented shortages, and streamlined procurement workflows.",
        "github_link": "https://github.com/manojkommareddy/inventory-automation" # Update this link
    },
    {
    "id": "proj-4",
    "title": "Supplier Registration Assistant",
    "short_desc": "A browser automation script to streamline registration on vendor portals and new websites by auto-filling company information.",
    "goal": "The team frequently signs up for new supplier portals, SaaS tools, and industry newsletters, which involves repetitive manual data entry. This tool is needed to accelerate access and ensure data consistency.",
    "process": [
        "Create a secure, local configuration (e.g., a JSON file) to store the standard company profile (email, company name, etc.).",
        "Develop a browser automation script (using JavaScript for an extension or Python with Selenium) to control the web browser.",
        "Write logic to scan a webpage and detect common form field identifiers (like '<input type=\"email\">' or 'id=\"company_name\"').",
        "Implement an auto-fill action that injects the stored profile data into the corresponding detected fields.",
        "Add a user-facing trigger, such as a browser button, to activate the 'Fill Profile' command on a given page."
    ], 
        "github_link": "https://github.com/manojkommareddy/inventory-automation" 
},
]

YOUR_EXPERIENCE = [
    {
        "id": "exp-1",
        "company": "Aviation Component Solutions",
        "role": "Data Analytics Engineer",
        "date": "Feb 2025 - Present",
        "location": "Cleveland, Ohio",
        "details": [
            "Administered Oracle database and built ETL pipelines for efficient data flow and reporting.",
            "Designed and maintained dashboards in Power BI to analyze component reliability, attrition rates, and usage trends.",
            "Conducted failure trend and predictive analytics on PMA Parts, repair cycles, and cost-saving opportunities.",
            "Utilize Component Control Quantum ERP and Oracle SQL to manage parts inventory and maintain the MAXQPROD DB.",
            "Developed Power Automate alerts to proactively track parts shortages, part events, and inventory levels.",
            "Create and compile comprehensive Technical Data Packages (TDPs) for airline and MRO customers.",
        ]
    },
    {
        "id": "exp-2",
        "company": "CYIENT (at Pratt & Whitney)",
        "role": "Reliability Engineer",
        "date": "Nov 2021 - June 2023",
        "location": "Bangalore, India",
        "details": [
            "Led field event investigations (FEM) for IFSD, AOG, and turn-backs; performed Root Cause Analysis (RCA).",
            "Analyzed system and component reliability data (MTBF, failure trends, performance metrics) to ensure compliance.",
            "Managed warranty adjudication, cost analysis, and reliability reporting using CRM, CAF, NOR, and shop event data.",
            "Developed Excel-based automation tools and Power BI dashboards, reducing operational costs by 20%.",
            "Integrated and validated data from multiple sources (SAP, SQL, CRM, Power BI).",
        ]
    },
    {
        "id": "exp-3",
        "company": "GMR Aero Technic",
        "role": "Aircraft Maintenance Trainee",
        "date": "March 2021 - Nov 2021",
        "location": "Hyderabad, India",
        "details": [
            "Prepared aircraft work packages and ensured tooling, parts, and materials availability.",
            "Supported scheduled and unscheduled maintenance, troubleshooting hydraulic, avionics, and landing gear systems.",
            "Maintained FAA/DGCA-compliant records, service bulletins, and lease return documentation.",
        ]
    },
    {
        "id": "exp-4",
        "company": "TS Aviation Academy",
        "role": "Line Maintenance Planner",
        "date": "Nov 2020 - Feb 2021",
        "location": "Hyderabad, India",
        "details": [
            "Performed line maintenance and troubleshooting on Cessna 172/152, DA-42, and Learjet 25B aircraft.",
            "Conducted pre-flight checks, fueling, and component inspections to ensure airworthiness and safety.",
            "Assisted in routine and unscheduled maintenance of hydraulics, avionics, airframes, and landing gear.",
            "Maintained DGCA/FAA-compliant logs and service records.",
        ]
    },
]

YOUR_EDUCATION = [
    {
        "school": "Kent State University",
        "location": "Kent, Ohio",
        "degree": "Master of Science, Business Analytics (STEM Extension)",
        "date": "Dec 2024",
        "gpa": "3.8 GPA"
    },
    {
        "school": "Jawaharlal Nehru Technological University",
        "location": "Hyderabad, India",
        "degree": "Master of Science: Aviation",
        "date": "Aug 2022"
    },
    {
        "school": "Telangana State Aviation Academy",
        "location": "Hyderabad, India",
        "degree": "Diploma in Aircraft Maintenance Engineering (DGCA Approved)",
        "date": "June 2020"
    }
]

YOUR_CERTS = [
    "ATA 104 Level 1 General Familiarization on Pratt and Whitney Engines",
    "Career Essentials in Data Analysis by Microsoft and LinkedIn",
    "Lean Six Sigma Foundations - Upskill"
]

YOUR_ACHIEVEMENTS = [
    "ACE pilot for performing QCPC & RRCA",
    "Awarded silver and bronze for valuable Team and performer"
]


# --- Flask Routes ---
@app.route('/')
def home():
    # Pass all the data to the template
    return render_template(
        'index.html',
        info=YOUR_INFO,
        skills=YOUR_SKILLS,
        projects=YOUR_PROJECTS,
        experience=YOUR_EXPERIENCE,
        education=YOUR_EDUCATION,
        certs=YOUR_CERTS,
        achievements=YOUR_ACHIEVEMENTS
    )

if __name__ == '__main__':
    app.run(debug=True)
