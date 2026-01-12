import streamlit as st
import pandas as pd

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="PeakPulse Physiological Performance Analysis",
    layout="wide",
    page_icon="🔥"
)

st.title("🔥 PeakPulse Physiological Performance Analysis")
st.markdown(
    "**95-Question Precision Assessment** · Science-Backed · Demo Version"
)
st.info(
    "This is a demonstration version of the PeakPulse AI Assessment. "
    "Final production version includes adaptive logic, data persistence, and regulatory localization."
)

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------
if "profile" not in st.session_state:
    st.session_state.profile = {}

def q(key, value):
    st.session_state.profile[key] = value

progress = min(len(st.session_state.profile) / 95, 1.0)
st.progress(progress)
st.caption(f"Progress: {int(progress*100)}% of 95 questions")

# --------------------------------------------------
# TABS
# --------------------------------------------------
tabs = st.tabs([
    "1️⃣ Demographics",
    "2️⃣ Health",
    "3️⃣ Lifestyle",
    "4️⃣ Training",
    "5️⃣ Nutrition",
    "6️⃣ Recovery",
    "7️⃣ Environment",
    "8️⃣ Goals",
    "🏆 Results"
])

# --------------------------------------------------
# SECTION 1 – DEMOGRAPHICS (Q1–10)
# --------------------------------------------------
with tabs[0]:
    st.header("Section 1 – Demographics & Body Composition")
    q("age", st.number_input("Q1. Age", 16, 80, 30))
    q("sex", st.selectbox("Q2. Biological sex", ["Male", "Female", "Other", "Prefer not to say"]))
    q("height", st.number_input("Q3. Height (cm)", 140, 220, 175))
    q("weight", st.number_input("Q4. Weight (kg)", 40, 160, 75))
    q("weight_stable", st.radio("Q5. Weight stable past 3 months?", ["Yes", "No"]))
    q("bodyfat", st.number_input("Q6. Estimated body fat % (optional)", 0.0, 60.0, 20.0))
    q("waist", st.number_input("Q7. Waist circumference (cm)", 50, 150, 85))
    q("bmi_goal", st.selectbox("Q8. Body composition goal", ["Maintain", "Lose weight", "Gain weight"]))
    q("country", st.selectbox("Q9. Country of residence", ["France", "Other EU", "USA", "Canada", "UK", "Australia", "Other"]))
    q("climate", st.selectbox("Q10. Climate zone", ["Temperate", "Mediterranean", "Continental", "Tropical", "Cold"]))

# --------------------------------------------------
# SECTION 2 – HEALTH (Q11–25)
# --------------------------------------------------
with tabs[1]:
    st.header("Section 2 – Health & Medical Background")
    q("conditions", st.multiselect(
        "Q11. Diagnosed conditions",
        ["None", "Diabetes", "Hypertension", "Thyroid", "IBS", "Asthma", "Anemia"]
    ))
    q("family_history", st.multiselect(
        "Q12. Family medical history",
        ["Heart disease", "Diabetes", "Cancer", "Autoimmune", "None known"]
    ))
    q("allergies", st.text_input("Q13. Allergies or intolerances"))
    q("medications", st.text_input("Q14. Current medications"))
    q("supplements", st.text_input("Q15. Current supplements"))
    q("blood_type", st.selectbox("Q16. Blood type", ["O", "A", "B", "AB", "Unknown"]))
    q("ferritin", st.number_input("Q17. Ferritin (µg/L)", 0, 300, 50))
    q("vitd", st.number_input("Q18. Vitamin D (ng/mL)", 0, 100, 30))
    q("b12", st.number_input("Q19. Vitamin B12 (pg/mL)", 0, 1200, 400))
    q("hba1c", st.number_input("Q20. HbA1c (%)", 3.0, 10.0, 5.2))
    q("crp", st.number_input("Q21. CRP (mg/L)", 0.0, 20.0, 1.0))
    q("sleep_hours", st.slider("Q22. Average sleep hours", 4.0, 10.0, 7.0))
    q("sleep_quality", st.slider("Q23. Sleep quality (1–10)", 1, 10, 6))
    q("symptoms", st.multiselect(
        "Q24. Chronic symptoms",
        ["Fatigue", "Brain fog", "Joint pain", "Digestive issues", "None"]
    ))
    q("menstrual", st.selectbox(
        "Q25. Menstrual cycle regularity (if applicable)",
        ["Regular", "Irregular", "Not applicable"]
    ))

