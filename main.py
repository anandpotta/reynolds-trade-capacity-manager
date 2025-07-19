import os
import dash
from dash import Dash, html, dcc, Input, Output, State, ALL
import dash_bootstrap_components as dbc
import dash_ag_grid as dag
from dash.exceptions import PreventUpdate
import plotly.graph_objects as go
from werkzeug.security import check_password_hash, generate_password_hash

# Initialize the Dash app with Bootstrap theme
dash_app = Dash(__name__, 
           external_stylesheets=[dbc.themes.BOOTSTRAP, 
                                "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"],
           suppress_callback_exceptions=True,
           title="Reynolds Trade Capacity Manager",
           assets_folder='static')

# Set the secret key for sessions
dash_app.server.secret_key = os.environ.get("SESSION_SECRET", "demo-secret-key-for-development")

# Demo user credentials
DEMO_USERS = {
    'demo@reynolds.com': {
        'password_hash': generate_password_hash('demo123'),
        'name': 'Demo User'
    },
    'admin@reynolds.com': {
        'password_hash': generate_password_hash('admin123'),
        'name': 'Admin User'
    }
}

# Function to create SSO login form
def create_sso_login_form():
    return html.Div([
        # Alert for messages - preserved when switching forms
        html.Div(id="login-alert", style={'marginBottom': '1rem', 'minHeight': '40px'}),
        html.H3("Sign In", style={'fontSize': '1.375rem', 'fontWeight': '500', 'color': '#2d3748', 'marginBottom': '0.125rem', 'textAlign': 'center'}),
        html.P("Let's build something great", style={'color': '#a0aec0', 'fontSize': '0.75rem', 'marginBottom': '1.75rem', 'textAlign': 'center', 'fontWeight': '400'}),
        
        # SSO message
        html.P("Single Sign On is enabled in your organization. Use your organization's network to sign in.", 
               style={'color': '#4a5568', 'fontSize': '0.8125rem', 'textAlign': 'center', 
                      'marginBottom': '2rem', 'lineHeight': '1.5'}),
        
        # SSO Login button
        dbc.Button(
            "Click here to login",
            id="sso-login-button",
            style={
                'backgroundColor': '#1e3c72',
                'border': 'none',
                'borderRadius': '5px',
                'padding': '0.625rem 1.5rem',
                'fontSize': '0.875rem',
                'fontWeight': '500',
                'color': '#ffffff',
                'width': '100%',
                'marginBottom': '1.5rem',
                'height': '42px',
                'boxShadow': '0 1px 3px rgba(30, 60, 114, 0.15)'
            },
            n_clicks=0
        ),
        
        # Contact administrator text
        html.P("Contact your site administrator to request access.", 
               style={'color': '#a0aec0', 'fontSize': '0.75rem', 'textAlign': 'center', 
                      'marginBottom': 0})
    ])

# Custom CSS styles that match the screenshot exactly
custom_styles = {
    'login_container': {
        'minHeight': '100vh',
        'background': '''linear-gradient(rgba(30, 60, 114, 0.8), rgba(42, 82, 152, 0.8)), 
                         url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='100' height='100' viewBox='0 0 100 100'%3E%3Cg fill-opacity='0.1'%3E%3Cpolygon fill='white' points='50 0 60 40 100 50 60 60 50 100 40 60 0 50 40 40'/%3E%3C/g%3E%3C/svg%3E")''',
        'backgroundColor': '#1e3c72',
        'backgroundSize': 'cover, 100px 100px',
        'backgroundPosition': 'center',
        'position': 'relative',
        'overflow': 'hidden'
    },
    'overlay': {
        'position': 'absolute',
        'top': 0,
        'left': 0,
        'right': 0,
        'bottom': 0,
        'backgroundColor': 'rgba(0, 0, 0, 0.4)',
        'backgroundImage': '''linear-gradient(45deg, transparent 30%, rgba(255,255,255,0.02) 50%, transparent 70%),
                              linear-gradient(-45deg, transparent 30%, rgba(255,255,255,0.02) 50%, transparent 70%)''',
        'zIndex': 1
    },
    'content_wrapper': {
        'position': 'relative',
        'zIndex': 2,
        'minHeight': '100vh',
        'display': 'flex',
        'flexDirection': 'column'
    },
    'login_card': {
        'backgroundColor': '#ffffff',
        'borderRadius': '10px',
        'boxShadow': '0 10px 30px rgba(0, 0, 0, 0.15)',
        'padding': '2rem 1.75rem',
        'width': '100%',
        'maxWidth': '380px',
        'margin': '0 auto'
    },
    'brand_section': {
        'textAlign': 'left',
        'padding': '2rem',
        'color': 'white'
    },
    'logo_text': {
        'fontSize': '2.5rem',
        'fontWeight': '300',
        'letterSpacing': '0.2em',
        'marginBottom': '0.5rem',
        'color': '#ffffff'
    },
    'tagline': {
        'fontSize': '0.9rem',
        'color': '#b8c5d1',
        'marginBottom': 0,
        'letterSpacing': '0.1em'
    },
    'welcome_title': {
        'fontSize': '2.2rem',
        'fontWeight': '400',
        'color': '#ffffff',
        'marginBottom': '1rem'
    },
    'welcome_subtitle': {
        'fontSize': '1.1rem',
        'color': '#b8c5d1',
        'marginBottom': 0
    },
    'login_button': {
        'background': 'linear-gradient(135deg, #1e3c72 0%, #2a5298 100%)',
        'border': 'none',
        'borderRadius': '4px',
        'padding': '0.75rem 1.5rem',
        'fontSize': '1rem',
        'fontWeight': '500',
        'color': '#ffffff',
        'width': '100%',
        'marginTop': '1rem',
        'marginBottom': '1rem'
    },
    'footer': {
        'position': 'absolute',
        'bottom': 0,
        'left': 0,
        'right': 0,
        'backgroundColor': 'rgba(0, 0, 0, 0.2)',
        'padding': '1rem 0',
        'zIndex': 3,
        'color': '#b8c5d1',
        'fontSize': '0.8rem'
    },
    'demo_info': {
        'position': 'fixed',
        'top': '20px',
        'right': '20px',
        'maxWidth': '300px',
        'zIndex': 1000
    }
}

