import streamlit as st
import pandas as pd

def display_educational_resources():
    st.markdown('<div class="section-certification">Educational Resources</div>', unsafe_allow_html=True)
    
    st.markdown("""
    This section provides educational resources for interventional radiologists at all stages of their career,
    from trainees to experienced practitioners seeking to expand their knowledge.
    """)
    
    tab1, tab2, tab3, tab4 = st.tabs(["Training Resources", "Clinical Cases", "Procedural Videos", "IR Glossary"])
    
    with tab1:
        st.subheader("Training Resources for Interventional Radiology")
        
        st.markdown("""
        ### European Curriculum and Syllabus for Interventional Radiology
        
        The European Curriculum and Syllabus for Interventional Radiology serves as a comprehensive guide for training
        in interventional radiology across Europe. It outlines the knowledge, skills, and competencies required for
        interventional radiologists.
        
        ### CIRSE Academy
        
        The CIRSE Academy offers online courses covering various aspects of interventional radiology. These courses
        are designed to provide in-depth knowledge on specific topics and procedures.
        
        ### European Board of Interventional Radiology (EBIR)
        
        The EBIR is a certification of excellence in interventional radiology. It validates that certified individuals
        have the necessary knowledge and skills to practice interventional radiology at a high standard.
        
        ### CIRSE Library
        
        The CIRSE Library contains a vast collection of scientific presentations, posters, and abstracts from CIRSE
        congresses and meetings. It serves as a valuable resource for staying updated with the latest developments
        in interventional radiology.
        """)
        
        st.markdown("### Recommended Reading")
        
        recommended_reading = pd.DataFrame({
            "Title": [
                "Cardiovascular and Interventional Radiological Society of Europe Guidelines on Endovascular Treatment in Aortoiliac Arterial Disease",
                "Quality Improvement Guidelines for Percutaneous Transhepatic Cholangiography, Biliary Drainage, and Percutaneous Cholecystostomy",
                "Standards of Practice: Guidelines for Thermal Ablation of Primary and Secondary Lung Tumors",
                "Standards of Practice in Transarterial Radioembolization",
                "CIRSE Guidelines on Percutaneous Vertebral Augmentation"
            ],
            "Authors": [
                "Rand T, et al.",
                "Tsetis D, et al.",
                "Venturini M, et al.",
                "Bilbao JI, et al.",
                "Tsoumakidou G, et al."
            ],
            "Year": ["2019", "2018", "2020", "2017", "2017"],
            "Journal": [
                "Cardiovasc Intervent Radiol",
                "Cardiovasc Intervent Radiol",
                "Cardiovasc Intervent Radiol",
                "Cardiovasc Intervent Radiol",
                "Cardiovasc Intervent Radiol"
            ]
        })
        
        st.dataframe(recommended_reading)
    
    with tab2:
        st.subheader("Clinical Cases")
        
        case_categories = [
            "Vascular Interventions",
            "Oncologic Interventions",
            "Nonvascular Interventions",
            "Embolization Procedures"
        ]
        
        selected_category = st.selectbox("Select Category", case_categories)
        
        if selected_category == "Vascular Interventions":
            display_vascular_case()
        elif selected_category == "Oncologic Interventions":
            display_oncologic_case()
        elif selected_category == "Nonvascular Interventions":
            display_nonvascular_case()
        elif selected_category == "Embolization Procedures":
            display_embolization_case()
    
    with tab3:
        st.subheader("Procedural Videos")
        
        st.markdown("""
        This section would contain instructional videos demonstrating various interventional radiology procedures.
        In a production environment, these videos would be hosted and embedded here.
        
        ### Available Procedures:
        
        - Bronchial Artery Embolisation
        - Transjugular Intrahepatic Portosystemic Shunt (TIPS)
        - Thermal Ablation of Liver Tumors
        - Prostatic Artery Embolisation
        - Carotid Artery Stenting
        - Percutaneous Transhepatic Cholangiography
        """)
        
        st.info("Video content would be available in the production version of this application.")
    
    with tab4:
        st.subheader("Interventional Radiology Glossary")
        
        st.markdown("""
        This glossary provides definitions for common terms and abbreviations used in interventional radiology.
        """)
        
        glossary_terms = {
            "BAE": "Bronchial Artery Embolisation - A procedure to stop bleeding from the bronchial arteries.",
            "TACE": "Transarterial Chemoembolisation - A procedure that delivers chemotherapy directly to liver tumors while blocking their blood supply.",
            "TIPS": "Transjugular Intrahepatic Portosystemic Shunt - A procedure to create a new pathway between the portal vein and hepatic vein to reduce portal hypertension.",
            "PAE": "Prostatic Artery Embolisation - A procedure to treat benign prostatic hyperplasia by blocking blood flow to the prostate.",
            "UAE": "Uterine Artery Embolisation - A procedure to treat uterine fibroids by blocking blood flow to the fibroids.",
            "PTC": "Percutaneous Transhepatic Cholangiography - A procedure to visualize the biliary system.",
            "PTBD": "Percutaneous Transhepatic Biliary Drainage - A procedure to drain bile from the liver when there is a blockage in the bile ducts.",
            "CAS": "Carotid Artery Stenting - A procedure to open narrowed carotid arteries using a stent.",
            "EVAR": "Endovascular Aneurysm Repair - A procedure to repair an aortic aneurysm using a stent graft.",
            "RFA": "Radiofrequency Ablation - A procedure that uses heat generated by radio waves to destroy abnormal tissue.",
            "MWA": "Microwave Ablation - A procedure that uses microwave energy to destroy abnormal tissue.",
            "HIFU": "High-Intensity Focused Ultrasound - A procedure that uses focused ultrasound waves to destroy abnormal tissue.",
            "DSA": "Digital Subtraction Angiography - An imaging technique used to visualize blood vessels.",
            "CTA": "Computed Tomography Angiography - An imaging technique that uses CT to visualize blood vessels.",
            "MRA": "Magnetic Resonance Angiography - An imaging technique that uses MRI to visualize blood vessels.",
            "SEMS": "Self-Expanding Metal Stent - A type of stent that expands on its own when deployed.",
            "DAPT": "Dual Antiplatelet Therapy - The use of two antiplatelet medications to prevent blood clots.",
            "LMWH": "Low Molecular Weight Heparin - A type of anticoagulant medication.",
            "DOAC": "Direct Oral Anticoagulant - A type of anticoagulant medication that directly inhibits specific clotting factors.",
            "IR": "Interventional Radiology - A medical specialty that uses imaging guidance to perform minimally invasive procedures."
        }
        
        search_term = st.text_input("Search for a term:")
        
        if search_term:
            filtered_terms = {k: v for k, v in glossary_terms.items() if search_term.lower() in k.lower() or search_term.lower() in v.lower()}
            if filtered_terms:
                for term, definition in filtered_terms.items():
                    st.markdown(f"**{term}**: {definition}")
            else:
                st.info("No matching terms found.")
        else:
            for term, definition in glossary_terms.items():
                st.markdown(f"**{term}**: {definition}")

