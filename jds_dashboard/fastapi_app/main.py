from fastapi import FastAPI, HTTPException, Depends

from auth import verify_token
from database import (
    select_jds_jml_slb,
    select_jds_jml_kepsek_guru_slb,
    select_jds_rasio_murid_guru_slb
)

app = FastAPI()

@app.get("/api/jds_jml_slb/tahun_ajaran")
async def read_jds_jml_slb(tahun_ajaran: str) :
     jds_jml_slb = select_jds_jml_slb(tahun_ajaran=tahun_ajaran)
     if not jds_jml_slb:
         raise HTTPException(status_code=404, detail="Data not found")
     return jds_jml_slb
 
@app.get("/api/jds_rasio_murid_guru_slb/tahun_ajaran")
async def read_jds_rasio_murid_guru_slb(payload: dict = Depends(verify_token)) :
     rasio_murid_guru_slb = select_jds_rasio_murid_guru_slb()
     if not rasio_murid_guru_slb:
         raise HTTPException(status_code=404, detail="Data not found")
     return rasio_murid_guru_slb

@app.get("/api/jds_jml_kepsek_guru_slb/tahun")
async def read_jds_jml_kepsek_guru_slb(tahun: str, payload: dict = Depends(verify_token)) :
    jds_jml_kepsek_guru_slb = select_jds_jml_kepsek_guru_slb(tahun=tahun)
    if not jds_jml_kepsek_guru_slb:
        raise HTTPException(status_code=404, detail="Data not found")
    return jds_jml_kepsek_guru_slb