# Login layout
def create_login_layout():
    return html.Div([
        # Main container
        html.Div([
            # Overlay
            html.Div(style=custom_styles['overlay']),
            
            # Content wrapper
            html.Div([
                # Main content area
                dbc.Container([
                    dbc.Row([
                        # Left side - Branding
                        dbc.Col([
                            html.Div([
                                # Reynolds logo
                                html.Img(
                                    src='/assets/reynolds-logo.png',
                                    style={
                                        'width': '280px',
                                        'height': 'auto',
                                        'marginBottom': '2rem'
                                    }
                                ),
                                
                                # Welcome text
                                html.Div([
                                    html.H2("Welcome to Reynolds", style={
                                        'fontSize': '1.875rem',
                                        'fontWeight': '400',
                                        'color': '#ffffff',
                                        'marginBottom': '0.5rem'
                                    }),
                                    html.P("This is your Trade capacity manager", style={
                                        'fontSize': '0.9375rem',
                                        'color': 'rgba(255, 255, 255, 0.8)',
                                        'marginBottom': 0
                                    })
                                ])
                            ], style={'textAlign': 'left', 'padding': '1.5rem', 'color': 'white'})
                        ], lg=6, className="d-flex align-items-center justify-content-center"),
                        
                        # Right side - Login Form
                        dbc.Col([
                            html.Div([
                                # Form container
                                html.Div(id='login-form-container', children=[
                                    # Alert for messages - now inside the form
                                    html.Div(id="login-alert", style={'marginBottom': '1rem', 'minHeight': '40px'}),
                                    html.H3("Sign In", style={'fontSize': '1.375rem', 'fontWeight': '500', 'color': '#2d3748', 'marginBottom': '0.125rem', 'textAlign': 'center'}),
                                    html.P("Let's build something great", style={'color': '#a0aec0', 'fontSize': '0.75rem', 'marginBottom': '1.5rem', 'textAlign': 'center', 'fontWeight': '400'}),
                                
                                # Email input
                                html.Div([
                                    dbc.Label("Enter your E-mail id", style={'fontWeight': '400', 'color': '#495057', 'fontSize': '0.8125rem', 'marginBottom': '0.375rem'}),
                                    dbc.Input(
                                        type="email",
                                        id="email-input",
                                        placeholder="Enter your password",  # This matches the screenshot
                                        style={'borderRadius': '5px', 'padding': '0.5rem 0.75rem', 'fontSize': '0.8125rem', 
                                               'border': '1px solid #ced4da', 'backgroundColor': '#fafbfc', 
                                               'height': '38px'}
                                    )
                                ], style={'marginBottom': '1rem'}),
                                
                                # Password input
                                html.Div([
                                    dbc.Label("Enter your Password", style={'fontWeight': '400', 'color': '#495057', 'fontSize': '0.8125rem', 'marginBottom': '0.375rem'}),
                                    html.Div([
                                        dbc.Input(
                                            type="password",
                                            id="password-input",
                                            placeholder="Enter your password",
                                            style={'borderRadius': '5px', 'padding': '0.5rem 2.25rem 0.5rem 0.75rem', 
                                                   'fontSize': '0.8125rem', 'border': '1px solid #ced4da', 
                                                   'backgroundColor': '#fafbfc', 'width': '100%', 
                                                   'height': '38px'}
                                        ),
                                        html.I(id="password-toggle", className="fas fa-eye", 
                                               style={'position': 'absolute', 'right': '10px', 'top': '50%', 
                                                      'transform': 'translateY(-50%)', 'cursor': 'pointer', 
                                                      'color': '#6c757d', 'fontSize': '0.75rem'})
                                    ], style={'position': 'relative'})
                                ], style={'marginBottom': '1.25rem'}),
                                
                                # Login button
                                dbc.Button(
                                    "Login",
                                    id="login-button",
                                    style={
                                        'backgroundColor': '#1e3c72',
                                        'border': 'none',
                                        'borderRadius': '5px',
                                        'padding': '0.5rem 1.5rem',
                                        'fontSize': '0.875rem',
                                        'fontWeight': '500',
                                        'color': '#ffffff',
                                        'width': '100%',
                                        'marginTop': '0.25rem',
                                        'marginBottom': '0.75rem',
                                        'height': '38px',
                                        'boxShadow': '0 1px 3px rgba(30, 60, 114, 0.15)'
                                    },
                                    n_clicks=0
                                ),
                                
                                # Forgot password link
                                html.Div([
                                    html.Span("Cannot remember your password? ", style={'color': '#6c757d', 'fontSize': '0.75rem'}),
                                    html.A("Click here", href="#", id="forgot-password-link", 
                                          style={'color': '#0066cc', 'textDecoration': 'none', 'fontSize': '0.75rem'})
                                ], style={'textAlign': 'center'})
                                ], style=custom_styles['login_card'])
                            ], style={'position': 'relative'})
                        ], lg=6, className="d-flex align-items-center justify-content-center")
                    ], className="h-100 align-items-center", style={'minHeight': 'calc(100vh - 100px)'})
                ], fluid=True),
                
                # Login options (By Email / By SSO) - positioned in bottom right
                html.Div([
                    html.Div([
                        dbc.Button("By Email", 
                                 id='by-email-btn',
                                 color="link",
                                 style={'color': '#ffffff', 'fontSize': '0.75rem', 
                                        'cursor': 'pointer', 'marginRight': '1rem',
                                        'fontWeight': '400', 'padding': '0.25rem 0.5rem',
                                        'textDecoration': 'none'}),
                        dbc.Button("By SSO", 
                                 id='by-sso-btn',
                                 color="link",
                                 style={'color': 'rgba(255, 255, 255, 0.5)', 
                                        'fontSize': '0.75rem', 
                                        'padding': '0.25rem 0.75rem', 
                                        'borderRadius': '3px',
                                        'cursor': 'pointer',
                                        'backgroundColor': 'rgba(255, 255, 255, 0.1)',
                                        'fontWeight': '400', 'textDecoration': 'none'})
                    ], style={'textAlign': 'right', 'paddingRight': '2.5rem', 'display': 'flex', 'justifyContent': 'flex-end', 'alignItems': 'center'})
                ], style={
                    'position': 'absolute',
                    'bottom': '50px',
                    'right': '20px',
                    'zIndex': 10
                }),
                
                # Footer
                html.Footer([
                    html.Div([
                        html.P("© 2025 Reynolds, Incorporated and its Affiliates. All Rights Reserved", 
                              style={'marginBottom': 0, 'fontSize': '0.75rem', 'color': 'rgba(255, 255, 255, 0.6)',
                                     'textAlign': 'center', 'width': '100%', 'margin': '0 auto'})
                    ], style={'display': 'flex', 'justifyContent': 'center', 'width': '100%'})
                ], style={
                    'position': 'absolute',
                    'bottom': 0,
                    'left': 0,
                    'right': 0,
                    'backgroundColor': 'rgba(0, 0, 0, 0.2)',
                    'padding': '1rem 0',
                    'zIndex': 1,
                    'textAlign': 'center'
                })
            ], style=custom_styles['content_wrapper'])
        ], style=custom_styles['login_container']),
        

        
        # Store for session data
        dcc.Store(id='session-store', storage_type='session'),
        # Store for login mode (email or sso)
        dcc.Store(id='login-mode-store', data={'mode': 'email'}),
        # Store for alert messages
        dcc.Store(id='alert-message-store', data=None),
        # Interval for auto-hiding alerts (5 seconds)
        dcc.Interval(id='alert-interval', interval=1000, n_intervals=0, disabled=True, max_intervals=5)
    ])

