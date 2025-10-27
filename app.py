import streamlit as st
import joblib
import numpy as np
import gdown
import os

url = "https://drive.google.com/uc?id=YOUR_FILE_ID"
output = "my_model.pkl"

if not os.path.exists(output):
    gdown.download(url, output, quiet=False)

# تحميل النموذج
model = joblib.load('my_model.pkl')

# العنوان والوصف
st.title("🔮 تطبيق التنبؤ بالإصابة بالسكري")
st.write("أدخل بيانات المريض لمعرفة احتمال الإصابة بالسكري:")

# ===== مدخلات المستخدم =====
age = st.number_input("👤 العمر:", 0, 120)

hypertension_text = st.selectbox("💓 ضغط الدم:", ['غير مرتفع', 'مرتفع'])
hypertension = 1 if hypertension_text == 'مرتفع' else 0

heart_disease_text = st.selectbox("❤️ مرض قلبي:", ['غير مصاب', 'مصاب'])
heart_disease = 1 if heart_disease_text == 'مصاب' else 0

HbA1c_level = st.number_input("🧪 مستوى HbA1c:", 0.0, 20.0, step=0.1)
blood_glucose_level = st.number_input("🩸 مستوى الجلوكوز:", 0.0, 500.0, step=1.0)

BMI_Category_text = st.selectbox(
    "⚖️ تصنيف مؤشر كتلة الجسم (BMI):",
    ["نقص وزن", "طبيعي", "زيادة وزن", "سمنة"]
)
BMI_Category = ["نقص وزن", "طبيعي", "زيادة وزن", "سمنة"].index(BMI_Category_text)

gender_text = st.selectbox("🚻 الجنس:", ["ذكر", "أنثى"])
gender_male = 1 if gender_text == "ذكر" else 0
gender_other = 0  # إذا ما عندك فئة أخرى بالنموذج، خليه دائمًا صفر

# ===== التنبؤ =====
if st.button("🔍 التنبؤ"):
    X_new = np.array([[age, hypertension, heart_disease, HbA1c_level,
                       blood_glucose_level, BMI_Category, gender_male, gender_other]])
    
    prediction = model.predict(X_new)

    if prediction[0] == 1:
        st.error("🔴 المريض مصاب بالسكري")
    else:
        st.success("🟢 المريض غير مصاب بالسكري")

