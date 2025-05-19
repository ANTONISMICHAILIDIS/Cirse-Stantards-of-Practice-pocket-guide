import streamlit as st
import pandas as pd

def display_procedures():
    st.markdown('<div class="section-certification">Procedures</div>', unsafe_allow_html=True)
    
    st.markdown("""
    This section provides detailed procedural guides for common interventional radiology procedures.
    Each guide includes pre-procedure preparation, procedural steps, and post-procedure care.
    """)
    
    procedures = [
        "Bronchial Artery Embolisation",
        "Varicocele Embolisation",
        "Prostatic Artery Embolisation",
        "Thermal Ablation of Liver Tumours",
        "Percutaneous Transhepatic Biliary Drainage",
        "Transjugular Intrahepatic Portosystemic Shunt (TIPS)",
        "Carotid Artery Stenting",
        "Uterine Artery Embolisation",
        "Inferior Vena Cava Filter Placement",
        "Endovascular Aneurysm Repair",
        "Peripheral Arterial Angioplasty and Stenting",
        "Vertebroplasty and Kyphoplasty",
        "Radiofrequency Ablation of Osteoid Osteoma",
        "Transarterial Chemoembolization (TACE)",
        "Percutaneous Nephrostomy"
    ]
    
    selected_procedure = st.selectbox("Select Procedure", procedures)
    
    if selected_procedure == "Bronchial Artery Embolisation":
        display_bae_procedure()
    elif selected_procedure == "Varicocele Embolisation":
        display_varicocele_procedure()
    elif selected_procedure == "Prostatic Artery Embolisation":
        display_pae_procedure()
    elif selected_procedure == "Thermal Ablation of Liver Tumours":
        display_liver_ablation_procedure()
    elif selected_procedure == "Percutaneous Transhepatic Biliary Drainage":
        display_ptbd_procedure()
    elif selected_procedure == "Transjugular Intrahepatic Portosystemic Shunt (TIPS)":
        display_tips_procedure()
    elif selected_procedure == "Carotid Artery Stenting":
        display_cas_procedure()
    elif selected_procedure == "Uterine Artery Embolisation":
        display_uae_procedure()
    elif selected_procedure == "Inferior Vena Cava Filter Placement":
        display_ivcf_procedure()
    elif selected_procedure == "Endovascular Aneurysm Repair":
        display_evar_procedure()
    elif selected_procedure == "Peripheral Arterial Angioplasty and Stenting":
        display_peripheral_procedure()
    elif selected_procedure == "Vertebroplasty and Kyphoplasty":
        display_vertebroplasty_procedure()
    elif selected_procedure == "Radiofrequency Ablation of Osteoid Osteoma":
        display_osteoid_osteoma_procedure()
    elif selected_procedure == "Transarterial Chemoembolization (TACE)":
        display_tace_procedure()
    elif selected_procedure == "Percutaneous Nephrostomy":
        display_nephrostomy_procedure()

def display_bae_procedure():
    st.markdown("""
    ### Bronchial Artery Embolisation (BAE) Procedure
    
    <div class="procedure-diagram">
    <h4>Pre-Procedure</h4>
    <ol>
        <li><strong>Initial Assessment</strong>
            <ul>
                <li>Confirm that bleeding is from the lungs</li>
                <li>Assess severity of haemoptysis</li>
                <li>Rule out non-pulmonary sources (e.g., gastrointestinal, nasopharyngeal)</li>
                <li>Review patient history, including previous haemoptysis episodes, infections, malignancies, and lung disease</li>
            </ul>
        </li>
        <li><strong>Imaging</strong>
            <ul>
                <li>Computed tomography angiography (CTA) - gold standard for localizing bleeding source</li>
                <li>Chest X-ray - initial screening (low sensitivity)</li>
                <li>Consider flexible bronchoscopy to clear airway if needed</li>
            </ul>
        </li>
        <li><strong>Laboratory Tests</strong>
            <ul>
                <li>Complete blood count</li>
                <li>Coagulation profile (PT/INR, aPTT)</li>
                <li>Renal function tests</li>
            </ul>
        </li>
        <li><strong>Optimization</strong>
            <ul>
                <li>Correct coagulopathy if present</li>
                <li>Stabilize patient hemodynamically</li>
                <li>Consider prophylactic antibiotics</li>
            </ul>
        </li>
    </ol>
    
    <h4>Procedure</h4>
    <ol>
        <li><strong>Access</strong>
            <ul>
                <li>Femoral artery (retrograde approach)</li>
                <li>4-5 Fr standard catheter for initial evaluation</li>
            </ul>
        </li>
        <li><strong>Angiography</strong>
            <ul>
                <li>Thoracic aortogram to identify bronchial arteries and non-bronchial systemic collaterals</li>
                <li>Selective catheterization of target vessels</li>
            </ul>
        </li>
        <li><strong>Superselective Catheterization</strong>
            <ul>
                <li>Microcatheter (2.7 Fr or smaller) for precise embolization</li>
                <li>Identify and avoid spinal arteries</li>
            </ul>
        </li>
        <li><strong>Embolization</strong>
            <ul>
                <li>Preferred agent: Polyvinyl alcohol (PVA) particles (300-500 μm)</li>
                <li>Alternatives: N-butyl-2-cyanoacrylate (NBCA) glue for high-flow fistulas, coils (used selectively)</li>
                <li>Slowly infuse embolic material until stasis is achieved</li>
                <li>Avoid reflux to prevent non-target embolization</li>
            </ul>
        </li>
        <li><strong>Post-Embolization Assessment</strong>
            <ul>
                <li>Perform post-embolization angiography to confirm treatment success</li>
                <li>Assess for any residual abnormal vascularity</li>
            </ul>
        </li>
    </ol>
    
    <h4>Post-Procedure</h4>
    <ol>
        <li><strong>Immediate Monitoring</strong>
            <ul>
                <li>Observe for recurrence of haemoptysis</li>
                <li>Monitor oxygen saturation and airway patency</li>
                <li>Assess for post-embolization syndrome (chest pain, fever)</li>
                <li>Monitor for neurological symptoms (spinal cord ischemia)</li>
            </ul>
        </li>
        <li><strong>Discharge Planning</strong>
            <ul>
                <li>Typically 24-48 hours post-procedure if no complications</li>
                <li>Provide patient education on warning signs requiring medical attention</li>
            </ul>
        </li>
        <li><strong>Follow-Up</strong>
            <ul>
                <li>Clinical follow-up at 2-4 weeks</li>
                <li>Repeat CTA or bronchoscopy if haemoptysis recurs</li>
                <li>Additional embolization may be required in 10-30% of cases due to recanalization</li>
                <li>Long-term management of underlying condition</li>
            </ul>
        </li>
    </ol>
    </div>
    """, unsafe_allow_html=True)

def display_varicocele_procedure():
    st.markdown("""
    ### Varicocele Embolisation Procedure
    
    <div class="procedure-diagram">
    <h4>Pre-Procedure</h4>
    <ol>
        <li><strong>Initial Assessment</strong>
            <ul>
                <li>Confirm varicocele diagnosis</li>
                <li>Assess severity using Valsalva maneuver</li>
                <li>Evaluate for infertility, testicular hypotrophy, or scrotal pain</li>
                <li>Review patient history, including previous varicocele treatments</li>
            </ul>
        </li>
        <li><strong>Imaging</strong>
            <ul>
                <li>Scrotal ultrasound (gold standard) and Doppler ultrasound</li>
                <li>Grade varicocele severity (Grade 1-3)</li>
            </ul>
        </li>
        <li><strong>Laboratory Tests</strong>
            <ul>
                <li>Coagulation profile</li>
                <li>Renal function tests</li>
                <li>Consider semen analysis for infertility cases</li>
            </ul>
        </li>
        <li><strong>Patient Preparation</strong>
            <ul>
                <li>Discuss alternative treatments (surgical ligation)</li>
                <li>Obtain informed consent</li>
                <li>NPO for 4-6 hours before procedure</li>
            </ul>
        </li>
    </ol>
    
    <h4>Procedure</h4>
    <ol>
        <li><strong>Access</strong>
            <ul>
                <li>Preferred: Right femoral or jugular vein</li>
                <li>5 Fr vascular sheath</li>
            </ul>
        </li>
        <li><strong>Venography</strong>
            <ul>
                <li>Catheterize left renal vein</li>
                <li>Identify left internal spermatic vein</li>
                <li>Perform venography to confirm reflux and identify collaterals</li>
            </ul>
        </li>
        <li><strong>Superselective Catheterization</strong>
            <ul>
                <li>Advance microcatheter into internal spermatic vein</li>
                <li>Perform venography to map venous anatomy</li>
            </ul>
        </li>
        <li><strong>Embolization</strong>
            <ul>
                <li>Options: Coils, sclerosing agents, or NBCA glue</li>
                <li>Coils are preferred for most cases</li>
                <li>Embolize main spermatic vein and significant collaterals</li>
            </ul>
        </li>
        <li><strong>Post-Embolization Assessment</strong>
            <ul>
                <li>Perform post-embolization venography to confirm occlusion</li>
                <li>Ensure no contrast extravasation</li>
            </ul>
        </li>
    </ol>
    
    <h4>Post-Procedure</h4>
    <ol>
        <li><strong>Immediate Monitoring</strong>
            <ul>
                <li>Monitor for pain, allergic reaction, or coil migration</li>
                <li>Observe for 2-4 hours before discharge</li>
            </ul>
        </li>
        <li><strong>Discharge Instructions</strong>
            <ul>
                <li>Mild scrotal discomfort may persist for 24-48 hours</li>
                <li>Avoid heavy lifting and strenuous activity for 1 week</li>
                <li>Return to normal activities within 1-2 days</li>
            </ul>
        </li>
        <li><strong>Follow-Up</strong>
            <ul>
                <li>Clinical exam at 1-3 months</li>
                <li>Repeat Doppler ultrasound at 3-6 months</li>
                <li>For infertility cases, repeat semen analysis at 3-6 months</li>
            </ul>
        </li>
    </ol>
    </div>
    """, unsafe_allow_html=True)

