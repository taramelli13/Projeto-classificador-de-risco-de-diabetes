import streamlit as st
import numpy as np
import pandas as pd
import pickle


try:
    with open('modelo_diabetes.pkl', 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("❌ Arquivo do modelo não encontrado. Verifique se 'modelo_diabetes.pkl' está na mesma pasta.")
    st.stop()
except Exception as e:
    st.error(f"❌ Erro ao carregar o modelo: {e}")
    st.stop()


st.set_page_config(page_title="Classificador de Risco de Diabetes", layout="centered")
st.title("🩺 Avaliação de Risco de Diabetes")
st.write("Preencha os dados abaixo para obter uma estimativa do risco de diabetes com base no seu perfil clínico.")

# Inputs do usuário
glucose = st.slider('Glicose', 50, 200, 120)
blood_pressure = st.slider('Pressão Arterial (mmHg)', 40, 122, 70)
skin_thickness = st.slider('Espessura da pele (mm)', 0, 99, 20)
insulin = st.slider('Insulina (mu U/ml)', 0, 846, 79)
bmi = st.slider('IMC (kg/m²)', 15.0, 67.1, 30.0)
pedigree = st.slider('Índice genético (pedigree)', 0.0, 2.5, 0.5)
age = st.slider('Idade', 10, 90, 33)
pregnancies = st.slider('Número de gestações', 0, 17, 1)

# Agrupar entrada para predição
input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, pedigree, age]])

# Threshold ajustado com base no recall ideal
threshold = 0.226

# Predição
if st.button("📊 Avaliar Risco"):
    prob = model.predict_proba(input_data)[0][1]
    pred = int(prob >= threshold)

    st.write(f"\n### 🔬 Probabilidade estimada de diabetes: **{prob * 100:.1f}%**")
    
    if pred == 1:
        st.error("⚠️ Alto risco de diabetes detectado. Recomendamos acompanhamento profissional.")
    else:
        st.success("✅ Baixo risco detectado. Continue monitorando e mantendo bons hábitos!")

    with st.expander("Ver dados usados na avaliação"):
        st.write(pd.DataFrame(input_data, columns=[
            "Pregnancies", "Glucose", "BloodPressure", "SkinThickness",
            "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"
        ]))
