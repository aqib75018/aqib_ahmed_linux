import dash     #  bibliothèques pour creer un Dashboard
from dash import dcc 
from dash import html
from dash.dependencies import Input, Output
import pandas as pd  #  bibliothèques pour la manipulation de données
import plotly.graph_objects as go  # Bibliothèques pour créer des graphiques 
from datetime import datetime, time, date  # bibliothèques pour manipuler des dates et des heures
from apscheduler.schedulers.background import BackgroundScheduler  # Importation de la bibliothèque apscheduler pour planifier des tâches
import plotly.express as px

# Dans la fonction load_data, on charge les données via le fichier csv et on les traitent afin de les afficher 
def load_data():
    global df, daily_data, fig, table
    df = pd.read_csv('/home/ec2-user/projet_linux/prix.csv', names=['Date', 'Prix'])
    df['Date'] = pd.to_datetime(df['Date'], format="%a %b %d %H:%M:%S %Z %Y")
    df['Jour'] = df['Date'].dt.strftime('%Y-%m-%d')

    # On ajoute cette ligne pour rajouter les valeurs manquantes, on les interpole afin de ne pas avoir de trous dans notre graphique
    df['Prix'] = df['Prix'].interpolate()

    # On regroupe les données dans le groupby et on calcule les métriques nécéassires pour notre tableau de synthèse
    daily_data = df.groupby('Jour').agg(
        {
            'Prix': ['first', 'last', 'min', 'max']
        }
    )
    daily_data.columns = daily_data.columns.map('_'.join)
    daily_data.reset_index(inplace=True)
    daily_data['Variation'] = ((daily_data['Prix_last'] - daily_data['Prix_first']) / daily_data['Prix_first']) * 100
    daily_data['Volatilite'] = (daily_data['Prix_max'] - daily_data['Prix_min']) / daily_data['Prix_min'] * 100
    daily_data['Rendement'] = (daily_data['Prix_last'] - daily_data['Prix_first']) / daily_data['Prix_first']
    daily_data = daily_data.sort_values(by='Jour', ascending=False)

    # On filtre les données pour n'avoir que les données d'aujourd'hui
    today = date.today().strftime('%Y-%m-%d')
    daily_data = daily_data[daily_data['Jour'] == today]

    # On crée le graphique ici :
    fig = px.line(df, x='Date', y='Prix', markers=True, title='Cours du Litecoin en Euro')
    fig.update_xaxes(title_text='Jour et heure')
    fig.update_yaxes(title_text='Prix')

    
   # On crée une table HTML pour afficher les statistiques journalières
    table = html.Table(
        [html.Tr([html.Th(col) for col in daily_data.columns], style={"border": "1px solid black", "padding": "8px"})] +
        [html.Tr([
            html.Td("{:.3g}".format(daily_data.iloc[i][col]) if col in ["Variation", "Volatilite", "Rendement"] else daily_data.iloc[i][col], style={"border": "1px solid black", "padding": "8px"})
            for col in daily_data.columns
        ]) for i in range(len(daily_data))],
        style={"width": "100%", "margin": "auto", "border-collapse": "collapse"}
)

# On applique la fonction load_data
load_data()

# On crée un planificateur de taches afin de recharger les données tous les jours à 20h
scheduler = BackgroundScheduler()
scheduler.add_job(load_data, 'cron', hour=20)
scheduler.start()

# On initialise l'instance Dash
app = dash.Dash(__name__)

# On crée l'interface utilisateur avec un titre, un bouton pour obtenir le dernier prix, et un graphique
app.layout = html.Div([
    html.Div(html.H1("Cours du Litecoin en Euro"), style={"textAlign": "center"}),
    html.Button("Obtenir le dernier prix", id="get-price-button", style={"fontSize": "20px", "padding": "10px"}),
    html.Div(id="last-price", style={"fontSize": 24, "textAlign": "center"}),
    dcc.Graph(id='price-graph', figure=fig),
    html.Div(html.H2("Tableau de synthèse"), style={"textAlign": "center"}),
    html.Div(id="summary-table", children=table)
])

# On crée un callback pour mettre à jour le graphique et le tableau lorsqu'on clique sur le bouton
@app.callback(
    [Output("price-graph", "figure"), Output("summary-table", "children")],
    [Input("get-price-button", "n_clicks")]
)
def update_chart(n_clicks):
      return fig, table

# Callback pour récupérer le dernier prix et le tableau lorsqu'on clique sur le bouton
@app.callback(
    Output("last-price", "children"),
    [Input("get-price-button", "n_clicks")]
)
def update_last_price(n_clicks):
    if n_clicks:
        last_price = df["Prix"].iloc[-1]
        return f"Dernier prix: {last_price}"
    else:
        return ""

# On lance application Dash dans le main
if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8050)