def display_vascular_case():
    st.markdown("""
    ### Case Study: Endovascular Management of Endoleak Following EVAR
    
    #### Clinical Presentation
    A 72-year-old male with a history of hypertension and coronary artery disease presented with an incidentally discovered 5.8 cm infrarenal abdominal aortic aneurysm (AAA) on CT scan. The patient underwent successful endovascular aneurysm repair (EVAR) with a bifurcated stent graft. At the 6-month follow-up CT scan, a type II endoleak was identified with contrast extravasation into the aneurysm sac from a lumbar artery. The aneurysm sac had enlarged to 6.2 cm.
    
    #### Diagnosis
    Type II endoleak following EVAR with aneurysm sac enlargement.
    
    #### Treatment Plan
    Given the enlargement of the aneurysm sac, intervention was recommended. The patient was scheduled for transarterial embolization of the feeding lumbar artery.
    
    #### Procedure
    1. Right common femoral artery access was obtained using ultrasound guidance.
    2. Selective catheterization of the internal iliac artery was performed.
    3. A microcatheter was advanced into the feeding lumbar artery.
    4. Embolization was performed using a combination of coils and liquid embolic agent.
    5. Post-embolization angiography confirmed successful occlusion of the feeding vessel.
    
    #### Outcome
    Follow-up CT scan at 3 months showed no evidence of endoleak and stable aneurysm sac size. The patient remained asymptomatic and continued to be followed with annual CT scans.
    
    #### Learning Points
    - Type II endoleaks are the most common type of endoleak after EVAR, occurring in up to 20% of cases.
    - Not all type II endoleaks require intervention; the decision to intervene is based on aneurysm sac enlargement.
    - Transarterial embolization is the preferred approach for type II endoleaks, with a technical success rate of 80-90%.
    - Alternative approaches include translumbar direct sac puncture and transcaval embolization.
    - Long-term follow-up is essential to monitor for recurrence of endoleak and aneurysm sac enlargement.
    """)

