import streamlit as st

st.title("Comprehensive Radiologic Classification App")
st.markdown("""
This app allows you to input imaging characteristics for various radiologic studies. Based on your input, the app provides a classification (or score/grade), an analysis of that result, and clinical recommendations (next steps) to guide further diagnosis and management.

**Note:** All scoring, analysis, and recommendations here are for demonstration purposes only. Always refer to validated clinical guidelines for decision‐making.
""")

# =============================================================================
# Main Category Selection
# =============================================================================
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
    st.header("NEURO – Brain & Spine Classifications")
    neuro_option = st.sidebar.selectbox(
        "Select a Neuro Classification System", 
        [
            "Hunt and Hess (SAH)", 
            "Fisher (SAH)", 
            "Spetzler-Martin (AVMs)", 
            "WHO Brain Tumor Grades", 
            "Modified Rankin Scale (mRS)",
            "Fazekas Scale for WM Lesions",
            "Spine Classifications",
            "Scheltens Score (Temporal Lobe Atrophy)"
        ]
    )
    
    # ------------------------------
    # Hunt and Hess (SAH)
    # ------------------------------
    if neuro_option == "Hunt and Hess (SAH)":
        st.subheader("Hunt and Hess Classification (Subarachnoid Hemorrhage)")
        st.markdown(
            """
            **Overview:**  
            Although primarily a clinical scale, imaging (CT/MR) helps assess the extent of subarachnoid blood.
            """
        )
        hh_grade = st.selectbox("Select Hunt and Hess Grade", ["I", "II", "III", "IV", "V"])
        st.write(f"**Hunt and Hess Grade Selected:** {hh_grade}")
        if hh_grade == "I":
            analysis = "Minimal hemorrhage with a favorable prognosis."
            next_steps = "Monitor the patient with routine imaging; neurosurgical consultation is not urgent."
        elif hh_grade == "II":
            analysis = "Mild-to-moderate hemorrhage; symptoms are modest."
            next_steps = "Recommend neurosurgical consultation and close observation for any deterioration."
        elif hh_grade == "III":
            analysis = "Moderate-to-severe symptoms; increased risk for complications."
            next_steps = "Urgently involve neurosurgery and consider repeat imaging to monitor for vasospasm."
        elif hh_grade == "IV":
            analysis = "Severe deficits and a high risk for complications."
            next_steps = "Immediate neurosurgical evaluation is warranted; prepare for potential intensive care management."
        else:
            analysis = "Critical condition with a poor prognosis."
            next_steps = "Emergency neurosurgical and critical care management are required."
        st.markdown(f"**Analysis:** {analysis}")
        st.markdown(f"**Next Steps:** {next_steps}")
        
    # ------------------------------
    # Fisher (SAH)
    # ------------------------------
    elif neuro_option == "Fisher (SAH)":
        st.subheader("Fisher Classification (Subarachnoid Hemorrhage)")
        st.markdown(
            """
            **Overview:**  
            Assesses the amount/distribution of blood on noncontrast CT to predict vasospasm risk.
            """
        )
        fisher_grade = st.selectbox("Select Fisher Grade", [1, 2, 3, 4])
        st.write(f"**Fisher Grade Selected:** {fisher_grade}")
        if fisher_grade == 1:
            analysis = "No or minimal hemorrhage; low risk for vasospasm."
            next_steps = "Continue monitoring; no immediate intervention needed."
        elif fisher_grade == 2:
            analysis = "Thin layer of blood present; relatively low risk."
            next_steps = "Monitor clinically with serial imaging and consider prophylactic measures."
        elif fisher_grade == 3:
            analysis = "Thick or diffuse blood; higher risk for vasospasm."
            next_steps = "Initiate vasospasm prophylaxis and plan for intensive monitoring."
        else:
            analysis = "Intraventricular extension increases the risk for severe vasospasm."
            next_steps = "Aggressive management including possible endovascular therapy is recommended."
        st.markdown(f"**Analysis:** {analysis}")
        st.markdown(f"**Next Steps:** {next_steps}")
        
    # ------------------------------
    # Spetzler-Martin (AVMs)
    # ------------------------------
    elif neuro_option == "Spetzler-Martin (AVMs)":
        st.subheader("Spetzler-Martin Grading (Arteriovenous Malformations)")
        st.markdown(
            """
            **Overview:**  
            Evaluates AVM characteristics on DSA or MRI/MRA:
            - Nidus size (small <3 cm, medium 3–6 cm, large >6 cm)
            - Eloquent cortex involvement
            - Venous drainage (superficial vs. deep)
            """
        )
        avm_size = st.number_input("Enter AVM Nidus Size (cm)", min_value=0.0, step=0.1, value=2.0)
        eloquent = st.selectbox("Eloquent Cortex Involvement?", ["Yes", "No"])
        deep_venous = st.selectbox("Deep Venous Drainage?", ["Yes", "No"])
        grade = 1 + (1 if avm_size > 3.0 else 0) + (1 if eloquent == "Yes" else 0) + (1 if deep_venous == "Yes" else 0)
        st.write(f"**Estimated Spetzler-Martin Grade:** {grade}")
        analysis = f"A grade of {grade} correlates with increased surgical risk."
        next_steps = "Recommend neurosurgical consultation for treatment planning (embolization, resection, or radiosurgery)."
        st.markdown(f"**Analysis:** {analysis}")
        st.markdown(f"**Next Steps:** {next_steps}")
        
    # ------------------------------
    # WHO Brain Tumor Grades
    # ------------------------------
    elif neuro_option == "WHO Brain Tumor Grades":
        st.subheader("WHO Brain Tumor Grades")
        st.markdown(
            """
            **Overview:**  
            Imaging findings (enhancement, necrosis, edema) can suggest tumor grade, though histopathology is definitive.
            """
        )
        tumor_grade = st.selectbox("Select WHO Tumor Grade", ["I", "II", "III", "IV"])
        st.write(f"**WHO Brain Tumor Grade Selected:** {tumor_grade}")
        if tumor_grade == "I":
            analysis = "Typically benign with an excellent prognosis."
            next_steps = "Plan for surgical resection if indicated; follow up with histopathology."
        elif tumor_grade == "II":
            analysis = "Low-grade tumor; usually slow-growing."
            next_steps = "Consider surgical resection and close radiological follow-up."
        elif tumor_grade == "III":
            analysis = "Anaplastic tumor; requires aggressive treatment."
            next_steps = "Recommend multimodality therapy including surgery, radiotherapy, and possibly chemotherapy."
        else:
            analysis = "High-grade tumor; poor prognosis."
            next_steps = "Urgent oncologic management with aggressive therapy is indicated."
        st.markdown(f"**Analysis:** {analysis}")
        st.markdown(f"**Next Steps:** {next_steps}")
        
    # ------------------------------
    # Modified Rankin Scale (mRS)
    # ------------------------------
    elif neuro_option == "Modified Rankin Scale (mRS)":
        st.subheader("Modified Rankin Scale (mRS)")
        st.markdown(
            """
            **Overview:**  
            A clinical outcome measure (0–6) that correlates with stroke severity and imaging findings.
            """
        )
        mrs = st.selectbox("Select mRS Score", [0, 1, 2, 3, 4, 5, 6])
        st.write(f"**mRS Score Selected:** {mrs}")
        if mrs == 0:
            analysis = "No symptoms present."
            next_steps = "Continue routine care; no rehabilitation needed."
        elif mrs == 1:
            analysis = "Minor symptoms without significant disability."
            next_steps = "Standard post-stroke management and follow-up."
        elif mrs == 2:
            analysis = "Slight disability; patient can perform most activities."
            next_steps = "Consider outpatient rehabilitation to optimize recovery."
        elif mrs == 3:
            analysis = "Moderate disability; assistance required for some activities."
            next_steps = "Initiate structured rehabilitation and supportive care."
        elif mrs == 4:
            analysis = "Moderately severe disability; significant help needed."
            next_steps = "Plan for inpatient rehabilitation and long-term support."
        elif mrs == 5:
            analysis = "Severe disability; patient is bedridden."
            next_steps = "Comprehensive rehabilitation and caregiver support are essential."
        else:
            analysis = "Patient is deceased."
            next_steps = "Focus on palliative care and family counseling."
        st.markdown(f"**Analysis:** {analysis}")
        st.markdown(f"**Next Steps:** {next_steps}")
        
    # ------------------------------
    # Fazekas Scale for White Matter Lesions
    # ------------------------------
    elif neuro_option == "Fazekas Scale for WM Lesions":
        st.subheader("Fazekas Scale for White Matter Lesions")
        st.markdown(
            """
            **Overview:**  
            Quantifies white matter hyperintensities (WMH) seen on T2/FLAIR MRI:
            - **Periventricular WMH:** Score 0 (none) to 3 (extensive)
            - **Deep WMH:** Score 0 (none) to 3 (large confluent areas)
            """
        )
        pv_score = st.selectbox("Periventricular Lesions Score", [0, 1, 2, 3])
        dwm_score = st.selectbox("Deep White Matter Lesions Score", [0, 1, 2, 3])
        st.write(f"**Fazekas Score:** Periventricular = {pv_score}, Deep WM = {dwm_score}")
        analysis = (f"A periventricular score of {pv_score} and a deep white matter score of {dwm_score} indicate the extent of small vessel disease.")
        next_steps = "Manage vascular risk factors; consider further evaluation if scores are high."
        st.markdown(f"**Analysis:** {analysis}")
        st.markdown(f"**Next Steps:** {next_steps}")
        
    # ------------------------------
    # Spine Classifications
    # ------------------------------
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
                Classifies traumatic vertebral fractures based on morphology and stability.
                """
            )
            ao_type = st.selectbox("Select AO Fracture Type", ["A", "B", "C"])
            st.write(f"**AO Spine Fracture Type Selected:** {ao_type}")
            if ao_type == "A":
                analysis = "Compression-type fracture; generally stable."
                next_steps = "Conservative management or surgical fixation based on clinical assessment."
            elif ao_type == "B":
                analysis = "Distraction injury; potential instability."
                next_steps = "Surgical consultation for possible stabilization is recommended."
            else:
                analysis = "Rotational injury; high instability risk."
                next_steps = "Urgent surgical evaluation is needed."
            st.markdown(f"**Analysis:** {analysis}")
            st.markdown(f"**Next Steps:** {next_steps}")
        elif spine_option == "TLICS (Thoracolumbar Injury)":
            st.subheader("TLICS – Thoracolumbar Injury Classification & Severity Score")
            st.markdown(
                """
                **Overview:**  
                Assesses injury morphology, ligamentous integrity, and neurological status.
                """
            )
            tlics_score = st.number_input("Enter TLICS Score", min_value=0, max_value=20, value=4)
            st.write(f"**TLICS Score:** {tlics_score}")
            analysis = f"A TLICS Score of {tlics_score} suggests that scores above 7 often favor surgical management."
            next_steps = "If the score is high, consult spine surgery; if low, consider conservative management."
            st.markdown(f"**Analysis:** {analysis}")
            st.markdown(f"**Next Steps:** {next_steps}")
        elif spine_option == "Modic (Vertebral Endplate Changes)":
            st.subheader("Modic Classification (Vertebral Endplate Changes)")
            st.markdown(
                """
                **Overview:**  
                Assesses signal changes on MRI adjacent to disc endplates:
                - **Type 1:** Edema/inflammation  
                - **Type 2:** Fatty degeneration  
                - **Type 3:** Sclerosis
                """
            )
            modic_type = st.selectbox("Select Modic Type", ["Type 1", "Type 2", "Type 3"])
            st.write(f"**Modic Type Selected:** {modic_type}")
            if modic_type == "Type 1":
                analysis = "Active inflammation is present."
                next_steps = "Consider anti-inflammatory treatment and further evaluation if symptoms persist."
            elif modic_type == "Type 2":
                analysis = "Chronic fatty degeneration noted."
                next_steps = "Manage conservatively with physical therapy and risk factor modification."
            else:
                analysis = "Sclerotic changes indicate advanced degeneration."
                next_steps = "Evaluate for surgical intervention if associated with instability or neural compression."
            st.markdown(f"**Analysis:** {analysis}")
            st.markdown(f"**Next Steps:** {next_steps}")
        elif spine_option == "Pfirrmann (Disc Degeneration)":
            st.subheader("Pfirrmann Classification (Intervertebral Disc Degeneration)")
            st.markdown(
                """
                **Overview:**  
                Uses T2-weighted MRI to grade disc degeneration from I (normal) to V (severe degeneration).
                """
            )
            pf_grade = st.selectbox("Select Pfirrmann Grade", [1, 2, 3, 4, 5])
            st.write(f"**Pfirrmann Grade Selected:** {pf_grade}")
            analysis = f"Grade {pf_grade} indicates the severity of disc degeneration; higher grades suggest loss of disc height and structure."
            next_steps = "Consider conservative management (physical therapy, pain management) for lower grades; higher grades may need surgical evaluation."
            st.markdown(f"**Analysis:** {analysis}")
            st.markdown(f"**Next Steps:** {next_steps}")
            
    # ------------------------------
    # Scheltens Score (Temporal Lobe Atrophy)
    # ------------------------------
    elif neuro_option == "Scheltens Score (Temporal Lobe Atrophy)":
        st.subheader("Scheltens Score for Temporal Lobe Atrophy (MTA Score)")
        st.markdown(
            """
            **Overview:**  
            Assessed on coronal T1 MRI at the level of the hippocampus. Scores range from 0 (no atrophy) to 4 (severe atrophy).
            """
        )
        age = st.number_input("Patient Age (years)", min_value=18, max_value=120, value=60)
        scheltens = st.selectbox("Select Scheltens Score", [0, 1, 2, 3, 4])
        st.write(f"**Scheltens Score Selected:** {scheltens}")
        if age < 75:
            abnormal = scheltens >= 2
        else:
            abnormal = scheltens >= 3
        analysis = f"For a {age}-year-old, a Scheltens score of {scheltens} is " + ("abnormal." if abnormal else "within normal limits.")
        next_steps = "If abnormal, consider evaluation for neurodegenerative disorders and correlate with clinical findings."
        st.markdown(f"**Analysis:** {analysis}")
        st.markdown(f"**Next Steps:** {next_steps}")

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
        st.markdown("Assesses tumor extent (T), nodal involvement (N), and metastasis (M).")
        T = st.number_input("Enter Tumor (T) Stage", min_value=0, max_value=4, value=2)
        N = st.number_input("Enter Node (N) Stage", min_value=0, max_value=3, value=1)
        M = st.selectbox("Select Metastasis (M) Stage", ["0", "1"])
        st.write(f"**TNM Staging:** T{T} N{N} M{M}")
        analysis = "Higher T, N, or M values indicate more advanced disease."
        next_steps = "Recommend biopsy confirmation, followed by multidisciplinary treatment planning (surgery, radiation, and/or chemotherapy)."
        st.markdown(f"**Analysis:** {analysis}")
        st.markdown(f"**Next Steps:** {next_steps}")
    elif head_neck == "Lugano Classification (Lymphoma)":
        st.subheader("Lugano Classification (Lymphoma)")
        st.markdown("Stages lymphoma based on nodal and extranodal involvement using PET-CT findings.")
        lugano_stage = st.selectbox("Select Lugano Stage", ["I", "II", "III", "IV"])
        st.write(f"**Lugano Stage Selected:** {lugano_stage}")
        analysis = f"Stage {lugano_stage} reflects the extent of lymphoma involvement."
        next_steps = "Based on staging, consider appropriate chemotherapeutic regimens and monitor response with serial imaging."
        st.markdown(f"**Analysis:** {analysis}")
        st.markdown(f"**Next Steps:** {next_steps}")
    elif head_neck == "Friedman Staging for Tonsillar Hypertrophy":
        st.subheader("Friedman Staging for Tonsillar Hypertrophy")
        st.markdown("Assesses the degree of tonsillar hypertrophy and its impact on the airway.")
        friedman = st.selectbox("Select Friedman Stage", ["1", "2", "3", "4"])
        st.write(f"**Friedman Stage Selected:** {friedman}")
        analysis = f"Stage {friedman} indicates increasing severity of tonsillar enlargement."
        next_steps = "If severe, consider evaluation for adenotonsillectomy and airway management strategies."
        st.markdown(f"**Analysis:** {analysis}")
        st.markdown(f"**Next Steps:** {next_steps}")

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
                **Overview:**  
                - **Type A:** Involves the ascending aorta (surgical emergency).  
                - **Type B:** Confined to the descending aorta.
                """
            )
            stanford_type = st.selectbox("Select Stanford Type", ["Type A", "Type B"])
            st.write(f"**Stanford Type Selected:** {stanford_type}")
            analysis = f"Stanford {stanford_type} dissection is critical; Type A requires urgent surgical repair."
            next_steps = ("For Type A, arrange immediate surgical consultation. For Type B, manage medically with blood pressure control and monitoring.")
            st.markdown(f"**Analysis:** {analysis}")
            st.markdown(f"**Next Steps:** {next_steps}")
        elif dissection_sys == "DeBakey":
            st.subheader("DeBakey Classification (Aortic Dissection)")
            st.markdown(
                """
                **Overview:**  
                - **Type I:** Ascending aorta to beyond the arch.  
                - **Type II:** Confined to the ascending aorta.  
                - **Type III:** Originates in the descending aorta.
                """
            )
            debakey_type = st.selectbox("Select DeBakey Type", ["Type I", "Type II", "Type III"])
            st.write(f"**DeBakey Type Selected:** {debakey_type}")
            analysis = f"DeBakey {debakey_type} dissection indicates the anatomic extent; Types I and II are particularly concerning."
            next_steps = "Urgent cardiothoracic consultation is needed for Types I and II, while Type III may be managed medically."
            st.markdown(f"**Analysis:** {analysis}")
            st.markdown(f"**Next Steps:** {next_steps}")
            
    elif cardio_option == "Pulmonary Embolism (Qanadli Score)":
        st.subheader("Qanadli Score (Pulmonary Embolism)")
        st.markdown(
            """
            **Overview:**  
            Assesses clot burden on CT pulmonary angiography by scoring 20 segmental arteries:
            - 1 point for partial occlusion  
            - 2 points for complete occlusion  
            Maximum score = 40.
            """
        )
        partial = st.number_input("Number of Partially Occluded Segmental Arteries", min_value=0, max_value=20, value=0)
        complete = st.number_input("Number of Completely Occluded Segmental Arteries", min_value=0, max_value=20, value=0)
        qanadli_score = partial * 1 + complete * 2
        st.write(f"**Calculated Qanadli Score:** {qanadli_score} / 40")
        analysis = f"A Qanadli score of {qanadli_score} indicates a " + \
                   ("high" if qanadli_score > 20 else "moderate" if qanadli_score > 10 else "low") + \
                   " clot burden."
        next_steps = "In high-score cases, consider thrombolytic therapy and close hemodynamic monitoring."
        st.markdown(f"**Analysis:** {analysis}")
        st.markdown(f"**Next Steps:** {next_steps}")
        
    elif cardio_option == "Lung & Pleura":
        lung_pleura = st.sidebar.selectbox(
            "Select a Lung & Pleura Classification", 
            ["Lung-RADS", "COVID-19 Chest Imaging (RSNA)", "Light’s Criteria (Pleural Effusion)", "ATS/ERS Classification (Idiopathic Interstitial Pneumonias)"]
        )
        if lung_pleura == "Lung-RADS":
            st.subheader("Lung-RADS")
            st.markdown("Used for lung cancer screening on low-dose CT; categories guide follow-up.")
            lung_rads = st.selectbox("Select Lung-RADS Category", ["0", "1", "2", "3", "4A", "4B", "4X"])
            st.write(f"**Lung-RADS Category Selected:** {lung_rads}")
            analysis = f"Lung-RADS {lung_rads} suggests that higher categories are associated with increased malignancy risk."
            next_steps = "For categories 3 and above, consider short-term follow-up imaging and, if indicated, biopsy."
            st.markdown(f"**Analysis:** {analysis}")
            st.markdown(f"**Next Steps:** {next_steps}")
        elif lung_pleura == "COVID-19 Chest Imaging (RSNA)":
            st.subheader("RSNA COVID-19 Chest Imaging Classification")
            st.markdown(
                """
                **Overview:**  
                Classifies CT findings as Typical, Indeterminate, Atypical, or Negative for COVID-19 pneumonia.
                """
            )
            covid_class = st.selectbox("Select RSNA Category", ["Typical", "Indeterminate", "Atypical", "Negative"])
            st.write(f"**RSNA Category Selected:** {covid_class}")
            if covid_class == "Typical":
                analysis = "Findings are highly suggestive of COVID-19 pneumonia."
                next_steps = "Advise RT-PCR testing and initiate isolation protocols."
            elif covid_class == "Indeterminate":
                analysis = "Findings are non-specific."
                next_steps = "Correlate with clinical history and laboratory tests; consider repeat imaging."
            elif covid_class == "Atypical":
                analysis = "Findings are unusual for COVID-19."
                next_steps = "Evaluate for alternative diagnoses."
            else:
                analysis = "No imaging evidence of COVID-19 pneumonia."
                next_steps = "Continue standard care."
            st.markdown(f"**Analysis:** {analysis}")
            st.markdown(f"**Next Steps:** {next_steps}")
        elif lung_pleura == "Light’s Criteria (Pleural Effusion)":
            st.subheader("Light’s Criteria (Pleural Effusion)")
            st.markdown(
                """
                **Overview:**  
                Though primarily lab-based, imaging findings (e.g., septations) can support the evaluation.
                """
            )
            protein_ratio = st.number_input("Pleural fluid protein / Serum protein ratio", min_value=0.0, value=0.5)
            ldh_ratio = st.number_input("Pleural fluid LDH / Serum LDH ratio", min_value=0.0, value=1.0)
            st.write(f"**Protein Ratio:** {protein_ratio} | **LDH Ratio:** {ldh_ratio}")
            analysis = "These ratios help differentiate exudative from transudative effusions."
            next_steps = "Combine with clinical data to guide management; exudative effusions may require drainage and further workup."
            st.markdown(f"**Analysis:** {analysis}")
            st.markdown(f"**Next Steps:** {next_steps}")
        elif lung_pleura == "ATS/ERS Classification (Idiopathic Interstitial Pneumonias)":
            st.subheader("ATS/ERS Classification")
            st.markdown("Categorizes interstitial lung disease patterns on HRCT.")
            pattern = st.selectbox("Select HRCT Pattern", ["UIP", "NSIP", "COP", "Other"])
            st.write(f"**Selected Pattern:** {pattern}")
            analysis = f"The pattern '{pattern}' helps narrow the differential for interstitial lung disease."
            next_steps = "Correlate with clinical and laboratory findings; consider lung biopsy if diagnosis remains uncertain."
            st.markdown(f"**Analysis:** {analysis}")
            st.markdown(f"**Next Steps:** {next_steps}")
            
    elif cardio_option == "Breast (BI-RADS)":
        st.subheader("BI-RADS (Breast Imaging Reporting & Data System)")
        st.markdown(
            """
            **Overview (ACR BI-RADS):**  
            Categorizes breast findings:
            - 0: Incomplete  
            - 1: Negative  
            - 2: Benign  
            - 3: Probably benign  
            - 4: Suspicious (4A, 4B, 4C)  
            - 5: Highly suspicious  
            - 6: Known malignancy
            """
        )
        birads = st.selectbox("Select BI-RADS Category", [0, 1, 2, 3, 4, 5, 6])
        st.write(f"**BI-RADS Category Selected:** {birads}")
        if birads == 0:
            analysis = "Incomplete study; further imaging is required."
            next_steps = "Obtain additional views or modalities."
        elif birads == 1:
            analysis = "Negative; no abnormalities detected."
            next_steps = "Continue routine screening."
        elif birads == 2:
            analysis = "Benign findings; no intervention needed."
            next_steps = "Maintain routine follow-up."
        elif birads == 3:
            analysis = "Probably benign; low risk for malignancy."
            next_steps = "Recommend short-term follow-up imaging."
        elif birads == 4:
            analysis = ("Suspicious abnormality; consider biopsy. " 
                        "Subclassification (4A, 4B, 4C) can further refine risk.")
            next_steps = "Arrange tissue sampling for definitive diagnosis."
        elif birads == 5:
            analysis = "Highly suggestive of malignancy."
            next_steps = "Immediate biopsy and oncologic evaluation are indicated."
        else:
            analysis = "Known malignancy; imaging used for treatment planning."
            next_steps = "Coordinate with oncology for further management."
        st.markdown(f"**Analysis:** {analysis}")
        st.markdown(f"**Next Steps:** {next_steps}")

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
        Grades injury severity based on CT/operative findings.
        """)
        injury_grade = st.selectbox("Select Injury Grade", ["I", "II", "III", "IV", "V"])
        st.write(f"**{organ} Injury Grade Selected:** {injury_grade}")
        analysis = f"Grade {injury_grade} indicates increasing injury severity in the {organ}."
        next_steps = "For high-grade injuries (IV–V), urgent surgical evaluation is recommended."
        st.markdown(f"**Analysis:** {analysis}")
        st.markdown(f"**Next Steps:** {next_steps}")
        
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
                Evaluates liver lesions in high-risk patients using CT/MRI features.
                """
            )
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
            analysis = f"LI-RADS {li_category} indicates an increasing likelihood of HCC."
            next_steps = "For LR-4 lesions, recommend biopsy and multidisciplinary evaluation."
            st.markdown(f"**Analysis:** {analysis}")
            st.markdown(f"**Next Steps:** {next_steps}")
            
        elif abdo_class == "Bosniak Classification (Kidney/Adrenal)":
            st.subheader("Bosniak Classification (Renal Cysts)")
            bosniak = st.selectbox("Select Bosniak Category", ["I", "II", "IIF", "III", "IV"])
            st.write(f"**Bosniak Category Selected:** {bosniak}")
            analysis = ("Bosniak I and II are benign; IIF requires follow-up; III and IV have increased malignancy risk.")
            next_steps = "For Bosniak III/IV, consider surgical evaluation and possible resection."
            st.markdown(f"**Analysis:** {analysis}")
            st.markdown(f"**Next Steps:** {next_steps}")
            
        elif abdo_class == "Balthazar Grade (Pancreas)":
            st.subheader("Balthazar Grade (Acute Pancreatitis)")
            balthazar = st.selectbox("Select Balthazar Grade", ["A", "B", "C", "D", "E"])
            st.write(f"**Balthazar Grade Selected:** {balthazar}")
            analysis = f"Balthazar Grade {balthazar} reflects the severity of pancreatitis; higher grades indicate more extensive inflammatory changes."
            next_steps = "Manage pancreatitis supportively and monitor for complications; severe cases may require ICU care."
            st.markdown(f"**Analysis:** {analysis}")
            st.markdown(f"**Next Steps:** {next_steps}")
            
        elif abdo_class == "CT Severity Index (Pancreatitis)":
            st.subheader("CT Severity Index (CTSI) for Pancreatitis")
            ctsi = st.number_input("Enter CTSI Score (0-10)", min_value=0, max_value=10, value=4)
            st.write(f"**CT Severity Index:** {ctsi}")
            if ctsi <= 3:
                severity = "mild"
            elif ctsi <= 6:
                severity = "moderate"
            else:
                severity = "severe"
            analysis = f"A CTSI score of {ctsi} suggests {severity} pancreatitis."
            next_steps = "Monitor closely and consider intensive care for severe cases."
            st.markdown(f"**Analysis:** {analysis}")
            st.markdown(f"**Next Steps:** {next_steps}")
            
        elif abdo_class == "PI-RADS (Prostate)":
            st.subheader("PI-RADS (Prostate Imaging Reporting and Data System)")
            pi_findings = st.multiselect(
                "Select Prostate Findings", 
                ["Low signal intensity on T2", "Restricted diffusion", "Early enhancement"]
            )
            pi_score = 4 if "Restricted diffusion" in pi_findings else 2
            st.write(f"**PI-RADS Score Estimated:** {pi_score}")
            analysis = f"A PI-RADS score of {pi_score} suggests a {'high' if pi_score >= 4 else 'low'} likelihood of clinically significant prostate cancer."
            next_steps = "For higher scores, recommend prostate biopsy and urology consultation."
            st.markdown(f"**Analysis:** {analysis}")
            st.markdown(f"**Next Steps:** {next_steps}")
            
        elif abdo_class == "O-RADS (Ovarian/Adnexal)":
            st.subheader("O-RADS (Ovarian-Adnexal Imaging Reporting and Data System)")
            orads = st.selectbox("Select O-RADS Category", ["0", "1", "2", "3", "4", "5"])
            st.write(f"**O-RADS Category Selected:** {orads}")
            analysis = f"O-RADS {orads} stratifies the risk of ovarian malignancy."
            next_steps = "For lesions with high O-RADS scores, consider surgical evaluation and possible biopsy."
            st.markdown(f"**Analysis:** {analysis}")
            st.markdown(f"**Next Steps:** {next_steps}")
            
        elif abdo_class == "TI-RADS (Thyroid)":
            st.subheader("TI-RADS (Thyroid Imaging Reporting and Data System)")
            tirads = st.selectbox("Select TI-RADS Category", ["TR1", "TR2", "TR3", "TR4", "TR5"])
            st.write(f"**TI-RADS Category Selected:** {tirads}")
            analysis = f"TI-RADS {tirads} helps determine the need for a thyroid nodule biopsy."
            next_steps = "Nodules in TR4 or TR5 should be considered for fine-needle aspiration biopsy."
            st.markdown(f"**Analysis:** {analysis}")
            st.markdown(f"**Next Steps:** {next_steps}")
            
        elif abdo_class == "FIGO Staging (Uterus & Cervix)":
            st.subheader("FIGO Staging (Gynecologic Cancers)")
            figo = st.selectbox("Select FIGO Stage", ["I", "II", "III", "IV"])
            st.write(f"**FIGO Stage Selected:** {figo}")
            analysis = f"FIGO Stage {figo} reflects the extent of tumor spread in gynecologic cancers."
            next_steps = "Coordinate with oncology for a tailored treatment plan including surgery, radiation, and/or chemotherapy."
            st.markdown(f"**Analysis:** {analysis}")
            st.markdown(f"**Next Steps:** {next_steps}")

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
            "Magerl Classification (Thoracolumbar Fractures)",
            "Other Fracture Classifications"
        ]
    )
    if msk_option == "AO/OTA Fracture Classification (Long Bones)":
        st.subheader("AO/OTA Fracture Classification")
        st.markdown("Assesses fracture pattern (e.g., simple, wedge, complex) based on bone segment and articular involvement.")
        fracture_type = st.selectbox("Select Fracture Pattern", ["Simple", "Wedge", "Complex"])
        st.write(f"**Fracture Pattern Selected:** {fracture_type}")
        analysis = f"A {fracture_type.lower()} fracture typically guides treatment toward conservative or operative management."
        next_steps = "Evaluate stability; consult orthopedics for surgical fixation if indicated."
        st.markdown(f"**Analysis:** {analysis}")
        st.markdown(f"**Next Steps:** {next_steps}")
        
    elif msk_option == "Gustilo–Anderson (Open Fractures)":
        st.subheader("Gustilo–Anderson Classification (Open Fractures)")
        st.markdown(
            """
            **Overview:**  
            Grades open fractures by wound size and soft tissue injury.
            - Type I: Clean wound <1 cm  
            - Type II: Wound 1–10 cm  
            - Type III: Wound >10 cm or severe soft tissue injury
            """
        )
        gustilo = st.selectbox("Select Gustilo–Anderson Type", ["I", "II", "III"])
        st.write(f"**Gustilo–Anderson Type Selected:** {gustilo}")
        analysis = f"Type {gustilo} open fractures indicate increasing severity and infection risk."
        next_steps = "For Type III injuries, urgent surgical debridement and stabilization are required."
        st.markdown(f"**Analysis:** {analysis}")
        st.markdown(f"**Next Steps:** {next_steps}")
        
    elif msk_option == "Tscherne Classification (Soft Tissue Injuries)":
        st.subheader("Tscherne Classification (Soft Tissue Injuries)")
        st.markdown("Evaluates the severity of soft tissue damage associated with fractures.")
        tscherne = st.selectbox("Select Tscherne Grade", ["I", "II", "III", "IV"])
        st.write(f"**Tscherne Grade Selected:** {tscherne}")
        analysis = f"Tscherne Grade {tscherne} correlates with soft tissue injury severity."
        next_steps = "Higher grades may require surgical debridement and specialized wound care."
        st.markdown(f"**Analysis:** {analysis}")
        st.markdown(f"**Next Steps:** {next_steps}")
        
    elif msk_option == "Salter-Harris (Physeal Fractures)":
        st.subheader("Salter-Harris Classification (Pediatric)")
        st.markdown("Grades growth plate injuries (Types I–V).")
        sh_type = st.selectbox("Select Salter-Harris Type", ["I", "II", "III", "IV", "V"])
        st.write(f"**Salter-Harris Type Selected:** {sh_type}")
        analysis = f"Type {sh_type} fractures involve progressively more damage to the growth plate."
        next_steps = "Consult pediatric orthopedics; higher types may affect future bone growth."
        st.markdown(f"**Analysis:** {analysis}")
        st.markdown(f"**Next Steps:** {next_steps}")
        
    elif msk_option == "Magerl Classification (Thoracolumbar Fractures)":
        st.subheader("Magerl Classification (Thoracolumbar Fractures)")
        st.markdown(
            """
            **Overview:**  
            Classifies thoracolumbar fractures based on CT findings:
            - Type A (Compression): A1 (impaction), A2 (split), A3 (burst)
            - Type B (Distraction): B1 (ligamentous), B2 (osseous), B3 (disc disruption)
            - Type C (Rotation): Various rotational injuries
            """
        )
        magerl_main = st.selectbox("Select Magerl Main Type", ["A (Compression)", "B (Distraction)", "C (Rotation)"])
        if magerl_main.startswith("A"):
            subtype = st.selectbox("Select Subtype", ["A1: Impaction", "A2: Split", "A3: Burst"])
        elif magerl_main.startswith("B"):
            subtype = st.selectbox("Select Subtype", ["B1: Ligamentous", "B2: Osseous", "B3: Disc (Hyperextension-Shear)"])
        else:
            subtype = st.selectbox("Select Subtype", ["C1: Compression with Rotation", "C2: Distraction with Rotation", "C3: Rotational-shear"])
        st.write(f"**Magerl Classification Selected:** {magerl_main} – {subtype}")
        analysis = f"The Magerl classification {magerl_main} with subtype {subtype} indicates the mechanism of injury."
        next_steps = "Based on fracture stability and patient factors, decide between conservative management and surgical fixation."
        st.markdown(f"**Analysis:** {analysis}")
        st.markdown(f"**Next Steps:** {next_steps}")
        
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
            st.markdown(
                """
                **Overview:**  
                Evaluates displacement of femoral neck fractures:
                - Type 1: Incomplete, valgus impacted  
                - Type 2: Complete, non-displaced  
                - Type 3: Partially displaced  
                - Type 4: Completely displaced
                """
            )
            garden = st.selectbox("Select Garden Type", ["1", "2", "3", "4"])
            st.write(f"**Garden Type Selected:** {garden}")
            analysis = f"Garden Type {garden} indicates the degree of displacement and risk of avascular necrosis."
            next_steps = "For higher Garden types, consider surgical fixation or arthroplasty."
            st.markdown(f"**Analysis:** {analysis}")
            st.markdown(f"**Next Steps:** {next_steps}")
        elif fracture_sys == "Pauwels (Femoral Neck)":
            st.subheader("Pauwels Classification (Femoral Neck Fractures)")
            pauwels = st.selectbox("Select Pauwels Type", ["I", "II", "III"])
            st.write(f"**Pauwels Type Selected:** {pauwels}")
            analysis = f"Pauwels Type {pauwels} describes the fracture angle; higher angles (Type III) suggest greater shear forces."
            next_steps = "Surgical fixation is often indicated for high-angle (Type III) fractures."
            st.markdown(f"**Analysis:** {analysis}")
            st.markdown(f"**Next Steps:** {next_steps}")
        elif fracture_sys == "Neer (Proximal Humerus)":
            st.subheader("Neer Classification (Proximal Humerus Fractures)")
            neer = st.selectbox("Select Neer Classification", ["One-Part", "Two-Part", "Three-Part", "Four-Part"])
            st.write(f"**Neer Classification Selected:** {neer}")
            analysis = f"The Neer classification '{neer}' indicates the number of displaced segments."
            next_steps = "More complex fractures (three- or four-part) usually require surgical intervention."
            st.markdown(f"**Analysis:** {analysis}")
            st.markdown(f"**Next Steps:** {next_steps}")
        elif fracture_sys == "Weber (Ankle)":
            st.subheader("Weber Classification (Ankle Fractures)")
            weber = st.selectbox("Select Weber Type", ["A", "B", "C"])
            st.write(f"**Weber Type Selected:** {weber}")
            analysis = f"Weber Type {weber} indicates the level of the fibular fracture; Type C is typically associated with syndesmotic injury."
            next_steps = "Evaluate for ligamentous injury; Type C fractures often require surgical stabilization."
            st.markdown(f"**Analysis:** {analysis}")
            st.markdown(f"**Next Steps:** {next_steps}")
        elif fracture_sys == "Lauge-Hansen (Ankle)":
            st.subheader("Lauge-Hansen Classification (Ankle Fractures)")
            lh = st.selectbox("Select Mechanism", ["Supination-External Rotation", "Pronation-External Rotation", "Supination-Adduction", "Pronation-Abduction"])
            st.write(f"**Lauge-Hansen Mechanism Selected:** {lh}")
            analysis = f"The mechanism '{lh}' helps predict fracture pattern and ligamentous injury."
            next_steps = "Use this information to plan reduction and possible surgical fixation."
            st.markdown(f"**Analysis:** {analysis}")
            st.markdown(f"**Next Steps:** {next_steps}")
        elif fracture_sys == "Frykman (Distal Radius)":
            st.subheader("Frykman Classification (Distal Radius Fractures)")
            frykman = st.selectbox("Select Frykman Type", ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"])
            st.write(f"**Frykman Type Selected:** {frykman}")
            analysis = f"Frykman Type {frykman} takes into account involvement of the radiocarpal and distal radioulnar joints."
            next_steps = "Higher Frykman types may require operative management."
            st.markdown(f"**Analysis:** {analysis}")
            st.markdown(f"**Next Steps:** {next_steps}")
        elif fracture_sys == "Sanders (Calcaneal)":
            st.subheader("Sanders Classification (Calcaneal Fractures)")
            sanders = st.selectbox("Select Sanders Type", ["I", "II", "III", "IV"])
            st.write(f"**Sanders Type Selected:** {sanders}")
            analysis = f"Sanders Type {sanders} is based on CT evaluation of the posterior facet; higher types suggest more comminution."
            next_steps = "Surgical fixation is often indicated for Sanders III and IV fractures."
            st.markdown(f"**Analysis:** {analysis}")
            st.markdown(f"**Next Steps:** {next_steps}")
        elif fracture_sys == "Mayo (Olecranon)":
            st.subheader("Mayo Classification (Olecranon Fractures)")
            mayo = st.selectbox("Select Mayo Type", ["Stable", "Unstable"])
            st.write(f"**Mayo Classification Selected:** {mayo}")
            analysis = f"{mayo} olecranon fractures indicate the stability of the fracture."
            next_steps = "Unstable fractures typically require surgical fixation."
            st.markdown(f"**Analysis:** {analysis}")
            st.markdown(f"**Next Steps:** {next_steps}")

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
            Grades reperfusion after stroke intervention from 0 (no perfusion) to 3 (complete perfusion).
            """
        )
        tici = st.selectbox("Select TICI Grade", ["0", "1", "2a", "2b", "3"])
        st.write(f"**TICI Grade Selected:** {tici}")
        analysis = f"TICI Grade {tici} reflects the degree of reperfusion achieved."
        next_steps = "If reperfusion is suboptimal (grades 0–2), consider additional thrombectomy or medical management."
        st.markdown(f"**Analysis:** {analysis}")
        st.markdown(f"**Next Steps:** {next_steps}")
    elif vascular_option == "Hamburg Classification (Vascular Malformations)":
        st.subheader("Hamburg Classification")
        st.markdown(
            """
            **Overview:**  
            Categorizes vascular malformations based on flow dynamics and embryologic origin.
            """
        )
        hamburg = st.selectbox("Select Hamburg Type", ["Type I", "Type II", "Type III"])
        st.write(f"**Hamburg Classification Selected:** {hamburg}")
        analysis = f"Type {hamburg} vascular malformations help determine the treatment approach."
        next_steps = "Treatment options may include sclerotherapy, embolization, or surgical resection."
        st.markdown(f"**Analysis:** {analysis}")
        st.markdown(f"**Next Steps:** {next_steps}")
    elif vascular_option == "VARC Criteria for TAVR Outcomes":
        st.subheader("VARC Criteria")
        st.markdown(
            """
            **Overview:**  
            Evaluates outcomes of transcatheter aortic valve replacement (TAVR) across several domains.
            """
        )
        varc = st.selectbox("Select VARC Outcome Category", ["Device Success", "Early Safety", "Clinical Efficacy"])
        st.write(f"**VARC Outcome Category Selected:** {varc}")
        analysis = f"The selected VARC outcome '{varc}' provides insight into the procedural success and potential complications."
        next_steps = "Ensure multidisciplinary follow-up to address any complications and optimize valve performance."
        st.markdown(f"**Analysis:** {analysis}")
        st.markdown(f"**Next Steps:** {next_steps}")

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
        st.subheader("ACR BI-RADS")
        st.markdown(
            """
            **Overview:**  
            Standardizes breast imaging reporting into categories from 0 (incomplete) to 6 (known malignancy).
            """
        )
        birads_rads = st.selectbox("Select BI-RADS Category", [0, 1, 2, 3, 4, 5, 6])
        st.write(f"**BI-RADS Category Selected:** {birads_rads}")
        if birads_rads == 0:
            analysis = "Incomplete study; additional imaging is necessary."
            next_steps = "Obtain supplemental imaging to complete the assessment."
        elif birads_rads == 1:
            analysis = "Negative; no abnormalities detected."
            next_steps = "Continue routine screening."
        elif birads_rads == 2:
            analysis = "Benign findings; no further intervention required."
            next_steps = "Schedule routine follow-up exams."
        elif birads_rads == 3:
            analysis = "Probably benign; low likelihood of malignancy."
            next_steps = "Recommend short-term follow-up imaging."
        elif birads_rads == 4:
            analysis = ("Suspicious abnormality detected; consider biopsy. " 
                        "Subclassification into 4A, 4B, or 4C may help refine risk.")
            next_steps = "Arrange tissue sampling for definitive diagnosis."
        elif birads_rads == 5:
            analysis = "Findings are highly suggestive of malignancy."
            next_steps = "Immediate biopsy and oncologic evaluation are indicated."
        else:
            analysis = "Biopsy-proven malignancy; imaging is used for treatment planning."
            next_steps = "Coordinate with oncology for further management."
        st.markdown(f"**Analysis:** {analysis}")
        st.markdown(f"**Next Steps:** {next_steps}")
    elif rads_option == "Lung-RADS (Lung)":
        st.subheader("Lung-RADS")
        st.markdown("Used for lung cancer screening; higher categories indicate higher malignancy risk.")
        lung_rads = st.selectbox("Select Lung-RADS Category", ["0", "1", "2", "3", "4A", "4B", "4X"])
        st.write(f"**Lung-RADS Category Selected:** {lung_rads}")
        analysis = f"Lung-RADS {lung_rads} directs follow-up intensity; lesions in higher categories require urgent evaluation."
        next_steps = "Recommend follow-up CT imaging and, if indicated, biopsy for suspicious lesions."
        st.markdown(f"**Analysis:** {analysis}")
        st.markdown(f"**Next Steps:** {next_steps}")
    elif rads_option == "LI-RADS (Liver)":
        st.subheader("LI-RADS")
        st.markdown("Evaluates liver lesions in at-risk patients based on CT/MRI features.")
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
        analysis = f"LI-RADS {li_category} suggests an increasing probability of HCC."
        next_steps = "For LR-4/5 lesions, consider further evaluation with biopsy or surgical consultation."
        st.markdown(f"**Analysis:** {analysis}")
        st.markdown(f"**Next Steps:** {next_steps}")
    elif rads_option == "PI-RADS (Prostate)":
        st.subheader("PI-RADS")
        st.markdown("Assesses prostate lesions on multiparametric MRI on a scale of 1–5.")
        pi_findings = st.multiselect(
            "Select Prostate Findings", 
            ["Low signal intensity on T2", "Restricted diffusion", "Early enhancement"]
        )
        pi_score = 4 if "Restricted diffusion" in pi_findings else 2
        st.write(f"**PI-RADS Score Estimated:** {pi_score}")
        analysis = f"A PI-RADS score of {pi_score} suggests a {'high' if pi_score >= 4 else 'low'} risk for clinically significant prostate cancer."
        next_steps = "For high scores, recommend prostate biopsy and urology consultation."
        st.markdown(f"**Analysis:** {analysis}")
        st.markdown(f"**Next Steps:** {next_steps}")
    elif rads_option == "TI-RADS (Thyroid)":
        st.subheader("TI-RADS")
        st.markdown("Standardizes thyroid nodule evaluation on ultrasound; higher categories indicate increased suspicion for malignancy.")
        ti_rads = st.selectbox("Select TI-RADS Category", ["TR1", "TR2", "TR3", "TR4", "TR5"])
        st.write(f"**TI-RADS Category Selected:** {ti_rads}")
        analysis = f"TI-RADS {ti_rads} provides guidance on the need for a nodule biopsy."
        next_steps = "For nodules in TR4 or TR5, consider fine-needle aspiration biopsy."
        st.markdown(f"**Analysis:** {analysis}")
        st.markdown(f"**Next Steps:** {next_steps}")
    elif rads_option == "O-RADS (Ovarian/Adnexal)":
        st.subheader("O-RADS")
        st.markdown("Stratifies ovarian/adnexal masses on a scale from 0 to 5.")
        o_rads = st.selectbox("Select O-RADS Category", ["0", "1", "2", "3", "4", "5"])
        st.write(f"**O-RADS Category Selected:** {o_rads}")
        analysis = f"O-RADS {o_rads} stratifies the risk of ovarian malignancy."
        next_steps = "High-risk lesions (O-RADS 4/5) should be further evaluated with surgical consultation and possible biopsy."
        st.markdown(f"**Analysis:** {analysis}")
        st.markdown(f"**Next Steps:** {next_steps}")
    elif rads_option == "NI-RADS (Neck)":
        st.subheader("NI-RADS")
        st.markdown("Standardizes reporting and follow-up for neck tumors.")
        ni_rads = st.selectbox("Select NI-RADS Category", ["1", "2", "3", "4"])
        st.write(f"**NI-RADS Category Selected:** {ni_rads}")
        analysis = f"NI-RADS {ni_rads} helps guide the interval for follow-up imaging and the need for additional diagnostic procedures."
        next_steps = "For higher NI-RADS categories, recommend closer clinical follow-up and additional imaging studies."
        st.markdown(f"**Analysis:** {analysis}")
        st.markdown(f"**Next Steps:** {next_steps}")

st.markdown("---")
st.markdown("**Disclaimer:** This app is for demonstration purposes only and does not substitute for professional diagnosis or clinical judgment.")