def display_pae_procedure():
    st.markdown("""
    ### Prostatic Artery Embolisation (PAE) Procedure
    
    <div class="procedure-diagram">
    <h4>Pre-Procedure</h4>
    <ol>
        <li><strong>Initial Assessment</strong>
            <ul>
                <li>Confirm BPH diagnosis and symptoms (IPSS >12)</li>
                <li>Assess prostate volume (>40 mL ideal)</li>
                <li>Evaluate for contraindications (active UTI, malignancy)</li>
                <li>Review patient history, including previous BPH treatments</li>
            </ul>
        </li>
        <li><strong>Urological Evaluation</strong>
            <ul>
                <li>PSA measurement</li>
                <li>Digital rectal examination</li>
                <li>Uroflowmetry</li>
                <li>Post-void residual volume</li>
                <li>Exclude malignancy (biopsy if indicated)</li>
            </ul>
        </li>
        <li><strong>Imaging</strong>
            <ul>
                <li>CTA or MRA for planning</li>
                <li>Assess pelvic arterial anatomy</li>
                <li>Identify prostatic arteries and potential anatomical variants</li>
            </ul>
        </li>
        <li><strong>Patient Preparation</strong>
            <ul>
                <li>Discuss alternative treatments (TURP, medications)</li>
                <li>Obtain informed consent</li>
                <li>Antibiotic prophylaxis</li>
                <li>Consider alpha-blocker 1 week before procedure</li>
            </ul>
        </li>
    </ol>
    
    <h4>Procedure</h4>
    <ol>
        <li><strong>Access</strong>
            <ul>
                <li>Femoral or radial arterial access</li>
                <li>5-6 Fr vascular sheath</li>
            </ul>
        </li>
        <li><strong>Angiography</strong>
            <ul>
                <li>Pelvic angiography to identify prostatic arteries</li>
                <li>Cone-beam CT may be used for better visualization</li>
            </ul>
        </li>
        <li><strong>Superselective Catheterization</strong>
            <ul>
                <li>Microcatheter to selectively catheterize prostatic arteries</li>
                <li>Identify and avoid non-target vessels (bladder, rectum, penis)</li>
            </ul>
        </li>
        <li><strong>Embolization</strong>
            <ul>
                <li>Embolize with 100-500 μm particles</li>
                <li>Endpoint: Near stasis in prostatic arteries</li>
                <li>Embolize both sides if possible</li>
            </ul>
        </li>
        <li><strong>Post-Embolization Assessment</strong>
            <ul>
                <li>Confirm adequate embolization</li>
                <li>Ensure no non-target embolization</li>
            </ul>
        </li>
    </ol>
    
    <h4>Post-Procedure</h4>
    <ol>
        <li><strong>Immediate Monitoring</strong>
            <ul>
                <li>Monitor for post-PAE syndrome (pelvic pain, dysuria, hematuria)</li>
                <li>Observe for 4-6 hours before discharge</li>
            </ul>
        </li>
        <li><strong>Discharge Instructions</strong>
            <ul>
                <li>Mild pelvic discomfort may persist for 3-5 days</li>
                <li>Dysuria and urgency may occur for 1-2 weeks</li>
                <li>Continue alpha-blocker for 1 month</li>
                <li>Avoid strenuous activity for 1 week</li>
            </ul>
        </li>
        <li><strong>Follow-Up</strong>
            <ul>
                <li>Clinical follow-up at 1, 3, and 6 months</li>
                <li>IPSS assessment at each visit</li>
                <li>Uroflowmetry at 3 months</li>
                <li>MRI or ultrasound at 3-6 months to assess prostate volume reduction</li>
            </ul>
        </li>
    </ol>
    </div>
    """, unsafe_allow_html=True)

def display_liver_ablation_procedure():
    st.markdown("""
    ### Thermal Ablation of Liver Tumours Procedure
    
    <div class="procedure-diagram">
    <h4>Pre-Procedure</h4>
    <ol>
        <li><strong>Initial Assessment</strong>
            <ul>
                <li>Confirm diagnosis (HCC, metastases)</li>
                <li>Assess tumor size, number, and location</li>
                <li>Evaluate liver function (Child-Pugh score)</li>
                <li>Review patient history, including previous treatments</li>
            </ul>
        </li>
        <li><strong>Imaging</strong>
            <ul>
                <li>Multiphasic CT or MRI with contrast</li>
                <li>Assess tumor characteristics and relationship to critical structures</li>
                <li>Plan access route</li>
            </ul>
        </li>
        <li><strong>Laboratory Tests</strong>
            <ul>
                <li>Complete blood count</li>
                <li>Coagulation profile (PT/INR, aPTT)</li>
                <li>Liver function tests</li>
                <li>Renal function tests</li>
                <li>Tumor markers (AFP for HCC)</li>
            </ul>
        </li>
        <li><strong>Multidisciplinary Discussion</strong>
            <ul>
                <li>Discuss alternative treatments (resection, transplantation, TACE)</li>
                <li>Confirm ablation as appropriate treatment option</li>
            </ul>
        </li>
        <li><strong>Patient Preparation</strong>
            <ul>
                <li>Obtain informed consent</li>
                <li>NPO for 6 hours before procedure</li>
                <li>Antibiotic prophylaxis</li>
                <li>Plan for anesthesia (general anesthesia preferred)</li>
            </ul>
        </li>
    </ol>
    
    <h4>Procedure</h4>
    <ol>
        <li><strong>Anesthesia</strong>
            <ul>
                <li>General anesthesia or deep sedation</li>
                <li>Local anesthesia at puncture site</li>
            </ul>
        </li>
        <li><strong>Imaging Guidance</strong>
            <ul>
                <li>Ultrasound, CT, or fusion imaging</li>
                <li>Identify target lesion and plan approach</li>
                <li>Avoid critical structures (major vessels, bile ducts)</li>
            </ul>
        </li>
        <li><strong>Ablation Technique</strong>
            <ul>
                <li>Options: Radiofrequency ablation (RFA), microwave ablation (MWA), cryoablation</li>
                <li>MWA preferred for larger tumors (>3 cm) or near vessels</li>
                <li>Position electrode/antenna in center of tumor</li>
                <li>For tumors >3 cm, consider multiple overlapping ablations</li>
                <li>Aim for 5-10 mm ablation margin beyond tumor edge</li>
            </ul>
        </li>
        <li><strong>Ablation Parameters</strong>
            <ul>
                <li>RFA: 12-15 minutes per ablation cycle</li>
                <li>MWA: 5-10 minutes per ablation cycle at 60-100W</li>
                <li>Adjust based on manufacturer recommendations and tumor size</li>
            </ul>
        </li>
        <li><strong>Post-Ablation Assessment</strong>
            <ul>
                <li>Immediate post-ablation imaging to confirm adequate coverage</li>
                <li>Assess for complications (bleeding, pneumothorax)</li>
                <li>Track ablation for hemostasis during withdrawal</li>
            </ul>
        </li>
    </ol>
    
    <h4>Post-Procedure</h4>
    <ol>
        <li><strong>Immediate Monitoring</strong>
            <ul>
                <li>Monitor vital signs for 4-6 hours</li>
                <li>Assess for post-ablation syndrome (fever, pain, malaise)</li>
                <li>Pain management</li>
            </ul>
        </li>
        <li><strong>Discharge Planning</strong>
            <ul>
                <li>Typically 24 hours post-procedure if no complications</li>
                <li>Provide patient education on warning signs requiring medical attention</li>
                <li>Avoid strenuous activity for 1 week</li>
            </ul>
        </li>
        <li><strong>Follow-Up</strong>
            <ul>
                <li>Contrast-enhanced CT or MRI at 1 month to assess treatment response</li>
                <li>Subsequent imaging at 3, 6, and 12 months, then every 6 months</li>
                <li>Monitor tumor markers if applicable</li>
                <li>Repeat ablation for local tumor progression if needed</li>
            </ul>
        </li>
    </ol>
    </div>
    """, unsafe_allow_html=True)

