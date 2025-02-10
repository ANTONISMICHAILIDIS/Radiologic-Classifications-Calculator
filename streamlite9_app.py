import streamlit as st

st.title("Radiologic Classifications Calculator")
st.markdown("<small>Created by Michailidis A. for free use</small>", unsafe_allow_html=True)

st.markdown("""
This app assists in radiologic classification by having you first select an organ and a classification system.  
Then, you’ll enter key imaging criteria (e.g., size, enhancement, morphology).  
Based on your input, the app automatically calculates a score or category, provides an interpretation, and suggests next steps in diagnosis/management.

**Note:** All scoring and recommendations in this demo are simplified and for educational purposes only.
""")

# =============================================================================
# MAIN CATEGORY SELECTION
# =============================================================================
category = st.sidebar.selectbox(
    "Select an Anatomical/Clinical Category", 
    [
        "NEURO (BRAIN & SPINE)",
        "HEAD & NECK",
        "CARDIOTHORACIC",
        "ABDOMINOPELVIC",
        "MUSCULOSKELETAL (MSK)",
        "INTERVENTIONAL RADIOLOGY/VASCULAR",
        "-RADS SYSTEMS"
    ]
)

# =============================================================================
# 1. NEURO (BRAIN & SPINE)
# =============================================================================
if category == "NEURO (BRAIN & SPINE)":
    st.header("NEURO – Brain & Spine Classifications")
    neuro_option = st.sidebar.selectbox(
        "Select a Neuro Classification System", 
        [
            "1.1 Hunt and Hess (SAH)",
            "1.2 Fisher (SAH)",
            "1.3 Spetzler-Martin (AVMs)",
            "1.4 Modic (Vertebral Endplate Changes)",
            "1.5 Pfirrmann (Disc Degeneration)",
            "1.6 TLICS (Thoracolumbar Injury)"
        ]
    )

    # -----------------------------------------------------------
    # 1.1 Hunt and Hess Classification (SAH)
    # -----------------------------------------------------------
    if neuro_option == "1.1 Hunt and Hess (SAH)":
        st.subheader("Hunt and Hess Classification for Subarachnoid Hemorrhage (SAH)")
        st.markdown("""
        **Key Features to Identify:**
        - **Headache severity:** Minimal, moderate, severe  
        - **Level of Consciousness:** Normal, drowsy/confused, stuporous, deep coma  
        - **Focal neurological deficits:** Absent, mild, or severe  
        - **CT Appearance:** Small/subtle SAH vs. diffuse/large SAH (with possible intraventricular extension)
        """)
        headache = st.radio("Headache severity", ["Minimal", "Moderate", "Severe"])
        consciousness = st.radio("Level of consciousness", ["Normal", "Drowsy/Confused", "Stupor", "Deep Coma"])
        focal_deficit = st.radio("Focal neurological deficits", ["None", "Mild", "Severe"])
        ct_sah = st.radio("CT appearance of SAH", ["Subtle/Small", "Moderate", "Diffuse/Large with IVH"])
        
        # (Simplified logic; in practice, clinical assessment predominates.)
        if headache == "Minimal" and consciousness == "Normal" and focal_deficit == "None" and ct_sah == "Subtle/Small":
            hh_grade = "I"
        elif headache == "Moderate" and (consciousness in ["Normal", "Drowsy/Confused"]) and focal_deficit in ["None", "Mild"] and ct_sah == "Moderate":
            hh_grade = "II"
        elif consciousness == "Drowsy/Confused" or focal_deficit == "Mild" or ct_sah == "Moderate":
            hh_grade = "III"
        elif consciousness == "Stupor" or focal_deficit == "Severe" or ct_sah == "Diffuse/Large with IVH":
            hh_grade = "IV"
        else:
            hh_grade = "V"
            
        st.write(f"**Calculated Hunt and Hess Grade:** {hh_grade}")
        # Provide a brief clinical interpretation and next steps.
        if hh_grade == "I":
            st.markdown("**Interpretation:** Minimal symptoms; imaging shows only subtle SAH.  **Next Steps:** Routine monitoring; neurosurgical consult as needed.")
        elif hh_grade == "II":
            st.markdown("**Interpretation:** Moderate symptoms; SAH is visible on CT.  **Next Steps:** Close observation and neurosurgical consultation.")
        elif hh_grade == "III":
            st.markdown("**Interpretation:** Moderate to severe symptoms; thicker SAH may be present.  **Next Steps:** Consider intensive care and early neurosurgical evaluation.")
        elif hh_grade == "IV":
            st.markdown("**Interpretation:** Severe deficits and diffuse SAH.  **Next Steps:** Urgent neurosurgical evaluation and intensive care management.")
        else:
            st.markdown("**Interpretation:** Critical condition with large, diffuse SAH (possibly with intraventricular extension).  **Next Steps:** Emergency neurosurgical and critical care management required.")
    
    # -----------------------------------------------------------
    # 1.2 Fisher Classification (SAH)
    # -----------------------------------------------------------
    elif neuro_option == "1.2 Fisher (SAH)":
        st.subheader("Fisher Classification for Subarachnoid Hemorrhage")
        st.markdown("""
        **Key Radiologic Findings:**
        - **Blood detection on CT:** None, thin layer (<1 mm), thick clot (≥1 mm)
        - **Additional findings:** Presence or absence of intraventricular/intraparenchymal blood
        """)
        blood_detected = st.radio("Is blood detected on CT?", ["No", "Yes"])
        if blood_detected == "Yes":
            blood_thickness = st.radio("If yes, is the blood layer:", ["Thin (<1 mm)", "Thick (≥1 mm)"])
        else:
            blood_thickness = "None"
        extra = st.radio("Is there intraventricular/intraparenchymal blood?", ["No", "Yes"])
        
        # Simplified scoring:
        if blood_detected == "No":
            fisher_grade = 1
        elif blood_thickness == "Thin (<1 mm)":
            fisher_grade = 2
        elif blood_thickness == "Thick (≥1 mm)" and extra == "No":
            fisher_grade = 3
        else:
            fisher_grade = 4
        
        st.write(f"**Calculated Fisher Grade:** {fisher_grade}")
        if fisher_grade == 1:
            st.markdown("**Interpretation:** No blood detected; low risk of vasospasm.  **Next Steps:** Routine monitoring.")
        elif fisher_grade == 2:
            st.markdown("**Interpretation:** Thin layer of blood; relatively low risk.  **Next Steps:** Monitor and consider prophylaxis.")
        elif fisher_grade == 3:
            st.markdown("**Interpretation:** Thick clot in the subarachnoid space; higher risk of vasospasm.  **Next Steps:** Initiate vasospasm prophylaxis and intensive monitoring.")
        else:
            st.markdown("**Interpretation:** Presence of intraventricular/intraparenchymal blood; highest risk for vasospasm.  **Next Steps:** Aggressive management including possible endovascular intervention.")
    
    # -----------------------------------------------------------
    # 1.3 Spetzler-Martin Grading (AVMs)
    # -----------------------------------------------------------
    elif neuro_option == "1.3 Spetzler-Martin (AVMs)":
        st.subheader("Spetzler-Martin Grading for Intracranial AVMs")
        st.markdown("""
        **Key Radiologic Features:**
        - **Nidus size (cm):** Small (<3), Medium (3–6), Large (>6)
        - **Eloquence of adjacent brain:** Non-eloquent or Eloquent
        - **Venous drainage:** Superficial only or Deep drainage
        """)
        size = st.number_input("Enter AVM nidus size (cm)", min_value=0.0, value=2.0, step=0.1)
        eloquent = st.radio("Is the AVM adjacent to eloquent brain areas?", ["No", "Yes"])
        drainage = st.radio("Type of venous drainage", ["Superficial only", "Deep drainage"])
        
        # Scoring:
        if size < 3:
            size_points = 1
        elif 3 <= size <= 6:
            size_points = 2
        else:
            size_points = 3
        eloquence_points = 1 if eloquent == "Yes" else 0
        drainage_points = 1 if drainage == "Deep drainage" else 0
        total_score = size_points + eloquence_points + drainage_points
        
        st.write(f"**Spetzler-Martin Score:** {total_score}")
        st.markdown(f"**Interpretation:** A higher score (closer to 5 or more) suggests a higher surgical risk.")
        st.markdown("**Next Steps:** Multidisciplinary evaluation (neurosurgery, interventional radiology) is advised to plan treatment.")
    
    # -----------------------------------------------------------
    # 1.4 Modic Classification (Vertebral Endplate Changes)
    # -----------------------------------------------------------
    elif neuro_option == "1.4 Modic (Vertebral Endplate Changes)":
        st.subheader("Modic Classification for Vertebral Endplate Changes")
        st.markdown("""
        **Key Radiologic Findings on MRI:**
        - **T1 signal:** Hypointense or Hyperintense
        - **T2 signal:** Hyperintense or Hypointense
        """)
        t1_signal = st.radio("T1 signal of endplate", ["Hypointense", "Hyperintense"])
        t2_signal = st.radio("T2 signal of endplate", ["Hyperintense", "Hypointense", "Isointense"])
        # Determine Modic type based on key criteria:
        if t1_signal == "Hypointense" and t2_signal == "Hyperintense":
            modic_type = "Type I (Edematous/Inflammatory)"
        elif t1_signal == "Hyperintense" and t2_signal in ["Hyperintense", "Isointense"]:
            modic_type = "Type II (Fatty Degeneration)"
        elif t1_signal == "Hypointense" and t2_signal == "Hypointense":
            modic_type = "Type III (Sclerotic)"
        else:
            modic_type = "Unclassified"
        st.write(f"**Modic Classification:** {modic_type}")
        st.markdown("**Next Steps:** Correlate with patient symptoms; conservative management versus intervention is guided by clinical context.")
    
    # -----------------------------------------------------------
    # 1.5 Pfirrmann Classification (Disc Degeneration)
    # -----------------------------------------------------------
    elif neuro_option == "1.5 Pfirrmann (Disc Degeneration)":
        st.subheader("Pfirrmann Classification for Intervertebral Disc Degeneration")
        st.markdown("""
        **Key Radiologic Findings on T2 MRI:**
        - Disc signal brightness, disc height, and distinction between nucleus and annulus.
        """)
        disc_desc = st.selectbox("Select the disc appearance", [
            "Homogeneous, bright T2 signal; normal disc height; clear distinction (Grade I)",
            "Slightly less bright; normal height; clear boundary (Grade II)",
            "Intermediate signal; slight decrease in height; borderline boundary (Grade III)",
            "Hypointense; moderate height loss; unclear boundary (Grade IV)",
            "Very hypointense; collapsed disc space; severe degeneration (Grade V)"
        ])
        if "Grade I" in disc_desc:
            pf_grade = "I"
        elif "Grade II" in disc_desc:
            pf_grade = "II"
        elif "Grade III" in disc_desc:
            pf_grade = "III"
        elif "Grade IV" in disc_desc:
            pf_grade = "IV"
        else:
            pf_grade = "V"
        st.write(f"**Pfirrmann Grade:** {pf_grade}")
        st.markdown("**Next Steps:** For mild degeneration, conservative treatment is usually recommended; severe degeneration may require interventional or surgical management.")
    
    # -----------------------------------------------------------
    # 1.6 TLICS – Thoracolumbar Injury Classification
    # -----------------------------------------------------------
    elif neuro_option == "1.6 TLICS (Thoracolumbar Injury)":
        st.subheader("TLICS – Thoracolumbar Injury Classification & Severity Score")
        st.markdown("""
        **Key Features to Assess:**
        - **Injury Morphology:** Compression, Burst, Translation/Rotation, or Distraction  
        - **Posterior Ligamentous Complex (PLC):** Intact or Disrupted  
        - **Neurological Status:** Intact, Incomplete deficit, or Complete deficit
        """)
        morphology = st.selectbox("Injury Morphology", ["Compression", "Burst", "Translation/Rotation", "Distraction"])
        plc = st.radio("Posterior Ligamentous Complex", ["Intact", "Disrupted"])
        neuro = st.selectbox("Neurological Status", ["Intact", "Incomplete deficit", "Complete deficit"])
        
        # Assign points (example values):
        if morphology == "Compression":
            morph_points = 1
        elif morphology == "Burst":
            morph_points = 2
        elif morphology == "Translation/Rotation":
            morph_points = 3
        else:  # Distraction
            morph_points = 4
        
        plc_points = 0 if plc == "Intact" else 3
        if neuro == "Intact":
            neuro_points = 0
        elif neuro == "Incomplete deficit":
            neuro_points = 2
        else:
            neuro_points = 3
        
        tlics_score = morph_points + plc_points + neuro_points
        st.write(f"**TLICS Score:** {tlics_score}")
        st.markdown("**Interpretation:** A TLICS score of ≥5 generally indicates that surgical treatment is recommended.")
        if tlics_score >= 5:
            st.markdown("**Next Steps:** Recommend surgical consultation for stabilization.")
        else:
            st.markdown("**Next Steps:** Consider conservative management with close follow-up.")

