from dash import html, dcc, callback, Input, Output, State, ALL
import dash_bootstrap_components as dbc


def create_multiselect_dropdown(dropdown_id, label, options, default_values=None):
    """Create a multiselect dropdown with checkboxes and count display"""
    
    # Convert options to list of dicts if they're strings
    if options and isinstance(options[0], str):
        options = [{"label": opt, "value": opt} for opt in options]
    
    # Default to empty list if no default values
    if default_values is None:
        default_values = []
    
    return html.Div([
        # Label
        html.Label(label, style={
            'fontSize': '12px',
            'color': '#666',
            'fontWeight': '500',
            'marginBottom': '4px',
            'display': 'block'
        }),
        
        # Dropdown container
        html.Div([
            # Display selected values or placeholder
            html.Div(
                id=f"{dropdown_id}-display",
                children="Select...",
                style={
                    'border': '1px solid #ddd',
                    'borderRadius': '4px',
                    'padding': '8px 35px 8px 12px',
                    'backgroundColor': 'white',
                    'cursor': 'pointer',
                    'fontSize': '14px',
                    'color': '#333',
                    'position': 'relative',
                    'minHeight': '38px',
                    'display': 'flex',
                    'alignItems': 'center'
                },
                n_clicks=0
            ),
            
            # Dropdown arrow
            html.I(className="fas fa-chevron-down", style={
                'position': 'absolute',
                'right': '12px',
                'top': '50%',
                'transform': 'translateY(-50%)',
                'color': '#666',
                'fontSize': '12px',
                'pointerEvents': 'none'
            }),
            
            # Dropdown menu
            html.Div(
                id=f"{dropdown_id}-menu",
                children=[
                    # Select All option
                    html.Div([
                        dcc.Checklist(
                            id=f"{dropdown_id}-select-all",
                            options=[{"label": "Select All", "value": "all"}],
                            value=[],
                            style={'marginBottom': '8px'},
                            inputStyle={'marginRight': '8px'}
                        ),
                        html.Hr(style={'margin': '8px 0'}),
                        
                        # Options with checkboxes
                        dcc.Checklist(
                            id=f"{dropdown_id}-checklist",
                            options=options,
                            value=default_values,
                            style={'maxHeight': '200px', 'overflowY': 'auto'},
                            inputStyle={'marginRight': '8px'},
                            labelStyle={
                                'display': 'block',
                                'padding': '4px 0',
                                'cursor': 'pointer',
                                'fontSize': '14px'
                            }
                        )
                    ], style={'padding': '8px'})
                ],
                style={
                    'position': 'absolute',
                    'top': '100%',
                    'left': '0',
                    'right': '0',
                    'backgroundColor': 'white',
                    'border': '1px solid #ddd',
                    'borderRadius': '4px',
                    'boxShadow': '0 2px 8px rgba(0,0,0,0.1)',
                    'marginTop': '2px',
                    'zIndex': '1000',
                    'display': 'none'  # Initially hidden
                },
                className=f"dropdown-menu-{dropdown_id}"
            ),
            
            # Hidden store for dropdown state
            dcc.Store(id=f"{dropdown_id}-is-open", data=False)
            
        ], style={'position': 'relative'})
    ], style={'marginBottom': '16px'})