def display_oncologic_case():
    st.markdown("""
    ### Case Study: Thermal Ablation of Hepatocellular Carcinoma
    
    #### Clinical Presentation
    A 65-year-old male with a history of hepatitis C cirrhosis (Child-Pugh A) presented with a 2.5 cm hypervascular lesion in segment VI of the liver on surveillance ultrasound. Subsequent multiphasic CT scan showed arterial enhancement with washout on portal venous phase, consistent with hepatocellular carcinoma (HCC). The patient had preserved liver function with a bilirubin of 1.2 mg/dL, albumin of 3.8 g/dL, and INR of 1.1.
    
    #### Diagnosis
    Hepatocellular carcinoma (HCC) in a patient with hepatitis C cirrhosis.
    
    #### Treatment Plan
    After discussion in a multidisciplinary tumor board, the patient was deemed a candidate for thermal ablation given the size and location of the tumor.
    
    #### Procedure
    1. The procedure was performed under general anesthesia with CT guidance.
    2. A microwave ablation antenna was placed percutaneously into the center of the tumor.
    3. Ablation was performed with a power of 65W for 10 minutes.
    4. Post-ablation CT showed complete coverage of the tumor with a margin of at least 5 mm.
    
    #### Outcome
    Follow-up CT scan at 1 month showed complete ablation of the tumor with no evidence of residual or recurrent disease. The patient tolerated the procedure well with no complications. Subsequent surveillance imaging at 3, 6, and 12 months showed no evidence of local tumor progression or new lesions.
    
    #### Learning Points
    - Thermal ablation is a curative treatment option for early-stage HCC (BCLC 0-A) in patients who are not candidates for resection or transplantation.
    - For tumors <3 cm, thermal ablation achieves complete response rates of 90-95%.
    - Microwave ablation offers advantages over radiofrequency ablation, including larger ablation zones, shorter procedure times, and less susceptibility to heat sink effect.
    - A minimum ablation margin of 5 mm is recommended to ensure complete tumor destruction.
    - Regular surveillance imaging is essential to detect early recurrence or new lesions.
    """)