def display_ptbd_procedure():
    st.markdown("""
    ### Percutaneous Transhepatic Biliary Drainage (PTBD) Procedure
    
    <div class="procedure-diagram">
    <h4>Pre-Procedure</h4>
    <ol>
        <li><strong>Initial Assessment</strong>
            <ul>
                <li>Confirm biliary obstruction</li>
                <li>Assess level and cause of obstruction</li>
                <li>Evaluate for contraindications (severe coagulopathy, massive ascites)</li>
                <li>Review patient history, including previous biliary interventions</li>
            </ul>
        </li>
        <li><strong>Imaging</strong>
            <ul>
                <li>Ultrasound to confirm biliary dilation</li>
                <li>CT or MRI/MRCP to determine level and cause of obstruction</li>
                <li>Plan access route (right vs. left approach)</li>
            </ul>
        </li>
        <li><strong>Laboratory Tests</strong>
            <ul>
                <li>Complete blood count</li>
                <li>Coagulation profile (PT/INR, aPTT)</li>
                <li>Liver function tests</li>
                <li>Renal function tests</li>
                <li>Blood cultures if cholangitis suspected</li>
            </ul>
        </li>
        <li><strong>Patient Preparation</strong>
            <ul>
                <li>Correct coagulopathy (INR <1.5, platelets >50,000/µL)</li>
                <li>Antibiotic prophylaxis (e.g., Ceftriaxone + Metronidazole)</li>
                <li>NPO for 6 hours before procedure</li>
                <li>Obtain informed consent</li>
            </ul>
        </li>
    </ol>
    
    <h4>Procedure</h4>
    <ol>
        <li><strong>Anesthesia</strong>
            <ul>
                <li>Conscious sedation or general anesthesia</li>
                <li>Local anesthesia at puncture site</li>
            </ul>
        </li>
        <li><strong>Percutaneous Transhepatic Cholangiography (PTC)</strong>
            <ul>
                <li>Ultrasound-guided puncture of peripheral bile duct</li>
                <li>Right-sided approach preferred for distal obstructions</li>
                <li>Left-sided approach preferred for hilar obstructions</li>
                <li>Inject contrast to visualize biliary system</li>
                <li>Identify level and extent of obstruction</li>
            </ul>
        </li>
        <li><strong>Guidewire Manipulation</strong>
            <ul>
                <li>Advance guidewire through stricture if possible</li>
                <li>For external drainage only: position wire in biliary system above obstruction</li>
                <li>For internal-external drainage: advance wire through obstruction into bowel</li>
            </ul>
        </li>
        <li><strong>Biliary Drainage Catheter Placement</strong>
            <ul>
                <li>Dilate tract with fascial dilators</li>
                <li>Place 8-12 Fr drainage catheter</li>
                <li>External drainage: position above obstruction</li>
                <li>Internal-external drainage: position across obstruction into bowel</li>
                <li>Secure catheter to skin</li>
            </ul>
        </li>
        <li><strong>Biliary Stenting (if indicated)</strong>
            <ul>
                <li>Usually performed as a second-stage procedure after tract maturation</li>
                <li>Self-expanding metal stent (SEMS) preferred for malignant obstruction</li>
                <li>Plastic stents for benign strictures</li>
                <li>Confirm stent position with contrast injection</li>
            </ul>
        </li>
    </ol>
    
    <h4>Post-Procedure</h4>
    <ol>
        <li><strong>Immediate Monitoring</strong>
            <ul>
                <li>Monitor vital signs for 4-6 hours</li>
                <li>Assess for complications (bleeding, bile leak, sepsis)</li>
                <li>Check drain output and characteristics</li>
            </ul>
        </li>
        <li><strong>Catheter Management</strong>
            <ul>
                <li>Keep external drain open for 24-48 hours</li>
                <li>For internal-external drains, cap after 48 hours if drainage is adequate</li>
                <li>Flush catheter with 10 mL saline daily</li>
                <li>Secure catheter to prevent dislodgement</li>
            </ul>
        </li>
        <li><strong>Discharge Planning</strong>
            <ul>
                <li>Typically 24-48 hours post-procedure if no complications</li>
                <li>Provide patient education on catheter care</li>
                <li>Arrange home nursing if needed</li>
                <li>Continue antibiotics for 5-7 days</li>
            </ul>
        </li>
        <li><strong>Follow-Up</strong>
            <ul>
                <li>Clinical follow-up at 1-2 weeks</li>
                <li>Catheter exchange every 8-12 weeks</li>
                <li>For stents: imaging (CT/MRCP) at 3 months to assess patency</li>
                <li>Monitor liver function tests</li>
            </ul>
        </li>
    </ol>
    </div>
    """, unsafe_allow_html=True)

def display_tips_procedure():
    st.markdown("""
    ### Transjugular Intrahepatic Portosystemic Shunt (TIPS) Procedure
    
    <div class="procedure-diagram">
    <h4>Pre-Procedure</h4>
    <ol>
        <li><strong>Initial Assessment</strong>
            <ul>
                <li>Confirm portal hypertension and indication (variceal bleeding, refractory ascites)</li>
                <li>Assess liver function (Child-Pugh score, MELD score)</li>
                <li>Evaluate for contraindications (severe hepatic encephalopathy, heart failure)</li>
                <li>Review patient history, including previous treatments</li>
            </ul>
        </li>
        <li><strong>Imaging</strong>
            <ul>
                <li>Doppler ultrasound to assess portal vein patency and flow direction</li>
                <li>CT or MRI to evaluate vascular anatomy and liver parenchyma</li>
                <li>Assess for hepatocellular carcinoma</li>
            </ul>
        </li>
        <li><strong>Laboratory Tests</strong>
            <ul>
                <li>Complete blood count</li>
                <li>Coagulation profile (PT/INR, aPTT)</li>
                <li>Liver function tests</li>
                <li>Renal function tests</li>
                <li>Ammonia level (baseline for encephalopathy risk)</li>
            </ul>
        </li>
        <li><strong>Patient Preparation</strong>
            <ul>
                <li>Correct coagulopathy if possible (platelets >50,000/µL)</li>
                <li>Antibiotic prophylaxis</li>
                <li>NPO for 6 hours before procedure</li>
                <li>Obtain informed consent</li>
            </ul>
        </li>
    </ol>
    
    <h4>Procedure</h4>
    <ol>
        <li><strong>Anesthesia</strong>
            <ul>
                <li>Conscious sedation or general anesthesia</li>
                <li>Local anesthesia at puncture site</li>
            </ul>
        </li>
        <li><strong>Venous Access</strong>
            <ul>
                <li>Right internal jugular vein access</li>
                <li>Place 10 Fr vascular sheath</li>
            </ul>
        </li>
        <li><strong>Right Hepatic Vein Catheterization</strong>
            <ul>
                <li>Advance catheter into right hepatic vein</li>
                <li>Perform hepatic venography</li>
                <li>Measure hepatic venous pressure gradient (HVPG)</li>
            </ul>
        </li>
        <li><strong>Portal Vein Access</strong>
            <ul>
                <li>Use TIPS needle to puncture from hepatic vein to portal vein</li>
                <li>Confirm position with contrast injection</li>
                <li>Advance guidewire into portal vein</li>
            </ul>
        </li>
        <li><strong>Tract Dilation and Stent Placement</strong>
            <ul>
                <li>Dilate parenchymal tract with balloon</li>
                <li>Deploy covered stent (8-10 mm diameter) from portal vein to hepatic vein</li>
                <li>Post-dilation if needed</li>
                <li>Measure portal pressure gradient (should decrease by at least 50%)</li>
            </ul>
        </li>
        <li><strong>Variceal Embolization (if indicated)</strong>
            <ul>
                <li>Catheterize gastroesophageal varices</li>
                <li>Embolize with coils or sclerosing agents</li>
            </ul>
        </li>
        <li><strong>Final Assessment</strong>
            <ul>
                <li>Perform shunt venography to confirm patency</li>
                <li>Measure final portosystemic gradient</li>
            </ul>
        </li>
    </ol>
    
    <h4>Post-Procedure</h4>
    <ol>
        <li><strong>Immediate Monitoring</strong>
            <ul>
                <li>Monitor vital signs for 6-12 hours</li>
                <li>Assess for complications (bleeding, encephalopathy)</li>
                <li>Monitor for signs of heart failure due to increased preload</li>
            </ul>
        </li>
        <li><strong>Medical Management</strong>
            <ul>
                <li>Lactulose to prevent encephalopathy</li>
                <li>Diuretics for ascites management</li>
                <li>Beta-blockers may be discontinued</li>
            </ul>
        </li>
        <li><strong>Discharge Planning</strong>
            <ul>
                <li>Typically 24-48 hours post-procedure if no complications</li>
                <li>Provide patient education on signs of encephalopathy</li>
                <li>Dietary sodium restriction for ascites</li>
            </ul>
        </li>
        <li><strong>Follow-Up</strong>
            <ul>
                <li>Clinical follow-up at 2 weeks</li>
                <li>Doppler ultrasound at 1, 3, and 6 months, then annually</li>
                <li>Monitor for shunt dysfunction (stenosis, thrombosis)</li>
                <li>Adjust medications based on clinical response</li>
            </ul>
        </li>
    </ol>
    </div>
    """, unsafe_allow_html=True)

