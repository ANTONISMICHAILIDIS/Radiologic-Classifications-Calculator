import streamlit as st

st.title("Comprehensive Radiologic Classification App")
st.markdown("""
This app allows the radiologist to input radiologic findings and select the relevant classification system to obtain a score/grade.  
**Note:** All scoring here is for demonstration purposes only. Always refer to current clinical guidelines for actual decision‐making.
""")

# Main Category Selection
category = st.sidebar.selectbox(
    "Select an Anatomical/Clinical Category", 
    [
        "NEURO", 
        "HEAD & NECK", 
        "CARDIOTHORACIC", 
        "ABDOMINOPELVIC", 
        "MUSCULOSKELETAL (MSK)", 
        "INTERVENTIONAL RADIOLOGY/VASCULAR", 
        "-RADS SYSTEMS"
    ]
)

# =============================================================================
# 1. NEURO
# =============================================================================
if category == "NEURO":
    st.header("NEURO - Brain & Spine Classifications")
    neuro_option = st.sidebar.selectbox(
        "Select a Neuro Classification System", 
        [
            "Hunt and Hess (SAH)", 
            "Fisher (SAH)", 
            "Spetzler-Martin (AVMs)", 
            "WHO Brain Tumor Grades", 
            "Modified Rankin Scale (mRS)", 
            "Spine Classifications"
        ]
    )
    
    if neuro_option == "Hunt and Hess (SAH)":
        st.subheader("Hunt and Hess Classification (Subarachnoid Hemorrhage)")
        st.markdown(
            """
            **Overview:**  
            Although primarily clinical, imaging (CT/MR) is used to identify the presence and approximate amount of subarachnoid blood.  
            **Key Imaging Feature:** Extent and density of SAH.
            """
        )
        hh_grade = st.selectbox("Select Hunt and Hess Grade", ["I", "II", "III", "IV", "V"])
        st.write(f"**Hunt and Hess Grade Selected:** {hh_grade}")
        
    elif neuro_option == "Fisher (SAH)":
        st.subheader("Fisher Classification (Subarachnoid Hemorrhage)")
        st.markdown(
            """
            **Overview:**  
            Focuses on the amount and distribution of subarachnoid blood on noncontrast head CT.  
            **Key Checks:**  
            - No hemorrhage vs. thin (<1 mm) or thick (>1 mm) blood layers.  
            - Localized versus diffuse distribution and presence of intracerebral/intraventricular blood.
            """
        )
        fisher_grade = st.selectbox("Select Fisher Grade", [1, 2, 3, 4])
        st.write(f"**Fisher Grade Selected:** {fisher_grade}")
        
    elif neuro_option == "Spetzler-Martin (AVMs)":
        st.subheader("Spetzler-Martin Grading (Arteriovenous Malformations)")
        st.markdown(
            """
            **Overview:**  
            Used for intracranial AVMs based on digital subtraction angiography (DSA) or MRI/MRA.  
            **Key Radiological Checks:**  
            - **Nidus size:** Small (<3 cm), Medium (3–6 cm), or Large (>6 cm)  
            - **Eloquent Cortex Involvement:** Yes/No  
            - **Venous Drainage:** Superficial only vs. Deep drainage
            """
        )
        avm_size = st.number_input("Enter AVM Nidus Size (cm)", min_value=0.0, step=0.1, value=2.0)
        eloquent = st.selectbox("Involvement of Eloquent Cortex?", ["Yes", "No"])
        deep_venous = st.selectbox("Deep Venous Drainage?", ["Yes", "No"])
        # Dummy grading: start with 1, add 1 for each adverse feature.
        grade = 1 + (1 if avm_size > 3.0 else 0) + (1 if eloquent == "Yes" else 0) + (1 if deep_venous == "Yes" else 0)
        st.write(f"**Estimated Spetzler-Martin Grade:** {grade}")
        
    elif neuro_option == "WHO Brain Tumor Grades":
        st.subheader("WHO Brain Tumor Grades")
        st.markdown(
            """
            **Overview:**  
            While histopathological grading is definitive, imaging findings (enhancement, necrosis, edema, mass effect, diffusion restriction) can suggest the tumor grade.
            """
        )
        tumor_grade = st.selectbox("Select WHO Tumor Grade", ["I", "II", "III", "IV"])
        st.write(f"**WHO Brain Tumor Grade Selected:** {tumor_grade}")
        
    elif neuro_option == "Modified Rankin Scale (mRS)":
        st.subheader("Modified Rankin Scale (mRS)")
        st.markdown(
            """
            **Overview:**  
            A clinical outcome measure (0–6) often correlated with imaging findings (e.g., infarct volume in stroke).
            """
        )
        mrs = st.selectbox("Select mRS Score", [0, 1, 2, 3, 4, 5, 6])
        st.write(f"**Modified Rankin Scale Score Selected:** {mrs}")
        
    elif neuro_option == "Spine Classifications":
        spine_option = st.sidebar.selectbox(
            "Select a Spine Classification", 
            [
                "AO Spine (Vertebral Fractures)", 
                "TLICS (Thoracolumbar Injury)", 
                "Modic (Vertebral Endplate Changes)", 
                "Pfirrmann (Disc Degeneration)"
            ]
        )
        if spine_option == "AO Spine (Vertebral Fractures)":
            st.subheader("AO Spine Classification (Vertebral Fractures)")
            st.markdown(
                """
                **Overview:**  
                Used for traumatic vertebral injuries. Key factors include fracture morphology, integrity of posterior elements, and neurological involvement.
                """
            )
            ao_type = st.selectbox("Select AO Fracture Type", ["A", "B", "C"])
            st.write(f"**AO Spine Fracture Type Selected:** {ao_type}")
        elif spine_option == "TLICS (Thoracolumbar Injury)":
            st.subheader("TLICS – Thoracolumbar Injury Classification & Severity Score")
            st.markdown(
                """
                **Overview:**  
                Considers injury morphology, posterior ligamentous complex integrity, and neurological status.
                """
            )
            tlics_score = st.number_input("Enter TLICS Score", min_value=0, max_value=20, value=4)
            st.write(f"**TLICS Score:** {tlics_score}")
        elif spine_option == "Modic (Vertebral Endplate Changes)":
            st.subheader("Modic Classification (Vertebral Endplate Changes)")
            st.markdown(
                """
                **Overview:**  
                Evaluates MRI T1/T2 signal changes:  
                - **Type I:** T1 hypointense, T2 hyperintense (edema/inflammation)  
                - **Type II:** T1 & T2 hyperintense (fatty replacement)  
                - **Type III:** T1 & T2 hypointense (sclerosis)
                """
            )
            modic_type = st.selectbox("Select Modic Type", ["Type I", "Type II", "Type III"])
            st.write(f"**Modic Type Selected:** {modic_type}")
        elif spine_option == "Pfirrmann (Disc Degeneration)":
            st.subheader("Pfirrmann Classification (Intervertebral Disc Degeneration)")
            st.markdown(
                """
                **Overview:**  
                Based on T2-weighted MRI appearance evaluating disc signal, height, and distinction between nucleus and annulus.  
                Grades I to V indicate progressive degeneration.
                """
            )
            pf_grade = st.selectbox("Select Pfirrmann Grade", [1, 2, 3, 4, 5])
            st.write(f"**Pfirrmann Grade Selected:** {pf_grade}")

