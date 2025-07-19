from dash import html

def create_capacity_layout():
    """Create the capacity simulation page layout"""
    return html.Div([
        html.H4("Capacity Simulation", className="mb-3"),
        html.P("Simulate and analyze capacity scenarios.", className="text-muted"),
        html.Div("Capacity simulation content will be implemented here.", 
                className="bg-white p-4 rounded shadow-sm card-animate")
    ], className="capacity-page page-container", style={'paddingLeft': '60px', 'paddingTop': '20px', 'paddingRight': '20px'})