# Import additional components
from components.sidebar.sidebar import create_sidebar, create_hamburger_menu
from modules.overview.overview import create_overview_layout
from modules.activities.activities import create_activities_layout
from modules.capacity.capacity import create_capacity_layout
from modules.cycle.cycle import create_cycle_layout
from modules.control.control import create_control_layout

# Dashboard layout with sidebar and routing
def create_dashboard_layout(user_name="User", user_email=""):
    return html.Div([
        # Sidebar overlay
        html.Div(id='sidebar-overlay', className='sidebar-overlay', n_clicks=0, style={
            'position': 'fixed',
            'top': '0',
            'left': '0',
            'width': '100vw',
            'height': '100vh',
            'backgroundColor': 'rgba(0, 0, 0, 0)',
            'zIndex': '999',
            'pointerEvents': 'none',
            'transition': 'background-color 0.3s ease'
        }),
        
        # Sidebar
        create_sidebar(),
        
        # Hamburger menu
        create_hamburger_menu(),
        

        
        # Main content area
        html.Div([
            # Content container - Start with overview page
            html.Div(id='dashboard-page-content', children=create_overview_layout(), style={
                'backgroundColor': '#f5f6fa',
                'minHeight': '100vh'
            })
        ], style={'marginLeft': '0', 'transition': 'margin-left 0.3s ease-in-out'}, id='main-content', className='content-wrapper'),
        
        # Store for sidebar state
        dcc.Store(id='sidebar-state', data={'isOpen': False}),
        
        # Store for user data
        dcc.Store(id='user-data', data={'name': user_name, 'email': user_email})
    ])