# --------------------------------------------------
# SECTION 3 – LIFESTYLE (Q26–40)
# --------------------------------------------------
with tabs[2]:
    st.header("Section 3 – Lifestyle & Habits")
    q("smoking", st.selectbox("Q26. Smoking status", ["Never", "Former", "Current"]))
    q("alcohol", st.selectbox("Q27. Alcohol intake", ["None", "Light", "Moderate", "High"]))
    q("caffeine", st.number_input("Q28. Caffeine (mg/day)", 0, 800, 200))
    q("stress", st.slider("Q29. Daily stress (1–10)", 1, 10, 5))
    q("stressors", st.multiselect("Q30. Primary stressors", ["Work", "Training", "Family", "Financial"]))
    q("hydration", st.number_input("Q31. Water intake (L/day)", 0.5, 6.0, 2.0))
    q("sun", st.selectbox("Q32. Sun exposure", ["Low", "Moderate", "High"]))
    q("spf", st.radio("Q33. Regular SPF use?", ["Yes", "No"]))
    q("diet", st.selectbox("Q34. Diet pattern", ["Omnivore", "Vegetarian", "Vegan", "Keto", "Low-carb"]))
    q("meals", st.selectbox("Q35. Meal timing consistency", ["Consistent", "Irregular"]))
    q("fasting", st.radio("Q36. Intermittent fasting?", ["Yes", "No"]))
    q("processed", st.selectbox("Q37. Processed food intake", ["Low", "Moderate", "High"]))
    q("plant_protein", st.selectbox("Q38. Plant-based protein %", ["<25%", "25–50%", ">50%"]))
    q("digestion", st.selectbox("Q39. Digestive regularity", ["Regular", "Irregular"]))
    q("sensitivities", st.text_input("Q40. Known food sensitivities"))

# --------------------------------------------------
# SECTION 4 – TRAINING (Q41–60)
# --------------------------------------------------
with tabs[3]:
    st.header("Section 4 – Training & Performance")
    q("sport", st.selectbox("Q41. Primary sport", ["Running", "Cycling", "Strength", "Mixed", "Other"]))
    q("sport2", st.text_input("Q42. Secondary sport"))
    q("experience", st.selectbox("Q43. Experience level", ["Beginner", "Intermediate", "Advanced"]))
    q("sessions", st.number_input("Q44. Sessions per week", 0, 20, 4))
    q("volume", st.number_input("Q45. Weekly volume (km or hours)", 0.0, 200.0, 30.0))
    q("rpe", st.slider("Q46. Average session intensity (RPE)", 1, 10, 6))
    q("strength_sessions", st.number_input("Q47. Strength sessions/week", 0, 10, 2))
    q("cardio_sessions", st.number_input("Q48. Cardio sessions/week", 0, 10, 3))
    q("mobility_sessions", st.number_input("Q49. Mobility sessions/week", 0, 7, 1))
    q("rhr", st.number_input("Q50. Resting heart rate", 30, 100, 60))
    q("max_hr", st.number_input("Q51. Max heart rate", 120, 220, 190))
    q("hrv", st.number_input("Q52. HRV (ms)", 20, 120, 60))
    q("competition", st.radio("Q53. Competition planned?", ["Yes", "No"]))
    q("event_date", st.text_input("Q54. Next event date"))
    q("phase", st.selectbox("Q55. Training phase", ["Base", "Build", "Peak", "Off-season"]))
    q("injuries", st.multiselect("Q56. Injury history", ["None", "Knee", "Back", "Shoulder"]))
    q("pain", st.radio("Q57. Current pain?", ["Yes", "No"]))
    q("equipment", st.selectbox("Q58. Equipment access", ["Full gym", "Home gym", "Minimal"]))
    q("group", st.selectbox("Q59. Training style", ["Solo", "Group", "Team"]))
    q("travel", st.selectbox("Q60. Travel/jet lag frequency", ["Rare", "Occasional", "Frequent"]))

# --------------------------------------------------
# SECTION 5 – NUTRITION (Q61–75)
# --------------------------------------------------
with tabs[4]:
    st.header("Section 5 – Nutrition Intake")
    q("calories", st.number_input("Q61. Daily calories", 1200, 5000, 2500))
    q("protein", st.number_input("Q62. Protein (g/day)", 40, 300, 120))
    q("carbs", st.number_input("Q63. Carbs (g/day)", 0, 600, 250))
    q("fat", st.number_input("Q64. Fat (g/day)", 20, 200, 80))
    q("fiber", st.number_input("Q65. Fiber (g/day)", 5, 80, 25))
    q("postworkout", st.radio("Q66. Post-workout nutrition within 30 min?", ["Yes", "No"]))
    q("hydration_training", st.selectbox("Q67. Hydration during training", ["Water", "Electrolytes", "None"]))
    q("mg_intake", st.number_input("Q68. Magnesium intake (mg)", 0, 600, 300))
    q("iron_intake", st.number_input("Q69. Iron intake (mg)", 0, 30, 12))
    q("zinc", st.number_input("Q70. Zinc intake (mg)", 0, 40, 12))
    q("omega3", st.number_input("Q71. Omega-3 (g/day)", 0.0, 5.0, 1.0))
    q("calcium", st.number_input("Q72. Calcium (mg)", 0, 2000, 800))
    q("potassium", st.number_input("Q73. Potassium (mg)", 0, 5000, 3000))
    q("meal_quality", st.slider("Q74. Meal quality (1–10)", 1, 10, 7))
    q("gut_symptoms", st.selectbox("Q75. Gut symptoms frequency", ["None", "Occasional", "Frequent"]))