# =============================================================================
# 2. HEAD & NECK
# =============================================================================
elif category == "HEAD & NECK":
    st.header("Head & Neck Classifications")
    head_neck = st.sidebar.selectbox(
        "Select a Head & Neck Classification", 
        [
            "TNM Staging (AJCC) for Head & Neck Cancers", 
            "Lugano Classification (Lymphoma)", 
            "Friedman Staging for Tonsillar Hypertrophy"
        ]
    )
    if head_neck == "TNM Staging (AJCC) for Head & Neck Cancers":
        st.subheader("TNM Staging (AJCC)")
        st.markdown(
            """
            **Overview:**  
            Assesses the primary tumor (T), nodal involvement (N), and distant metastasis (M).  
            **Key Checks:** Tumor size/local extension, lymph node involvement, and distant spread.
            """
        )
        T = st.number_input("Enter Tumor (T) Stage", min_value=0, max_value=4, value=2)
        N = st.number_input("Enter Node (N) Stage", min_value=0, max_value=3, value=1)
        M = st.selectbox("Select Metastasis (M) Stage", ["0", "1"])
        st.write(f"**TNM Staging:** T{T} N{N} M{M}")
    elif head_neck == "Lugano Classification (Lymphoma)":
        st.subheader("Lugano Classification (Lymphoma)")
        st.markdown(
            """
            **Overview:**  
            Used for staging nodal and extranodal disease in lymphoma (often using PET-CT findings).  
            **Key Checks:** Nodal station involvement, extranodal lesions, and bone marrow uptake.
            """
        )
        lugano_stage = st.selectbox("Select Lugano Stage", ["I", "II", "III", "IV"])
        st.write(f"**Lugano Stage Selected:** {lugano_stage}")
    elif head_neck == "Friedman Staging for Tonsillar Hypertrophy":
        st.subheader("Friedman Staging for Tonsillar Hypertrophy")
        st.markdown(
            """
            **Overview:**  
            Evaluates the degree of tonsillar hypertrophy causing oropharyngeal airway obstruction.  
            **Key Check:** Visible overlap/intrusion into the oropharynx.
            """
        )
        friedman = st.selectbox("Select Friedman Stage", ["1", "2", "3", "4"])
        st.write(f"**Friedman Stage Selected:** {friedman}")

