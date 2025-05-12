# Análise de Risco de Diabetes: Um Classificador Inteligente 🩺

## 🌟 Visão Geral

Este projeto representa uma interseção entre **Ciência de Dados** e **Saúde**, desenvolvendo um classificador de aprendizado de máquina para prever o risco de diabetes com base em parâmetros clínicos. Implementado como uma aplicação web interativa com Streamlit, o sistema oferece uma ferramenta diagnóstica de apoio accessível e intuitiva com alta sensibilidade diagnóstica (87% de recall).

🔗 [**Acesse o aplicativo**](https://taramelli13-projeto-classificador-de-risco-de-diabet-app-0wlg3j.streamlit.app/)

![Diabetes Risk Classifier](https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Diabetes_Screening_Chart.svg/640px-Diabetes_Screening_Chart.svg.png)

## 💻 Tecnologias Utilizadas

- **Linguagem principal:** Python 3.8+
- **Machine Learning:** Scikit-learn (RandomForestClassifier)
- **Análise de dados:** Pandas, NumPy
- **Visualização:** Matplotlib, Seaborn
- **Frontend:** Streamlit
- **Deployment:** Streamlit Cloud

## 🧠 Metodologia e Recursos Técnicos

### Pipeline de ML

1. **Pré-processamento Avançado**
   - Tratamento especializado de valores ausentes (imputação via KNNImputer)
   - Detecção e manejo de outliers por método IQR
   - Engenharia de features para otimizar relevância clínica

2. **Modelagem Estratégica**
   - Algoritmo principal: Random Forest (escolhido após análise comparativa)
   - Otimização de hiperparâmetros via Grid Search
   - Validação cruzada (5-fold) para robustez estatística

3. **Ajuste Fino para Contexto Clínico**
   - Calibração do threshold de decisão (0.226) otimizada para maior sensibilidade
   - Foco em minimizar falsos negativos (critério crítico em saúde)

### Performance

| Métrica | Valor |
|---------|-------|
| Recall (Sensibilidade) | 87% |
| AUC | 0.81 |
| Precisão | 72% |
| F1-Score | 0.78 |

## 🖥️ Funcionalidades da Aplicação

- **Interface médica intuitiva** com controles deslizantes para parâmetros clínicos
- **Análise de risco em tempo real** com feedback visual imediato
- **Explicabilidade** através de importância de features e gráficos SHAP
- **Relatório personalizado** com recomendações baseadas no nível de risco
- **Design responsivo** para uso em dispositivos móveis e desktops

## 📊 Conjunto de Dados

Baseado no **Pima Indians Diabetes Dataset**, um benchmark reconhecido em pesquisas médicas:
- 768 registros de pacientes
- 8 parâmetros clínicos + variável alvo (diagnóstico)
- Distribuição de classes: 65% negativos, 35% positivos

### Variáveis Preditoras:

| Variável | Descrição | Relevância Clínica |
|----------|-----------|---------------------|
| Glucose | Concentração plasmática após 2h (TTGO) | Alta correlação com diagnóstico |
| BMI | Índice de Massa Corporal | Fator de risco estabelecido |
| Age | Idade em anos | Risco aumenta com idade |
| DiabetesPedigreeFunction | Função de histórico familiar | Componente genético |
| Insulin | Nível sérico de insulina | Indicador de resistência insulínica |
| BloodPressure | Pressão arterial diastólica | Comorbidade comum |
| Pregnancies | Número de gestações | Fator de risco para mulheres |
| SkinThickness | Espessura da dobra cutânea | Proxy para gordura subcutânea |

## 🚀 Instruções de Execução

```bash
# Clonar repositório
git clone https://github.com/yourusername/diabetes-risk-classifier.git
cd diabetes-risk-classifier

# Configurar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Instalar dependências
pip install -r requirements.txt

# Executar aplicação
streamlit run app.py
```

## ⚠️ Contexto Clínico e Limitações

Este sistema funciona como ferramenta de **triagem inicial** e não substitui avaliação médica especializada. O modelo foi desenvolvido seguindo diretrizes da **Sociedade Brasileira de Diabetes (2023)**, mas apresenta limitações inerentes:

- **Ausência de biomarcadores definitivos** como HbA1c e glicemia de jejum
- **Foco em fatores de risco** mais que em critérios diagnósticos formais
- **Calibrado para alta sensibilidade** em detrimento da especificidade

Para uso clínico efetivo, recomenda-se integração com avaliação médica completa e exames laboratoriais padrão-ouro.

## 🔍 Diferencial Técnico

- **Modelo interpretável**: Implementação de técnicas de explicabilidade (SHAP values)
- **Viés e Fairness**: Análise e mitigação de possíveis vieses demográficos
- **Documentação clínica**: Embasamento em diretrizes médicas atuais

## 📈 Potencial de Expansão

- Integração com sistemas de prontuário eletrônico (via API)
- Versão multi-plataforma (web, móvel, desktop)
- Expansão para classificação de complicações da diabetes
- Incorporação de novos biomarcadores e exames complementares

## 📞 Contato Profissional

**Ygor Taramelli** | Cientista de Dados & Desenvolvedor

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ygor-taramelli-03a859359/)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:taramelli@icloud.com)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/yourusername)
[![Portfolio](https://img.shields.io/badge/Portfolio-1DA1F2?style=for-the-badge&logo=website&logoColor=white)](https://yourportfolio.com)

---

**Referências**: Este projeto segue as diretrizes clínicas da [Sociedade Brasileira de Diabetes (2023)](https://diretriz.diabetes.org.br/diagnostico-de-diabetes-mellitus) e utiliza metodologias recomendadas pela comunidade de ML em saúde.
