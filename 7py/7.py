##BOKEH

import warnings
warnings.filterwarnings('ignore')
#GLYPHS - output en Jupyter
from bokeh.plotting import figure, output_file, show, reset_output

p = figure(width=400, height=400)

# glyph scatter
p.scatter([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="navy", alpha=0.5)

# mostrar resultados
#show(p)

# output static HTML file
#output_file("mi_scatter_1.html")
#en colab muestra directamente el plot, pero en jupyter no lo hace sin el show(p)

reset_output()

#GLYPH línea

from bokeh.plotting import figure, output_notebook, reset_output, show

output_notebook() # colab usa esto por default

x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')
p.line(x, y,
       legend_label="Temp.",
       line_width=2, line_dash='dashed')

show(p)

##Caso 1: NBA Interactivo
from bokeh.io import output_notebook
from bokeh.plotting import figure, output_notebook, reset_output, show

output_notebook()

# Crear un lienzo (canvas) vacío con .figure()
fig = figure(height=300, width=500,
             background_fill_color='gray', background_fill_alpha=0.8,
             border_fill_color='skyblue', border_fill_alpha=0.99,
             x_axis_label='X Label',
              x_axis_type='datetime',
              x_axis_location='below',
              x_range=('2018-01-01', '2018-06-30'), # no se va a mostrar como tal aun
             y_axis_label='Y Label',
              y_axis_type='linear',
              y_axis_location='left',
              y_range=(0, 100),
             title='Example Figure', title_location='above',
             toolbar_location='below', tools='save'
             )
show(fig)

# Cambios
fig.grid.grid_line_color = None

show(fig)

#EJEMPLO CIRCULO
from bokeh.io import output_file
from bokeh.plotting import figure, output_notebook, reset_output, show

# data
x = [1, 2, 1]
y = [1, 1, 2]

output_notebook()

# Crear figura sin toolbar con ejes de [0,3]
fig = figure(title='Coordenadas',
             height=300, width=300,
             x_range=(0, 3), y_range=(0, 3),
             toolbar_location=None
             )

# Dibujar circulos
fig.circle(x=x, y=y,
           color='green', size=10, alpha=0.5
           )

show(fig)

reset_output()

#EJEMPLO COMBINADO
import numpy as np

from bokeh.io import output_notebook
from bokeh.plotting import figure, output_notebook, reset_output, show

# data
day_num = np.linspace(1, 10, 10) # "desde... hasta... esta cantidad de valores"
daily_words = [450, 628, 488, 210, 287, 791, 508, 639, 397, 943]
cumulative_words = np.cumsum(daily_words)

output_notebook()

# figura con eje tipo datetime
fig = figure(height=400, width=700,
             title='Progreso',
             x_axis_label='Día', x_minor_ticks=2,
             y_axis_label='Palabras', y_range=(0, 6000),
             toolbar_location=None
             )

# representar palabras como columnas
fig.vbar(x=day_num,
         bottom=0, top=daily_words,
         color='blue', width=0.75,
         legend_label='Diario'
         )

# representar el acumulado como línea
fig.line(x=day_num, y=cumulative_words,
         color='gray', line_width=1,
         legend_label='Acumulado'
         )

# ubicación de la leyenda
fig.legend.location = 'top_left'

show(fig)  

#---------------------------------
#pandas
import pandas as pd

# leer csv
player_stats = pd.read_csv('2017-18_playerBoxScore.csv', parse_dates=['gmDate'])
team_stats = pd.read_csv('2017-18_teamBoxScore.csv', parse_dates=['gmDate'])
standings = pd.read_csv('2017-18_standings.csv', parse_dates=['stDate'])

#vista de exploración - records de Houston vs Golden State
west_top_2 = (standings[(standings['teamAbbr'] == 'HOU') | (standings['teamAbbr'] == 'GS')]
             .loc[:, ['stDate', 'teamAbbr', 'gameWon']]
              .sort_values(['teamAbbr','stDate']  )
              )
west_top_2.head()

#Uso de Column Data Source - para referenciar fuentes
from bokeh.plotting import figure, output_notebook, reset_output, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource

output_notebook()

# Filtrar datos
rockets_data = west_top_2[west_top_2['teamAbbr'] == 'HOU']
warriors_data = west_top_2[west_top_2['teamAbbr'] == 'GS']

# Usar .ColumnDataSource() para transformar datos
  # Bokeh no trabaja directamente con los DFs de Pandas.
  # Necesita transformarlos para vincular datos a gráficos interactivos
rockets_cds = ColumnDataSource(rockets_data)
warriors_cds = ColumnDataSource(warriors_data)

# Crear figura
west_fig = figure(x_axis_type='datetime',
             height=300, width=600,
             title='Western Conference Top 2 Teams Wins Race, 2017-18',
             x_axis_label='Date', y_axis_label='Wins',
             toolbar_location=None)

# usar step lines
west_fig.step('stDate', 'gameWon',
         color='#CE1141', legend_label='Rockets',
         source=rockets_cds)
west_fig.step('stDate', 'gameWon',
         color='#006BB6', legend_label='Warriors',
         source=warriors_cds)

west_fig.legend.location = 'top_left'
show(west_fig)

#Eastern conference
from bokeh.plotting import figure, output_notebook, reset_output, show
from bokeh.io import output_file, output_notebook
from bokeh.models import ColumnDataSource, CDSView, GroupFilter

# mostrar el plot
#reset_output()
output_notebook()

# # Guardar el plot
# reset_output()
# output_file('mi_plot.html')


# usar .ColumnDataSource()
standings_cds = ColumnDataSource(standings)

# views de los equipos: BOS y TOR
celtics_view = CDSView(
    filter=GroupFilter(column_name='teamAbbr', group='BOS'))
raptors_view = CDSView(
    filter=GroupFilter(column_name='teamAbbr', group='TOR'))

# figura
east_fig = figure(x_axis_type='datetime',
           height=300, width=600,
           title='Eastern Conference Top 2 Teams Wins Race, 2017-18',
           x_axis_label='Date', y_axis_label='Wins',
           toolbar_location=None)

# líneas escalonadas (step lines)
east_fig.step('stDate', 'gameWon',
              color='#007A33', legend_label='Celtics',
              source=standings_cds,
              view=celtics_view
              )
east_fig.step('stDate', 'gameWon',
              color='#CE1141', legend_label='Raptors',
              source=standings_cds,
              view=raptors_view
              )

east_fig.legend.location = 'top_left'


show(east_fig)
# save(east_fig)


# LAYOUT COLUMNA: mostrar ambos plots uno sobre otro
from bokeh.plotting import figure, output_notebook, reset_output, show, save
from bokeh.io import output_file, output_notebook
from bokeh.layouts import column

# Mostrar uno ensima dle otro
# reset_output()
output_notebook()
show(column(west_fig, east_fig))

# # Guardar
# reset_output()
# output_file('plots_apilados.html')
# save(column(west_fig, east_fig))


#GRID - mas opciones
from bokeh.io import output_file
from bokeh.layouts import gridplot

# Output
# reset_output()
output_notebook()

# tamaño
east_fig.width = west_fig.width = 300

#titulos
east_fig.title.text = 'Eastern Conference'
west_fig.title.text = 'Western Conference'

#ploteo con vacios
east_west_gridplot = gridplot(
    [[west_fig, None],
     [None, east_fig]],
    toolbar_location='right')

show(east_west_gridplot)

#TAB - pestañas ----------
from bokeh.io import output_file
from bokeh.models.layouts import TabPanel, Tabs

# reset_output()
output_notebook()

east_fig.width = west_fig.width = 800

# Paneles
east_panel = TabPanel(child=east_fig, title='Eastern Conference')
west_panel = TabPanel(child=west_fig, title='Western Conference')

# Tabs
tabs = Tabs(tabs=[west_panel, east_panel])

show(tabs)

#Interacción
#dataframe creado para jugadores 3PTOS

# Encontrar jugadores
three_takers = player_stats[player_stats['play3PA'] > 0]

# Combinar nombres
three_takers['name'] = three_takers['playFNm'] +' '+three_takers['playLNm']

# Agregar los puntos
three_takers = (three_takers.loc[:,['name','play3PA', 'play3PM']]
                            .groupby('name')
                            .sum()
                            .sort_values('play3PA', ascending=False))

# Filtrar los que no llegaron a 100
three_takers = three_takers[three_takers['play3PA'] >= 100].reset_index()

# agregar columna con calculo (made/attempted)
three_takers['pct3PM'] = three_takers['play3PM'] / three_takers['play3PA']

#visualizar lo anterior
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource, NumeralTickFormatter

# Output
# reset_output()
output_notebook()

# ColumnDataSource
three_takers_cds = ColumnDataSource(three_takers)

# elegir herramientas de selección
select_tools = ['box_select', 'lasso_select', 'poly_select', 'tap', 'reset']

# Crear figura
fig = figure(height=400,
             width=600,
             x_axis_label='Three-Point Shots Attempted',
             y_axis_label='Percentage Made',
             title='3PT Shots Attempted vs. Percentage Made (min. 100 3PA), 2017-18',
             toolbar_location='below',
             tools=select_tools)

# Formatear eje y
fig.yaxis[0].formatter = NumeralTickFormatter(format='00.0%')

# cuadrados
fig.scatter(x='play3PA', y='pct3PM',
            source=three_takers_cds,
            marker='square',
            color='royalblue', selection_color='deepskyblue',
            nonselection_color='lightgray', nonselection_alpha=0.3)

show(fig)

#hover
from bokeh.models import HoverTool

# reset_output()

# Formateo
tooltips = [
            ('Player','@name'),
            ('Three-Pointers Made', '@play3PM'),
            ('Three-Pointers Attempted', '@play3PA'),
            ('Three-Point Percentage','@pct3PM{00.0%}'),
           ]

fig.add_tools(HoverTool(tooltips=tooltips))

show(fig)
#"siue en codigo y dejo el ultimo antes de ..."
from bokeh.plotting import figure, show, output_notebook
from bokeh.io import output_file
from bokeh.models import ColumnDataSource, CategoricalColorMapper, NumeralTickFormatter
from bokeh.layouts import gridplot

# Output inline in the notebook
# reset_output()
output_notebook()

# ColumnDataSource - crea el link
gm_stats_cds = ColumnDataSource(phi_gm_stats_2)

win_loss_mapper = CategoricalColorMapper(factors = ['W', 'L'], palette=['Green', 'Red'])

# tools
toolList = ['lasso_select', 'tap', 'reset', 'save']

# figura con porcentajes
pctFig = figure(title='2PT FG % vs 3PT FG %, 2017-18 Regular Season',
                height=400, width=400, tools=toolList,
                x_axis_label='2PT FG%', y_axis_label='3PT FG%')

# circulo
pctFig.circle(x='team2P%', y='team3P%', source=gm_stats_cds,
              size=12, color='black')

# Formateo eje y
pctFig.xaxis[0].formatter = NumeralTickFormatter(format='00.0%')
pctFig.yaxis[0].formatter = NumeralTickFormatter(format='00.0%')

# figura con totales
totFig = figure(title='Team Points vs Opponent Points, 2017-18 Regular Season',
                height=400, width=400, tools=toolList,
                x_axis_label='Team Points', y_axis_label='Opponent Points')

# Dibujar marcadores
totFig.square(x='teamPTS', y='opptPTS', source=gm_stats_cds, size=10,
              color=dict(field='winLoss', transform=win_loss_mapper))

# layout
grid = gridplot([[pctFig, totFig]])

# Visualizar
show(grid)