def display_cas_procedure():
    st.markdown("""
    ### Carotid Artery Stenting Procedure
    
    <div class="procedure-diagram">
    <h4>Pre-Procedure</h4>
    <ol>
        <li><strong>Initial Assessment</strong>
            <ul>
                <li>Confirm carotid stenosis (>70% symptomatic or >80% asymptomatic)</li>
                <li>Assess neurological status</li>
                <li>Evaluate for contraindications (severe tortuosity, heavy calcification)</li>
                <li>Review patient history, including previous stroke/TIA</li>
            </ul>
        </li>
        <li><strong>Imaging</strong>
            <ul>
                <li>Carotid duplex ultrasound</li>
                <li>CTA or MRA of carotid and cerebral arteries</li>
                <li>Digital subtraction angiography (if needed)</li>
                <li>Brain imaging to rule out recent infarction</li>
            </ul>
        </li>
        <li><strong>Laboratory Tests</strong>
            <ul>
                <li>Complete blood count</li>
                <li>Coagulation profile</li>
                <li>Renal function tests</li>
                <li>Lipid profile</li>
            </ul>
        </li>
        <li><strong>Medical Optimization</strong>
            <ul>
                <li>Dual antiplatelet therapy (aspirin + clopidogrel) for at least 5 days</li>
                <li>Statin therapy</li>
                <li>Optimize blood pressure control</li>
                <li>Hydration for renal protection</li>
            </ul>
        </li>
        <li><strong>Patient Preparation</strong>
            <ul>
                <li>Obtain informed consent</li>
                <li>NPO for 6 hours before procedure</li>
                <li>Baseline neurological examination</li>
            </ul>
        </li>
    </ol>
    
    <h4>Procedure</h4>
    <ol>
        <li><strong>Anesthesia</strong>
            <ul>
                <li>Conscious sedation preferred to monitor neurological status</li>
                <li>Local anesthesia at puncture site</li>
            </ul>
        </li>
        <li><strong>Arterial Access</strong>
            <ul>
                <li>Common femoral artery (preferred) or radial artery</li>
                <li>Place 6-8 Fr sheath</li>
            </ul>
        </li>
        <li><strong>Diagnostic Angiography</strong>
            <ul>
                <li>Arch aortography to assess arch type and origins of great vessels</li>
                <li>Selective catheterization of common carotid artery</li>
                <li>Angiography of carotid bifurcation and intracranial circulation</li>
            </ul>
        </li>
        <li><strong>Embolic Protection</strong>
            <ul>
                <li>Deploy distal filter or proximal protection device</li>
                <li>Distal filter placed beyond stenosis but before cerebral circulation</li>
                <li>Proximal protection with flow reversal or occlusion balloons</li>
            </ul>
        </li>
        <li><strong>Pre-dilation (if needed)</strong>
            <ul>
                <li>Low-profile balloon (2-3 mm) for tight stenoses</li>
                <li>Gentle inflation to allow stent passage</li>
            </ul>
        </li>
        <li><strong>Stent Deployment</strong>
            <ul>
                <li>Self-expanding stent sized to normal carotid diameter</li>
                <li>Position across stenosis with coverage of entire plaque</li>
                <li>Deploy stent with continuous monitoring of patient's neurological status</li>
            </ul>
        </li>
        <li><strong>Post-dilation</strong>
            <ul>
                <li>Balloon sized to 80-90% of normal carotid diameter</li>
                <li>Gentle inflation to optimize stent expansion</li>
                <li>Avoid aggressive dilation to reduce embolic risk</li>
            </ul>
        </li>
        <li><strong>Final Assessment</strong>
            <ul>
                <li>Perform completion angiography</li>
                <li>Assess for residual stenosis, dissection, or distal embolization</li>
                <li>Remove embolic protection device</li>
                <li>Perform intracranial angiography to confirm no embolization</li>
            </ul>
        </li>
    </ol>
    
    <h4>Post-Procedure</h4>
    <ol>
        <li><strong>Immediate Monitoring</strong>
            <ul>
                <li>Neurological checks every 15-30 minutes for first 2 hours</li>
                <li>Monitor for hypotension due to baroreceptor stimulation</li>
                <li>Monitor access site for bleeding or hematoma</li>
            </ul>
        </li>
        <li><strong>Medical Management</strong>
            <ul>
                <li>Continue dual antiplatelet therapy (aspirin indefinitely, clopidogrel for at least 1 month)</li>
                <li>Statin therapy</li>
                <li>Blood pressure control (avoid hypotension in first 24 hours)</li>
            </ul>
        </li>
        <li><strong>Discharge Planning</strong>
            <ul>
                <li>Typically 24 hours post-procedure if no complications</li>
                <li>Provide patient education on signs of stroke or TIA</li>
                <li>Instructions for medication compliance</li>
            </ul>
        </li>
        <li><strong>Follow-Up</strong>
            <ul>
                <li>Clinical follow-up at 1 month</li>
                <li>Carotid duplex ultrasound at 1, 6, and 12 months, then annually</li>
                <li>Monitor for in-stent restenosis</li>
                <li>Risk factor modification (smoking cessation, diabetes control)</li>
            </ul>
        </li>
    </ol>
    </div>
    """, unsafe_allow_html=True)

def display_uae_procedure():
    st.markdown("""
    ### Uterine Artery Embolisation Procedure
    
    <div class="procedure-diagram">
    <h4>Pre-Procedure</h4>
    <ol>
        <li><strong>Initial Assessment</strong>
            <ul>
                <li>Confirm uterine fibroids diagnosis</li>
                <li>Assess symptoms (heavy bleeding, pain, bulk symptoms)</li>
                <li>Evaluate for contraindications (pregnancy, malignancy, active infection)</li>
                <li>Review patient history, including desire for future fertility</li>
            </ul>
        </li>
        <li><strong>Imaging</strong>
            <ul>
                <li>Pelvic ultrasound to confirm fibroids</li>
                <li>MRI preferred for detailed assessment of fibroid number, size, and location</li>
                <li>Exclude adenomyosis or other pathology</li>
            </ul>
        </li>
        <li><strong>Laboratory Tests</strong>
            <ul>
                <li>Complete blood count</li>
                <li>Coagulation profile</li>
                <li>Renal function tests</li>
                <li>Pregnancy test</li>
                <li>Consider endometrial biopsy to exclude malignancy</li>
            </ul>
        </li>
        <li><strong>Patient Preparation</strong>
            <ul>
                <li>Discuss alternative treatments (myomectomy, hysterectomy, medical therapy)</li>
                <li>Obtain informed consent</li>
                <li>NPO for 6 hours before procedure</li>
                <li>Foley catheter placement</li>
                <li>Prophylactic antibiotics</li>
            </ul>
        </li>
    </ol>
    
    <h4>Procedure</h4>
    <ol>
        <li><strong>Anesthesia</strong>
            <ul>
                <li>Conscious sedation or general anesthesia</li>
                <li>Local anesthesia at puncture site</li>
            </ul>
        </li>
        <li><strong>Arterial Access</strong>
            <ul>
                <li>Common femoral artery (unilateral or bilateral approach)</li>
                <li>Place 5-6 Fr sheath</li>
            </ul>
        </li>
        <li><strong>Pelvic Angiography</strong>
            <ul>
                <li>Aortography to assess pelvic arterial anatomy</li>
                <li>Identify uterine arteries and potential collateral supply</li>
            </ul>
        </li>
        <li><strong>Selective Catheterization</strong>
            <ul>
                <li>Catheterize internal iliac artery</li>
                <li>Selective catheterization of uterine artery</li>
                <li>Advance microcatheter to distal uterine artery (beyond cervicovaginal branch)</li>
            </ul>
        </li>
        <li><strong>Embolization</strong>
            <ul>
                <li>Embolize with calibrated microspheres (500-900 μm)</li>
                <li>Endpoint: Near stasis in uterine artery with preservation of main trunk</li>
                <li>Avoid reflux to prevent non-target embolization</li>
            </ul>
        </li>
        <li><strong>Contralateral Embolization</strong>
            <ul>
                <li>Repeat procedure on contralateral side</li>
                <li>Bilateral embolization is standard</li>
            </ul>
        </li>
        <li><strong>Final Assessment</strong>
            <ul>
                <li>Perform completion angiography</li>
                <li>Confirm adequate embolization of both uterine arteries</li>
                <li>Assess for non-target embolization</li>
            </ul>
        </li>
    </ol>
    
    <h4>Post-Procedure</h4>
    <ol>
        <li><strong>Immediate Monitoring</strong>
            <ul>
                <li>Monitor vital signs</li>
                <li>Pain management (PCA, NSAIDs, opioids)</li>
                <li>Assess for post-embolization syndrome (pain, fever, nausea)</li>
                <li>Monitor for complications (groin hematoma, vaginal discharge)</li>
            </ul>
        </li>
        <li><strong>Medical Management</strong>
            <ul>
                <li>Aggressive pain control for first 24-48 hours</li>
                <li>Anti-inflammatory medications</li>
                <li>Antiemetics as needed</li>
                <li>Consider prophylactic antibiotics for 5-7 days</li>
            </ul>
        </li>
        <li><strong>Discharge Planning</strong>
            <ul>
                <li>Typically 24 hours post-procedure if pain is controlled</li>
                <li>Provide patient education on expected post-procedure course</li>
                <li>Warning signs requiring medical attention</li>
                <li>Gradual return to normal activities over 1-2 weeks</li>
            </ul>
        </li>
        <li><strong>Follow-Up</strong>
            <ul>
                <li>Clinical follow-up at 2 weeks and 3 months</li>
                <li>MRI at 3-6 months to assess fibroid shrinkage</li>
                <li>Monitor for symptom improvement</li>
                <li>Long-term follow-up to assess for recurrence</li>
            </ul>
        </li>
    </ol>
    </div>
    """, unsafe_allow_html=True)