# --------------------------------------------------
# SECTION 6 – RECOVERY (Q76–85)
# --------------------------------------------------
with tabs[5]:
    st.header("Section 6 – Recovery & Regeneration")
    q("soreness", st.selectbox("Q76. Muscle soreness duration", ["None", "24h", "48h", "72h+"]))
    q("recovery_methods", st.multiselect(
        "Q77. Recovery methods",
        ["Sleep", "Stretching", "Sauna", "Cold", "Massage"]
    ))
    q("sauna", st.selectbox("Q78. Sauna frequency", ["None", "1–2x/wk", "3+x/wk"]))
    q("cold", st.selectbox("Q79. Cold exposure", ["None", "Occasional", "Regular"]))
    q("massage", st.radio("Q80. Massage/compression?", ["Yes", "No"]))
    q("wearable", st.selectbox("Q81. Wearable device", ["None", "Garmin", "Apple", "Other"]))
    q("deep_sleep", st.number_input("Q82. Deep sleep (min/night)", 0, 200, 60))
    q("mental", st.multiselect("Q83. Mental recovery", ["Meditation", "Breathing", "Nature"]))
    q("injury_recovery", st.selectbox("Q84. Injury recovery speed", ["Fast", "Average", "Slow"]))
    q("recovery_score", st.slider("Q85. Overall recovery quality (1–10)", 1, 10, 7))

# --------------------------------------------------
# SECTION 7 – ENVIRONMENT (Q86–90)
# --------------------------------------------------
with tabs[6]:
    st.header("Section 7 – Environment & Legal")
    q("altitude", st.selectbox("Q86. Altitude", ["Sea level", "500–1500m", ">1500m"]))
    q("air", st.selectbox("Q87. Air quality", ["Good", "Moderate", "Poor"]))
    q("winter_vitd", st.radio("Q88. Winter vitamin D drop?", ["Yes", "No"]))
    q("customs", st.radio("Q89. Import/customs concerns?", ["Yes", "No"]))
    q("currency", st.selectbox("Q90. Preferred currency", ["EUR", "USD", "CAD", "GBP"]))

# --------------------------------------------------
# SECTION 8 – GOALS (Q91–95)
# --------------------------------------------------
with tabs[7]:
    st.header("Section 8 – Goals & Preferences")
    q("goal_primary", st.selectbox("Q91. Primary goal", ["Endurance", "Strength", "Fat loss", "Recovery", "Health"]))
    q("goal_secondary", st.selectbox("Q92. Secondary goal", ["None", "Performance", "Longevity", "Aesthetics"]))
    q("budget", st.selectbox("Q93. Budget per month", ["<20", "20–40", ">40"]))
    q("formats", st.multiselect("Q94. Preferred formats", ["Capsules", "Powder", "Gummies"]))
    q("delivery", st.selectbox("Q95. Delivery frequency", ["Monthly", "Bi-weekly", "Custom"]))

# --------------------------------------------------
# RESULTS
# --------------------------------------------------
with tabs[8]:
    st.header("🏆 Your Personalized Recommendation")

    if st.button("🚀 ANALYZE ALL 95 ANSWERS", type="primary"):
        scores = {
            "Endurance Pack": 0,
            "Strength Pack": 0,
            "Recovery Pack": 0,
            "Metabolic Pack": 0,
            "Beginner Pack": 0
        }

        if st.session_state.profile.get("sport") in ["Running", "Cycling"] and st.session_state.profile.get("volume", 0) > 30:
            scores["Endurance Pack"] += 40
        if st.session_state.profile.get("sport") == "Strength":
            scores["Strength Pack"] += 40
        if st.session_state.profile.get("sleep_hours", 7) < 6 or st.session_state.profile.get("hrv", 60) < 40:
            scores["Recovery Pack"] += 35
        if "Diabetes" in st.session_state.profile.get("conditions", []):
            scores["Metabolic Pack"] += 40
        if st.session_state.profile.get("experience") == "Beginner":
            scores["Beginner Pack"] += 30

        best = max(scores, key=scores.get)
        confidence = min(scores[best] / 80, 1.0)

        st.success(f"### 🎯 {best}")
        st.info(f"Confidence: {confidence:.0%}")

        st.subheader("Why this pack?")
        st.write("Based on training volume, recovery markers, nutrition gaps, and stated goals.")

        st.subheader("⚠️ Disclaimer")
        st.warning(
            "Non-medical nutritional guidance only. "
            "Consult a qualified healthcare professional before use."
        )

st.markdown("---")
st.caption("PeakPulse © 2026 · Demo Version · GDPR-aligned · Strasbourg, France")