from dash import html, dcc
import dash_bootstrap_components as dbc
from components.filters.filters import create_filters_section
from components.map.map_component import create_choropleth_map, create_map_controls
from components.grid.grid_component import create_capacity_grid

def create_overview_layout():
    """Create the overview page layout"""
    
    layout = html.Div([
        # Main container with proper spacing
        html.Div([
            # Filters section
            html.Div([
                create_filters_section()
            ], className="filter-container mb-4", style={
                'backgroundColor': 'white',
                'padding': '24px',
                'borderRadius': '8px',
                'boxShadow': '0 1px 3px rgba(0,0,0,0.08)'
            }),
            
            # Map and Grid Row
            dbc.Row([
                # Map Column
                dbc.Col([
                    html.Div([
                        # Map Header
                        html.Div([
                            html.H5("By Map > North America", style={
                                'fontSize': '16px',
                                'fontWeight': '600',
                                'color': '#1e293b',
                                'marginBottom': '16px'
                            }),
                            
                            # Map controls
                            html.Div([
                                html.Div(create_map_controls()[0], className="me-3"),
                                html.Div([
                                    html.Span("Organize data by: ", style={
                                        'fontSize': '14px',
                                        'color': '#64748b',
                                        'marginRight': '8px'
                                    }),
                                    create_map_controls()[1]
                                ], style={'display': 'flex', 'alignItems': 'center'})
                            ], style={
                                'display': 'flex',
                                'alignItems': 'center',
                                'justifyContent': 'space-between',
                                'marginBottom': '16px'
                            }),
                        ], style={'marginBottom': '16px'}),
                        
                        # Map container
                        html.Div(id='map-container', children=[
                            create_choropleth_map()
                        ], className="map-wrapper"),
                        
                        # Graph container (hidden by default)
                        html.Div(id='graph-container', style={'display': 'none'})
                    ], className="dashboard-card h-100")
                ], width=6, className="mb-4"),
                
                # Grid Column
                dbc.Col([
                    html.Div([
                        create_capacity_grid()
                    ], className="dashboard-card h-100")
                ], width=6, className="mb-4")
            ], className="g-4")
        ], style={
            'paddingLeft': '60px',
            'paddingTop': '24px',
            'paddingRight': '24px',
            'paddingBottom': '24px',
            'backgroundColor': '#f5f6fa',
            'minHeight': '100vh'
        })
    ], className="overview-page page-enter")
    
    return layout