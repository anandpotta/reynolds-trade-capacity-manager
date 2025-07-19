import dash_bootstrap_components as dbc
from dash import html, dcc
import pandas as pd

def create_filter_dropdown(filter_id, label, options=None, default_values=None):
    """Create a filter dropdown with checkbox selection and count display"""
    
    # Default options if none provided
    if options is None:
        options = []
    
    if default_values is None:
        default_values = []
    
    # Create the dropdown component
    dropdown = html.Div([
        # Label
        html.Label(label, style={
            'fontSize': '13px',
            'color': '#555',
            'fontWeight': '500',
            'marginBottom': '4px',
            'display': 'block'
        }),
        
        # Dropdown container
        dcc.Dropdown(
            id=f"{filter_id}-dropdown",
            options=[{"label": opt, "value": opt} for opt in options],
            value=default_values,
            multi=True,
            clearable=True,
            searchable=True,
            placeholder=f"Select {label}...",
            style={
                'fontSize': '14px',
                'minHeight': '38px',
                'width': '100%'
            },
            optionHeight=35
        ),
        
        # Store for selected values
        dcc.Store(id=f"{filter_id}-selected", data=default_values)
    ], style={'width': '100%'})
    



def create_filters_section():
    """Create the complete filters section with all dropdowns"""
    
    # Sample data for filters with more options
    activities = ["Trade Planning", "Trade Execution", "Trade Analysis", "Risk Management", 
                  "Portfolio Optimization", "Market Research", "Client Management", "Compliance"]
    cycles = ["Cycle 1", "Cycle 2", "Cycle 3", "Cycle 4", "Cycle 5", "Q1 2024", "Q2 2024", "Q3 2024"]
    areas = ["North America", "South America", "Europe", "Asia Pacific", "Middle East", 
             "Africa", "Central America", "Eastern Europe"]
    regions = ["US West", "US East", "US Central", "Canada", "Mexico", "UK", "Germany", 
               "France", "Japan", "China", "Australia", "Brazil"]
    divisions = ["Technology", "Healthcare", "Finance", "Energy", "Consumer Goods", 
                 "Industrial", "Real Estate", "Telecommunications"]
    territories = ["California", "New York", "Texas", "Florida", "Illinois", "Pennsylvania",
                   "Ohio", "Georgia", "North Carolina", "Michigan", "New Jersey", "Virginia"]
    
    return html.Div([
        html.Div([
            html.Span("Current Cycle Overview", style={
                'fontSize': '24px',
                'fontWeight': '600',
                'color': '#1a1a1a'
            })
        ], style={'marginBottom': '24px'}),
        
        # Filters row
        dbc.Row([
            dbc.Col(create_filter_dropdown("activity", "Activity", activities, ["Trade Planning"]), width=2),
            dbc.Col(create_filter_dropdown("cycle", "Cycle", cycles, ["Cycle 3"]), width=2),
            dbc.Col(create_filter_dropdown("area", "Area", areas, []), width=2),
            dbc.Col(create_filter_dropdown("region", "Region", regions, []), width=2),
            dbc.Col(create_filter_dropdown("division", "Division", divisions, []), width=2),
            dbc.Col(create_filter_dropdown("territory", "Territory", territories, []), width=2),
        ], className="g-3", style={'marginBottom': '24px'})
    ])