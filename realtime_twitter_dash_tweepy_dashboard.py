# pip install dash-bootstrap-components
# Ensure libraries are installed (not a real code, just a reminder for setup)
# pip install dash dash-bootstrap-components tweepy psycopg2-binary pandas plotly

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
    user='Your User',
    password='Your Pass'
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

# Authenticate to Twitter using OAuth handler
#auth = tweepy.OAuthHandler("YOUR_API_KEY", "YOUR_API_SECRET")
#auth.set_access_token("YOUR_ACCESS_TOKEN", "YOUR_ACCESS_SECRET")
auth = tweepy.OAuthHandler("YOUR_API_KEY", "YOUR_API_SECRET")
auth.set_access_token("YOUR_ACCESS_TOKEN", "YOUR_ACCESS_SECRET")

# Define a stream listener using the new `tweepy.StreamingClient`
class MyStream(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        tweet_text = tweet.text
        try:
            cursor.execute("INSERT INTO tweets (tweet) VALUES (%s)", (tweet_text,))
            conn.commit()
        except Exception as e:
            print(e)

# Set up a stream using the updated API with the correct bearer token
my_stream = MyStream("YOUR_CORRECT_BEARER_TOKEN")  # Replace YOUR_CORRECT_BEARER_TOKEN with actual bearer token

# Start streaming tweets about a specific topic
try:
    my_stream.add_rules(tweepy.StreamRule("python"), dry_run=False)  # Add rule for filtering tweets
    my_stream.filter()  # This starts the stream with the added rules
except Exception as e:
    print(f"An error occurred: {e}")


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