# Main app layout
dash_app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
    dcc.Store(id='session-data', storage_type='session')
])

# Callback for page routing
@dash_app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname'),
     Input('session-data', 'data')]
)
def display_page(pathname, session_data):
    if session_data and session_data.get('authenticated'):
        # Return the dashboard layout with routing capabilities
        return create_dashboard_layout(
            user_name=session_data.get('user_name', 'User'),
            user_email=session_data.get('user_email', '')
        )
    return create_login_layout()

# Callback for login - Bypass authentication for Plotly Dash Enterprise
@dash_app.callback(
    [Output('session-data', 'data'),
     Output('alert-message-store', 'data'),
     Output('url', 'pathname'),
     Output('alert-interval', 'disabled'),
     Output('alert-interval', 'n_intervals', allow_duplicate=True)],
    [Input('login-button', 'n_clicks')],
    [State('email-input', 'value'),
     State('password-input', 'value'),
     State('session-data', 'data')],
    prevent_initial_call=True
)
def handle_login(n_clicks, email, password, session_data):
    if not n_clicks:
        raise PreventUpdate
    
    # Force reset interval
    if not session_data:
        session_data = {}
    
    # Skip authentication - directly login for Plotly Dash Enterprise compatibility
    # Login successful - bypass credential checking
    new_session = {
        'authenticated': True,
        'user_email': email if email else 'user@reynolds.com',
        'user_name': 'Demo User'
    }
    return new_session, None, '/', True, 0

# Callback for logout
@dash_app.callback(
    [Output('session-data', 'data', allow_duplicate=True),
     Output('url', 'pathname', allow_duplicate=True)],
    [Input('logout-button', 'n_clicks')],
    prevent_initial_call=True
)
def handle_logout(n_clicks):
    if n_clicks:
        return {}, '/'
    raise PreventUpdate

# Callback for password toggle
@dash_app.callback(
    [Output('password-input', 'type'),
     Output('password-toggle', 'className')],
    [Input('password-toggle', 'n_clicks')],
    [State('password-input', 'type')],
    prevent_initial_call=True
)
def toggle_password(n_clicks, current_type):
    if n_clicks:
        if current_type == 'password':
            return 'text', 'fas fa-eye-slash'
        else:
            return 'password', 'fas fa-eye'
    return current_type, 'fas fa-eye'

# Callback for forgot password
@dash_app.callback(
    [Output('alert-message-store', 'data', allow_duplicate=True),
     Output('alert-interval', 'disabled', allow_duplicate=True),
     Output('alert-interval', 'n_intervals', allow_duplicate=True)],
    [Input('forgot-password-link', 'n_clicks')],
    prevent_initial_call=True
)
def handle_forgot_password(n_clicks):
    if n_clicks:
        return {"message": "Password reset functionality would be implemented here", "color": "info"}, False, 0
    raise PreventUpdate

