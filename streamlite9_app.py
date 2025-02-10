import streamlit as st
import pandas as pd

st.title("Radiologic Classification App")
st.markdown("""
This demo app provides a menu of radiologic classification systems organized by anatomical/clinical category.
Each system uses simplified/dummy inputs for demonstration purposes only.
**Disclaimer:** This app is for demonstration only and does not constitute medical advice.
""")

# Main category selection
category = st.sidebar.selectbox(
    "Select Classification Category", 
    [
        "Neuro (Brain & Spine)",
        "Head & Neck",
        "Cardiothoracic",
        "Abdominopelvic",
        "Musculoskeletal (MSK)",
        "Interventional Radiology / Vascular",
        "RADS Systems"
    ]
)

# ================================
# 1. Neuro (Brain & Spine)
# ================================
if category == "Neuro (Brain & Spine)":
    region = st.sidebar.selectbox("Select Region", ["Brain", "Spine"])
    
    if region == "Brain":
        system = st.sidebar.selectbox(
            "Select Classification",
            [
                "Hunt and Hess Classification (SAH)",
                "Fisher Classification (SAH)",
                "Spetzler-Martin Grading (AVMs)",
                "WHO Brain Tumor Grades",
                "ICH Volume (ABC/2 Method)",
                "Modified Rankin Scale (mRS) for Stroke"
            ]
        )
        if system == "Hunt and Hess Classification (SAH)":
            st.header("Hunt and Hess Classification (SAH)")
            grade = st.selectbox("Select Grade", ["I", "II", "III", "IV", "V"])
            st.write(f"Selected Hunt and Hess Grade: **{grade}**")
            
        elif system == "Fisher Classification (SAH)":
            st.header("Fisher Classification (SAH)")
            fisher = st.selectbox("Select Fisher Score", [1, 2, 3, 4])
            st.write(f"Selected Fisher Score: **{fisher}**")
            
        elif system == "Spetzler-Martin Grading (AVMs)":
            st.header("Spetzler-Martin Grading (AVMs)")
            size = st.number_input("AVM Size (cm)", min_value=0.0, max_value=10.0, value=2.0)
            eloquence = st.radio("Eloquent Location?", ["Yes", "No"])
            venous = st.radio("Deep Venous Drainage?", ["Yes", "No"])
            # Dummy grade calculation: base grade 1 + 1 point each for size >3, eloquent, and deep venous drainage
            grade = 1 + (1 if size > 3 else 0) + (1 if eloquence == "Yes" else 0) + (1 if venous == "Yes" else 0)
            st.write(f"Approximate Spetzler-Martin Grade: **{grade}**")
            
        elif system == "WHO Brain Tumor Grades":
            st.header("WHO Brain Tumor Grades")
            grade = st.selectbox("Select Grade", ["I", "II", "III", "IV"])
            st.write(f"WHO Brain Tumor Grade: **{grade}**")
            
        elif system == "ICH Volume (ABC/2 Method)":
            st.header("ICH Volume (ABC/2 Method)")
            A = st.number_input("Dimension A (cm)", min_value=0.0, value=5.0)
            B = st.number_input("Dimension B (cm)", min_value=0.0, value=4.0)
            C = st.number_input("Dimension C (cm)", min_value=0.0, value=3.0)
            volume = (A * B * C) / 2
            st.write(f"Estimated ICH Volume: **{volume:.2f} cc**")
            
        elif system == "Modified Rankin Scale (mRS) for Stroke":
            st.header("Modified Rankin Scale (mRS) for Stroke")
            mrs = st.selectbox("Select mRS Score", [0, 1, 2, 3, 4, 5, 6])
            st.write(f"Modified Rankin Scale Score: **{mrs}**")
            
    elif region == "Spine":
        system = st.sidebar.selectbox(
            "Select Classification",
            [
                "AO Spine Classification (Vertebral Fractures)",
                "TLICS – Thoracolumbar Injury Classification",
                "Modic Classification (Vertebral Endplate Changes)",
                "Pfirrmann Classification (Intervertebral Disc Degeneration)"
            ]
        )
        if system == "AO Spine Classification (Vertebral Fractures)":
            st.header("AO Spine Classification (Vertebral Fractures)")
            fracture = st.selectbox("Select Fracture Type", ["A", "B", "C"])
            st.write(f"AO Spine Fracture Type: **{fracture}**")
            
        elif system == "TLICS – Thoracolumbar Injury Classification":
            st.header("TLICS – Thoracolumbar Injury Classification")
            score = st.number_input("Enter TLICS Score", min_value=0, max_value=20, value=4)
            st.write(f"TLICS Score: **{score}**")
            
        elif system == "Modic Classification (Vertebral Endplate Changes)":
            st.header("Modic Classification (Vertebral Endplate Changes)")
            modic = st.selectbox("Select Modic Type", ["Type I", "Type II", "Type III"])
            st.write(f"Modic Classification: **{modic}**")
            
        elif system == "Pfirrmann Classification (Intervertebral Disc Degeneration)":
            st.header("Pfirrmann Classification (Intervertebral Disc Degeneration)")
            grade = st.selectbox("Select Grade", [1, 2, 3, 4, 5])
            st.write(f"Pfirrmann Grade: **{grade}**")