def display_nonvascular_case():
    st.markdown("""
    ### Case Study: Percutaneous Transhepatic Biliary Drainage for Malignant Biliary Obstruction
    
    #### Clinical Presentation
    A 58-year-old female presented with jaundice, pruritus, and weight loss. Laboratory tests showed elevated bilirubin (15.2 mg/dL) and alkaline phosphatase (450 U/L). CT scan revealed a pancreatic head mass with dilated intrahepatic and extrahepatic bile ducts. ERCP was attempted but failed due to tumor infiltration of the duodenum.
    
    #### Diagnosis
    Malignant biliary obstruction due to pancreatic head adenocarcinoma.
    
    #### Treatment Plan
    Given the failed ERCP, the patient was referred for percutaneous transhepatic biliary drainage (PTBD) to relieve the biliary obstruction.
    
    #### Procedure
    1. Under ultrasound and fluoroscopic guidance, a right-sided percutaneous transhepatic cholangiography (PTC) was performed, confirming dilated biliary ducts with obstruction at the level of the pancreatic head.
    2. A guidewire was advanced through the stricture into the duodenum.
    3. The tract was dilated, and an 8.5 Fr internal-external biliary drainage catheter was placed across the stricture.
    4. After 5 days, the patient returned for placement of a 10 mm × 80 mm self-expanding metal stent (SEMS) across the stricture.
    5. The internal-external drain was removed after confirming good stent position and function.
    
    #### Outcome
    The patient's jaundice and pruritus resolved within a week. Bilirubin levels decreased to 2.1 mg/dL at 2 weeks. The patient was able to start chemotherapy 3 weeks after the procedure. The stent remained patent for 8 months until the patient's death from disease progression.
    
    #### Learning Points
    - PTBD is indicated when ERCP fails or is not feasible.
    - Technical success rates for PTBD are 90-95%.
    - SEMS are preferred over plastic stents for malignant biliary obstruction due to longer patency rates (8-10 months vs. 3-4 months).
    - Complications include cholangitis, bleeding, and catheter dislodgement.
    - Prophylactic antibiotics are recommended to reduce the risk of cholangitis.
    - PTBD allows for rapid relief of symptoms and improvement in liver function, enabling patients to receive chemotherapy.
    """)

def display_embolization_case():
    st.markdown("""
    ### Case Study: Prostatic Artery Embolization for Benign Prostatic Hyperplasia
    
    #### Clinical Presentation
    A 68-year-old male presented with severe lower urinary tract symptoms (LUTS) including frequency, urgency, weak stream, and nocturia. His International Prostate Symptom Score (IPSS) was 26 (severe symptoms). Uroflowmetry showed a maximum flow rate (Qmax) of 8 mL/s. Prostate volume on transrectal ultrasound was 85 mL. The patient had tried medical therapy with alpha-blockers and 5-alpha reductase inhibitors with minimal improvement. He was not interested in surgical options due to concerns about sexual dysfunction.
    
    #### Diagnosis
    Benign prostatic hyperplasia (BPH) with severe LUTS refractory to medical therapy.
    
    #### Treatment Plan
    After discussion of treatment options, the patient elected to undergo prostatic artery embolization (PAE).
    
    #### Procedure
    1. Right femoral artery access was obtained using ultrasound guidance.
    2. Pelvic angiography was performed to identify the prostatic arteries.
    3. The right prostatic artery was selectively catheterized using a microcatheter.
    4. Embolization was performed using 300-500 μm microspheres until stasis was achieved.
    5. The left prostatic artery was then selectively catheterized and embolized in a similar fashion.
    6. Post-embolization angiography confirmed successful embolization of both prostatic arteries.
    
    #### Outcome
    The patient experienced mild post-embolization syndrome (pelvic pain, dysuria) for 3 days, which resolved with conservative management. At 3-month follow-up, his IPSS had improved to 8 (mild symptoms), and Qmax had increased to 15 mL/s. Prostate volume had decreased to 65 mL (24% reduction). The patient reported significant improvement in quality of life and preservation of sexual function.
    
    #### Learning Points
    - PAE is a minimally invasive alternative to surgery for BPH with severe LUTS.
    - Ideal candidates have prostate volumes >40 mL and moderate to severe LUTS (IPSS >12).
    - Technical success rates are >90%, with clinical success rates of 70-80%.
    - Complications are generally mild and include post-embolization syndrome, hematuria, and rectal bleeding (rare).
    - PAE preserves sexual function, making it an attractive option for sexually active men.
    - Prostate volume reduction of 20-40% can be expected at 3-6 months post-procedure.
    - Long-term outcomes show sustained improvement in symptoms for up to 3-5 years.
    """)