# Callback to switch between email and SSO login
@dash_app.callback(
    [Output('login-form-container', 'children'),
     Output('by-email-btn', 'style'),
     Output('by-sso-btn', 'style')],
    [Input('by-email-btn', 'n_clicks'),
     Input('by-sso-btn', 'n_clicks')],
    [State('login-mode-store', 'data')],
    prevent_initial_call=False
)
def toggle_login_mode(email_clicks, sso_clicks, mode_data):
    ctx = dash.callback_context
    
    # Default styles
    email_style_active = {'color': '#ffffff', 'fontSize': '0.75rem', 'cursor': 'pointer', 'marginRight': '1rem', 'fontWeight': '400'}
    email_style_inactive = {'color': 'rgba(255, 255, 255, 0.5)', 'fontSize': '0.75rem', 'cursor': 'pointer', 'marginRight': '1rem', 'fontWeight': '400'}
    
    sso_style_active = {'color': '#ffffff', 'fontSize': '0.75rem', 'padding': '0.25rem 0.75rem', 'borderRadius': '3px', 'cursor': 'pointer', 'backgroundColor': 'rgba(255, 255, 255, 0.1)', 'fontWeight': '400'}
    sso_style_inactive = {'color': 'rgba(255, 255, 255, 0.5)', 'fontSize': '0.75rem', 'padding': '0.25rem 0.75rem', 'borderRadius': '3px', 'cursor': 'pointer', 'backgroundColor': 'rgba(255, 255, 255, 0.1)', 'fontWeight': '400'}
    
    # Determine which button was clicked
    if ctx.triggered:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        
        if button_id == 'by-sso-btn':
            # Return SSO form
            return create_sso_login_form(), email_style_inactive, sso_style_active
        else:
            # Return email form (default)
            email_form = html.Div([
                # Alert for messages - preserved when switching forms
                html.Div(id="login-alert", style={'marginBottom': '1rem', 'minHeight': '40px'}),
                html.H3("Sign In", style={'fontSize': '1.375rem', 'fontWeight': '500', 'color': '#2d3748', 'marginBottom': '0.125rem', 'textAlign': 'center'}),
                html.P("Let's build something great", style={'color': '#a0aec0', 'fontSize': '0.75rem', 'marginBottom': '1.5rem', 'textAlign': 'center', 'fontWeight': '400'}),
                

                
                # Email input
                html.Div([
                    dbc.Label("Enter your E-mail id", style={'fontWeight': '400', 'color': '#495057', 'fontSize': '0.8125rem', 'marginBottom': '0.375rem'}),
                    dbc.Input(
                        type="email",
                        id="email-input",
                        placeholder="Enter your email",
                        style={'borderRadius': '5px', 'padding': '0.5rem 0.75rem', 'fontSize': '0.8125rem', 
                               'border': '1px solid #ced4da', 'backgroundColor': '#fafbfc', 
                               'height': '38px'}
                    )
                ], style={'marginBottom': '1rem'}),
                
                # Password input
                html.Div([
                    dbc.Label("Enter your Password", style={'fontWeight': '400', 'color': '#495057', 'fontSize': '0.8125rem', 'marginBottom': '0.375rem'}),
                    html.Div([
                        dbc.Input(
                            type="password",
                            id="password-input",
                            placeholder="Enter your password",
                            style={'borderRadius': '5px', 'padding': '0.5rem 2.25rem 0.5rem 0.75rem', 
                                   'fontSize': '0.8125rem', 'border': '1px solid #ced4da', 
                                   'backgroundColor': '#fafbfc', 'width': '100%', 
                                   'height': '38px'}
                        ),
                        html.I(id='password-toggle', className='fas fa-eye', 
                              style={'position': 'absolute', 'right': '0.75rem', 'top': '50%', 
                                     'transform': 'translateY(-50%)', 'cursor': 'pointer', 
                                     'color': '#6c757d', 'fontSize': '0.75rem'})
                    ], style={'position': 'relative'})
                ], style={'marginBottom': '1.25rem'}),
                
                # Login button
                dbc.Button(
                    "Login",
                    id="login-button",
                    style={
                        'backgroundColor': '#1e3c72',
                        'border': 'none',
                        'borderRadius': '5px',
                        'padding': '0.5rem 1.5rem',
                        'fontSize': '0.875rem',
                        'fontWeight': '500',
                        'color': '#ffffff',
                        'width': '100%',
                        'marginTop': '0.25rem',
                        'marginBottom': '0.75rem',
                        'height': '38px',
                        'boxShadow': '0 1px 3px rgba(30, 60, 114, 0.15)'
                    },
                    n_clicks=0
                ),
                
                # Forgot password link
                html.Div([
                    html.Span("Cannot remember your password? ", style={'color': '#6c757d', 'fontSize': '0.75rem'}),
                    html.A("Click here", href="#", id="forgot-password-link", 
                          style={'color': '#0066cc', 'textDecoration': 'none', 'fontSize': '0.75rem'})
                ], style={'textAlign': 'center'})
            ])
            return email_form, email_style_active, sso_style_inactive
    
    # Default to email form
    email_form = html.Div([
        # Alert for messages - preserved when switching forms
        html.Div(id="login-alert", style={'marginBottom': '1rem', 'minHeight': '40px'}),
        html.H3("Sign In", style={'fontSize': '1.375rem', 'fontWeight': '500', 'color': '#2d3748', 'marginBottom': '0.125rem', 'textAlign': 'center'}),
        html.P("Let's build something great", style={'color': '#a0aec0', 'fontSize': '0.75rem', 'marginBottom': '1.5rem', 'textAlign': 'center', 'fontWeight': '400'}),
        

        
        # Email input
        html.Div([
            dbc.Label("Enter your E-mail id", style={'fontWeight': '400', 'color': '#495057', 'fontSize': '0.8125rem', 'marginBottom': '0.375rem'}),
            dbc.Input(
                type="email",
                id="email-input",
                placeholder="Enter your email",
                style={'borderRadius': '5px', 'padding': '0.5rem 0.75rem', 'fontSize': '0.8125rem', 
                       'border': '1px solid #ced4da', 'backgroundColor': '#fafbfc', 
                       'height': '38px'}
            )
        ], style={'marginBottom': '1rem'}),
        
        # Password input
        html.Div([
            dbc.Label("Enter your Password", style={'fontWeight': '400', 'color': '#495057', 'fontSize': '0.8125rem', 'marginBottom': '0.375rem'}),
            html.Div([
                dbc.Input(
                    type="password",
                    id="password-input",
                    placeholder="Enter your password",
                    style={'borderRadius': '5px', 'padding': '0.5rem 2.25rem 0.5rem 0.75rem', 
                           'fontSize': '0.8125rem', 'border': '1px solid #ced4da', 
                           'backgroundColor': '#fafbfc', 'width': '100%', 
                           'height': '38px'}
                ),
                html.I(id='password-toggle', className='fas fa-eye', 
                      style={'position': 'absolute', 'right': '0.75rem', 'top': '50%', 
                             'transform': 'translateY(-50%)', 'cursor': 'pointer', 
                             'color': '#6c757d', 'fontSize': '0.75rem'})
            ], style={'position': 'relative'})
        ], style={'marginBottom': '1.25rem'}),
        
        # Login button
        dbc.Button(
            "Login",
            id="login-button",
            style={
                'backgroundColor': '#1e3c72',
                'border': 'none',
                'borderRadius': '5px',
                'padding': '0.5rem 1.5rem',
                'fontSize': '0.875rem',
                'fontWeight': '500',
                'color': '#ffffff',
                'width': '100%',
                'marginTop': '0.25rem',
                'marginBottom': '0.75rem',
                'height': '38px',
                'boxShadow': '0 1px 3px rgba(30, 60, 114, 0.15)'
            },
            n_clicks=0
        ),
        
        # Forgot password link
        html.Div([
            html.Span("Cannot remember your password? ", style={'color': '#6c757d', 'fontSize': '0.75rem'}),
            html.A("Click here", href="#", id="forgot-password-link", 
                  style={'color': '#0066cc', 'textDecoration': 'none', 'fontSize': '0.75rem'})
        ], style={'textAlign': 'center'})
    ])
    return email_form, email_style_active, sso_style_inactive

