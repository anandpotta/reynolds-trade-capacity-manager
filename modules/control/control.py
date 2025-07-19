from dash import html

def create_control_layout():
    """Create the control table page layout"""
    return html.Div([
        html.H4("Control Table", className="mb-3"),
        html.P("View and manage control settings.", className="text-muted"),
        html.Div("Control table content will be implemented here.", 
                className="bg-white p-4 rounded shadow-sm card-animate")
    ], className="control-page page-container", style={'paddingLeft': '60px', 'paddingTop': '20px', 'paddingRight': '20px'})