# ================================
# 2. Head & Neck
# ================================
elif category == "Head & Neck":
    system = st.sidebar.selectbox(
        "Select Classification",
        [
            "TNM Staging (AJCC) for Head & Neck Cancers",
            "Lugano Classification (Lymphoma)",
            "Friedman Staging for Tonsillar Hypertrophy"
        ]
    )
    if system == "TNM Staging (AJCC) for Head & Neck Cancers":
        st.header("TNM Staging (AJCC) for Head & Neck Cancers")
        T = st.number_input("Tumor (T) Stage", min_value=0, max_value=4, value=2)
        N = st.number_input("Node (N) Stage", min_value=0, max_value=3, value=1)
        M = st.selectbox("Metastasis (M) Stage", ["0", "1"])
        st.write(f"Staging: **T{T} N{N} M{M}**")
        
    elif system == "Lugano Classification (Lymphoma)":
        st.header("Lugano Classification (Lymphoma)")
        stage = st.selectbox("Select Stage", ["I", "II", "III", "IV"])
        st.write(f"Lugano Stage: **{stage}**")
        
    elif system == "Friedman Staging for Tonsillar Hypertrophy":
        st.header("Friedman Staging for Tonsillar Hypertrophy")
        stage = st.selectbox("Select Stage", ["I", "II", "III", "IV"])
        st.write(f"Friedman Stage: **{stage}**")