# Callback to display alerts from store
@dash_app.callback(
    Output('login-alert', 'children'),
    [Input('alert-message-store', 'data')],
    prevent_initial_call=False
)
def display_alert(alert_data):
    if alert_data and alert_data.get('message'):
        return dbc.Alert(
            alert_data['message'],
            color=alert_data.get('color', 'danger'), 
            dismissable=True,
            is_open=True,
            className="alert-custom",
            style={
                'fontSize': '0.85rem',
                'padding': '0.75rem 2.5rem 0.75rem 1rem', 
                'marginBottom': '1rem',
                'boxShadow': '0 2px 4px rgba(0,0,0,0.1)',
                'border': '1px solid rgba(0,0,0,0.1)',
                'position': 'relative'
            }
        )
    return None

# Callback to auto-hide alerts after interval
@dash_app.callback(
    [Output('alert-message-store', 'data', allow_duplicate=True),
     Output('alert-interval', 'disabled', allow_duplicate=True),
     Output('alert-interval', 'n_intervals')],
    [Input('alert-interval', 'n_intervals')],
    [State('alert-message-store', 'data')],
    prevent_initial_call=True
)
def auto_hide_alert(n_intervals, alert_data):
    # Only hide after 5 intervals of 1 second each (5 seconds total)
    if n_intervals and n_intervals >= 5 and alert_data:
        # Clear the alert and reset the interval
        return None, True, 0
    raise PreventUpdate

# Callback for SSO login - Bypass authentication for Plotly Dash Enterprise
@dash_app.callback(
    [Output('session-data', 'data', allow_duplicate=True),
     Output('url', 'pathname', allow_duplicate=True)],
    [Input('sso-login-button', 'n_clicks')],
    prevent_initial_call=True
)
def handle_sso_login(n_clicks):
    if n_clicks:
        # Skip SSO authentication - directly login for Plotly Dash Enterprise compatibility
        new_session = {
            'authenticated': True,
            'user_email': 'sso.user@reynolds.com',
            'user_name': 'SSO User'
        }
        return new_session, '/'
    raise PreventUpdate

