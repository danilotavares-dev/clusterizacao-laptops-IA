import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    return pd.read_csv('./datasets/clusterizacao_laptops.csv')

df = load_data()



st.sidebar.header("Filtros")

# selecionar modelos
model = st.sidebar.selectbox('Selecionar Modelo', df['model'].unique())

# Filtrar modelo
df_laptops_modelo = df[df['model'] == model]

# Filtrar cluster do modelo escolhido
df_laptops_final = df[df['cluster'] == df_laptops_modelo.iloc[0]['cluster']]

# Visualizar modelos
st.write('Recomendações de Modelos')
st.dataframe(df_laptops_final, use_container_width=True, hide_index=True, height=800)