# ================================
# 3. Cardiothoracic
# ================================
elif category == "Cardiothoracic":
    cardio_sub = st.sidebar.selectbox(
        "Select Subcategory", 
        ["Cardiac & Aorta", "Pulmonary Embolism", "Lung & Pleura", "Breast"]
    )
    if cardio_sub == "Cardiac & Aorta":
        system = st.sidebar.selectbox(
            "Select Classification",
            ["Stanford Classification (Aortic Dissection)", "DeBakey Classification (Aortic Dissection)"]
        )
        if system == "Stanford Classification (Aortic Dissection)":
            st.header("Stanford Classification (Aortic Dissection)")
            typ = st.selectbox("Select Type", ["Type A", "Type B"])
            st.write(f"Stanford Type: **{typ}**")
        elif system == "DeBakey Classification (Aortic Dissection)":
            st.header("DeBakey Classification (Aortic Dissection)")
            typ = st.selectbox("Select Type", ["Type I", "Type II", "Type III"])
            st.write(f"DeBakey Type: **{typ}**")
            
    elif cardio_sub == "Pulmonary Embolism":
        st.header("Qanadli Score (Pulmonary Artery Obstruction Index)")
        score = st.slider("Select Qanadli Score (0 to 40)", 0, 40, 10)
        st.write(f"Qanadli Score: **{score}**")
        
    elif cardio_sub == "Lung & Pleura":
        system = st.sidebar.selectbox(
            "Select Classification",
            [
                "Lung-RADS (Lung Cancer Screening)",
                "COVID-19 Chest Imaging Classifications (RSNA)",
                "Light’s Criteria (Pleural Effusion)",
                "ATS/ERS Classification of Idiopathic Interstitial Pneumonias"
            ]
        )
        if system == "Lung-RADS (Lung Cancer Screening)":
            st.header("Lung-RADS (Lung Cancer Screening)")
            category_lr = st.selectbox("Select Lung-RADS Category", ["1", "2", "3", "4A", "4B", "4X"])
            st.write(f"Lung-RADS Category: **{category_lr}**")
        elif system == "COVID-19 Chest Imaging Classifications (RSNA)":
            st.header("COVID-19 Chest Imaging Classifications (RSNA)")
            finding = st.selectbox("Select Finding", ["Typical", "Indeterminate", "Atypical", "Negative"])
            st.write(f"RSNA Classification: **{finding}**")
        elif system == "Light’s Criteria (Pleural Effusion)":
            st.header("Light’s Criteria (Pleural Effusion)")
            protein_ratio = st.number_input("Pleural fluid protein/serum protein ratio", 0.0, 2.0, 0.5)
            ldh_ratio = st.number_input("Pleural fluid LDH/serum LDH ratio", 0.0, 3.0, 1.0)
            st.write(f"Protein Ratio: **{protein_ratio}**; LDH Ratio: **{ldh_ratio}**")
        elif system == "ATS/ERS Classification of Idiopathic Interstitial Pneumonias":
            st.header("ATS/ERS Classification of Idiopathic Interstitial Pneumonias")
            subtype = st.selectbox("Select Subtype", ["UIP", "NSIP", "OP", "Other"])
            st.write(f"Subtype: **{subtype}**")
            
    elif cardio_sub == "Breast":
        st.header("BI-RADS (Breast Imaging Reporting & Data System)")
        birads = st.selectbox("Select BI-RADS Category", [0, 1, 2, 3, 4, 5, 6])
        st.write(f"BI-RADS Category: **{birads}**")

# ================================
# 4. Abdominopelvic
# ================================
elif category == "Abdominopelvic":
    abdo_sub = st.sidebar.selectbox(
        "Select Subcategory", 
        ["Trauma-Specific Organ Injury Scales (AAST/OIS)", "Other Abdominopelvic Classifications"]
    )
    if abdo_sub == "Trauma-Specific Organ Injury Scales (AAST/OIS)":
        organ = st.sidebar.selectbox("Select Organ", ["Spleen", "Liver", "Kidney", "Pancreas"])
        st.header(f"AAST/OIS for {organ}")
        grade = st.selectbox("Select Injury Grade", ["I", "II", "III", "IV", "V"])
        st.write(f"{organ} Injury Grade: **{grade}**")
        
    elif abdo_sub == "Other Abdominopelvic Classifications":
        system = st.sidebar.selectbox(
            "Select Classification",
            [
                "LI-RADS (Liver)",
                "Bosniak Classification (Kidney/Adrenal)",
                "Balthazar Grade (Pancreas)",
                "CT Severity Index (CTSI) for Pancreatitis",
                "PI-RADS (Prostate)",
                "O-RADS (Ovarian/Adnexal)",
                "TI-RADS (Thyroid)",
                "FIGO Staging (Uterus & Cervix)"
            ]
        )
        if system == "LI-RADS (Liver)":
            st.header("LI-RADS (Liver Imaging Reporting and Data System)")
            features = st.multiselect("Select Observed Features", 
                                      ["Hyperintensity", "Arterial Washout", "Capsule Appearance", "Threshold Growth"])
            if "Hyperintensity" in features and "Arterial Washout" in features:
                score = 4
                description = "LI-RADS 4: Probably HCC. Further evaluation is recommended."
            elif features:
                score = 3
                description = "LI-RADS 3: Intermediate probability of HCC."
            else:
                score = 2
                description = "LI-RADS 2: Probably benign lesion."
            st.write(f"LI-RADS Category: **{score}**")
            st.write(description)
            
        elif system == "Bosniak Classification (Kidney/Adrenal)":
            st.header("Bosniak Classification (Renal Cysts)")
            bosniak = st.selectbox("Select Bosniak Category", ["I", "II", "IIF", "III", "IV"])
            st.write(f"Bosniak Category: **{bosniak}**")
            
        elif system == "Balthazar Grade (Pancreas)":
            st.header("Balthazar Grade (Acute Pancreatitis)")
            grade = st.selectbox("Select Balthazar Grade", ["A", "B", "C", "D", "E"])
            st.write(f"Balthazar Grade: **{grade}**")
            
        elif system == "CT Severity Index (CTSI) for Pancreatitis":
            st.header("CT Severity Index (CTSI) for Pancreatitis")
            ctsi = st.number_input("Enter CTSI Score (0-10)", min_value=0, max_value=10, value=4)
            st.write(f"CT Severity Index: **{ctsi}**")
            
        elif system == "PI-RADS (Prostate)":
            st.header("PI-RADS (Prostate Imaging Reporting and Data System)")
            findings = st.multiselect("Select Findings", 
                                      ["Low signal intensity on T2", "Restricted diffusion", "Early enhancement"])
            if "Restricted diffusion" in findings:
                score = 4
                description = "PI-RADS 4: Likely clinically significant cancer."
            else:
                score = 2
                description = "PI-RADS 2: Low likelihood of clinically significant cancer."
            st.write(f"PI-RADS Score: **{score}**")
            st.write(description)
            
        elif system == "O-RADS (Ovarian/Adnexal)":
            st.header("O-RADS (Ovarian-Adnexal Imaging Reporting and Data System)")
            orads = st.selectbox("Select O-RADS Category", ["1", "2", "3", "4", "5"])
            st.write(f"O-RADS Category: **{orads}**")
            
        elif system == "TI-RADS (Thyroid)":
            st.header("TI-RADS (Thyroid Imaging Reporting and Data System)")
            tirads = st.selectbox("Select TI-RADS Category", ["TR1", "TR2", "TR3", "TR4", "TR5"])
            st.write(f"TI-RADS Category: **{tirads}**")
            
        elif system == "FIGO Staging (Uterus & Cervix)":
            st.header("FIGO Staging (Gynecological Cancers)")
            stage = st.selectbox("Select FIGO Stage", ["I", "II", "III", "IV"])
            st.write(f"FIGO Stage: **{stage}**")