# Callback for sidebar toggle - simplified
@dash_app.callback(
    [Output('sidebar', 'style'),
     Output('main-content', 'style'),
     Output('sidebar-overlay', 'style'),
     Output('sidebar-state', 'data')],
    [Input('hamburger-menu', 'n_clicks')],
    [State('sidebar-state', 'data')]
)
def toggle_sidebar(n_clicks, sidebar_state):
    # Initial state
    if n_clicks is None or n_clicks == 0:
        sidebar_style = {
            'position': 'fixed',
            'top': '0',
            'left': '-280px',
            'width': '280px',
            'height': '100vh',
            'backgroundColor': 'white',
            'boxShadow': '2px 0 5px rgba(0,0,0,0.1)',
            'transition': 'left 0.3s ease',
            'zIndex': '1050',
            'display': 'flex',
            'flexDirection': 'column'
        }
        
        main_style = {
            'marginLeft': '0',
            'transition': 'margin-left 0.3s ease'
        }
        
        overlay_style = {
            'position': 'fixed',
            'top': '0',
            'left': '0',
            'width': '100vw',
            'height': '100vh',
            'backgroundColor': 'rgba(0, 0, 0, 0)',
            'zIndex': '999',
            'pointerEvents': 'none',
            'transition': 'background-color 0.3s ease'
        }
        
        return sidebar_style, main_style, overlay_style, {'isOpen': False}
    
    # Toggle state based on clicks
    is_open = n_clicks % 2 == 1
    
    sidebar_style = {
        'position': 'fixed',
        'top': '0',
        'left': '0' if is_open else '-280px',
        'width': '280px',
        'height': '100vh',
        'backgroundColor': 'white',
        'boxShadow': '2px 0 5px rgba(0,0,0,0.1)',
        'transition': 'left 0.3s ease',
        'zIndex': '1050',
        'display': 'flex',
        'flexDirection': 'column'
    }
    
    main_style = {
        'marginLeft': '280px' if is_open else '0',
        'transition': 'margin-left 0.3s ease'
    }
    
    overlay_style = {
        'position': 'fixed',
        'top': '0',
        'left': '0',
        'width': '100vw',
        'height': '100vh',
        'backgroundColor': 'rgba(0, 0, 0, 0.5)' if is_open else 'rgba(0, 0, 0, 0)',
        'zIndex': '999',
        'pointerEvents': 'auto' if is_open else 'none',
        'transition': 'background-color 0.3s ease'
    }
    
    return sidebar_style, main_style, overlay_style, {'isOpen': is_open}


# Callback to close sidebar when overlay is clicked
@dash_app.callback(
    Output('hamburger-menu', 'n_clicks'),
    [Input('sidebar-overlay', 'n_clicks')],
    [State('hamburger-menu', 'n_clicks'),
     State('sidebar-state', 'data')],
    prevent_initial_call=True
)
def close_sidebar_on_overlay(overlay_clicks, hamburger_clicks, sidebar_state):
    if overlay_clicks and sidebar_state.get('isOpen', False):
        # Increment hamburger clicks to close sidebar
        return (hamburger_clicks or 0) + 1
    raise PreventUpdate

# Callback for logout functionality
@dash_app.callback(
    [Output('url', 'pathname', allow_duplicate=True),
     Output('session-data', 'data', allow_duplicate=True)],
    [Input('logout-link', 'n_clicks')],
    prevent_initial_call=True
)
def handle_logout(n_clicks):
    if n_clicks:
        # Clear session data and redirect to login
        return '/login', {'authenticated': False}
    raise PreventUpdate

# Callback for page routing within dashboard with animation
@dash_app.callback(
    Output('dashboard-page-content', 'children'),
    [Input('url', 'pathname')],
    [State('session-data', 'data')],
    prevent_initial_call=True
)
def display_dashboard_page(pathname, session_data):
    # Only route within dashboard if user is authenticated
    if session_data and session_data.get('authenticated'):
        if pathname == '/activities':
            return create_activities_layout()
        elif pathname == '/capacity':
            return create_capacity_layout()
        elif pathname == '/cycle':
            return create_cycle_layout()
        elif pathname == '/control':
            return create_control_layout()
        elif pathname == '/' or pathname is None:
            # Default to overview
            return create_overview_layout()
    raise PreventUpdate




# Callback for row selection details
@dash_app.callback(
    Output('row-details-container', 'children'),
    [Input('capacity-grid', 'selectedRows')],
    prevent_initial_call=True
)
def display_row_details(selected_rows):
    if selected_rows and len(selected_rows) > 0:
        row = selected_rows[0]  # Show details for first selected row
        
        details_card = dbc.Card([
            dbc.CardHeader([
                html.H6("Territory Details", className="mb-0"),
                html.Small(f"{row.get('tm_territory', '')}", className="text-muted")
            ]),
            dbc.CardBody([
                dbc.Row([
                    dbc.Col([
                        html.P([html.Strong("Area: "), row.get('tm_area', '')], className="mb-2"),
                        html.P([html.Strong("Region: "), row.get('tm_region', '')], className="mb-2")
                    ], md=6),
                    dbc.Col([
                        html.P([html.Strong("Division: "), row.get('tm_division', '')], className="mb-2"),
                        html.P([html.Strong("Territory: "), row.get('tm_territory', '')], className="mb-2")
                    ], md=6)
                ]),
                html.Hr(),
                dbc.Row([
                    dbc.Col([
                        html.Div([
                            html.H3(f"{row.get('capacity_percent', 0)}%", className="mb-1"),
                            html.P("Current Capacity", className="text-muted mb-0")
                        ], className="text-center")
                    ], md=3),
                    dbc.Col([
                        html.Div([
                            html.H3(f"{row.get('pacing_percent', 0)}%", className="mb-1"),
                            html.P("YTD Pacing", className="text-muted mb-0")
                        ], className="text-center")
                    ], md=3),
                    dbc.Col([
                        html.Div([
                            html.H3("Over Capacity" if row.get('capacity_percent', 0) > 100 else "Within Limits", 
                                   className="mb-1 text-danger" if row.get('capacity_percent', 0) > 100 else "mb-1 text-success",
                                   style={'fontSize': '1.2rem'}),
                            html.P("Status", className="text-muted mb-0")
                        ], className="text-center")
                    ], md=3),
                    dbc.Col([
                        html.Div([
                            html.H3("On Track" if row.get('pacing_percent', 0) > 50 else "Needs Attention",
                                   className="mb-1 text-success" if row.get('pacing_percent', 0) > 50 else "mb-1 text-warning",
                                   style={'fontSize': '1.2rem'}),
                            html.P("Trend", className="text-muted mb-0")
                        ], className="text-center")
                    ], md=3)
                ])
            ])
        ], className="shadow-sm")
        
        return details_card
    
    return None

