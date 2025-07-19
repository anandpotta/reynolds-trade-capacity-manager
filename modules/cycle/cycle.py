from dash import html

def create_cycle_layout():
    """Create the cycle management page layout"""
    return html.Div([
        html.H4("Cycle Management", className="mb-3"),
        html.P("Manage your trading cycles.", className="text-muted"),
        html.Div("Cycle management content will be implemented here.", 
                className="bg-white p-4 rounded shadow-sm card-animate")
    ], className="cycle-page page-container", style={'paddingLeft': '60px', 'paddingTop': '20px', 'paddingRight': '20px'})