def display_ivcf_procedure():
    st.markdown("""
    ### Inferior Vena Cava Filter Placement Procedure
    
    <div class="procedure-diagram">
    <h4>Pre-Procedure</h4>
    <ol>
        <li><strong>Initial Assessment</strong>
            <ul>
                <li>Confirm indication (VTE with contraindication to anticoagulation, recurrent VTE despite anticoagulation)</li>
                <li>Determine if temporary or permanent filter is needed</li>
                <li>Evaluate for contraindications (IVC thrombosis, severe uncorrected coagulopathy)</li>
                <li>Review patient history, including previous VTE and anticoagulation</li>
            </ul>
        </li>
        <li><strong>Imaging</strong>
            <ul>
                <li>Duplex ultrasound of lower extremities to assess for DVT</li>
                <li>CT venography or MR venography to assess IVC anatomy</li>
                <li>Evaluate IVC diameter, renal vein position, and presence of anomalies</li>
            </ul>
        </li>
        <li><strong>Laboratory Tests</strong>
            <ul>
                <li>Complete blood count</li>
                <li>Coagulation profile</li>
                <li>Renal function tests</li>
            </ul>
        </li>
        <li><strong>Patient Preparation</strong>
            <ul>
                <li>Discuss filter type (retrievable vs. permanent)</li>
                <li>Obtain informed consent</li>
                <li>NPO for 4-6 hours before procedure</li>
                <li>Continue anticoagulation if not contraindicated</li>
            </ul>
        </li>
    </ol>
    
    <h4>Procedure</h4>
    <ol>
        <li><strong>Anesthesia</strong>
            <ul>
                <li>Local anesthesia at puncture site</li>
                <li>Conscious sedation if needed</li>
            </ul>
        </li>
        <li><strong>Venous Access</strong>
            <ul>
                <li>Right internal jugular vein (preferred) or femoral vein</li>
                <li>Ultrasound-guided puncture</li>
                <li>Place 7-10 Fr sheath (depending on filter type)</li>
            </ul>
        </li>
        <li><strong>Venography</strong>
            <ul>
                <li>Perform inferior vena cavagram</li>
                <li>Identify renal veins and any anatomic variants</li>
                <li>Measure IVC diameter</li>
                <li>Assess for IVC thrombosis</li>
            </ul>
        </li>
        <li><strong>Filter Selection</strong>
            <ul>
                <li>Choose appropriate filter type based on indication and IVC anatomy</li>
                <li>Retrievable filters preferred for temporary indications</li>
                <li>Consider suprarenal placement if thrombus extends to renal veins</li>
            </ul>
        </li>
        <li><strong>Filter Deployment</strong>
            <ul>
                <li>Position filter delivery system below renal veins (typically at L2-L3 level)</li>
                <li>Confirm position with venography</li>
                <li>Deploy filter according to manufacturer's instructions</li>
            </ul>
        </li>
        <li><strong>Final Assessment</strong>
            <ul>
                <li>Perform completion venography</li>
                <li>Confirm proper filter position and deployment</li>
                <li>Assess for complications (tilting, migration)</li>
            </ul>
        </li>
    </ol>
    
    <h4>Post-Procedure</h4>
    <ol>
        <li><strong>Immediate Monitoring</strong>
            <ul>
                <li>Monitor vital signs</li>
                <li>Assess access site for bleeding or hematoma</li>
                <li>Bed rest for 2-4 hours</li>
            </ul>
        </li>
        <li><strong>Medical Management</strong>
            <ul>
                <li>Resume or initiate anticoagulation when safe</li>
                <li>Document filter type, indication, and retrieval plan</li>
            </ul>
        </li>
        <li><strong>Discharge Planning</strong>
            <ul>
                <li>Typically same day if no complications</li>
                <li>Provide patient education on filter purpose and follow-up</li>
                <li>For retrievable filters, emphasize importance of follow-up for potential removal</li>
            </ul>
        </li>
        <li><strong>Follow-Up</strong>
            <ul>
                <li>Clinical follow-up at 1 month</li>
                <li>For retrievable filters, reassess need for filter at 1-3 months</li>
                <li>Plan filter retrieval when anticoagulation can be safely initiated or indication resolves</li>
                <li>If filter remains in place >1 year, annual imaging to assess for complications</li>
            </ul>
        </li>
    </ol>
    </div>
    """, unsafe_allow_html=True)

def display_evar_procedure():
    st.markdown("""
    ### Endovascular Aneurysm Repair (EVAR) Procedure
    
    <div class="procedure-diagram">
    <h4>Pre-Procedure</h4>
    <ol>
        <li><strong>Initial Assessment</strong>
            <ul>
                <li>Confirm AAA diagnosis and size (typically >5.5 cm for men, >5.0 cm for women)</li>
                <li>Assess symptoms (most AAAs are asymptomatic)</li>
                <li>Evaluate for anatomic suitability (neck length, angulation, iliac access)</li>
                <li>Review patient history, including cardiac and pulmonary status</li>
            </ul>
        </li>
        <li><strong>Imaging</strong>
            <ul>
                <li>CTA with 3D reconstruction (gold standard)</li>
                <li>Assess proximal neck, aneurysm morphology, iliac arteries</li>
                <li>Measure key dimensions for stent graft sizing</li>
                <li>Evaluate access vessels for tortuosity and calcification</li>
            </ul>
        </li>
        <li><strong>Laboratory Tests</strong>
            <ul>
                <li>Complete blood count</li>
                <li>Coagulation profile</li>
                <li>Renal function tests</li>
                <li>Cardiac risk assessment</li>
            </ul>
        </li>
        <li><strong>Patient Preparation</strong>
            <ul>
                <li>Discuss alternative treatments (open repair, surveillance)</li>
                <li>Obtain informed consent</li>
                <li>NPO for 6 hours before procedure</li>
                <li>Prophylactic antibiotics</li>
                <li>Hydration for renal protection</li>
            </ul>
        </li>
    </ol>
    
    <h4>Procedure</h4>
    <ol>
        <li><strong>Anesthesia</strong>
            <ul>
                <li>General, regional, or local anesthesia with sedation</li>
            </ul>
        </li>
        <li><strong>Arterial Access</strong>
            <ul>
                <li>Bilateral common femoral artery access</li>
                <li>Surgical cutdown or percutaneous approach</li>
                <li>Place large-bore sheaths (12-24 Fr depending on device)</li>
            </ul>
        </li>
        <li><strong>Diagnostic Angiography</strong>
            <ul>
                <li>Perform aortography</li>
                <li>Identify renal arteries and other key landmarks</li>
                <li>Confirm measurements from pre-procedure imaging</li>
            </ul>
        </li>
        <li><strong>Main Body Deployment</strong>
            <ul>
                <li>Advance main body device over stiff guidewire</li>
                <li>Position just below renal arteries</li>
                <li>Confirm position with angiography</li>
                <li>Deploy main body of stent graft</li>
            </ul>
        </li>
        <li><strong>Contralateral Limb Cannulation</strong>
            <ul>
                <li>Catheterize contralateral gate from contralateral access</li>
                <li>Confirm position in gate with angiography</li>
                <li>Advance guidewire and catheter through gate</li>
            </ul>
        </li>
        <li><strong>Limb Deployment</strong>
            <ul>
                <li>Deploy contralateral limb</li>
                <li>Deploy ipsilateral limb if needed</li>
                <li>Ensure adequate overlap between components</li>
            </ul>
        </li>
        <li><strong>Balloon Molding</strong>
            <ul>
                <li>Balloon all attachment sites and overlap zones</li>
                <li>Ensure good apposition to vessel wall</li>
            </ul>
        </li>
        <li><strong>Final Assessment</strong>
            <ul>
                <li>Perform completion angiography</li>
                <li>Check for endoleaks</li>
                <li>Confirm patency of renal and iliac arteries</li>
                <li>Treat any type I or III endoleaks immediately</li>
            </ul>
        </li>
        <li><strong>Closure</strong>
            <ul>
                <li>Surgical closure of cutdowns</li>
                <li>Use closure devices for percutaneous access</li>
            </ul>
        </li>
    </ol>
    
    <h4>Post-Procedure</h4>
    <ol>
        <li><strong>Immediate Monitoring</strong>
            <ul>
                <li>Monitor vital signs</li>
                <li>Assess distal pulses</li>
                <li>Monitor for access site complications</li>
                <li>Assess for post-implantation syndrome (fever, leukocytosis)</li>
            </ul>
        </li>
        <li><strong>Medical Management</strong>
            <ul>
                <li>Antiplatelet therapy</li>
                <li>Pain management</li>
                <li>Continue antibiotics for 24 hours</li>
            </ul>
        </li>
        <li><strong>Discharge Planning</strong>
            <ul>
                <li>Typically 1-2 days post-procedure if no complications</li>
                <li>Provide patient education on activity restrictions</li>
                <li>Warning signs requiring medical attention</li>
                <li>Emphasize importance of follow-up imaging</li>
            </ul>
        </li>
        <li><strong>Follow-Up</strong>
            <ul>
                <li>CTA at 1 month, 6 months, 12 months, then annually</li>
                <li>Monitor for endoleaks, migration, aneurysm sac size</li>
                <li>Duplex ultrasound may be used for some follow-up visits to reduce radiation exposure</li>
                <li>Lifelong surveillance required</li>
            </ul>
        </li>
    </ol>
    </div>
    """, unsafe_allow_html=True)

