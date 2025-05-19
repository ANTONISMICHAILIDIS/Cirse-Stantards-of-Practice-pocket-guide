import streamlit as st

# =====================
# Custom CSS Styling with CIRSE Official Colors
# =====================
st.markdown(
    """
    <style>
    /* Overall background and text colors */
    .reportview-container {
        background-color: #ffffff;
        color: #333333;
    }
    
    /* CIRSE Logo Colors */
    .cirse-logo {
        color: #6a4c93; /* Purple for C and E */
    }
    .cirse-logo-yellow {
        color: #f9c80e; /* Yellow for vertical bar */
    }
    
    /* Header colors (CIRSE purple) */
    h1 {
        color: #6a4c93;
        font-weight: bold;
    }
    
    h2, h3, h4 {
        color: #6a4c93;
    }
    
    /* Section headers with CIRSE color scheme */
    .section-society {
        background-color: #6a4c93; /* Purple */
        color: white;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    
    .section-onsite {
        background-color: #f86624; /* Orange */
        color: white;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    
    .section-online {
        background-color: #43aa8b; /* Green */
        color: white;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    
    .section-research {
        background-color: #bc4749; /* Red */
        color: white;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    
    .section-certification {
        background-color: #4361ee; /* Blue */
        color: white;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    
    .section-publications {
        background-color: #bc4749; /* Red */
        color: white;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    
    .section-patients {
        background-color: #43aa8b; /* Green */
        color: white;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    
    /* Document cards */
    .document-card {
        background-color: #f8f9fa;
        border-left: 4px solid #6a4c93;
        padding: 15px;
        margin-bottom: 15px;
        border-radius: 5px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    
    /* Sidebar styling */
    .sidebar .sidebar-content {
        background-color: #f2f2f2;
    }
    
    /* Small subtitle style */
    .small-font {
        font-size: 14px;
        color: #666666;
    }
    
    /* Disclaimer styling */
    .disclaimer {
        font-size: 12px;
        color: #666666;
        border-top: 1px solid #ddd;
        padding-top: 10px;
        margin-top: 20px;
    }
    
    /* Search box styling */
    .search-box {
        border: 2px solid #6a4c93;
        border-radius: 5px;
        padding: 10px;
    }
    
    /* Button styling */
    .stButton>button {
        background-color: #6a4c93;
        color: white;
    }
    
    /* CIRSE Standards of Practice logo styling */
    .sop-logo {
        background-color: #333333;
        color: white;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 20px;
    }
    
    .sop-logo-yellow {
        color: #f9c80e;
    }
    
    /* Year badge */
    .year-badge {
        background-color: #6a4c93;
        color: white;
        padding: 3px 8px;
        border-radius: 10px;
        font-size: 12px;
        margin-right: 10px;
    }
    
    /* Author badge */
    .author-badge {
        background-color: #f9c80e;
        color: #333333;
        padding: 3px 8px;
        border-radius: 10px;
        font-size: 12px;
    }
    </style>
    """, unsafe_allow_html=True
)

# =====================
# CIRSE Logo and Header
# =====================
def display_cirse_logo():
    st.markdown(
        """
        <div style="display: flex; align-items: center; margin-bottom: 20px;">
            <div style="font-size: 40px; font-weight: bold; margin-right: 10px;">
                <span class="cirse-logo">C</span><span class="cirse-logo-yellow">I</span><span class="cirse-logo">RSE</span>
            </div>
            <div style="font-size: 16px; color: #666666; margin-top: 5px;">
                Cardiovascular and Interventional Radiological Society of Europe
            </div>
        </div>
        """, unsafe_allow_html=True
    )

def display_sop_logo():
    st.markdown(
        """
        <div class="sop-logo">
            <span style="color: #f9c80e;">• • • •</span> <span style="color: white;">C</span><span style="color: #f9c80e;">IR</span><span style="color: white;">SE</span>
            <div style="font-size: 12px; margin-top: 5px;">STANDARDS OF PRACTICE</div>
        </div>
        """, unsafe_allow_html=True
    )

