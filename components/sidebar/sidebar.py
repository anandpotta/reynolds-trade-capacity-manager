import dash_bootstrap_components as dbc
from dash import html, dcc
import base64

def create_sidebar():
    """Create the sidebar navigation component"""
    
    # Navigation items
    nav_items = [
        {"id": "overview", "icon": "fa-th", "label": "Overview", "path": "/"},
        {"id": "activities", "icon": "fa-tasks", "label": "Activities Management", "path": "/activities"},
        {"id": "capacity", "icon": "fa-chart-line", "label": "Capacity Simulation", "path": "/capacity"},
        {"id": "cycle", "icon": "fa-sync", "label": "Cycle management", "path": "/cycle"},
        {"id": "control", "icon": "fa-table", "label": "Control Table", "path": "/control"}
    ]
    
    # Create navigation links
    nav_links = []
    for item in nav_items:
        nav_link = dbc.NavLink(
            [
                html.I(className=f"fas {item['icon']} me-2", style={'width': '20px', 'textAlign': 'center'}),
                html.Span(item['label'], className="nav-label")
            ],
            href=item['path'],
            active="exact",
            className="nav-link-custom",
            id=f"nav-{item['id']}"
        )
        nav_links.append(html.Li(nav_link, className="nav-item"))
    
    sidebar = html.Div([
        # Logo section
        html.Div([
            html.Img(src="/assets/reynolds-logo.png", 
                    style={'width': '40px', 'height': '40px', 'marginRight': '10px'}),
            html.Span("REYNOLDS", className="logo-text", 
                     style={'fontSize': '1.2rem', 'fontWeight': 'bold', 'color': '#1a237e'})
        ], className="logo-section d-flex align-items-center p-3", 
           style={'borderBottom': '1px solid #e0e0e0'}),
        
        # Title
        html.Div([
            html.P("Welcome to your", style={'fontSize': '0.75rem', 'color': '#666', 'marginBottom': '0'}),
            html.H6("Capacity management", style={'fontSize': '0.9rem', 'fontWeight': '600', 'marginBottom': '0'})
        ], className="px-3 py-2", style={'borderBottom': '1px solid #e0e0e0'}),
        
        # Navigation
        html.Nav([
            html.Ul(nav_links, className="nav flex-column", style={'padding': '0'})
        ], className="sidebar-nav flex-grow-1", style={'overflowY': 'auto'}),
        
        # Footer section with user info and settings
        html.Div([
            # Settings link
            html.Div([
                html.A([
                    html.I(className="fas fa-bell me-2"),
                    html.Span("Notification")
                ], href="#", className="text-decoration-none text-muted d-flex align-items-center py-2",
                   style={'fontSize': '0.85rem'})
            ], className="px-3", style={'borderTop': '1px solid #e0e0e0'}),
            
            html.Div([
                html.A([
                    html.I(className="fas fa-cog me-2"),
                    html.Span("Settings")
                ], href="#", className="text-decoration-none text-muted d-flex align-items-center py-2",
                   style={'fontSize': '0.85rem'})
            ], className="px-3"),
            
            # Logout button
            html.Div([
                html.Button([
                    html.I(className="fas fa-sign-out-alt me-2"),
                    html.Span("Logout")
                ], id="logout-button", className="btn btn-link text-danger d-flex align-items-center py-2",
                   style={'fontSize': '0.85rem', 'fontWeight': '500', 'border': 'none', 
                          'background': 'none', 'textDecoration': 'none', 'padding': '0.5rem 0',
                          'width': '100%', 'textAlign': 'left'}, n_clicks=0)
            ], className="px-3"),
            
            # User info
            html.Div([
                html.Div([
                    html.Div([
                        html.Div("JL", className="user-avatar",
                                style={'width': '32px', 'height': '32px', 
                                      'borderRadius': '50%', 'backgroundColor': '#ff9800',
                                      'color': 'white', 'display': 'flex', 
                                      'alignItems': 'center', 'justifyContent': 'center',
                                      'fontSize': '0.85rem', 'fontWeight': 'bold'}),
                    ], className="me-2"),
                    html.Div([
                        html.Div("James Lawrence", style={'fontSize': '0.85rem', 'fontWeight': '500'}),
                        html.Div("View Profile", style={'fontSize': '0.7rem', 'color': '#666'})
                    ])
                ], className="d-flex align-items-center")
            ], className="px-3 py-3", style={'borderTop': '1px solid #e0e0e0', 'backgroundColor': '#f8f9fa'})
        ])
    ], id="sidebar", className="sidebar", style={
        'position': 'fixed',
        'top': '0',
        'left': '-280px',  # Hidden by default
        'width': '280px',
        'height': '100vh',
        'backgroundColor': 'white',
        'boxShadow': '2px 0 5px rgba(0,0,0,0.1)',
        'transition': 'left 0.3s ease-in-out',
        'zIndex': '1050',
        'display': 'flex',
        'flexDirection': 'column'
    })
    
    return sidebar


def create_hamburger_menu():
    """Create the hamburger menu button"""
    return html.Div([
        html.Button([
            html.I(className="fas fa-bars")
        ], id="hamburger-menu", className="btn btn-light shadow-sm",
           style={
               'padding': '10px 15px',
               'border': '1px solid #dee2e6',
               'borderRadius': '6px',
               'backgroundColor': 'white',
               'color': '#495057',
               'fontSize': '18px',
               'cursor': 'pointer',
               'transition': 'all 0.2s ease',
               'display': 'flex',
               'alignItems': 'center',
               'justifyContent': 'center'
           },
           n_clicks=0)
    ], style={
        'position': 'fixed',
        'top': '20px',
        'left': '20px',
        'zIndex': '1200',
        'pointerEvents': 'auto'
    })