def display_peripheral_procedure():
    st.markdown("""
    ### Peripheral Arterial Angioplasty and Stenting Procedure
    
    <div class="procedure-diagram">
    <h4>Pre-Procedure</h4>
    <ol>
        <li><strong>Initial Assessment</strong>
            <ul>
                <li>Confirm peripheral arterial disease diagnosis</li>
                <li>Assess symptoms (claudication, rest pain, tissue loss)</li>
                <li>Determine Rutherford classification</li>
                <li>Review patient history, including cardiovascular risk factors</li>
            </ul>
        </li>
        <li><strong>Imaging</strong>
            <ul>
                <li>Duplex ultrasound to localize stenoses/occlusions</li>
                <li>CTA or MRA for detailed anatomic assessment</li>
                <li>Assess lesion length, calcification, and runoff vessels</li>
            </ul>
        </li>
        <li><strong>Laboratory Tests</strong>
            <ul>
                <li>Complete blood count</li>
                <li>Coagulation profile</li>
                <li>Renal function tests</li>
                <li>Lipid profile</li>
            </ul>
        </li>
        <li><strong>Medical Optimization</strong>
            <ul>
                <li>Antiplatelet therapy (aspirin +/- clopidogrel)</li>
                <li>Statin therapy</li>
                <li>Optimize diabetes control</li>
                <li>Smoking cessation</li>
                <li>Hydration for renal protection</li>
            </ul>
        </li>
        <li><strong>Patient Preparation</strong>
            <ul>
                <li>Discuss alternative treatments (medical therapy, bypass surgery)</li>
                <li>Obtain informed consent</li>
                <li>NPO for 6 hours before procedure</li>
            </ul>
        </li>
    </ol>
    
    <h4>Procedure</h4>
    <ol>
        <li><strong>Anesthesia</strong>
            <ul>
                <li>Local anesthesia at puncture site</li>
                <li>Conscious sedation if needed</li>
            </ul>
        </li>
        <li><strong>Arterial Access</strong>
            <ul>
                <li>Common femoral artery (antegrade or retrograde depending on lesion location)</li>
                <li>Alternative access: Brachial, radial, or popliteal artery</li>
                <li>Place appropriate sheath (5-7 Fr)</li>
            </ul>
        </li>
        <li><strong>Diagnostic Angiography</strong>
            <ul>
                <li>Perform baseline angiography</li>
                <li>Assess lesion characteristics (length, stenosis severity, calcification)</li>
                <li>Evaluate inflow and outflow vessels</li>
            </ul>
        </li>
        <li><strong>Lesion Crossing</strong>
            <ul>
                <li>Cross lesion with appropriate guidewire (0.035", 0.018", or 0.014")</li>
                <li>For occlusions, use specialized crossing techniques (subintimal, retrograde)</li>
                <li>Confirm intraluminal position distal to lesion</li>
            </ul>
        </li>
        <li><strong>Balloon Angioplasty</strong>
            <ul>
                <li>Select appropriate balloon size (match to reference vessel diameter)</li>
                <li>Inflate balloon to nominal pressure</li>
                <li>Consider prolonged inflation for resistant lesions</li>
                <li>For calcified lesions, consider specialty balloons (cutting, scoring)</li>
            </ul>
        </li>
        <li><strong>Stent Placement (if indicated)</strong>
            <ul>
                <li>Indications: Flow-limiting dissection, residual stenosis >30%, elastic recoil</li>
                <li>Select appropriate stent type (self-expanding for SFA/popliteal, balloon-expandable for iliac)</li>
                <li>Size stent to reference vessel diameter</li>
                <li>Deploy stent across lesion with adequate coverage</li>
                <li>Post-dilate stent if needed</li>
            </ul>
        </li>
        <li><strong>Drug-Coated Balloon (if indicated)</strong>
            <ul>
                <li>Consider for SFA/popliteal lesions to reduce restenosis</li>
                <li>Predilate with plain balloon</li>
                <li>Inflate DCB for recommended dwell time (typically 2-3 minutes)</li>
            </ul>
        </li>
        <li><strong>Final Assessment</strong>
            <ul>
                <li>Perform completion angiography</li>
                <li>Assess for residual stenosis, dissection, or distal embolization</li>
                <li>Evaluate runoff vessels</li>
            </ul>
        </li>
    </ol>
    
    <h4>Post-Procedure</h4>
    <ol>
        <li><strong>Immediate Monitoring</strong>
            <ul>
                <li>Monitor vital signs</li>
                <li>Assess distal pulses and compare to baseline</li>
                <li>Monitor access site for bleeding or hematoma</li>
                <li>Bed rest for 2-6 hours depending on access site and closure method</li>
            </ul>
        </li>
        <li><strong>Medical Management</strong>
            <ul>
                <li>Dual antiplatelet therapy for at least 1 month after stenting</li>
                <li>Continue statin therapy</li>
                <li>Pain management as needed</li>
            </ul>
        </li>
        <li><strong>Discharge Planning</strong>
            <ul>
                <li>Typically same day or next day if no complications</li>
                <li>Provide patient education on activity guidelines</li>
                <li>Warning signs requiring medical attention</li>
                <li>Emphasize importance of risk factor modification</li>
            </ul>
        </li>
        <li><strong>Follow-Up</strong>
            <ul>
                <li>Clinical follow-up at 1 month</li>
                <li>Duplex ultrasound at 3, 6, and 12 months</li>
                <li>Ankle-brachial index measurements</li>
                <li>Monitor for restenosis or disease progression</li>
                <li>Continued risk factor modification</li>
            </ul>
        </li>
    </ol>
    </div>
    """, unsafe_allow_html=True)

