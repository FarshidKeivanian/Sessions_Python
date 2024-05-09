import dash
import psycopg2
import tweepy
import pandas as pd
from dash import html, dcc
import plotly.express as px
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

# Set up database connection
conn = psycopg2.connect(
    host='localhost',
    database='TwitterProject',
    user='postgres',
    password='FK225280146'
)

cursor = conn.cursor()

# Create the 'tweets' table if it does not exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tweets (
        id SERIAL PRIMARY KEY, 
        tweet TEXT, 
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
""")

# Authenticate to Twitter
auth = tweepy.OAuthHandler("YOUR_API_KEY", "YOUR_API_SECRET")
auth.set_access_token("YOUR_ACCESS_TOKEN", "YOUR_ACCESS_SECRET")
api = tweepy.API(auth, wait_on_rate_limit=True)

# Define a stream listener
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        tweet = status.text
        try:
            cursor.execute("INSERT INTO tweets (tweet) VALUES (%s)", (tweet,))
            conn.commit()
        except Exception as e:
            print(e)

# Set up a stream
my_listener = MyStreamListener()
my_stream = tweepy.Stream(auth=api.auth, listener=my_listener)

# Start streaming tweets about a specific topic
my_stream.filter(track=['python'], is_async=True)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout of the Dash app
app.layout = html.Div([
    dcc.Interval(id='interval-component', interval=5*1000, n_intervals=0),
    html.H1("Real-Time Twitter Dashboard"),
    dcc.Graph(id='live-update-graph')
])

# Callback to update the graph
@app.callback(Output('live-update-graph', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph_live(n):
    cursor.execute("SELECT timestamp, tweet FROM tweets ORDER BY timestamp DESC LIMIT 100")
    rows = cursor.fetchall()
    df = pd.DataFrame(rows, columns=['timestamp', 'tweet'])
    fig = px.scatter(df, x='timestamp', y='tweet', title='Twitter Data Over Time')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