# =====================
# Sidebar Configuration
# =====================
def setup_sidebar():
    with st.sidebar:
        display_cirse_logo()
        
        st.markdown("---")
        
        with st.expander("About CIRSE", expanded=False):
            st.markdown("""
            **CIRSE (Cardiovascular and Interventional Radiological Society of Europe)**  
            CIRSE is the world's biggest community of healthcare professionals involved in minimally invasive image-guided procedures. CIRSE promotes excellence in interventional radiology through education, research, and dissemination of best practices.  
            Visit the [CIRSE website](https://www.cirse.org) for more information.
            """)
            
        with st.expander("Contact", expanded=False):
            st.markdown("""
            **Contact Information**  
            Email: info@cirse.org  
            Phone: +43 1 904 2003  
            Address: CIRSE Central Office, Neutorgasse 9/6, 1010 Vienna, AUSTRIA
            """)
        
        st.markdown("---")
        
        selected_language = st.selectbox("Select Language", ["English", "Spanish", "French", "German", "Chinese"])
        if selected_language != "English":
            st.info("Currently, all documents are only available in English. Translations coming soon!")
        
        st.markdown("---")
        
        st.markdown('<div class="small-font">Created for educational purposes</div>', unsafe_allow_html=True)

# =====================
# Main Page Configuration
# =====================
def main():
    setup_sidebar()
    
    # Main page header
    st.title("CIRSE Standards of Practice Pocket Guide")
    display_sop_logo()
    
    # Search functionality
    st.markdown('<div class="section-publications">Search Documents</div>', unsafe_allow_html=True)
    search_query = st.text_input("Enter search term:", key="search_box")
    
    # Filter tabs
    tab1, tab2, tab3 = st.tabs(["All Documents", "By Year", "By Category"])
    
    with tab1:
        if search_query:
            st.write(f"Showing results for: '{search_query}'")
        
        display_documents(search_query)
    
    with tab2:
        years = ["2024", "2023", "2022", "2021", "2020", "2019", "2018", "2017", "2016"]
        selected_year = st.selectbox("Select Year", years)
        display_documents_by_year(selected_year, search_query)
    
    with tab3:
        categories = [
            "Vascular Interventions", 
            "Oncologic Interventions", 
            "Nonvascular Interventions",
            "Embolization Procedures",
            "Procedural Care",
            "Quality and Safety"
        ]
        selected_category = st.selectbox("Select Category", categories)
        display_documents_by_category(selected_category, search_query)
    
    # Disclaimer
    st.markdown("""
    <div class="disclaimer">
    <strong>Disclaimer:</strong> The information provided in these standards of practice documents is believed to be true and accurate at the time of publication. 
    Neither the Standards of Practice Committee members, their working group members, nor CIRSE can accept any legal responsibility for any errors or omissions made.
    </div>
    """, unsafe_allow_html=True)

# =====================
# Document Display Functions
# =====================
def display_document_card(title, year, authors, content_preview):
    st.markdown(f"""
    <div class="document-card">
        <h3>{title}</h3>
        <div style="margin-bottom: 10px;">
            <span class="year-badge">{year}</span>
            <span class="author-badge">{authors}</span>
        </div>
        <p>{content_preview}...</p>
        <button style="background-color: #6a4c93; color: white; border: none; padding: 5px 10px; border-radius: 5px; cursor: pointer;">View Full Document</button>
    </div>
    """, unsafe_allow_html=True)

def display_documents(search_query=""):
    # This function will display all documents or filtered by search query
    documents_data = get_documents_data()
    
    displayed_count = 0
    for doc in documents_data:
        if search_query.lower() in doc["title"].lower() or search_query.lower() in doc["content_preview"].lower():
            display_document_card(doc["title"], doc["year"], doc["authors"], doc["content_preview"])
            displayed_count += 1
    
    if displayed_count == 0:
        st.info("No documents found matching your search criteria.")

def display_documents_by_year(year, search_query=""):
    # This function will display documents filtered by year and optionally by search query
    documents_data = get_documents_data()
    
    displayed_count = 0
    for doc in documents_data:
        if doc["year"] == year and (search_query == "" or search_query.lower() in doc["title"].lower() or search_query.lower() in doc["content_preview"].lower()):
            display_document_card(doc["title"], doc["year"], doc["authors"], doc["content_preview"])
            displayed_count += 1
    
    if displayed_count == 0:
        st.info(f"No documents found from {year} matching your search criteria.")