def display_vertebroplasty_procedure():
    st.markdown("""
    ### Vertebroplasty and Kyphoplasty Procedure
    
    <div class="procedure-diagram">
    <h4>Pre-Procedure</h4>
    <ol>
        <li><strong>Initial Assessment</strong>
            <ul>
                <li>Confirm vertebral compression fracture diagnosis</li>
                <li>Assess pain and functional status</li>
                <li>Determine fracture age (acute/subacute preferred)</li>
                <li>Evaluate for contraindications (infection, coagulopathy, radiculopathy)</li>
            </ul>
        </li>
        <li><strong>Imaging</strong>
            <ul>
                <li>Spine radiographs to identify fracture level</li>
                <li>MRI to assess fracture age (edema indicates acute/subacute fracture)</li>
                <li>CT for detailed anatomy and posterior wall integrity</li>
                <li>Bone scan if MRI contraindicated</li>
            </ul>
        </li>
        <li><strong>Laboratory Tests</strong>
            <ul>
                <li>Complete blood count</li>
                <li>Coagulation profile</li>
                <li>Renal function tests</li>
                <li>Consider metabolic workup for osteoporosis</li>
            </ul>
        </li>
        <li><strong>Patient Preparation</strong>
            <ul>
                <li>Discuss procedure options (vertebroplasty vs. kyphoplasty)</li>
                <li>Obtain informed consent</li>
                <li>NPO for 6 hours before procedure</li>
                <li>Prophylactic antibiotics</li>
            </ul>
        </li>
    </ol>
    
    <h4>Procedure</h4>
    <ol>
        <li><strong>Anesthesia</strong>
            <ul>
                <li>Conscious sedation or general anesthesia</li>
                <li>Local anesthesia at puncture site</li>
            </ul>
        </li>
        <li><strong>Patient Positioning</strong>
            <ul>
                <li>Prone position on radiolucent table</li>
                <li>Pillows under chest and pelvis to reduce lordosis</li>
            </ul>
        </li>
        <li><strong>Imaging Guidance</strong>
            <ul>
                <li>Fluoroscopy (biplane preferred)</li>
                <li>Identify target vertebra and plan approach</li>
                <li>Transpedicular approach for thoracic and lumbar spine</li>
                <li>Parapedicular approach if pedicles are small</li>
            </ul>
        </li>
        <li><strong>Needle Placement</strong>
            <ul>
                <li>Advance 11-13G vertebroplasty needle through pedicle</li>
                <li>Confirm position with AP and lateral fluoroscopy</li>
                <li>Advance needle to anterior third of vertebral body</li>
                <li>Bilateral approach often needed for adequate filling</li>
            </ul>
        </li>
        <li><strong>For Kyphoplasty Only</strong>
            <ul>
                <li>Insert balloon tamp through working cannula</li>
                <li>Inflate balloon under fluoroscopic guidance</li>
                <li>Monitor inflation pressure and volume</li>
                <li>Create cavity and potentially restore vertebral height</li>
                <li>Deflate and remove balloon</li>
            </ul>
        </li>
        <li><strong>Cement Injection</strong>
            <ul>
                <li>Prepare polymethylmethacrylate (PMMA) cement</li>
                <li>Inject cement under continuous fluoroscopic guidance</li>
                <li>Monitor for cement leakage</li>
                <li>Stop injection if leakage occurs</li>
                <li>Aim for adequate filling of anterior two-thirds of vertebral body</li>
            </ul>
        </li>
        <li><strong>Needle Removal</strong>
            <ul>
                <li>Remove needle before cement hardens</li>
                <li>Consider needle rotation during removal</li>
            </ul>
        </li>
        <li><strong>Final Assessment</strong>
            <ul>
                <li>Perform final fluoroscopic images</li>
                <li>Assess cement distribution</li>
                <li>Document any cement leakage</li>
            </ul>
        </li>
    </ol>
    
    <h4>Post-Procedure</h4>
    <ol>
        <li><strong>Immediate Monitoring</strong>
            <ul>
                <li>Monitor vital signs</li>
                <li>Neurological examination</li>
                <li>Bed rest for 1-2 hours</li>
                <li>Assess for complications (cement leakage, embolism)</li>
            </ul>
        </li>
        <li><strong>Pain Management</strong>
            <ul>
                <li>Most patients experience immediate pain relief</li>
                <li>Analgesics as needed</li>
                <li>Ice to puncture site</li>
            </ul>
        </li>
        <li><strong>Discharge Planning</strong>
            <ul>
                <li>Typically same day if no complications</li>
                <li>Provide patient education on activity guidelines</li>
                <li>Warning signs requiring medical attention</li>
                <li>Gradual return to normal activities</li>
            </ul>
        </li>
        <li><strong>Follow-Up</strong>
            <ul>
                <li>Clinical follow-up at 2-4 weeks</li>
                <li>Radiographs to assess cement position</li>
                <li>Osteoporosis management to prevent future fractures</li>
                <li>Consider bone mineral density testing</li>
                <li>Calcium and vitamin D supplementation</li>
            </ul>
        </li>
    </ol>
    </div>
    """, unsafe_allow_html=True)

def display_osteoid_osteoma_procedure():
    st.markdown("""
    ### Radiofrequency Ablation of Osteoid Osteoma Procedure
    
    <div class="procedure-diagram">
    <h4>Pre-Procedure</h4>
    <ol>
        <li><strong>Initial Assessment</strong>
            <ul>
                <li>Confirm osteoid osteoma diagnosis</li>
                <li>Assess pain pattern (typically night pain relieved by NSAIDs)</li>
                <li>Evaluate lesion location and accessibility</li>
                <li>Review patient history, including previous treatments</li>
            </ul>
        </li>
        <li><strong>Imaging</strong>
            <ul>
                <li>Plain radiographs to identify nidus and reactive sclerosis</li>
                <li>CT (gold standard) for precise localization of nidus</li>
                <li>MRI for soft tissue assessment if needed</li>
                <li>Bone scan to confirm metabolic activity</li>
            </ul>
        </li>
        <li><strong>Laboratory Tests</strong>
            <ul>
                <li>Complete blood count</li>
                <li>Coagulation profile</li>
                <li>Renal function tests</li>
            </ul>
        </li>
        <li><strong>Patient Preparation</strong>
            <ul>
                <li>Discuss alternative treatments (surgical excision, medical management)</li>
                <li>Obtain informed consent</li>
                <li>NPO for 6 hours before procedure</li>
                <li>Prophylactic antibiotics</li>
            </ul>
        </li>
    </ol>
    
    <h4>Procedure</h4>
    <ol>
        <li><strong>Anesthesia</strong>
            <ul>
                <li>General anesthesia preferred, especially for lesions near neurovascular structures</li>
                <li>Conscious sedation with local anesthesia for superficial lesions</li>
            </ul>
        </li>
        <li><strong>Patient Positioning</strong>
            <ul>
                <li>Position based on lesion location</li>
                <li>Ensure access to target lesion</li>
                <li>Secure patient to prevent movement</li>
            </ul>
        </li>
        <li><strong>Imaging Guidance</strong>
            <ul>
                <li>CT guidance (preferred) for precise localization</li>
                <li>Fluoroscopy may be used for some locations</li>
                <li>Plan safest approach to nidus</li>
            </ul>
        </li>
        <li><strong>Access Planning</strong>
            <ul>
                <li>Identify entry point and trajectory</li>
                <li>Avoid neurovascular structures</li>
                <li>Mark skin entry site</li>
                <li>Sterilize and drape</li>
            </ul>
        </li>
        <li><strong>Needle Placement</strong>
            <ul>
                <li>Local anesthesia at entry site</li>
                <li>Use bone biopsy needle to create access tract</li>
                <li>Advance drill or trocar to nidus</li>
                <li>Confirm position with CT</li>
            </ul>
        </li>
        <li><strong>RFA Electrode Placement</strong>
            <ul>
                <li>Insert RFA electrode through access cannula</li>
                <li>Position electrode tip in center of nidus</li>
                <li>Confirm position with CT</li>
            </ul>
        </li>
        <li><strong>Ablation</strong>
            <ul>
                <li>Set RFA generator parameters (typically 90°C for 6 minutes)</li>
                <li>Perform ablation</li>
                <li>Monitor impedance and temperature</li>
                <li>For larger nidus (>1 cm), consider multiple overlapping ablations</li>
            </ul>
        </li>
        <li><strong>Tract Ablation</strong>
            <ul>
                <li>Ablate access tract during withdrawal to prevent bleeding</li>
                <li>Remove electrode and cannula</li>
            </ul>
        </li>
        <li><strong>Final Assessment</strong>
            <ul>
                <li>Perform final CT to assess for complications</li>
                <li>Apply sterile dressing</li>
            </ul>
        </li>
    </ol>
    
    <h4>Post-Procedure</h4>
    <ol>
        <li><strong>Immediate Monitoring</strong>
            <ul>
                <li>Monitor vital signs</li>
                <li>Assess pain level</li>
                <li>Neurological examination if lesion near neural structures</li>
                <li>Observe for 2-4 hours</li>
            </ul>
        </li>
        <li><strong>Pain Management</strong>
            <ul>
                <li>Most patients experience significant pain relief within 24-48 hours</li>
                <li>Analgesics as needed</li>
                <li>Ice to reduce swelling</li>
            </ul>
        </li>
        <li><strong>Discharge Planning</strong>
            <ul>
                <li>Typically same day if no complications</li>
                <li>Provide patient education on activity restrictions</li>
                <li>Warning signs requiring medical attention</li>
                <li>Gradual return to normal activities over 1-2 weeks</li>
                <li>Weight-bearing restrictions for lower extremity lesions</li>
            </ul>
        </li>
        <li><strong>Follow-Up</strong>
            <ul>
                <li>Clinical follow-up at 2-4 weeks</li>
                <li>Assess pain relief (>90% of patients experience complete relief)</li>
                <li>CT at 6 months if symptoms persist</li>
                <li>Long-term success rate >90%</li>
                <li>Recurrence rate <10%, may require repeat ablation</li>
            </ul>
        </li>
    </ol>
    </div>
    """, unsafe_allow_html=True)