# =============================================================================
# 3. CARDIOTHORACIC
# =============================================================================
elif category == "CARDIOTHORACIC":
    st.header("Cardiothoracic Classifications")
    cardio_option = st.sidebar.selectbox(
        "Select a Cardiothoracic Subcategory", 
        ["Aortic Dissection", "Pulmonary Embolism (Qanadli Score)", "Lung & Pleura", "Breast (BI-RADS)"]
    )
    if cardio_option == "Aortic Dissection":
        dissection_sys = st.sidebar.selectbox("Select Dissection Classification", ["Stanford", "DeBakey"])
        if dissection_sys == "Stanford":
            st.subheader("Stanford Classification (Aortic Dissection)")
            st.markdown(
                """
                **Stanford Classification:**  
                - **Type A:** Involves the ascending aorta (regardless of origin).  
                - **Type B:** Does not involve the ascending aorta.
                """
            )
            stanford_type = st.selectbox("Select Stanford Type", ["Type A", "Type B"])
            st.write(f"**Stanford Type Selected:** {stanford_type}")
        elif dissection_sys == "DeBakey":
            st.subheader("DeBakey Classification (Aortic Dissection)")
            st.markdown(
                """
                **DeBakey Classification:**  
                - **Type I:** Originates in ascending aorta, extends beyond the arch.  
                - **Type II:** Limited to the ascending aorta.  
                - **Type III:** Originates in the descending aorta (IIIa: thoracic, IIIb: extends below diaphragm).
                """
            )
            debakey_type = st.selectbox("Select DeBakey Type", ["Type I", "Type II", "Type III"])
            st.write(f"**DeBakey Type Selected:** {debakey_type}")
            
    elif cardio_option == "Pulmonary Embolism (Qanadli Score)":
        st.subheader("Qanadli Score (Pulmonary Embolism)")
        st.markdown(
            """
            **Overview:**  
            Assesses clot burden on CT Pulmonary Angiography.  
            **Method:** For each of 20 segmental arteries, assign 1 point if partially occluded and 2 points if completely occluded (max score = 40).
            """
        )
        partial = st.number_input("Enter Number of Partially Occluded Segmental Arteries", min_value=0, max_value=20, value=0)
        complete = st.number_input("Enter Number of Completely Occluded Segmental Arteries", min_value=0, max_value=20, value=0)
        qanadli_score = partial * 1 + complete * 2
        st.write(f"**Calculated Qanadli Score:** {qanadli_score} / 40")
        
    elif cardio_option == "Lung & Pleura":
        lung_pleura = st.sidebar.selectbox(
            "Select a Lung & Pleura Classification", 
            ["Lung-RADS", "COVID-19 Chest Imaging (RSNA)", "Light’s Criteria (Pleural Effusion)", "ATS/ERS Classification (Idiopathic Interstitial Pneumonias)"]
        )
        if lung_pleura == "Lung-RADS":
            st.subheader("Lung-RADS")
            st.markdown(
                """
                **Overview:**  
                Used for lung cancer screening on low-dose CT.  
                **Key Checks:** Nodule size, composition (solid, part-solid, ground-glass), and growth rate.
                """
            )
            lung_rads = st.selectbox("Select Lung-RADS Category", ["0", "1", "2", "3", "4A", "4B", "4X"])
            st.write(f"**Lung-RADS Category Selected:** {lung_rads}")
        elif lung_pleura == "COVID-19 Chest Imaging (RSNA)":
            st.subheader("RSNA COVID-19 Chest Imaging Classification")
            st.markdown(
                """
                **Categories:**  
                - **Typical:** Bilateral, peripheral ground-glass opacities  
                - **Indeterminate:** Nonspecific distribution  
                - **Atypical:** Unilateral consolidation, pleural effusion, etc.  
                - **Negative:** No pneumonia findings.
                """
            )
            covid_class = st.selectbox("Select RSNA Category", ["Typical", "Indeterminate", "Atypical", "Negative"])
            st.write(f"**RSNA Category Selected:** {covid_class}")
        elif lung_pleura == "Light’s Criteria (Pleural Effusion)":
            st.subheader("Light’s Criteria (Pleural Effusion)")
            st.markdown(
                """
                **Overview:**  
                Although primarily based on laboratory values, imaging can reveal features like septations or loculations.
                """
            )
            protein_ratio = st.number_input("Pleural fluid protein / Serum protein ratio", min_value=0.0, value=0.5)
            ldh_ratio = st.number_input("Pleural fluid LDH / Serum LDH ratio", min_value=0.0, value=1.0)
            st.write(f"**Protein Ratio:** {protein_ratio} | **LDH Ratio:** {ldh_ratio}")
        elif lung_pleura == "ATS/ERS Classification (Idiopathic Interstitial Pneumonias)":
            st.subheader("ATS/ERS Classification")
            st.markdown(
                """
                **Overview:**  
                Classifies interstitial lung disease patterns (e.g. UIP, NSIP, COP) based on HRCT.
                """
            )
            pattern = st.selectbox("Select Pattern", ["UIP", "NSIP", "COP", "Other"])
            st.write(f"**Selected Pattern:** {pattern}")
            
    elif cardio_option == "Breast (BI-RADS)":
        st.subheader("BI-RADS (Breast Imaging Reporting & Data System)")
        st.markdown(
            """
            **Overview:**  
            Categorizes breast imaging findings (mammography, US, MRI) from 0 to 6 to guide management.
            """
        )
        birads = st.selectbox("Select BI-RADS Category", [0, 1, 2, 3, 4, 5, 6])
        st.write(f"**BI-RADS Category Selected:** {birads}")

