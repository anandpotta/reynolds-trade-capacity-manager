from dash import html

def create_activities_layout():
    """Create the activities management page layout"""
    return html.Div([
        html.H4("Activities Management", className="mb-3"),
        html.P("Manage your trade activities here.", className="text-muted"),
        html.Div("Activities content will be implemented here.", 
                className="bg-white p-4 rounded shadow-sm card-animate")
    ], className="activities-page page-container", style={'paddingLeft': '60px', 'paddingTop': '20px', 'paddingRight': '20px'})