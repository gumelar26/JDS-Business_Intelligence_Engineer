import os
import pandas as pd
from dotenv import load_dotenv
import requests

from utils import discrete_background_color_bins

load_dotenv()

HOST_URL =  os.getenv("HOST_URL")
TOKEN = os.getenv("TOKEN")

def data_jml_slb(col_chosen: str):
    url = f"{HOST_URL}/api/jds_jml_slb/tahun_ajaran?tahun_ajaran={col_chosen}"
    df = pd.read_json(url)
    return df

def data_rasio_murid_guru() :
    url = f"{HOST_URL}/api/jds_rasio_murid_guru_slb/tahun_ajaran"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        df = pd.DataFrame(response.json())
        df_selected = df[['nama_kabupaten_kota', 'rasio_murid_guru', 'tahun_ajaran']]
        pivot_df = df_selected.pivot(index='nama_kabupaten_kota', columns='tahun_ajaran', values='rasio_murid_guru').reset_index()
        
        pivot_data = pivot_df.to_dict('records')
       
        columns = [{'id': c, 'name': c} for c in pivot_df.columns]
       
        (styles, legend) = discrete_background_color_bins(pivot_df)
        
        return pivot_data, columns, styles, legend
    else:
        return [], [], [], []

def data_kepsek_guru_slb(col_chosen: str):
    url = f"{HOST_URL}/api/jds_jml_kepsek_guru_slb/tahun?tahun={col_chosen}"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        df = pd.DataFrame(response.json())
        
        return df
    else:
        return None