# =============================================================================
# 2. HEAD & NECK
# =============================================================================
elif category == "HEAD & NECK":
    st.header("Head & Neck Classifications")
    head_neck_option = st.sidebar.selectbox(
        "Select a Head & Neck Classification", 
        [
            "2.1 TNM Staging (AJCC) – Head & Neck Cancers",
            "2.2 Lugano Classification (Lymphoma)",
            "2.3 Friedman Staging (Tonsillar Hypertrophy)"
        ]
    )
    
    # -----------------------------------------------------------
    # 2.1 TNM Staging (AJCC) – Head & Neck Cancers
    # -----------------------------------------------------------
    if head_neck_option == "2.1 TNM Staging (AJCC) – Head & Neck Cancers":
        st.subheader("TNM Staging (AJCC) for Head & Neck Cancers")
        st.markdown("""
        **Key Radiologic Features:**
        - **Tumor Size:** Measure the primary lesion (cm)  
        - **Invasion:** Assess if adjacent structures are invaded  
        - **Lymph Nodes:** Number and size; extranodal extension  
        - **Metastasis:** Presence of distant lesions
        """)
        tumor_size = st.number_input("Enter primary tumor size (cm)", min_value=0.0, step=0.1, value=2.0)
        invasion = st.radio("Is there invasion of adjacent structures?", ["No", "Yes"])
        nodes = st.number_input("Number of involved lymph nodes", min_value=0, step=1, value=1)
        metastasis = st.radio("Are distant metastases present?", ["No", "Yes"])
        
        # Simplified TNM assignment.
        if tumor_size < 2 and invasion == "No":
            T_cat = "T1"
        elif tumor_size < 4 and invasion == "No":
            T_cat = "T2"
        elif tumor_size < 4 and invasion == "Yes":
            T_cat = "T3"
        else:
            T_cat = "T4"
        
        if nodes == 0:
            N_cat = "N0"
        elif nodes == 1:
            N_cat = "N1"
        else:
            N_cat = "N2"
        
        M_cat = "M0" if metastasis == "No" else "M1"
        st.write(f"**TNM Staging:** {T_cat} {N_cat} {M_cat}")
        st.markdown("**Next Steps:** Confirm with biopsy and plan multidisciplinary management (surgery, radiation, chemotherapy) based on staging.")
    
    # -----------------------------------------------------------
    # 2.2 Lugano Classification (Lymphoma)
    # -----------------------------------------------------------
    elif head_neck_option == "2.2 Lugano Classification (Lymphoma)":
        st.subheader("Lugano Classification for Lymphoma")
        st.markdown("""
        **Key Features (from FDG-PET/CT):**
        - **Nodal Involvement:** Number of nodal regions  
        - **Extranodal Involvement:** Present or absent
        """)
        nodal_regions = st.number_input("Enter number of nodal regions involved", min_value=0, step=1, value=1)
        extranodal = st.radio("Is there extranodal involvement?", ["No", "Yes"])
        if nodal_regions == 1 and extranodal == "No":
            lugano_stage = "Stage I"
        elif nodal_regions > 1 and extranodal == "No":
            lugano_stage = "Stage II"
        elif extranodal == "Yes" and nodal_regions < 3:
            lugano_stage = "Stage IIE"
        elif extranodal == "Yes" and nodal_regions >= 3:
            lugano_stage = "Stage IV"
        else:
            lugano_stage = "Stage III"
        st.write(f"**Lugano Stage:** {lugano_stage}")
        st.markdown("**Next Steps:** Tailor treatment based on stage; consider chemotherapy and follow-up PET-CT for treatment response.")
    
    # -----------------------------------------------------------
    # 2.3 Friedman Staging (Tonsillar Hypertrophy)
    # -----------------------------------------------------------
    elif head_neck_option == "2.3 Friedman Staging (Tonsillar Hypertrophy)":
        st.subheader("Friedman Staging for Tonsillar Hypertrophy")
        st.markdown("""
        **Key Feature:**
        - Estimate the percentage of oropharyngeal width occupied by the tonsils.
        """)
        tonsil_percent = st.slider("Percentage of oropharyngeal width occupied", 0, 100, 30, step=5)
        if tonsil_percent < 25:
            friedman = "1+"
        elif 25 <= tonsil_percent < 50:
            friedman = "2+"
        elif 50 <= tonsil_percent < 75:
            friedman = "3+"
        else:
            friedman = "4+"
        st.write(f"**Friedman Stage:** {friedman}")
        st.markdown("**Next Steps:** Significant hypertrophy (3+ or 4+) warrants further evaluation for airway compromise and potential tonsillectomy.")