# =============================================================================
# 4. ABDOMINOPELVIC
# =============================================================================
elif category == "ABDOMINOPELVIC":
    st.header("Abdominopelvic Classifications")
    abdo_option = st.sidebar.selectbox(
        "Select a Subcategory", 
        ["Trauma-Specific Organ Injury Scales (AAST/OIS)", "Other Abdominopelvic Classifications"]
    )
    if abdo_option == "Trauma-Specific Organ Injury Scales (AAST/OIS)":
        organ = st.selectbox("Select an Organ", ["Spleen", "Liver", "Kidney", "Pancreas"])
        st.markdown(f"""
        **AAST/OIS for {organ}:**  
        These scales use CT and operative findings to grade injury severity based on hematoma size, laceration depth, and vascular injury.
        """)
        injury_grade = st.selectbox("Select Injury Grade", ["I", "II", "III", "IV", "V"])
        st.write(f"**{organ} Injury Grade Selected:** {injury_grade}")
        
    elif abdo_option == "Other Abdominopelvic Classifications":
        abdo_class = st.sidebar.selectbox(
            "Select a Classification", 
            [
                "LI-RADS (Liver)", 
                "Bosniak Classification (Kidney/Adrenal)", 
                "Balthazar Grade (Pancreas)", 
                "CT Severity Index (Pancreatitis)", 
                "PI-RADS (Prostate)", 
                "O-RADS (Ovarian/Adnexal)", 
                "TI-RADS (Thyroid)", 
                "FIGO Staging (Uterus & Cervix)"
            ]
        )
        if abdo_class == "LI-RADS (Liver)":
            st.subheader("LI-RADS (Liver Imaging Reporting and Data System)")
            st.markdown(
                """
                **Overview:**  
                Used in patients at high risk for HCC. Key imaging features on contrast-enhanced CT/MRI include arterial phase hyperenhancement, washout, and capsule appearance.
                """
            )
            li_features = st.multiselect(
                "Select Observed LI-RADS Features", 
                ["Arterial Phase Hyperenhancement", "Washout", "Capsule Appearance", "Lesion Size > 10mm"]
            )
            # Dummy logic for demonstration
            if "Arterial Phase Hyperenhancement" in li_features and "Washout" in li_features:
                li_category = "LR-4"
            elif li_features:
                li_category = "LR-3"
            else:
                li_category = "LR-2"
            st.write(f"**LI-RADS Category Estimated:** {li_category}")
            
        elif abdo_class == "Bosniak Classification (Kidney/Adrenal)":
            st.subheader("Bosniak Classification (Renal Cysts)")
            bosniak = st.selectbox("Select Bosniak Category", ["I", "II", "IIF", "III", "IV"])
            st.write(f"**Bosniak Category Selected:** {bosniak}")
            
        elif abdo_class == "Balthazar Grade (Pancreas)":
            st.subheader("Balthazar Grade (Acute Pancreatitis)")
            balthazar = st.selectbox("Select Balthazar Grade", ["A", "B", "C", "D", "E"])
            st.write(f"**Balthazar Grade Selected:** {balthazar}")
            
        elif abdo_class == "CT Severity Index (Pancreatitis)":
            st.subheader("CT Severity Index (CTSI) for Pancreatitis")
            ctsi = st.number_input("Enter CTSI Score (0-10)", min_value=0, max_value=10, value=4)
            st.write(f"**CT Severity Index:** {ctsi}")
            
        elif abdo_class == "PI-RADS (Prostate)":
            st.subheader("PI-RADS (Prostate Imaging Reporting and Data System)")
            pi_findings = st.multiselect(
                "Select Prostate Findings", 
                ["Low signal intensity on T2", "Restricted diffusion", "Early enhancement"]
            )
            # Dummy logic: if restricted diffusion is present, assign higher score.
            pi_score = 4 if "Restricted diffusion" in pi_findings else 2
            st.write(f"**PI-RADS Score Estimated:** {pi_score}")
            
        elif abdo_class == "O-RADS (Ovarian/Adnexal)":
            st.subheader("O-RADS (Ovarian-Adnexal Imaging Reporting and Data System)")
            orads = st.selectbox("Select O-RADS Category", ["0", "1", "2", "3", "4", "5"])
            st.write(f"**O-RADS Category Selected:** {orads}")
            
        elif abdo_class == "TI-RADS (Thyroid)":
            st.subheader("TI-RADS (Thyroid Imaging Reporting and Data System)")
            tirads = st.selectbox("Select TI-RADS Category", ["TR1", "TR2", "TR3", "TR4", "TR5"])
            st.write(f"**TI-RADS Category Selected:** {tirads}")
            
        elif abdo_class == "FIGO Staging (Uterus & Cervix)":
            st.subheader("FIGO Staging (Gynecologic Cancers)")
            figo = st.selectbox("Select FIGO Stage", ["I", "II", "III", "IV"])
            st.write(f"**FIGO Stage Selected:** {figo}")

