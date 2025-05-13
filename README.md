# Classificador de Risco de Diabetes 🩺

Este projeto aplica ciência de dados e aprendizado de máquina para prever o risco de diabetes com base em dados clínicos, oferecendo uma solução prática via um aplicativo interativo desenvolvido com Streamlit. O objetivo é entregar uma ferramenta acessível, com boa sensibilidade diagnóstica, que possa ser usada como apoio à tomada de decisão clínica ou estudos populacionais.

🔗 **Acesse o app online aqui:** [Classificador de Risco de Diabetes](https://taramelli13-projeto-classificador-de-risco-de-diabet-app-0wlg3j.streamlit.app/)

---

## 🧠 Visão Geral

* **Tipo de problema:** Classificação binária (diabetes: sim ou não)
* **Algoritmo usado:** Random Forest
* **Métrica-chave otimizada:** Recall (Sensibilidade)
* **Tecnologias:** Python, Scikit-learn, Pandas, Numpy, Streamlit
* **Abordagens:** Imputação de dados, análise de outliers, ajuste de limiar de decisão (threshold)

---

## 📂 Estrutura do Projeto

```
Projeto classificador de risco de diabetes/
├── app.py                  # App Streamlit para entrada de dados e inferência
├── diabetes.csv            # Dataset base (Pima Indians Diabetes)
├── get-pip.py              # Script auxiliar para instalação de pip
├── modelo_diabetes.pkl     # Modelo Random Forest serializado via pickle
├── modelo_diabetes         # Versão redundante do modelo (pode ser ignorada)
└── README.md               # Documentação do projeto
```

---

## 🖥️ Funcionalidades do App

* Interface intuitiva com sliders para inserir dados clínicos do paciente
* Cálculo da probabilidade de diabetes com base no modelo
* Exibição de mensagens adaptadas ao risco detectado
* Visualização da entrada do usuário para conferência
* Threshold de decisão ajustado (0.226) para maior recall da classe 1 (positivos)

---

## 📊 Sobre o Dataset

* **Origem:** Pima Indians Diabetes Dataset (UCI Repository)
* **Total de observações:** 768
* **Atributos:** 8 preditores + 1 variável alvo (Outcome)

**Variáveis incluídas:**

* Pregnancies: número de gestações
* Glucose: concentração de glicose plasmática
* BloodPressure: pressão arterial diastólica
* SkinThickness: espessura da dobra cutânea do tríceps
* Insulin: nível sérico de insulina
* BMI: índice de massa corporal
* DiabetesPedigreeFunction: histórico familiar
* Age: idade
* Outcome: 0 (não-diabético), 1 (diabético)

---

## 🧪 Sobre o Modelo

* **Algoritmo:** RandomForestClassifier

**Pré-processamento:**

* Zeros tratados como ausentes (NaN) em variáveis clínicas
* Imputação com mediana e KNNImputer (n=5)
* Detecção e análise de outliers via boxplots e IQR

**Ajuste de limiar (threshold tuning):**

* Ponto de corte ajustado para 0.226 com foco em maximizar o recall da classe 1

**Desempenho:**

* Recall (classe 1): 87%
* AUC: 0.81

---

## ⚠️ Limitações do Projeto

Este modelo é baseado em um conjunto limitado de variáveis e não substitui critérios diagnósticos clínicos formais.

### 📉 Ausência de exames laboratoriais fundamentais:

* Glicemia de jejum (não é uma medida exata no dataset)
* Hemoglobina glicada (HbA1c)
* Teste oral de tolerância à glicose (TTGO)

### 👩‍⚕️ Recomendações clínicas reais:

De acordo com a Diretriz Brasileira de Diabetes (SBD, 2023), o diagnóstico de diabetes deve considerar:

* Glicemia de jejum ≥ 126 mg/dL
* HbA1c ≥ 6,5%
* Glicemia 1h no TTGO ≥ 209 mg/dL
* Glicemia 2h no TTGO ≥ 200 mg/dL

Se apenas um desses exames estiver alterado, ele deve ser repetido para confirmação.
Referência oficial: [https://diretriz.diabetes.org.br/diagnostico-de-diabetes-mellitus](https://diretriz.diabetes.org.br/diagnostico-de-diabetes-mellitus)

### 📌 Sinais clínicos que não foram incluídos:

Além dos dados do dataset, sintomas clínicos que podem sugerir hiperglicemia incluem:

**Típicos:**

* Poliúria
* Polidipsia
* Polifagia
* Perda de peso inexplicada
* Desidratação

**Sugestivos:**

* Noctúria
* Visão turva
* Cansaço
* Infecções recorrentes (candidíase, periodontite)
* Má cicatrização de feridas
* Albuminúria transitória em DM1 recente

Esses sintomas podem ser úteis em uma triagem clínica, mas não substituem a confirmação bioquímica.

---

## 📋 Possíveis Extensões

* Exportação dos resultados para CSV/PDF
* Registro de histórico de avaliações
* Inclusão de gráficos explicativos
* Treinamento com mais algoritmos (Logistic Regression, XGBoost)
* Interface multilíngue (EN/PT)

---

## 📎 Requisitos

* Python >= 3.8
* streamlit
* pandas
* numpy
* scikit-learn

Para gerar o arquivo de dependências:

```bash
pip freeze > requirements.txt
```

---

## ✉️ Contato

Este projeto foi desenvolvido com fins educativos e demonstrativos. Para contribuições ou colaborações:

**Ygor Taramelli**
📧 Email: [taramelli@icloud.com](mailto:taramelli@icloud.com)
🔗 LinkedIn: [Ygor Taramelli](https://www.linkedin.com/in/ygor-taramelli-03a859359/)