# Callback for map click filtering
@dash_app.callback(
    [Output('capacity-grid', 'rowData'),
     Output('tm-area-dropdown', 'value'),
     Output('tm-region-dropdown', 'value'),
     Output('tm-division-dropdown', 'value'),
     Output('tm-territory-dropdown', 'value')],
    [Input('capacity-map', 'clickData')],
    [State('capacity-grid', 'rowData')],
    prevent_initial_call=True
)
def filter_by_map_click(clickData, current_data):
    if clickData:
        clicked_state = clickData['points'][0]['text']
        
        # Map state abbreviations to areas
        state_to_area_map = {
            'CA': 'AW - WESTERN AREA',
            'TX': 'AW - WESTERN AREA', 
            'FL': 'AE - EASTERN AREA',
            'NY': 'AE - EASTERN AREA',
            'OR': 'AW - WESTERN AREA',
            'WA': 'AW - WESTERN AREA'
        }
        
        area = state_to_area_map.get(clicked_state, None)
        if area:
            # Filter data based on clicked state
            import pandas as pd
            df = pd.DataFrame(current_data)
            filtered_df = df[df['tm_area'] == area]
            
            return filtered_df.to_dict('records'), area, dash.no_update, dash.no_update, dash.no_update
    
    raise PreventUpdate



# Callback for view mode buttons (by area, by map, by graph)
@dash_app.callback(
    [Output('map-container', 'style'),
     Output('graph-container', 'style', allow_duplicate=True),
     Output('btn-map', 'outline'),
     Output('btn-graph', 'outline'),
     Output('organize-by-dropdown', 'style')],
    [Input('btn-map', 'n_clicks'),
     Input('btn-graph', 'n_clicks'),
     Input('organize-by-dropdown', 'value')],
    prevent_initial_call=True
)
def toggle_view_mode(map_clicks, graph_clicks, organize_value):
    ctx = dash.callback_context
    
    if not ctx.triggered:
        raise PreventUpdate
    
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    # Default styles
    map_style = {'display': 'block'}
    graph_style = {'display': 'none'}
    map_outline = False
    graph_outline = True
    dropdown_style = {'width': '120px', 'fontSize': '0.8rem', 'display': 'inline-block'}
    
    if button_id == 'btn-map' or organize_value == 'area':
        # Show map view
        map_style = {'display': 'block'}
        graph_style = {'display': 'none'}
        map_outline = False
        graph_outline = True
    elif button_id == 'btn-graph':
        # Show graph view
        map_style = {'display': 'none'}
        graph_style = {'display': 'block', 'minHeight': '400px'}
        map_outline = True
        graph_outline = False
    
    return map_style, graph_style, map_outline, graph_outline, dropdown_style

# Add graph container to the overview layout
@dash_app.callback(
    Output('graph-container', 'children'),
    [Input('btn-graph', 'n_clicks')],
    prevent_initial_call=True
)
def show_graph_view(n_clicks):
    if n_clicks:
        # Create a bar chart view
        import plotly.graph_objects as go
        
        fig = go.Figure()
        
        # Sample data for the graph
        territories = ['San Francisco CA', 'Los Angeles CA', 'Houston TX', 'New York NY', 'Miami FL']
        capacities = [110, 87, 98, 92, 105]
        
        fig.add_trace(go.Bar(
            x=territories,
            y=capacities,
            marker_color=['#ff5722' if c > 100 else '#ff9800' if c >= 90 else '#4caf50' for c in capacities],
            text=[f'{c}%' for c in capacities],
            textposition='auto'
        ))
        
        fig.update_layout(
            title='Capacity by Territory',
            xaxis_title='Territory',
            yaxis_title='Capacity %',
            showlegend=False,
            plot_bgcolor='white',
            height=400
        )
        
        fig.add_hline(y=100, line_dash="dash", line_color="red", 
                      annotation_text="Capacity Limit", annotation_position="right")
        
        return dcc.Graph(figure=fig, config={'displayModeBar': False})
    
    raise PreventUpdate

# WSGI server compatibility - Export Flask server for gunicorn
app = dash_app.server

if __name__ == '__main__':
    # Run the Dash app directly when executing the script
    dash_app.run(host='0.0.0.0', port=5000, debug=True)