# =============================================================================
# 5. MUSCULOSKELETAL (MSK)
# =============================================================================
elif category == "MUSCULOSKELETAL (MSK)":
    st.header("Musculoskeletal (MSK) Classifications")
    msk_option = st.sidebar.selectbox(
        "Select an MSK Subcategory", 
        [
            "AO/OTA Fracture Classification (Long Bones)", 
            "Gustilo–Anderson (Open Fractures)", 
            "Tscherne Classification (Soft Tissue Injuries)", 
            "Salter-Harris (Physeal Fractures)", 
            "Other Fracture Classifications"
        ]
    )
    if msk_option == "AO/OTA Fracture Classification (Long Bones)":
        st.subheader("AO/OTA Fracture Classification")
        st.markdown("Assesses the fracture pattern (e.g., simple, wedge, complex) based on the bone segment and articular involvement.")
        fracture_type = st.selectbox("Select Fracture Pattern", ["Simple", "Wedge", "Complex"])
        st.write(f"**Fracture Pattern Selected:** {fracture_type}")
        
    elif msk_option == "Gustilo–Anderson (Open Fractures)":
        st.subheader("Gustilo–Anderson Classification (Open Fractures)")
        st.markdown(
            """
            **Overview:**  
            Grades the severity of open fractures primarily based on wound size and extent of soft tissue damage.  
            - Type I: Clean wound <1 cm  
            - Type II: 1–10 cm  
            - Type III: >10 cm or severe soft tissue injury
            """
        )
        gustilo = st.selectbox("Select Gustilo–Anderson Type", ["I", "II", "III"])
        st.write(f"**Gustilo–Anderson Type Selected:** {gustilo}")
        
    elif msk_option == "Tscherne Classification (Soft Tissue Injuries)":
        st.subheader("Tscherne Classification (Soft Tissue Injuries)")
        st.markdown("Evaluates soft tissue injury severity associated with fractures.")
        tscherne = st.selectbox("Select Tscherne Grade", ["I", "II", "III", "IV"])
        st.write(f"**Tscherne Grade Selected:** {tscherne}")
        
    elif msk_option == "Salter-Harris (Physeal Fractures)":
        st.subheader("Salter-Harris Classification (Pediatric)")
        st.markdown("Used for growth plate fractures in children. Types I–V describe increasing physeal involvement.")
        sh_type = st.selectbox("Select Salter-Harris Type", ["I", "II", "III", "IV", "V"])
        st.write(f"**Salter-Harris Type Selected:** {sh_type}")
        
    elif msk_option == "Other Fracture Classifications":
        fracture_sys = st.sidebar.selectbox(
            "Select a Specific Fracture Classification", 
            [
                "Garden (Femoral Neck)", 
                "Pauwels (Femoral Neck)", 
                "Neer (Proximal Humerus)", 
                "Weber (Ankle)", 
                "Lauge-Hansen (Ankle)", 
                "Frykman (Distal Radius)", 
                "Sanders (Calcaneal)", 
                "Mayo (Olecranon)"
            ]
        )
        if fracture_sys == "Garden (Femoral Neck)":
            st.subheader("Garden Classification (Femoral Neck Fractures)")
            garden = st.selectbox("Select Garden Stage", ["I", "II", "III", "IV"])
            st.write(f"**Garden Stage Selected:** {garden}")
        elif fracture_sys == "Pauwels (Femoral Neck)":
            st.subheader("Pauwels Classification (Femoral Neck Fractures)")
            pauwels = st.selectbox("Select Pauwels Type", ["I", "II", "III"])
            st.write(f"**Pauwels Type Selected:** {pauwels}")
        elif fracture_sys == "Neer (Proximal Humerus)":
            st.subheader("Neer Classification (Proximal Humerus Fractures)")
            neer = st.selectbox("Select Neer Classification", ["One-Part", "Two-Part", "Three-Part", "Four-Part"])
            st.write(f"**Neer Classification Selected:** {neer}")
        elif fracture_sys == "Weber (Ankle)":
            st.subheader("Weber Classification (Ankle Fractures)")
            weber = st.selectbox("Select Weber Type", ["A", "B", "C"])
            st.write(f"**Weber Type Selected:** {weber}")
        elif fracture_sys == "Lauge-Hansen (Ankle)":
            st.subheader("Lauge-Hansen Classification (Ankle Fractures)")
            lh = st.selectbox("Select Mechanism", ["Supination-External Rotation", "Pronation-External Rotation", "Supination-Adduction", "Pronation-Abduction"])
            st.write(f"**Lauge-Hansen Mechanism Selected:** {lh}")
        elif fracture_sys == "Frykman (Distal Radius)":
            st.subheader("Frykman Classification (Distal Radius Fractures)")
            frykman = st.selectbox("Select Frykman Type", ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"])
            st.write(f"**Frykman Type Selected:** {frykman}")
        elif fracture_sys == "Sanders (Calcaneal)":
            st.subheader("Sanders Classification (Calcaneal Fractures)")
            sanders = st.selectbox("Select Sanders Type", ["I", "II", "III", "IV"])
            st.write(f"**Sanders Type Selected:** {sanders}")
        elif fracture_sys == "Mayo (Olecranon)":
            st.subheader("Mayo Classification (Olecranon Fractures)")
            mayo = st.selectbox("Select Mayo Type", ["Stable", "Unstable"])
            st.write(f"**Mayo Classification Selected:** {mayo}")

# =============================================================================
# 6. INTERVENTIONAL RADIOLOGY/VASCULAR
# =============================================================================
elif category == "INTERVENTIONAL RADIOLOGY/VASCULAR":
    st.header("Interventional Radiology / Vascular Classifications")
    vascular_option = st.sidebar.selectbox(
        "Select a Vascular Classification", 
        [
            "TICI Score (Thrombolysis in Cerebral Infarction)", 
            "Hamburg Classification (Vascular Malformations)", 
            "VARC Criteria for TAVR Outcomes"
        ]
    )
    if vascular_option == "TICI Score (Thrombolysis in Cerebral Infarction)":
        st.subheader("TICI Score")
        st.markdown(
            """
            **Overview:**  
            Assesses reperfusion after acute stroke interventions.  
            **Grades:** 0 (no perfusion) to 3 (full perfusion).
            """
        )
        tici = st.selectbox("Select TICI Grade", ["0", "1", "2a", "2b", "3"])
        st.write(f"**TICI Grade Selected:** {tici}")
    elif vascular_option == "Hamburg Classification (Vascular Malformations)":
        st.subheader("Hamburg Classification")
        st.markdown(
            """
            **Overview:**  
            Categorizes vascular malformations based on flow dynamics and embryologic origin.
            """
        )
        hamburg = st.selectbox("Select Hamburg Classification", ["Type I", "Type II", "Type III"])
        st.write(f"**Hamburg Classification Selected:** {hamburg}")
    elif vascular_option == "VARC Criteria for TAVR Outcomes":
        st.subheader("VARC Criteria")
        st.markdown(
            """
            **Overview:**  
            Used for evaluating outcomes of transcatheter aortic valve replacement (TAVR).  
            **Key Domains:** Device success, early safety, and clinical efficacy.
            """
        )
        varc = st.selectbox("Select VARC Outcome Category", ["Device Success", "Early Safety", "Clinical Efficacy"])
        st.write(f"**VARC Outcome Category Selected:** {varc}")

# =============================================================================
# 7. -RADS SYSTEMS
# =============================================================================
elif category == "-RADS SYSTEMS":
    st.header("-RADS Systems Overview")
    rads_option = st.sidebar.selectbox(
        "Select a -RADS System", 
        [
            "BI-RADS (Breast)", 
            "Lung-RADS (Lung)", 
            "LI-RADS (Liver)", 
            "PI-RADS (Prostate)", 
            "TI-RADS (Thyroid)", 
            "O-RADS (Ovarian/Adnexal)", 
            "NI-RADS (Neck)"
        ]
    )
    if rads_option == "BI-RADS (Breast)":
        st.subheader("BI-RADS")
        st.markdown("Standardizes breast imaging reporting. Categories range from 0 to 6.")
        birads_rads = st.selectbox("Select BI-RADS Category", [0, 1, 2, 3, 4, 5, 6])
        st.write(f"**BI-RADS Category Selected:** {birads_rads}")
    elif rads_option == "Lung-RADS (Lung)":
        st.subheader("Lung-RADS")
        st.markdown("Used for lung cancer screening reporting on low-dose CT.")
        lung_rads = st.selectbox("Select Lung-RADS Category", ["0", "1", "2", "3", "4A", "4B", "4X"])
        st.write(f"**Lung-RADS Category Selected:** {lung_rads}")
    elif rads_option == "LI-RADS (Liver)":
        st.subheader("LI-RADS")
        st.markdown("Categorizes liver lesions in patients at high risk for HCC based on CT/MRI findings.")
        li_features = st.multiselect(
            "Select Observed LI-RADS Features", 
            ["Arterial Hyperenhancement", "Washout", "Capsule Appearance", "Lesion Size > 10mm"]
        )
        if "Arterial Hyperenhancement" in li_features and "Washout" in li_features:
            li_category = "LR-4"
        elif li_features:
            li_category = "LR-3"
        else:
            li_category = "LR-2"
        st.write(f"**LI-RADS Category Estimated:** {li_category}")
    elif rads_option == "PI-RADS (Prostate)":
        st.subheader("PI-RADS")
        st.markdown("Scores prostate lesions from 1 to 5 based on multiparametric MRI features.")
        pi_findings = st.multiselect(
            "Select Prostate Findings", 
            ["Low signal intensity on T2", "Restricted diffusion", "Early enhancement"]
        )
        pi_score = 4 if "Restricted diffusion" in pi_findings else 2
        st.write(f"**PI-RADS Score Estimated:** {pi_score}")
    elif rads_option == "TI-RADS (Thyroid)":
        st.subheader("TI-RADS")
        st.markdown("Standardizes reporting of thyroid nodules on ultrasound. Categories: TR1–TR5.")
        ti_rads = st.selectbox("Select TI-RADS Category", ["TR1", "TR2", "TR3", "TR4", "TR5"])
        st.write(f"**TI-RADS Category Selected:** {ti_rads}")
    elif rads_option == "O-RADS (Ovarian/Adnexal)":
        st.subheader("O-RADS")
        st.markdown("Provides a score from 0 to 5 for ovarian/adnexal masses based on imaging morphology.")
        o_rads = st.selectbox("Select O-RADS Category", ["0", "1", "2", "3", "4", "5"])
        st.write(f"**O-RADS Category Selected:** {o_rads}")
    elif rads_option == "NI-RADS (Neck)":
        st.subheader("NI-RADS")
        st.markdown("Used for standardized reporting and follow-up of neck tumors.")
        ni_rads = st.selectbox("Select NI-RADS Category", ["1", "2", "3", "4"])
        st.write(f"**NI-RADS Category Selected:** {ni_rads}")

st.markdown("---")
st.markdown("**Disclaimer:** This app is for demonstration purposes only and does not substitute for professional diagnosis or clinical judgment.")
