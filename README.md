
Built by https://www.blackbox.ai

---

# Reynolds Trade Capacity Manager

## Project Overview
The Reynolds Trade Capacity Manager is a Plotly Dash Enterprise application designed for managing trade capacity operations. This application provides a user-friendly interface with a dashboard for enhanced efficiency while including user authentication. It is developed using Python with Dash, Plotly Bootstrap Components, and Dash AG Grid, ensuring minimal reliance on JavaScript.

## Installation
To set up the project on your local machine, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/reynolds-trade-capacity-manager.git
   cd reynolds-trade-capacity-manager
   ```

2. **Create a virtual environment (optional, but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set environment variables:**
   - Create a `.env` file (or set them directly in your environment) and add:
     ```dotenv
     SESSION_SECRET=your_secret_key
     ```

## Usage
To run the application, execute the following command in your terminal:
```bash
python app.py
```
The application will start on `http://0.0.0.0:5000` by default. You can access it via your web browser by navigating to that URL.

## Features
- **User Authentication:** Supports demo user accounts with password hashing.
- **Responsive Dashboard:** Built with Dash Bootstrap for a fluid interface accommodating various devices.
- **Interactive Visualizations:** Includes choropleth maps and data grids for dynamic data presentation.
- **User-Friendly Login:** Offers Single Sign-On (SSO) and email login options.
- **Multi-Page Structure:** Facilitates easy navigation through various operational modules.

## Dependencies
The following dependencies are required for running this application. They can be found in `requirements.txt`:

- `dash==3.1.0`: Core framework for Dash applications.
- `dash-bootstrap-components==2.0.3`: Bootstrap integration for Dash.
- `dash-ag-grid==31.3.1`: Advanced grid component for displaying data tables.
- `Flask==3.0.3`: Backend web framework used by Dash.
- `gunicorn==20.0.4`: WSGI HTTP Server for serving the application.
- `Werkzeug==3.0.6`: Backing utilities for security and routing.
- `pandas==2.2.3`: Data manipulation library.
- `plotly==6.1.2`: Interactive data visualization library.
- Other necessary packages for deployment and development.

## Project Structure
Below is the high-level structure of the project:

```
reynolds-trade-capacity-manager/
│
├── app.py                   # Application entry point
├── main.py                  # Main Dash application with routing and callbacks
├── requirements.txt         # List of dependencies needed for the project
├── static/                  # Folder for static assets (images, CSS)
│   └── reynolds-logo.png    # Branding logo
├── components/              # Reusable UI components
│   ├── sidebar/             # Sidebar component
│   └── map/                 # Map component
├── modules/                 # Modular structure for each page
│   ├── overview/            # Overview Module
│   ├── activities/          # Activities Module
│   ├── capacity/            # Capacity Module
│   ├── cycle/               # Cycle Module
│   └── control/             # Control Module
├── replit.md                # Project overview and documentation (Markdown format)
└── .env                     # Environment variables (not monitored by git)
```

---

This README serves as a comprehensive guide to understand the Reynolds Trade Capacity Manager project, from setting it up to utilizing its features effectively. For any additional inquiries or contributions, feel free to reach out or open an issue on the repository.