# ================================
# 5. Musculoskeletal (MSK)
# ================================
elif category == "Musculoskeletal (MSK)":
    msk_sub = st.sidebar.selectbox(
        "Select Subcategory",
        ["General Fractures & Soft Tissue", "Pediatric", "Specific Fracture Classifications", "Spine"]
    )
    if msk_sub == "General Fractures & Soft Tissue":
        system = st.sidebar.selectbox(
            "Select Classification",
            [
                "AO/OTA Fracture Classification",
                "Gustilo–Anderson Classification (Open Fractures)",
                "Tscherne Classification (Closed & Open Soft-Tissue Injuries)"
            ]
        )
        if system == "AO/OTA Fracture Classification":
            st.header("AO/OTA Fracture Classification")
            fracture = st.selectbox("Select Fracture Type", ["Type A", "Type B", "Type C"])
            st.write(f"AO/OTA Fracture Type: **{fracture}**")
        elif system == "Gustilo–Anderson Classification (Open Fractures)":
            st.header("Gustilo–Anderson Classification (Open Fractures)")
            grade = st.selectbox("Select Grade", ["I", "II", "IIIA", "IIIB", "IIIC"])
            st.write(f"Gustilo–Anderson Grade: **{grade}**")
        elif system == "Tscherne Classification (Closed & Open Soft-Tissue Injuries)":
            st.header("Tscherne Classification (Soft-Tissue Injuries)")
            grade = st.selectbox("Select Grade", ["I", "II", "III", "IV"])
            st.write(f"Tscherne Grade: **{grade}**")
            
    elif msk_sub == "Pediatric":
        st.header("Salter-Harris Classification (Physeal Fractures)")
        sh = st.selectbox("Select Salter-Harris Type", ["I", "II", "III", "IV", "V"])
        st.write(f"Salter-Harris Type: **{sh}**")
        
    elif msk_sub == "Specific Fracture Classifications":
        system = st.sidebar.selectbox(
            "Select Classification",
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
        if system == "Garden (Femoral Neck)":
            st.header("Garden Classification (Femoral Neck Fractures)")
            garden = st.selectbox("Select Garden Stage", ["I", "II", "III", "IV"])
            st.write(f"Garden Stage: **{garden}**")
        elif system == "Pauwels (Femoral Neck)":
            st.header("Pauwels Classification (Femoral Neck Fractures)")
            pauwels = st.selectbox("Select Pauwels Type", ["I", "II", "III"])
            st.write(f"Pauwels Type: **{pauwels}**")
        elif system == "Neer (Proximal Humerus)":
            st.header("Neer Classification (Proximal Humerus Fractures)")
            neutype = st.selectbox("Select Neer Classification", ["One-Part", "Two-Part", "Three-Part", "Four-Part"])
            st.write(f"Neer Classification: **{neutype}**")
        elif system == "Weber (Ankle)":
            st.header("Weber Classification (Ankle Fractures)")
            weber = st.selectbox("Select Weber Type", ["A", "B", "C"])
            st.write(f"Weber Type: **{weber}**")
        elif system == "Lauge-Hansen (Ankle)":
            st.header("Lauge-Hansen Classification (Ankle Fractures)")
            lh = st.selectbox("Select Mechanism", ["Supination-External Rotation", "Pronation-External Rotation", "Supination-Adduction", "Pronation-Abduction"])
            st.write(f"Lauge-Hansen Mechanism: **{lh}**")
        elif system == "Frykman (Distal Radius)":
            st.header("Frykman Classification (Distal Radius Fractures)")
            frykman = st.selectbox("Select Frykman Type", ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"])
            st.write(f"Frykman Type: **{frykman}**")
        elif system == "Sanders (Calcaneal)":
            st.header("Sanders Classification (Calcaneal Fractures)")
            sanders = st.selectbox("Select Sanders Type", ["I", "II", "III", "IV"])
            st.write(f"Sanders Type: **{sanders}**")
        elif system == "Mayo (Olecranon)":
            st.header("Mayo Classification (Olecranon Fractures)")
            mayo = st.selectbox("Select Mayo Type", ["Stable", "Unstable"])
            st.write(f"Mayo Classification: **{mayo}**")
            
    elif msk_sub == "Spine":
        system = st.sidebar.selectbox(
            "Select Classification",
            [
                "Pfirrmann Classification (Intervertebral Disc Degeneration)",
                "Modic Classification (Vertebral Endplate Changes)",
                "AO Spine / TLICS (Spine Trauma)"
            ]
        )
        if system == "Pfirrmann Classification (Intervertebral Disc Degeneration)":
            st.header("Pfirrmann Classification (Intervertebral Disc Degeneration)")
            grade = st.selectbox("Select Pfirrmann Grade", [1, 2, 3, 4, 5])
            st.write(f"Pfirrmann Grade: **{grade}**")
        elif system == "Modic Classification (Vertebral Endplate Changes)":
            st.header("Modic Classification (Vertebral Endplate Changes)")
            modic = st.selectbox("Select Modic Type", ["Type I", "Type II", "Type III"])
            st.write(f"Modic Type: **{modic}**")
        elif system == "AO Spine / TLICS (Spine Trauma)":
            st.header("AO Spine / TLICS (Spine Trauma)")
            score = st.number_input("Enter TLICS Score", min_value=0, max_value=20, value=4)
            st.write(f"TLICS Score: **{score}**")

# ================================
# 6. Interventional Radiology / Vascular
# ================================
elif category == "Interventional Radiology / Vascular":
    system = st.sidebar.selectbox(
        "Select Classification",
        [
            "TICI Score (Thrombolysis in Cerebral Infarction)",
            "Hamburg Classification (Vascular Malformations)",
            "VARC Criteria for TAVR outcomes"
        ]
    )
    if system == "TICI Score (Thrombolysis in Cerebral Infarction)":
        st.header("TICI Score (Thrombolysis in Cerebral Infarction)")
        tici = st.selectbox("Select TICI Grade", ["0", "1", "2a", "2b", "3"])
        st.write(f"TICI Grade: **{tici}**")
    elif system == "Hamburg Classification (Vascular Malformations)":
        st.header("Hamburg Classification (Vascular Malformations)")
        classification = st.selectbox("Select Classification", ["Type I", "Type II", "Type III"])
        st.write(f"Hamburg Classification: **{classification}**")
    elif system == "VARC Criteria for TAVR outcomes":
        st.header("VARC Criteria for TAVR outcomes")
        outcome = st.selectbox("Select Outcome Category", ["Device success", "Early safety", "Clinical efficacy"])
        st.write(f"VARC Outcome: **{outcome}**")

# ================================
# 7. RADS Systems
# ================================
elif category == "RADS Systems":
    system = st.sidebar.selectbox(
        "Select RADS System",
        [
            "BI-RADS – Breast",
            "Lung-RADS – Lung cancer screening",
            "LI-RADS – Hepatocellular carcinoma",
            "PI-RADS – Prostate",
            "TI-RADS – Thyroid",
            "O-RADS – Ovarian/Adnexal",
            "NI-RADS – Neck Imaging Reporting and Data System"
        ]
    )
    if system == "BI-RADS – Breast":
        st.header("BI-RADS (Breast Imaging Reporting & Data System)")
        birads = st.selectbox("Select BI-RADS Category", [0, 1, 2, 3, 4, 5, 6])
        st.write(f"BI-RADS Category: **{birads}**")
    elif system == "Lung-RADS – Lung cancer screening":
        st.header("Lung-RADS (Lung Cancer Screening)")
        lr = st.selectbox("Select Lung-RADS Category", ["1", "2", "3", "4A", "4B", "4X"])
        st.write(f"Lung-RADS Category: **{lr}**")
    elif system == "LI-RADS – Hepatocellular carcinoma":
        st.header("LI-RADS (Liver Imaging Reporting and Data System)")
        features = st.multiselect("Select Observed Features", 
                                  ["Hyperintensity", "Arterial Washout", "Capsule Appearance", "Threshold Growth"])
        if "Hyperintensity" in features and "Arterial Washout" in features:
            score = 4
            description = "LI-RADS 4: Probably HCC. Further evaluation is recommended."
        elif features:
            score = 3
            description = "LI-RADS 3: Intermediate probability of HCC."
        else:
            score = 2
            description = "LI-RADS 2: Probably benign lesion."
        st.write(f"LI-RADS Category: **{score}**")
        st.write(description)
    elif system == "PI-RADS – Prostate":
        st.header("PI-RADS (Prostate Imaging Reporting and Data System)")
        findings = st.multiselect("Select Findings", 
                                  ["Low signal intensity on T2", "Restricted diffusion", "Early enhancement"])
        if "Restricted diffusion" in findings:
            score = 4
            description = "PI-RADS 4: Likely clinically significant cancer."
        else:
            score = 2
            description = "PI-RADS 2: Low likelihood of clinically significant cancer."
        st.write(f"PI-RADS Score: **{score}**")
        st.write(description)
    elif system == "TI-RADS – Thyroid":
        st.header("TI-RADS (Thyroid Imaging Reporting and Data System)")
        tirads = st.selectbox("Select TI-RADS Category", ["TR1", "TR2", "TR3", "TR4", "TR5"])
        st.write(f"TI-RADS Category: **{tirads}**")
    elif system == "O-RADS – Ovarian/Adnexal":
        st.header("O-RADS (Ovarian-Adnexal Imaging Reporting and Data System)")
        orads = st.selectbox("Select O-RADS Category", ["1", "2", "3", "4", "5"])
        st.write(f"O-RADS Category: **{orads}**")
    elif system == "NI-RADS – Neck Imaging Reporting and Data System":
        st.header("NI-RADS (Neck Imaging Reporting and Data System)")
        ni_rads = st.selectbox("Select NI-RADS Category", ["1", "2", "3", "4"])
        st.write(f"NI-RADS Category: **{ni_rads}**")

st.markdown("---")
st.markdown("**Disclaimer:** This app is for demonstration purposes only and does not substitute for professional diagnosis.")