# =============================================================================
# 3. CARDIOTHORACIC
# =============================================================================
elif category == "CARDIOTHORACIC":
    st.header("Cardiothoracic Classifications")
    cardio_option = st.sidebar.selectbox(
        "Select a Cardiothoracic Classification", 
        [
            "3.1 Aortic Dissection",
            "3.2 Pulmonary Embolism – Qanadli Score",
            "3.3 Lung-RADS (CT Screening)",
            "3.4 COVID-19 Chest Imaging (RSNA)",
            "3.5 ATS/ERS Classification (IIP)",
            "3.6 Breast: BI-RADS"
        ]
    )
    
    # -----------------------------------------------------------
    # 3.1 Aortic Dissection
    # -----------------------------------------------------------
    if cardio_option == "3.1 Aortic Dissection":
        st.subheader("Aortic Dissection Classification")
        st.markdown("""
        **Key Radiologic Findings on CT/MR/TEE:**
        - Presence of an intimal flap  
        - Involvement of the ascending aorta?
        """)
        ascending = st.radio("Is the ascending aorta involved?", ["Yes", "No"])
        if ascending == "Yes":
            stanford = "Type A"
        else:
            stanford = "Type B"
        st.write(f"**Stanford Classification:** {stanford}")
        st.markdown("**Next Steps:** For Stanford Type A, arrange immediate surgical consultation. For Type B, consider medical management and close monitoring.")
    
    # -----------------------------------------------------------
    # 3.2 Pulmonary Embolism – Qanadli Score
    # -----------------------------------------------------------
    elif cardio_option == "3.2 Pulmonary Embolism – Qanadli Score":
        st.subheader("Qanadli Score for Pulmonary Embolism")
        st.markdown("""
        **Key Steps:**
        - Count the number of partially and completely occluded segmental arteries (10 per lung).
        """)
        partial = st.number_input("Number of partially occluded segmental arteries", min_value=0, max_value=20, value=0)
        complete = st.number_input("Number of completely occluded segmental arteries", min_value=0, max_value=20, value=0)
        qanadli = partial * 1 + complete * 2
        st.write(f"**Calculated Qanadli Score:** {qanadli} / 40")
        st.markdown("**Next Steps:** A higher score indicates a larger clot burden. For high scores, consider thrombolysis and monitor right ventricular function.")
    
    # -----------------------------------------------------------
    # 3.3 Lung-RADS (CT Screening)
    # -----------------------------------------------------------
    elif cardio_option == "3.3 Lung-RADS (CT Screening)":
        st.subheader("Lung-RADS Classification")
        st.markdown("""
        **Key Radiologic Features:**
        - Nodule size (mm)  
        - Nodule composition (Solid, Part-solid, Ground-glass)
        """)
        nodule_size = st.number_input("Enter nodule size (mm)", min_value=0, value=6)
        nodule_type = st.radio("Nodule composition", ["Solid", "Part-solid", "Ground-glass"])
        # Simplified decision:
        if nodule_size < 6:
            lung_rads = "Category 2 (Benign)"
        elif 6 <= nodule_size < 8:
            lung_rads = "Category 3 (Probably benign)"
        else:
            lung_rads = "Category 4 (Suspicious)"
        st.write(f"**Lung-RADS Category:** {lung_rads}")
        st.markdown("**Next Steps:** For suspicious nodules (Category 4), recommend diagnostic CT and possible tissue sampling.")
    
    # -----------------------------------------------------------
    # 3.4 COVID-19 Chest Imaging (RSNA)
    # -----------------------------------------------------------
    elif cardio_option == "3.4 COVID-19 Chest Imaging (RSNA)":
        st.subheader("RSNA COVID-19 Chest Imaging Classification")
        st.markdown("""
        **Key Radiologic Findings:**
        - Distribution of ground-glass opacities (GGO)  
        - Laterality (bilateral vs. unilateral)  
        - Presence of consolidation or “crazy-paving”
        """)
        ggo = st.radio("Are bilateral peripheral GGOs present?", ["Yes", "No"])
        consolidation = st.radio("Is there consolidation or crazy-paving?", ["Yes", "No"])
        if ggo == "Yes" and consolidation == "Yes":
            covid_category = "Typical"
        elif ggo == "Yes":
            covid_category = "Indeterminate"
        elif consolidation == "Yes":
            covid_category = "Atypical"
        else:
            covid_category = "Negative"
        st.write(f"**RSNA COVID-19 Category:** {covid_category}")
        if covid_category == "Typical":
            st.markdown("**Next Steps:** Recommend confirmatory RT-PCR testing and initiate isolation protocols.")
        elif covid_category == "Indeterminate":
            st.markdown("**Next Steps:** Correlate clinically; consider repeat imaging.")
        elif covid_category == "Atypical":
            st.markdown("**Next Steps:** Evaluate for alternative pneumonia etiologies.")
        else:
            st.markdown("**Next Steps:** Routine care; no evidence of pneumonia.")
    
    # -----------------------------------------------------------
    # 3.5 ATS/ERS Classification (IIP)
    # -----------------------------------------------------------
    elif cardio_option == "3.5 ATS/ERS Classification (IIP)":
        st.subheader("ATS/ERS Classification for Idiopathic Interstitial Pneumonias")
        st.markdown("""
        **Key HRCT Patterns:**
        - UIP: Reticular opacities, honeycombing, basal/subpleural predominance  
        - NSIP: Ground-glass opacities with uniform distribution  
        - COP: Patchy consolidation with peripheral distribution
        """)
        pattern = st.selectbox("Select the predominant HRCT pattern", ["UIP", "NSIP", "COP", "Other"])
        st.write(f"**HRCT Pattern:** {pattern}")
        st.markdown("**Next Steps:** Correlate with clinical findings; if UIP, evaluate for idiopathic pulmonary fibrosis and refer to pulmonology.")
    
    # -----------------------------------------------------------
    # 3.6 Breast: BI-RADS
    # -----------------------------------------------------------
    elif cardio_option == "3.6 Breast: BI-RADS":
        st.subheader("BI-RADS Classification for Breast Imaging")
        st.markdown("""
        **Key Radiologic Features:**
        - Mass shape, margins, calcification morphology, enhancement pattern
        """)
        shape = st.selectbox("Mass shape", ["Oval", "Round", "Irregular"])
        margin = st.selectbox("Mass margin", ["Circumscribed", "Not-circumscribed"])
        calc = st.radio("Calcifications present?", ["No", "Yes"])
        if shape in ["Oval", "Round"] and margin == "Circumscribed" and calc == "No":
            birads = 2
        elif shape == "Irregular" or margin == "Not-circumscribed":
            birads = 4
        else:
            birads = 3
        st.write(f"**Calculated BI-RADS Category:** {birads}")
        st.markdown("**Next Steps:** For BI-RADS 4 lesions, consider biopsy; for BI-RADS 3, recommend short-term follow-up.")

