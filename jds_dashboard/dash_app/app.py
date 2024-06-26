from dash import Dash, dash_table, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px

from data import data_jml_slb, data_rasio_murid_guru, data_kepsek_guru_slb

external_stylesheets = [dbc.themes.BOOTSTRAP]
app = Dash(__name__, external_stylesheets=external_stylesheets)

data_rmg, columns_rmg, style_rmg, legend_rmg = data_rasio_murid_guru()

app.layout = dbc.Container([
    dbc.Row([
        html.Div('Jabar Digital Service Business Intelligence Task', className="text-primary text-center fs-3")
    ]),
    dbc.RadioItems(options=[{"label": x, "value": x} for x in ['2015/2016', '2016/2017', '2017/2018', '2018/2019', '2019/2020']],
                    value='2015/2016',
                    inline=True,
                    id='radio-buttons-jml-slb'),
    dbc.Row([
        dbc.Col([
            dcc.Graph(figure={}, id='bar-plot-jml-slb')
        ]),
    
    dbc.Row([
        dbc.Col([
            html.Div('Heatmap Rasio Murid dan Guru di SLB', className="text-primary text-left text-black text-bold fs-5"),
            html.Div(legend_rmg, style={'float': 'right'}),
            dash_table.DataTable(
                data=data_rmg,
                columns=columns_rmg,
                sort_action='native',
                style_cell={'padding': '5px'},
                style_header={
                    'backgroundColor': '#C0DEFF',
                    'fontWeight': 'bold',
                    'border': '1px solid black'
                },
                style_data={ 'border': '1px solid black' },
                style_data_conditional=style_rmg
            )
        ]),
        dbc.Col([
            html.Div('Analysis Perbandingan Jumlah Guru di SLB', className="text-primary text-left text-black text-bold fs-5"),
            html.P(),
            html.P("Tahun:"),
            html.Div(
                dcc.Dropdown(
                    options=['2019', '2020'], 
                    value='2019',
                    searchable=False,
                    placeholder="Pilih tahun",
                    id='dropdown-kepsek-guru-slb-1'),  
            ),
            html.P(),
            html.P("Names:"),
            html.Div(
                dcc.Dropdown(
                    options=['jenis_kelamin', 'ijazah_tertinggi'], 
                    value='jenis_kelamin',
                    searchable=False,
                    placeholder="Pilih names",
                    id='dropdown-kepsek-guru-slb-2'),  
            ),
            dcc.Graph(id="pie-kepsek-guru-slb"),
        ])
    ]),
    ]),
], fluid=True)

@callback(
    Output('bar-plot-jml-slb', 'figure'),
    Input('radio-buttons-jml-slb', 'value')
)
def jml_slb(col_chosen : str):
    df = data_jml_slb(col_chosen=col_chosen)
    fig = px.bar(df.sort_values(by='jumlah_sekolah'),
                 x='nama_kabupaten_kota', y='jumlah_sekolah',
                 color='jumlah_sekolah', title=f"Jumlah SLB untuk Tahun Ajaran {col_chosen}")
    return fig

@callback(
    Output("pie-kepsek-guru-slb", "figure"), 
    Input("dropdown-kepsek-guru-slb-1", "value"), 
    Input("dropdown-kepsek-guru-slb-2", "value")
)
def kepsek_guru_slb(col_chosen: str, names: str) :
    df = data_kepsek_guru_slb(col_chosen=col_chosen)
    fig = px.pie(df[df['tahun'] == col_chosen],
                 values='jumlah_kepsek_guru', names=names)
    
    return fig
if __name__ == '__main__':
    app.run(debug=True)