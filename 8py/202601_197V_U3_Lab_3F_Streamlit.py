import streamlit as st
import plotly.express as px

st.set_page_config(page_title='Ejemplo con Streamlit',
                   layout="wide")

col1, col2, col3 = st.columns([5, 30, 4])
with col2:
    st.title("Mi demo para Gapminder 3")

year_col, continent_col, log_x_col = st.columns([5, 5, 5])
with year_col:
    year_choice = st.slider(
        label="AÑOS",
        label_visibility='visible', # visible (def), hidden, collapsed
        min_value=1952, #año inicial
        max_value=2007, #año final
        step=5, # saltos en el slider de esta cantidad de años
        value=2007, # valor que se muestra cuando se carga
    )
with continent_col:
    continent_choice = st.selectbox(
        "CONTINENTE",
        ("TODOS", "Asia", "Europe", "Africa", "Americas", "Oceania"),
    )
with log_x_col:
    log_x_choice = st.checkbox("Log X Axis?")

# IMPORTAR DATOS
df = px.data.gapminder()

# Establecer año de análisis del dataset según lo elegido en el slider
filtered_df = df[(df.year == year_choice)]

# Establecer el continente según lo elegido en el selectbox 
if continent_choice != "TODOS":
    filtered_df = filtered_df[filtered_df.continent == continent_choice]

# Establecer colores 
continent_colors = {
    "Europe": "#636EFA",      # azul
    "Americas": "#EF553B",    # rojo
    "Africa": "#00CC96",    # verde
    "Oceania": "#AB63FA",  # violeta
    "Asia": "#FFA15A"    # naranja
}

# Graficar según las elecciones
fig = px.scatter(
    filtered_df,
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    color_discrete_map=continent_colors,
    hover_name="country",
    log_x=log_x_choice,
    size_max=50,
)

# # Graficar con barra de animación
# fig = px.scatter(
#     df if continent_choice == "TODOS" else df[df.continent == continent_choice],
#     x="gdpPercap",
#     y="lifeExp",
#     size="pop",
#     color="continent",
#     hover_name="country",
#     log_x=log_x_choice,
#     size_max=45,
#     animation_frame="year",
#     range_x=[100, 100_000],
#     range_y=[20, 90],
#     color_discrete_map=continent_colors
# )


fig.update_layout(title="GDP per Capita vs. Life Expectancy")

st.plotly_chart(fig, use_container_width=True)