# =============================================================================
# 4. ABDOMINOPELVIC
# =============================================================================
elif category == "ABDOMINOPELVIC":
    st.header("Abdominopelvic Classifications")
    abdo_option = st.sidebar.selectbox(
        "Select a Subcategory", 
        [
            "4.1 Bosniak Classification (Renal Cysts)",
            "4.2 AAST Organ Injury Scales (Trauma)",
            "4.3 Balthazar/CT Severity Index (Pancreatitis)",
            "4.4 LI-RADS (Liver)",
            "4.5 PI-RADS (Prostate)",
            "4.6 O-RADS (Ovarian-Adnexal)",
            "4.7 TI-RADS (Thyroid)",
            "4.8 FIGO Staging (Gynecologic Cancers)"
        ]
    )
    
    # -----------------------------------------------------------
    # 4.1 Bosniak Classification (Renal Cysts)
    # -----------------------------------------------------------
    if abdo_option == "4.1 Bosniak Classification (Renal Cysts)":
        st.subheader("Bosniak Classification for Renal Cystic Masses")
        st.markdown("""
        **Key Imaging Features:**
        - Presence and number of septa, septal thickness  
        - Calcifications (thin vs. thick/nodular)  
        - Enhancement of walls/septa  
        - Overall complexity
        """)
        septa = st.radio("Are septa present?", ["No", "Yes"])
        if septa == "Yes":
            septa_thickness = st.radio("Septa thickness", ["Thin", "Thick"])
        else:
            septa_thickness = "N/A"
        calcifications = st.radio("Calcifications", ["None", "Thin", "Thick/Nodular"])
        enhancement = st.radio("Is there enhancement of walls/septa?", ["No", "Yes"])
        if septa == "No" and calcifications == "None" and enhancement == "No":
            bosniak = "I"
        elif septa == "Yes" and septa_thickness == "Thin" and enhancement == "No":
            bosniak = "II"
        elif septa == "Yes" and (septa_thickness == "Thin" and enhancement == "Yes"):
            bosniak = "IIF"
        elif septa == "Yes" and septa_thickness == "Thick" and enhancement == "Yes":
            bosniak = "III"
        else:
            bosniak = "IV"
        st.write(f"**Bosniak Category:** {bosniak}")
        st.markdown("**Next Steps:** Based on the Bosniak category, further imaging follow-up or surgical consultation may be indicated.")
    
    # -----------------------------------------------------------
    # 4.2 AAST Organ Injury Scales (Trauma)
    # -----------------------------------------------------------
    elif abdo_option == "4.2 AAST Organ Injury Scales (Trauma)":
        st.subheader("AAST Organ Injury Scale (Example: Splenic Injury)")
        st.markdown("""
        **Key Radiologic Features for Splenic Injury on CT:**
        - Subcapsular hematoma (extent as % of surface)  
        - Laceration depth (cm)  
        - Vascular injury (Yes/No)
        """)
        area = st.selectbox("Estimated surface area involvement", ["<10%", "10–50%", ">50%"])
        depth = st.selectbox("Laceration depth", ["<1 cm", "1–3 cm", ">3 cm"])
        vascular = st.radio("Vascular injury present?", ["No", "Yes"])
        if area == "<10%" and depth == "<1 cm" and vascular == "No":
            grade = "I"
        elif area == "10–50%" and depth == "1–3 cm" and vascular == "No":
            grade = "II"
        elif area == ">50%" or depth == ">3 cm" or vascular == "Yes":
            grade = "III or higher"
        else:
            grade = "Intermediate"
        st.write(f"**Estimated Splenic Injury Grade:** {grade}")
        st.markdown("**Next Steps:** High-grade injuries may require surgical or interventional radiology management.")
    
    # -----------------------------------------------------------
    # 4.3 Balthazar & CTSI (Pancreatitis)
    # -----------------------------------------------------------
    elif abdo_option == "4.3 Balthazar/CT Severity Index (Pancreatitis)":
        st.subheader("Pancreatitis: Balthazar Grade & CT Severity Index (CTSI)")
        st.markdown("""
        **Key Features on Contrast CT:**
        - Pancreatic inflammation (graded A–E)  
        - Peripancreatic fluid collections  
        - Percentage of pancreatic necrosis (%)
        """)
        balthazar = st.selectbox("Select Balthazar Grade", ["A (Normal)", "B (Enlarged)", "C (Mild Inflammation)", "D (Single Fluid Collection)", "E (Multiple Fluid Collections)"])
        necrosis = st.slider("Estimate percentage of pancreatic necrosis (%)", 0, 100, 10, step=5)
        balthazar_points = {"A (Normal)": 0, "B (Enlarged)": 1, "C (Mild Inflammation)": 2, "D (Single Fluid Collection)": 3, "E (Multiple Fluid Collections)": 4}
        if necrosis < 33:
            necrosis_points = 0
        elif necrosis < 50:
            necrosis_points = 2
        else:
            necrosis_points = 4
        ctsi = balthazar_points[balthazar] + necrosis_points
        st.write(f"**CT Severity Index (CTSI):** {ctsi} / 10")
        st.markdown("**Next Steps:** Higher CTSI scores indicate more severe pancreatitis; manage accordingly with supportive care and ICU monitoring for severe cases.")
    
    # -----------------------------------------------------------
    # 4.4 LI-RADS, 4.5 PI-RADS, 4.6 O-RADS, 4.7 TI-RADS, 4.8 FIGO
    # -----------------------------------------------------------
    elif abdo_option in ["4.4 LI-RADS (Liver)", "4.5 PI-RADS (Prostate)", "4.6 O-RADS (Ovarian-Adnexal)", "4.7 TI-RADS (Thyroid)", "4.8 FIGO Staging (Gynecologic Cancers)"]:
        st.subheader(f"{abdo_option}")
        st.markdown("For these systems, please refer to the “-RADS SYSTEMS” section below for key imaging feature input and automatic classification.")
        st.info("This demo integrates LI-RADS, PI-RADS, O-RADS, TI-RADS, and FIGO staging in the -RADS SYSTEMS section.")
    