def display_documents_by_category(category, search_query=""):
    # This function will display documents filtered by category and optionally by search query
    documents_data = get_documents_data()
    
    displayed_count = 0
    for doc in documents_data:
        if doc["category"] == category and (search_query == "" or search_query.lower() in doc["title"].lower() or search_query.lower() in doc["content_preview"].lower()):
            display_document_card(doc["title"], doc["year"], doc["authors"], doc["content_preview"])
            displayed_count += 1
    
    if displayed_count == 0:
        st.info(f"No documents found in {category} matching your search criteria.")

# =====================
# Data Functions
# =====================
def get_documents_data():
    # This function returns a list of dictionaries containing document data
    # In a real app, this would likely come from a database
    return [
        {
            "title": "CIRSE Standards of Practice on Transjugular Intrahepatic Portosystemic Shunts",
            "year": "2024",
            "authors": "P. Lucatelli et al.",
            "category": "Vascular Interventions",
            "content_preview": "This document provides best practices for performing transjugular intrahepatic portosystemic shunts (TIPS) procedures, covering indications, contraindications, technical aspects, and follow-up care"
        },
        {
            "title": "CIRSE Standards of Practice on Portal Vein Embolization and Double Vein Embolization/Liver Venous Deprivation",
            "year": "2024",
            "authors": "T. Bilhim et al.",
            "category": "Vascular Interventions",
            "content_preview": "This document provides best practices for portal vein embolization (PVE) and double vein embolization/liver venous deprivation (DVE/LVD) procedures"
        },
        {
            "title": "CIRSE Standards of Practice on Carotid Artery Stenting",
            "year": "2024",
            "authors": "S. Spiliopoulos et al.",
            "category": "Vascular Interventions",
            "content_preview": "This document provides best practices for carotid artery stenting (CAS) procedures, covering patient selection, technical aspects, and complication management"
        },
        {
            "title": "CIRSE Standards of Practice on Management of Endoleaks Following Endovascular Aneurysm Repair",
            "year": "2024",
            "authors": "J-Y. Chun et al.",
            "category": "Vascular Interventions",
            "content_preview": "This document provides best practices for the management of endoleaks following endovascular aneurysm repair (EVAR)"
        },
        {
            "title": "CIRSE Standards of Practice for the Endovascular Treatment of Visceral and Renal Artery Aneurysms and Pseudoaneurysms",
            "year": "2023",
            "authors": "M. Rossi et al.",
            "category": "Vascular Interventions",
            "content_preview": "This document provides best practices for the endovascular treatment of visceral and renal artery aneurysms and pseudoaneurysms"
        },
        {
            "title": "CIRSE Standards of Practice on Oesophageal and Gastroduodenal Stenting",
            "year": "2023",
            "authors": "A. Diamantopoulos et al.",
            "category": "Nonvascular Interventions",
            "content_preview": "This document provides best practices for the safe and effective placement of self-expanding stents in the oesophagus and gastroduodenal tract"
        },
        {
            "title": "CIRSE Standards of Practice on Arterial Access for Interventions",
            "year": "2023",
            "authors": "E. Kashef et al.",
            "category": "Procedural Care",
            "content_preview": "This document provides best practices for safe and effective arterial access in interventional radiology, covering common femoral, radial, and brachial artery access"
        },
        {
            "title": "CIRSE Standards of Practice on Varicocele Embolisation",
            "year": "2022",
            "authors": "A. M. Ierardi et al.",
            "category": "Embolization Procedures",
            "content_preview": "This document provides best practices for performing percutaneous varicocele embolization, covering indications, contraindications, procedural steps, complications, and follow-up"
        },
        {
            "title": "CIRSE Standards of Practice on Bronchial Artery Embolisation",
            "year": "2022",
            "authors": "J. Kettenbach et al.",
            "category": "Embolization Procedures",
            "content_preview": "This document provides best practices to optimize safety and efficacy in performing bronchial artery embolisation (BAE), a minimally invasive, life-saving procedure used to treat haemoptysis"
        },
        {
            "title": "CIRSE Standards of Practice on Thermal Ablation of Bone Tumours",
            "year": "2022",
            "authors": "A. Ryan et al.",
            "category": "Oncologic Interventions",
            "content_preview": "This document provides best practices for thermal ablation of bone tumors, focusing on RFA, cryoablation, MWA, and HIFU for both benign and malignant bone lesions"
        },
        {
            "title": "CIRSE Standards of Practice on Hepatic Transarterial Chemoembolisation (TACE)",
            "year": "2021",
            "authors": "P. Lucatelli et al.",
            "category": "Oncologic Interventions",
            "content_preview": "This document provides best practices for TACE in hepatic tumors, covering indications, contraindications, technical aspects, and post-procedural management"
        },
        {
            "title": "CIRSE Standards of Practice on Percutaneous Transhepatic Cholangiography, Biliary Drainage and Stenting",
            "year": "2021",
            "authors": "M. Das et al.",
            "category": "Nonvascular Interventions",
            "content_preview": "This document provides best practices for performing percutaneous transhepatic cholangiography (PTC), biliary drainage (PTBD), and biliary stenting (PTBS)"
        },
        {
            "title": "CIRSE Standards of Practice on Below-the-Knee Revascularisation",
            "year": "2021",
            "authors": "S. Spiliopoulos et al.",
            "category": "Vascular Interventions",
            "content_preview": "This document provides best practices for performing below-the-knee (BTK) revascularisation, focusing on endovascular treatment for chronic limb-threatening ischemia (CLTI)"
        },
        {
            "title": "CIRSE Standards of Practice on Conducting Meetings on Morbidity and Mortality",
            "year": "2021",
            "authors": "J-Y. Chun et al.",
            "category": "Quality and Safety",
            "content_preview": "This document provides best practices for conducting morbidity and mortality (M&M) meetings in interventional radiology departments"
        },
        {
            "title": "CIRSE Standards of Practice on Peri-operative Anticoagulation Management During Interventional Radiology Procedures",
            "year": "2021",
            "authors": "M. Hadi/R. Uberoi et al.",
            "category": "Procedural Care",
            "content_preview": "This document provides best practices for peri-operative anticoagulation management during IR procedures, balancing bleeding and thromboembolic risks"
        },
        {
            "title": "CIRSE Standards of Practice on Gynaecological and Obstetric Haemorrhage",
            "year": "2020",
            "authors": "T. Rand et al.",
            "category": "Embolization Procedures",
            "content_preview": "This document provides best practices for the management of gynaecological and obstetric haemorrhage using interventional radiology techniques"
        },
        {
            "title": "CIRSE Standards of Practice on Analgesia and Sedation for Interventional Radiology in Adults",
            "year": "2020",
            "authors": "S. Romagnoli/F. Fanelli et al.",
            "category": "Procedural Care",
            "content_preview": "This document provides best practices for analgesia and sedation during interventional radiology procedures in adult patients"
        },
        {
            "title": "CIRSE Standards of Practice on Thermal Ablation of Liver Tumours",
            "year": "2020",
            "authors": "L. Crocetti et al.",
            "category": "Oncologic Interventions",
            "content_preview": "This document provides best practices for thermal ablation of liver tumors, covering patient selection, techniques, and follow-up care"
        },
        {
            "title": "CIRSE Standards of Practice on Thermal Ablation of Primary and Secondary Lung Tumours",
            "year": "2020",
            "authors": "M.Venturini et al.",
            "category": "Oncologic Interventions",
            "content_preview": "This document provides best practices for thermal ablation of primary and secondary lung tumors"
        },
        {
            "title": "CIRSE Standards of Practice on Diagnosis and Treatment of Pulmonary Arteriovenous Malformations",
            "year": "2020",
            "authors": "S. Müller-Hülsbeck et al.",
            "category": "Vascular Interventions",
            "content_preview": "This document provides best practices for the diagnosis and treatment of pulmonary arteriovenous malformations (PAVMs)"
        },
        {
            "title": "CIRSE Standards of Practice on Prostatic Artery Embolisation",
            "year": "2020",
            "authors": "F. Cornelis et al.",
            "category": "Embolization Procedures",
            "content_preview": "This document provides best practices for PAE as a treatment for BPH, covering patient selection, procedural techniques, safety measures, and follow-up care"
        }
    ]

if __name__ == "__main__":
    main()
