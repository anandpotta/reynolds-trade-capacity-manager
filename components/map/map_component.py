import plotly.graph_objects as go
from dash import dcc
import dash_bootstrap_components as dbc
import pandas as pd

def create_choropleth_map():
    """Create the US choropleth map showing capacity by state"""
    
    # Sample data for US states
    states_data = {
        'state': ['CA', 'TX', 'FL', 'NY', 'OR', 'WA', 'NV', 'AZ', 'CO', 'NM', 
                  'UT', 'ID', 'MT', 'WY', 'ND', 'SD', 'NE', 'KS', 'OK', 'MN',
                  'IA', 'MO', 'AR', 'LA', 'WI', 'IL', 'MS', 'AL', 'TN', 'KY',
                  'IN', 'MI', 'OH', 'WV', 'VA', 'NC', 'SC', 'GA', 'PA', 'MD',
                  'DE', 'NJ', 'CT', 'RI', 'MA', 'VT', 'NH', 'ME', 'AK', 'HI'],
        'capacity': [95, 88, 92, 87, 96, 94, 45, 85, 82, 78,
                    80, 48, 83, 52, 89, 55, 58, 60, 86, 91,
                    57, 85, 62, 88, 90, 92, 65, 68, 70, 72,
                    88, 89, 87, 75, 78, 82, 80, 91, 86, 84,
                    82, 88, 85, 83, 89, 87, 86, 88, 45, 92]
    }
    
    df = pd.DataFrame(states_data)
    
    # Create the choropleth map
    fig = go.Figure(data=go.Choropleth(
        locations=df['state'],
        z=df['capacity'],
        locationmode='USA-states',
        colorscale=[
            [0.0, '#e8eaf6'],  # Light blue for low values
            [0.5, '#ffeb3b'],  # Yellow for medium values
            [0.8, '#ff9800'],  # Orange for high values
            [1.0, '#ff5722']   # Red for highest values
        ],
        text=df['state'],
        hovertemplate='<b>%{text}</b><br>Capacity: %{z}%<extra></extra>',
        colorbar=dict(
            title=dict(
                text="Capacity %",
                font=dict(size=10)
            ),
            thickness=10,
            len=0.6,
            x=0.95,
            tickfont=dict(size=9),
            tickmode='array',
            tickvals=[0, 50, 100],
            ticktext=['0%', '50%', '100%']
        )
    ))
    
    fig.update_layout(
        geo=dict(
            scope='usa',
            projection=go.layout.geo.Projection(type='albers usa'),
            showlakes=False,
            bgcolor='rgba(0,0,0,0)',
            lakecolor='rgb(255, 255, 255)',
        ),
        margin=dict(l=0, r=0, t=0, b=0),
        height=400,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        hoverlabel=dict(
            bgcolor="white",
            font_size=12,
            font_family="Arial"
        )
    )
    
    return dcc.Graph(
        id='capacity-map',
        figure=fig,
        config={'displayModeBar': False},
        style={'height': '400px'}
    )


def create_map_controls():
    """Create the map control buttons"""
    return [
        dbc.ButtonGroup([
            dbc.Button('Cycle info', id='btn-cycle', color='primary', outline=True, size='sm'),
            dbc.Button('By Map', id='btn-map', color='primary', outline=False, size='sm'),
            dbc.Button('By Graph', id='btn-graph', color='primary', outline=True, size='sm')
        ], className='mb-3'),
        
        # Organize data by buttons
        dcc.Dropdown(
            id='organize-by-dropdown',
            options=[
                {'label': 'By Area', 'value': 'area'},
                {'label': 'By State', 'value': 'state'}
            ],
            value='area',
            clearable=False,
            style={'width': '120px', 'fontSize': '0.8rem', 'display': 'inline-block'}
        )
    ]