# =============================================================================
# 5. MUSCULOSKELETAL (MSK)
# =============================================================================
elif category == "MUSCULOSKELETAL (MSK)":
    st.header("Musculoskeletal (MSK) Classifications")
    msk_option = st.sidebar.selectbox(
        "Select an MSK Classification", 
        [
            "5.1 AO/OTA Fracture Classification",
            "5.2 Gustilo–Anderson (Open Fractures)",
            "5.3 Tscherne Classification (Soft-Tissue Injuries)",
            "5.4 Salter-Harris (Physeal Fractures)",
            "5.5 Other Fracture Classifications"
        ]
    )
    
    # -----------------------------------------------------------
    # 5.1 AO/OTA Fracture Classification
    # -----------------------------------------------------------
    if msk_option == "5.1 AO/OTA Fracture Classification":
        st.subheader("AO/OTA Fracture Classification (Long Bones)")
        st.markdown("""
        **Key Features:**
        - Location: Proximal, Diaphyseal, or Distal  
        - Fracture pattern: Simple, Wedge, or Complex  
        - Articular involvement: Yes/No
        """)
        location = st.selectbox("Fracture location", ["Proximal", "Diaphyseal", "Distal"])
        pattern = st.selectbox("Fracture pattern", ["Simple", "Wedge", "Complex"])
        articular = st.radio("Articular involvement", ["No", "Yes"])
        st.write(f"**AO/OTA Example:** {location} - {pattern} fracture{' with articular involvement' if articular=='Yes' else ''}.")
        st.markdown("**Next Steps:** Evaluate stability and consult orthopedics for treatment planning.")
    
    # -----------------------------------------------------------
    # 5.2 Gustilo–Anderson Classification
    # -----------------------------------------------------------
    elif msk_option == "5.2 Gustilo–Anderson (Open Fractures)":
        st.subheader("Gustilo–Anderson Classification for Open Fractures")
        st.markdown("""
        **Key Features:**
        - Wound size (cm)  
        - Degree of soft tissue injury (minimal, moderate, extensive)
        """)
        wound_size = st.number_input("Wound size (cm)", min_value=0.0, value=1.0, step=0.1)
        soft_tissue = st.radio("Extent of soft tissue injury", ["Minimal", "Moderate", "Extensive"])
        if wound_size < 1 and soft_tissue == "Minimal":
            gustilo = "Type I"
        elif 1 <= wound_size <= 10 and soft_tissue == "Moderate":
            gustilo = "Type II"
        else:
            gustilo = "Type III"
        st.write(f"**Gustilo–Anderson Type:** {gustilo}")
        st.markdown("**Next Steps:** High-grade open fractures (Type III) require urgent debridement and stabilization.")
    
    # -----------------------------------------------------------
    # 5.3 Tscherne Classification (Soft-Tissue Injuries)
    # -----------------------------------------------------------
    elif msk_option == "5.3 Tscherne Classification (Soft-Tissue Injuries)":
        st.subheader("Tscherne Classification for Soft-Tissue Injuries")
        st.markdown("""
        **Key Features:**
        - Degree of soft tissue damage in closed injuries (C0–C3)
        """)
        tscherne_grade = st.selectbox("Select Tscherne Grade (Closed)", ["C0", "C1", "C2", "C3"])
        st.write(f"**Tscherne Grade:** {tscherne_grade}")
        st.markdown("**Next Steps:** Higher grades may require surgical debridement and specialized soft-tissue management.")
    
    # -----------------------------------------------------------
    # 5.4 Salter-Harris Classification (Physeal Fractures)
    # -----------------------------------------------------------
    elif msk_option == "5.4 Salter-Harris (Physeal Fractures)":
        st.subheader("Salter-Harris Classification for Pediatric Fractures")
        st.markdown("""
        **Key Features:**
        - Involvement of physis, metaphysis, and/or epiphysis.
        """)
        sh_type = st.selectbox("Select Salter-Harris Type", ["I", "II", "III", "IV", "V"])
        st.write(f"**Salter-Harris Type:** {sh_type}")
        st.markdown("**Next Steps:** Higher types (III–V) warrant pediatric orthopedic consultation due to potential growth disturbances.")
    
    # -----------------------------------------------------------
    # 5.5 Other Fracture Classifications
    # -----------------------------------------------------------
    elif msk_option == "5.5 Other Fracture Classifications":
        st.subheader("Other Fracture Classifications")
        other_option = st.selectbox(
            "Select a Classification", 
            ["Garden (Femoral Neck)", "Pauwels (Femoral Neck)", "Neer (Proximal Humerus)",
             "Weber (Ankle)", "Lauge-Hansen (Ankle)", "Frykman (Distal Radius)",
             "Sanders (Calcaneal)", "Mayo (Olecranon)"]
        )
        if other_option == "Garden (Femoral Neck)":
            st.markdown("""
            **Key Features for Garden Classification:**
            - Degree of displacement on AP radiograph.
            """)
            displacement = st.radio("Displacement", ["Incomplete/Valgus Impaction", "Complete Non-displaced", "Partially Displaced", "Completely Displaced"])
            if displacement == "Incomplete/Valgus Impaction":
                garden = "Type I"
            elif displacement == "Complete Non-displaced":
                garden = "Type II"
            elif displacement == "Partially Displaced":
                garden = "Type III"
            else:
                garden = "Type IV"
            st.write(f"**Garden Type:** {garden}")
            st.markdown("**Next Steps:** Higher Garden types carry an increased risk of avascular necrosis; surgical treatment is usually indicated.")
        elif other_option == "Pauwels (Femoral Neck)":
            st.markdown("""
            **Key Feature:**  
            Angle of the fracture line relative to the horizontal.
            """)
            angle = st.number_input("Enter fracture angle (degrees)", min_value=0, max_value=90, value=25)
            if angle < 30:
                pauwels = "Type I"
            elif angle < 50:
                pauwels = "Type II"
            else:
                pauwels = "Type III"
            st.write(f"**Pauwels Type:** {pauwels}")
            st.markdown("**Next Steps:** Higher Pauwels types (Type III) are less stable and typically require surgical fixation.")
        elif other_option == "Neer (Proximal Humerus)":
            st.markdown("""
            **Key Feature:**  
            Number of displaced segments (>1 cm or >45° angulation).
            """)
            segments = st.selectbox("Select Neer Classification", ["One-Part", "Two-Part", "Three-Part", "Four-Part"])
            st.write(f"**Neer Classification:** {segments}")
            st.markdown("**Next Steps:** Multi-part fractures generally require surgical intervention.")
        elif other_option == "Weber (Ankle)":
            st.markdown("""
            **Key Feature:**  
            Level of fibular fracture relative to the syndesmosis.
            """)
            weber = st.selectbox("Select Weber Type", ["A (Below Syndesmosis)", "B (At Syndesmosis)", "C (Above Syndesmosis)"])
            st.write(f"**Weber Type:** {weber}")
            st.markdown("**Next Steps:** Evaluate for syndesmotic injury; Type C fractures often require surgical stabilization.")
        elif other_option == "Lauge-Hansen (Ankle)":
            st.markdown("""
            **Key Feature:**  
            Mechanism of injury.
            """)
            mechanism = st.selectbox("Select Mechanism", ["Supination–External Rotation", "Pronation–External Rotation", "Supination–Adduction", "Pronation–Abduction"])
            st.write(f"**Lauge-Hansen Mechanism:** {mechanism}")
            st.markdown("**Next Steps:** Use mechanism to guide management and assess for associated ligamentous injury.")
        elif other_option == "Frykman (Distal Radius)":
            st.markdown("""
            **Key Feature:**  
            Involvement of radiocarpal and distal radioulnar joints.
            """)
            frykman = st.selectbox("Select Frykman Type", ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"])
            st.write(f"**Frykman Type:** {frykman}")
            st.markdown("**Next Steps:** Higher Frykman types may require surgical intervention due to joint involvement.")
        elif other_option == "Sanders (Calcaneal)":
            st.markdown("""
            **Key Feature:**  
            Number of fracture lines in the posterior facet on CT.
            """)
            sanders = st.selectbox("Select Sanders Type", ["I (<2 fragments)", "II (2 fragments)", "III (3 fragments)", "IV (≥4 fragments)"])
            st.write(f"**Sanders Type:** {sanders}")
            st.markdown("**Next Steps:** Complex fractures (Sanders III and IV) often require surgical reconstruction.")
        elif other_option == "Mayo (Olecranon)":
            st.markdown("""
            **Key Feature:**  
            Displacement and stability.
            """)
            mayo = st.selectbox("Select Mayo Type", ["Stable", "Unstable"])
            st.write(f"**Mayo Classification:** {mayo}")
            st.markdown("**Next Steps:** Unstable fractures typically require surgical fixation.")
    
# =============================================================================
# 6. INTERVENTIONAL RADIOLOGY/VASCULAR
# =============================================================================
elif category == "INTERVENTIONAL RADIOLOGY/VASCULAR":
    st.header("Interventional Radiology / Vascular Classifications")
    vascular_option = st.sidebar.selectbox(
        "Select a Vascular Classification", 
        [
            "6.1 TICI Score (Stroke)",
            "6.2 Hamburg Classification (Vascular Malformations)",
            "6.3 VARC Criteria (TAVR)"
        ]
    )
    
    # -----------------------------------------------------------
    # 6.1 TICI Score (Stroke)
    # -----------------------------------------------------------
    if vascular_option == "6.1 TICI Score (Stroke)":
        st.subheader("TICI Score for Reperfusion in Stroke")
        st.markdown("""
        **Key Angiographic Findings (DSA):**
        - Degree of perfusion beyond the occlusion.
        """)
        tici = st.selectbox("Select TICI Grade", ["0", "1", "2a", "2b", "2c", "3"])
        st.write(f"**TICI Grade:** {tici}")
        st.markdown("**Next Steps:** Suboptimal reperfusion (grades 0–2) may require further thrombectomy or adjunctive therapy.")
    
    # -----------------------------------------------------------
    # 6.2 Hamburg Classification (Vascular Malformations)
    # -----------------------------------------------------------
    elif vascular_option == "6.2 Hamburg Classification (Vascular Malformations)":
        st.subheader("Hamburg Classification for Vascular Malformations")
        st.markdown("""
        **Key Features:**
        - Flow dynamics: Fast-flow vs. slow-flow  
        - Predominant tissue type: Capillary, venous, lymphatic, arterial, or combined.
        """)
        flow = st.selectbox("Flow type", ["Fast-flow", "Slow-flow"])
        tissue = st.selectbox("Dominant tissue component", ["Capillary", "Venous", "Lymphatic", "Arterial", "Combined"])
        st.write(f"**Classification:** {flow} {tissue} malformation")
        st.markdown("**Next Steps:** Treatment options include sclerotherapy, embolization, or surgical resection, depending on type.")
    
    # -----------------------------------------------------------
    # 6.3 VARC Criteria (TAVR)
    # -----------------------------------------------------------
    elif vascular_option == "6.3 VARC Criteria (TAVR)":
        st.subheader("VARC Criteria for TAVR Outcomes")
        st.markdown("""
        **Key Points:**
        - Valve positioning on fluoroscopy/CT  
        - Paravalvular leak on echocardiography  
        - Vascular access complications on CT angiography
        """)
        positioning = st.radio("Is valve positioning optimal?", ["Yes", "No"])
        leak = st.radio("Is there a significant paravalvular leak?", ["No", "Yes"])
        access = st.radio("Any vascular access complications?", ["No", "Yes"])
        if positioning == "Yes" and leak == "No" and access == "No":
            varc_outcome = "Favorable"
        else:
            varc_outcome = "Complicated"
        st.write(f"**VARC Outcome Assessment:** {varc_outcome}")
        st.markdown("**Next Steps:** For complicated outcomes, arrange a multidisciplinary review to manage complications and optimize patient care.")
    
# =============================================================================
# 7. “-RADS” SYSTEMS OVERVIEW
# =============================================================================
elif category == "-RADS SYSTEMS":
    st.header("-RADS Systems Overview")
    rads_option = st.sidebar.selectbox(
        "Select a -RADS System", 
        [
            "BI-RADS (Breast)",
            "Lung-RADS (Lung CT Screening)",
            "LI-RADS (Liver)",
            "PI-RADS (Prostate)",
            "TI-RADS (Thyroid)",
            "O-RADS (Ovarian-Adnexal)",
            "NI-RADS (Neck)"
        ]
    )
    
    # -----------------------------------------------------------
    # BI-RADS
    # -----------------------------------------------------------
    if rads_option == "BI-RADS (Breast)":
        st.subheader("ACR BI-RADS for Breast Imaging")
        st.markdown("""
        **Key Imaging Features:**
        - Mass shape: Oval, Round, Irregular  
        - Mass margin: Circumscribed, Not-circumscribed  
        - Calcification morphology: Absent, Benign, Suspicious
        """)
        shape = st.selectbox("Mass shape", ["Oval", "Round", "Irregular"])
        margin = st.selectbox("Mass margin", ["Circumscribed", "Not-circumscribed"])
        calc = st.radio("Calcifications", ["No", "Yes"])
        if shape in ["Oval", "Round"] and margin == "Circumscribed" and calc == "No":
            birads = 2
        elif shape == "Irregular" or margin == "Not-circumscribed":
            birads = 4
        else:
            birads = 3
        st.write(f"**BI-RADS Category:** {birads}")
        st.markdown("**Next Steps:** For BI-RADS 4 lesions, consider biopsy; for BI-RADS 3, recommend short-term follow-up.")
    
    # -----------------------------------------------------------
    # Lung-RADS
    # -----------------------------------------------------------
    elif rads_option == "Lung-RADS (Lung CT Screening)":
        st.subheader("Lung-RADS for CT Screening")
        st.markdown("""
        **Key Imaging Features:**
        - Nodule size (mm)  
        - Nodule type: Solid, Part-solid, Ground-glass
        """)
        nodule_size = st.number_input("Nodule size (mm)", min_value=0, value=5)
        nodule_type = st.radio("Nodule type", ["Solid", "Part-solid", "Ground-glass"])
        if nodule_size < 6:
            lung_rads = "Category 2"
        elif 6 <= nodule_size < 8:
            lung_rads = "Category 3"
        else:
            lung_rads = "Category 4"
        st.write(f"**Lung-RADS Category:** {lung_rads}")
        st.markdown("**Next Steps:** Recommend appropriate follow-up CT; suspicious nodules (Category 4) may need further diagnostic evaluation.")
    
    # -----------------------------------------------------------
    # LI-RADS
    # -----------------------------------------------------------
    elif rads_option == "LI-RADS (Liver)":
        st.subheader("LI-RADS for Liver Lesions")
        st.markdown("""
        **Key Imaging Features (on CT/MRI with contrast):**
        - Arterial phase hyperenhancement  
        - Washout in portal venous/delayed phase  
        - Capsule appearance  
        - Lesion size
        """)
        aphe = st.radio("Is arterial phase hyperenhancement present?", ["No", "Yes"])
        washout = st.radio("Is washout observed in later phases?", ["No", "Yes"])
        capsule = st.radio("Is capsule appearance present?", ["No", "Yes"])
        size = st.number_input("Lesion size (mm)", min_value=0, value=8)
        if aphe == "Yes" and washout == "Yes":
            li_category = "LR-4"
        elif any([aphe=="Yes", washout=="Yes", capsule=="Yes"]) or size >= 10:
            li_category = "LR-3"
        else:
            li_category = "LR-2"
        st.write(f"**LI-RADS Category:** {li_category}")
        st.markdown("**Next Steps:** For LI-RADS 4 lesions, further evaluation with biopsy or surgical consultation is advised.")
    
    # -----------------------------------------------------------
    # PI-RADS
    # -----------------------------------------------------------
    elif rads_option == "PI-RADS (Prostate)":
        st.subheader("PI-RADS for Prostate MRI")
        st.markdown("""
        **Key Imaging Features:**
        - T2 signal: Look for hypointense lesions in the peripheral zone  
        - Diffusion: Restricted diffusion on DWI/ADC  
        - Dynamic contrast enhancement (DCE)
        """)
        t2 = st.radio("Is there a hypointense lesion on T2?", ["No", "Yes"])
        dwi = st.radio("Is there restricted diffusion?", ["No", "Yes"])
        dce = st.radio("Is there early focal enhancement?", ["No", "Yes"])
        if dwi == "Yes":
            pi_score = 4
        else:
            pi_score = 2
        st.write(f"**PI-RADS Score:** {pi_score}")
        st.markdown("**Next Steps:** Lesions with PI-RADS ≥4 should be considered for biopsy and further urologic evaluation.")
    
    # -----------------------------------------------------------
    # TI-RADS
    # -----------------------------------------------------------
    elif rads_option == "TI-RADS (Thyroid)":
        st.subheader("TI-RADS for Thyroid Ultrasound")
        st.markdown("""
        **Key Imaging Features:**
        - Nodule composition: Cystic, Mixed, Solid  
        - Echogenicity: Anechoic, Isoechoic, Hypoechoic  
        - Shape: Taller-than-wide?  
        - Margins: Smooth or Irregular  
        - Presence of microcalcifications
        """)
        composition = st.selectbox("Nodule composition", ["Cystic", "Mixed", "Solid"])
        echogenicity = st.selectbox("Echogenicity", ["Anechoic", "Isoechoic", "Hypoechoic"])
        shape = st.radio("Nodule shape", ["Not taller-than-wide", "Taller-than-wide"])
        margins = st.radio("Margins", ["Smooth", "Irregular"])
        microcalc = st.radio("Microcalcifications present?", ["No", "Yes"])
        score = 0
        if composition == "Solid": score += 1
        if echogenicity == "Hypoechoic": score += 1
        if shape == "Taller-than-wide": score += 1
        if margins == "Irregular": score += 1
        if microcalc == "Yes": score += 1
        if score <= 1:
            ti_category = "TR1"
        elif score == 2:
            ti_category = "TR2"
        elif score == 3:
            ti_category = "TR3"
        elif score == 4:
            ti_category = "TR4"
        else:
            ti_category = "TR5"
        st.write(f"**TI-RADS Category:** {ti_category}")
        st.markdown("**Next Steps:** Nodules in TR4 or TR5 should be considered for fine-needle aspiration biopsy.")
    
    # -----------------------------------------------------------
    # O-RADS
    # -----------------------------------------------------------
    elif rads_option == "O-RADS (Ovarian-Adnexal)":
        st.subheader("O-RADS for Ovarian/Adnexal Masses")
        st.markdown("""
        **Key Imaging Features (US/MRI):**
        - Mass morphology: Simple cyst, Multilocular cyst, Complex mass  
        - Presence of septations and papillary projections  
        - Vascular flow on Doppler
        """)
        morphology = st.selectbox("Mass morphology", ["Simple cyst", "Multilocular cyst", "Complex mass"])
        septations = st.radio("Are septations present?", ["No", "Yes"])
        papillary = st.radio("Are papillary projections present?", ["No", "Yes"])
        if morphology == "Simple cyst" and septations == "No" and papillary == "No":
            orads = "O-RADS 1"
        elif morphology == "Multilocular cyst" or septations == "Yes":
            orads = "O-RADS 3"
        else:
            orads = "O-RADS 4"
        st.write(f"**O-RADS Category:** {orads}")
        st.markdown("**Next Steps:** Higher O-RADS categories (4 or above) warrant surgical evaluation and possible biopsy.")
    
    # -----------------------------------------------------------
    # NI-RADS
    # -----------------------------------------------------------
    elif rads_option == "NI-RADS (Neck)":
        st.subheader("NI-RADS for Neck Imaging")
        st.markdown("""
        **Key Imaging Features:**
        - Evaluation of the primary site and nodal regions post-treatment for head & neck cancers.
        """)
        ni_rads = st.selectbox("Select NI-RADS Category", ["1", "2", "3", "4"])
        st.write(f"**NI-RADS Category:** {ni_rads}")
        st.markdown("**Next Steps:** Higher NI-RADS categories require closer surveillance and possible further diagnostic workup.")

st.markdown("---")
st.markdown("**Disclaimer:** This application is for educational and demonstration purposes only and should not be used as a substitute for professional clinical judgment.")
