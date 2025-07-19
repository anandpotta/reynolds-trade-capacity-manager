import dash_ag_grid as dag
import pandas as pd
from dash import html, dcc

def create_capacity_grid():
    """Create the AG Grid showing capacity data with row details"""
    
    # Sample data
    data = [
        {
            'id': 1,
            'tm_area': 'AW - WESTERN AREA',
            'tm_region': 'SDR - LOS ANGELES REGION',
            'tm_division': 'DM - San Francisco CA',
            'tm_territory': 'TM - San Francisco CA',
            'capacity_percent': 110,
            'pacing_percent': 42,
            'region_color': '#ff9800'
        },
        {
            'id': 2,
            'tm_area': 'AW - WESTERN AREA',
            'tm_region': 'SDR - LOS ANGELES REGION',
            'tm_division': 'DM - Santa Rosa CA',
            'tm_territory': 'TM - Eureka CA',
            'capacity_percent': 98,
            'pacing_percent': 42,
            'region_color': '#ffeb3b'
        },
        {
            'id': 3,
            'tm_area': 'AW - WESTERN AREA',
            'tm_region': 'SDR - LOS ANGELES REGION',
            'tm_division': 'DM - San Francisco CA',
            'tm_territory': 'TM - Livermore CA',
            'capacity_percent': 120,
            'pacing_percent': 82,
            'region_color': '#ff5722'
        },
        {
            'id': 4,
            'tm_area': 'AW - WESTERN AREA',
            'tm_region': 'SDR - LOS ANGELES REGION',
            'tm_division': 'DM - Los Angeles CA',
            'tm_territory': 'TM - Hollywood CA',
            'capacity_percent': 87,
            'pacing_percent': 42,
            'region_color': '#4caf50'
        },
        {
            'id': 5,
            'tm_area': 'AW - WESTERN AREA',
            'tm_region': 'SDR - LOS ANGELES REGION',
            'tm_division': 'DM - Santa Rosa CA',
            'tm_territory': 'TM - La Mesa CA',
            'capacity_percent': 87,
            'pacing_percent': 42,
            'region_color': '#4caf50'
        },
        {
            'id': 6,
            'tm_area': 'AW - WESTERN AREA',
            'tm_region': 'SDR - LOS ANGELES REGION',
            'tm_division': 'DM - San Diego CA',
            'tm_territory': 'TM - El Cajon CA',
            'capacity_percent': 110,
            'pacing_percent': 42,
            'region_color': '#ff9800'
        },
        {
            'id': 7,
            'tm_area': 'AW - WESTERN AREA',
            'tm_region': 'SDR - HOUSTON REGION',
            'tm_division': 'DM - Bakersfield CA',
            'tm_territory': 'TM - Escondido CA',
            'capacity_percent': 110,
            'pacing_percent': 42,
            'region_color': '#ff9800'
        },
        {
            'id': 8,
            'tm_area': 'AW - WESTERN AREA',
            'tm_region': 'SDR - HOUSTON REGION',
            'tm_division': 'DM - Houston North TX',
            'tm_territory': 'TM - Lancaster CA',
            'capacity_percent': 87,
            'pacing_percent': 42,
            'region_color': '#4caf50'
        },
        {
            'id': 9,
            'tm_area': 'AW - WESTERN AREA',
            'tm_region': 'SDR - HOUSTON REGION',
            'tm_division': 'DM - Sacramento CA',
            'tm_territory': 'TM - Houston TX',
            'capacity_percent': 87,
            'pacing_percent': 42,
            'region_color': '#4caf50'
        }
    ]
    
    # Column definitions
    column_defs = [
        {
            'field': 'id',
            'headerName': '',
            'width': 40,
            'checkboxSelection': True,
            'headerCheckboxSelection': True,
            'headerCheckboxSelectionFilteredOnly': True,
            'cellStyle': {'textAlign': 'center'}
        },
        {
            'field': 'tm_area',
            'headerName': 'TM Area',
            'minWidth': 180,
            'cellStyle': {'fontSize': '0.8rem'}
        },
        {
            'field': 'tm_region',
            'headerName': 'TM Region',
            'minWidth': 200,
            'cellStyle': {'fontSize': '0.8rem'}
        },
        {
            'field': 'tm_division',
            'headerName': 'TM Division',
            'minWidth': 180,
            'cellStyle': {'fontSize': '0.8rem'}
        },
        {
            'field': 'tm_territory',
            'headerName': 'TM Territory',
            'minWidth': 180,
            'cellStyle': {'fontSize': '0.8rem'}
        },
        {
            'field': 'capacity_percent',
            'headerName': 'Capacity %',
            'width': 100,
            'cellStyle': {
                'styleConditions': [
                    {
                        'condition': 'params.value > 100',
                        'style': {'color': '#ff5722', 'fontWeight': 'bold'}
                    },
                    {
                        'condition': 'params.value >= 90 && params.value <= 100',
                        'style': {'color': '#ff9800', 'fontWeight': 'bold'}
                    },
                    {
                        'condition': 'params.value < 90',
                        'style': {'color': '#4caf50', 'fontWeight': 'bold'}
                    }
                ]
            },
            'valueFormatter': {'function': 'params.value + "%"'}
        },
        {
            'field': 'pacing_percent',
            'headerName': 'Pacing %',
            'width': 100,
            'valueFormatter': {'function': 'params.value + "%"'},
            'cellStyle': {'fontSize': '0.8rem'}
        }
    ]
    
    # Grid options with simple row selection
    grid_options = {
        'rowSelection': 'multiple',
        'suppressRowClickSelection': False,
        'animateRows': True,
        'pagination': True,
        'paginationPageSize': 50,
        'paginationPageSizeSelector': [10, 25, 50],
        'suppressRowHoverHighlight': False,
        'rowHeight': 40,
        'headerHeight': 40
    }
    
    # Create the grid component
    grid_component = html.Div([
        # Grid header
        html.Div([
            html.H6("Capacity by North America", className="mb-2", 
                    style={'fontSize': '0.9rem', 'fontWeight': '600'}),
            html.Div([
                html.Span("Records/Page: ", style={'fontSize': '0.75rem', 'color': '#666'}),
                dcc.Dropdown(
                    id='page-size-dropdown',
                    options=[
                        {'label': '10', 'value': 10},
                        {'label': '25', 'value': 25},
                        {'label': '50', 'value': 50}
                    ],
                    value=50,
                    clearable=False,
                    style={'width': '80px', 'display': 'inline-block', 'marginLeft': '0.5rem'}
                ),
                html.Span(" 1 - 10 records", style={'fontSize': '0.75rem', 'color': '#666', 'marginLeft': '1rem'})
            ], className="d-flex align-items-center justify-content-between mb-2")
        ]),
        
        # The AG Grid
        dag.AgGrid(
            id='capacity-grid',
            rowData=data,
            columnDefs=column_defs,
            defaultColDef={
                'sortable': True,
                'filter': True,
                'resizable': True,
                'floatingFilter': False
            },
            dashGridOptions=grid_options,
            className='ag-theme-alpine',
            style={'height': '500px', 'width': '100%'},
            persistence=True,
            persisted_props=['filterModel', 'sortModel']
        ),
        
        # Row details section
        html.Div(id='row-details-container', className='mt-3')
    ])
    
    return grid_component