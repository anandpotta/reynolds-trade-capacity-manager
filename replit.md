# Reynolds Trade Capacity Manager

## Overview

This is a Plotly Dash Enterprise application for the Reynolds Trade Capacity Manager. The application provides a user authentication system with a dashboard interface for managing trade capacity operations. It's built entirely in Python using Dash, Plotly Bootstrap Components, and Dash AG Grid, with no JavaScript required. The application uses in-memory demo user authentication.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Backend Architecture
- **Framework**: Plotly Dash Enterprise (Python-based reactive web framework)
- **Structure**: Multi-page application with sidebar navigation and client-side routing
- **Session Management**: Dash session storage with server-side state management
- **Security**: Werkzeug password hashing for demo authentication
- **Configuration**: Environment-based configuration with fallback defaults
- **Routing**: Dash location-based routing with URL patterns for different modules

### Frontend Architecture
- **UI Framework**: Dash Bootstrap Components (dbc) for responsive design
- **Data Grid**: Dash AG Grid for enterprise data tables with row details
- **Maps**: Plotly choropleth maps for US state capacity visualization
- **Icons**: Font Awesome 6.0.0 for UI icons (via CDN)
- **Interactivity**: Pure Python callbacks - no JavaScript required
- **Styling**: Inline styles with gradient backgrounds matching Reynolds branding
- **Navigation**: Sliding sidebar with hamburger menu toggle

### Authentication System
- **Method**: Session-based authentication using Flask sessions
- **Storage**: In-memory demo users (temporary solution)
- **Security**: Password hashing using Werkzeug's security utilities
- **Session Management**: Server-side session storage with configurable secret key

## Key Components

### Core Application Files
- `main.py`: Main Dash application with routing and all callbacks
- `app.py`: Application entry point
- `static/`: Static assets including Reynolds logo and custom CSS

### Modular Structure
- `modules/`: Individual page modules for each navigation item
  - `overview/`: Current cycle overview with map and grid
  - `activities/`: Activities management module
  - `capacity/`: Capacity simulation module
  - `cycle/`: Cycle management module
  - `control/`: Control table module
- `components/`: Reusable UI components
  - `sidebar/`: Sliding navigation sidebar with hamburger menu
  - `filters/`: Cascading dropdown filters with checkboxes
  - `map/`: Plotly choropleth map component
  - `grid/`: AG Grid component with row details

### Authentication Components
- Demo user credentials stored in memory
- Password hashing and verification
- Session management for user state
- Login/logout functionality with flash messages

### UI Components
- Login page with branded design and SSO/Email toggle
- Sliding sidebar navigation with hamburger menu toggle
- Current Cycle Overview dashboard with:
  - Cascading dropdown filters with multi-select checkboxes
  - US choropleth map showing capacity by state
  - AG Grid with expandable row details
  - Responsive design with mobile support
- Modular page structure for easy extension

## Data Flow

### Authentication Flow
1. User accesses application → redirected to login if not authenticated
2. Login form submission → credential validation against demo users
3. Successful authentication → session creation and redirect to dashboard
4. Dashboard access → session validation and user data display

### Request Flow
1. Client request → Flask application
2. Route matching → appropriate handler function
3. Template rendering → HTML response
4. Static assets served directly by Flask

## External Dependencies

### Frontend Dependencies (CDN)
- **Bootstrap 5.3.0**: UI framework and components
- **Font Awesome 6.0.0**: Icon library

### Python Dependencies
- **dash==3.1.0**: Core Dash framework
- **dash-bootstrap-components==2.0.3**: Bootstrap components for Dash
- **dash-ag-grid==31.3.1**: Enterprise data grid component
- **dash-auth==2.3.0**: Authentication module for Dash
- **Flask==3.0.3**: Web framework (used by Dash internally)
- **gunicorn==20.0.4**: WSGI HTTP Server
- **Werkzeug==3.0.6**: WSGI utilities and security functions
- **pandas==2.2.3**: Data manipulation library
- **plotly==6.1.2**: Interactive graphing library

### Development Dependencies
- Built-in Flask development server
- Debug mode enabled for development

## Deployment Strategy

### Current Configuration
- **Host**: 0.0.0.0 (accepts connections from any IP)
- **Port**: 5000
- **Debug Mode**: Enabled for development
- **WSGI**: ProxyFix middleware for reverse proxy deployment

### Environment Variables
- `SESSION_SECRET`: Session encryption key (falls back to development key)

### Deployment Considerations
- Application is configured for containerized deployment
- ProxyFix middleware suggests intended deployment behind reverse proxy
- Session secret should be set via environment variable in production
- Debug mode should be disabled in production environment

### Current Limitations
- No persistent database (users stored in memory)
- No production-grade session storage
- Limited error handling and logging
- No API endpoints for external integration

## Recent Changes (July 17, 2025)

### Fixed Issues
1. **Sidebar Toggle Mechanism**
   - Simplified toggle logic using n_clicks modulo for state management
   - Fixed immediate show/hide behavior
   - Separated overlay click handling to properly close sidebar

2. **Interactive Features Implementation**
   - **Map Click Filtering**: Clicking on states in the choropleth map now filters the grid data
   - **Row Details**: AG Grid now supports expandable row details showing:
     - Full territory path
     - Current capacity percentage
     - YTD pacing
     - Status (Over Capacity/Within Limits)
     - Trend analysis
   - **View Mode Switching**: "By Map" and "By Graph" buttons now properly toggle between views
     - Map view shows choropleth visualization
     - Graph view displays bar chart of capacity by territory

3. **Data Flow Integration**
   - Map clicks update dropdown filters and grid data
   - All components now properly synchronized
   - Proper state management between components

The application is designed as a foundation that can be extended with proper database integration, enhanced security measures, and additional trade capacity management features.