def display_tace_procedure():
    st.markdown("""
    ### Transarterial Chemoembolization (TACE) Procedure
    
    <div class="procedure-diagram">
    <h4>Pre-Procedure</h4>
    <ol>
        <li><strong>Initial Assessment</strong>
            <ul>
                <li>Confirm diagnosis (HCC, metastatic liver tumors)</li>
                <li>Assess liver function (Child-Pugh class, MELD score)</li>
                <li>Evaluate for contraindications (decompensated cirrhosis, portal vein thrombosis)</li>
                <li>Review patient history, including previous treatments</li>
            </ul>
        </li>
        <li><strong>Imaging</strong>
            <ul>
                <li>Multiphasic CT or MRI with contrast</li>
                <li>Assess tumor number, size, and location</li>
                <li>Evaluate vascular anatomy</li>
                <li>Rule out extrahepatic disease</li>
            </ul>
        </li>
        <li><strong>Laboratory Tests</strong>
            <ul>
                <li>Complete blood count</li>
                <li>Coagulation profile</li>
                <li>Liver function tests</li>
                <li>Renal function tests</li>
                <li>Tumor markers (AFP for HCC)</li>
            </ul>
        </li>
        <li><strong>Multidisciplinary Discussion</strong>
            <ul>
                <li>Discuss alternative treatments (ablation, resection, transplantation)</li>
                <li>Confirm TACE as appropriate treatment option</li>
                <li>Determine TACE type (conventional vs. drug-eluting beads)</li>
            </ul>
        </li>
        <li><strong>Patient Preparation</strong>
            <ul>
                <li>Obtain informed consent</li>
                <li>NPO for 6 hours before procedure</li>
                <li>Hydration for renal protection</li>
                <li>Prophylactic antibiotics</li>
                <li>Anti-emetics</li>
            </ul>
        </li>
    </ol>
    
    <h4>Procedure</h4>
    <ol>
        <li><strong>Anesthesia</strong>
            <ul>
                <li>Conscious sedation or general anesthesia</li>
                <li>Local anesthesia at puncture site</li>
            </ul>
        </li>
        <li><strong>Arterial Access</strong>
            <ul>
                <li>Common femoral artery</li>
                <li>Place 5-6 Fr sheath</li>
            </ul>
        </li>
        <li><strong>Diagnostic Angiography</strong>
            <ul>
                <li>Perform celiac and superior mesenteric arteriography</li>
                <li>Identify hepatic arterial anatomy and variants</li>
                <li>Assess tumor vascularity</li>
                <li>Identify potential extrahepatic supply</li>
            </ul>
        </li>
        <li><strong>Selective Catheterization</strong>
            <ul>
                <li>Catheterize common hepatic artery</li>
                <li>Advance to proper hepatic artery</li>
                <li>Superselective catheterization of tumor-feeding branches</li>
                <li>Use microcatheter for selective delivery</li>
            </ul>
        </li>
        <li><strong>Chemoembolization</strong>
            <ul>
                <li>Conventional TACE (cTACE):
                    <ul>
                        <li>Prepare emulsion of chemotherapy (doxorubicin, cisplatin, mitomycin C) with lipiodol</li>
                        <li>Inject emulsion followed by embolic agent (gelfoam, PVA particles)</li>
                    </ul>
                </li>
                <li>Drug-Eluting Bead TACE (DEB-TACE):
                    <ul>
                        <li>Load microspheres with chemotherapy (typically doxorubicin)</li>
                        <li>Inject drug-eluting beads</li>
                    </ul>
                </li>
            </ul>
        </li>
        <li><strong>Endpoint Assessment</strong>
            <ul>
                <li>Perform post-embolization angiography</li>
                <li>Confirm stasis or near-stasis in tumor-feeding vessels</li>
                <li>Assess for non-target embolization</li>
            </ul>
        </li>
    </ol>
    
    <h4>Post-Procedure</h4>
    <ol>
        <li><strong>Immediate Monitoring</strong>
            <ul>
                <li>Monitor vital signs</li>
                <li>Assess for post-embolization syndrome (pain, fever, nausea)</li>
                <li>Monitor for complications (access site bleeding, liver failure)</li>
            </ul>
        </li>
        <li><strong>Medical Management</strong>
            <ul>
                <li>Pain control</li>
                <li>Anti-emetics</li>
                <li>Hydration</li>
                <li>Antipyretics for post-embolization fever</li>
                <li>Continue antibiotics if indicated</li>
            </ul>
        </li>
        <li><strong>Discharge Planning</strong>
            <ul>
                <li>Typically 24-48 hours post-procedure if no complications</li>
                <li>Provide patient education on post-embolization syndrome</li>
                <li>Warning signs requiring medical attention</li>
                <li>Gradual return to normal activities over 1-2 weeks</li>
            </ul>
        </li>
        <li><strong>Follow-Up</strong>
            <ul>
                <li>Clinical follow-up at 2 weeks</li>
                <li>Liver function tests at 1-2 weeks</li>
                <li>Multiphasic CT or MRI at 4-6 weeks to assess response</li>
                <li>Tumor markers if applicable</li>
                <li>Consider repeat TACE for residual viable tumor or incomplete response</li>
                <li>Typical schedule: 2-3 sessions at 4-8 week intervals</li>
            </ul>
        </li>
    </ol>
    </div>
    """, unsafe_allow_html=True)

def display_nephrostomy_procedure():
    st.markdown("""
    ### Percutaneous Nephrostomy Procedure
    
    <div class="procedure-diagram">
    <h4>Pre-Procedure</h4>
    <ol>
        <li><strong>Initial Assessment</strong>
            <ul>
                <li>Confirm indication (urinary obstruction, urinary diversion, access for other procedures)</li>
                <li>Assess degree of hydronephrosis</li>
                <li>Evaluate for contraindications (uncorrected coagulopathy, renal tumor at access site)</li>
                <li>Review patient history, including previous urological interventions</li>
            </ul>
        </li>
        <li><strong>Imaging</strong>
            <ul>
                <li>Ultrasound to confirm hydronephrosis</li>
                <li>CT or MRI to determine cause and level of obstruction</li>
                <li>Plan access route</li>
            </ul>
        </li>
        <li><strong>Laboratory Tests</strong>
            <ul>
                <li>Complete blood count</li>
                <li>Coagulation profile</li>
                <li>Renal function tests</li>
                <li>Urinalysis and urine culture</li>
            </ul>
        </li>
        <li><strong>Patient Preparation</strong>
            <ul>
                <li>Correct coagulopathy if present (INR <1.5, platelets >50,000/µL)</li>
                <li>Prophylactic antibiotics (especially if infected system suspected)</li>
                <li>NPO for 4-6 hours before procedure</li>
                <li>Obtain informed consent</li>
            </ul>
        </li>
    </ol>
    
    <h4>Procedure</h4>
    <ol>
        <li><strong>Anesthesia</strong>
            <ul>
                <li>Conscious sedation or general anesthesia</li>
                <li>Local anesthesia at puncture site</li>
            </ul>
        </li>
        <li><strong>Patient Positioning</strong>
            <ul>
                <li>Prone or prone-oblique position</li>
                <li>Pillow under abdomen to reduce lordosis</li>
            </ul>
        </li>
        <li><strong>Access Planning</strong>
            <ul>
                <li>Ultrasound or fluoroscopic guidance</li>
                <li>Identify posterior calyx for access (preferably lower or middle pole)</li>
                <li>Avoid pleura, colon, spleen, liver</li>
                <li>Mark skin entry site</li>
            </ul>
        </li>
        <li><strong>Renal Access</strong>
            <ul>
                <li>Local anesthesia along anticipated tract</li>
                <li>Advance 18G needle into collecting system under imaging guidance</li>
                <li>Aim for posterior calyx</li>
                <li>Confirm position by aspiration of urine</li>
                <li>Collect urine sample for culture</li>
            </ul>
        </li>
        <li><strong>Guidewire Placement</strong>
            <ul>
                <li>Inject contrast to opacify collecting system</li>
                <li>Advance guidewire through needle into renal pelvis or ureter</li>
                <li>Secure guidewire position</li>
            </ul>
        </li>
        <li><strong>Tract Dilation</strong>
            <ul>
                <li>Remove needle leaving guidewire in place</li>
                <li>Dilate tract with fascial dilators</li>
                <li>Sequential dilation to 8-14 Fr depending on catheter size</li>
            </ul>
        </li>
        <li><strong>Nephrostomy Tube Placement</strong>
            <ul>
                <li>Advance nephrostomy catheter over guidewire</li>
                <li>Position pigtail loop in renal pelvis</li>
                <li>Confirm position with contrast injection</li>
                <li>Secure catheter to skin</li>
            </ul>
        </li>
        <li><strong>Antegrade Ureteral Stenting (if indicated)</strong>
            <ul>
                <li>Advance guidewire through obstruction into bladder</li>
                <li>Place ureteral stent over guidewire</li>
                <li>Position proximal end in renal pelvis and distal end in bladder</li>
                <li>May leave nephrostomy tube as safety or remove if stent functions well</li>
            </ul>
        </li>
    </ol>
    
    <h4>Post-Procedure</h4>
    <ol>
        <li><strong>Immediate Monitoring</strong>
            <ul>
                <li>Monitor vital signs</li>
                <li>Assess nephrostomy tube output and characteristics</li>
                <li>Monitor for complications (bleeding, sepsis)</li>
            </ul>
        </li>
        <li><strong>Catheter Management</strong>
            <ul>
                <li>Connect to drainage bag</li>
                <li>Document initial output</li>
                <li>Flush catheter with 5-10 mL saline if output decreases</li>
                <li>Secure catheter to prevent dislodgement</li>
            </ul>
        </li>
        <li><strong>Discharge Planning</strong>
            <ul>
                <li>Typically 24 hours post-procedure if no complications</li>
                <li>Provide patient education on catheter care</li>
                <li>Arrange home nursing if needed</li>
                <li>Continue antibiotics if indicated</li>
            </ul>
        </li>
        <li><strong>Follow-Up</strong>
            <ul>
                <li>Clinical follow-up at 1-2 weeks</li>
                <li>Nephrostogram to assess drainage and obstruction resolution</li>
                <li>Catheter exchange every 8-12 weeks if long-term drainage needed</li>
                <li>Plan for definitive management of underlying condition</li>
            </ul>
        </li>
    </ol>
    </div>
    """, unsafe_allow_html=True)
