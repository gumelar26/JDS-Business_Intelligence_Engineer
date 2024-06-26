import os
from dotenv import load_dotenv
from sqlmodel import Field, Session, SQLModel, create_engine, select

load_dotenv()

class jds_jml_slb(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    kode_provinsi: int
    nama_provinsi: str
    kode_kabupaten_kota: int
    nama_kabupaten_kota: str
    jumlah_sekolah: int
    satuan: str
    tahun_ajaran: str

class jds_rasio_murid_guru_slb(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    kode_provinsi: int
    nama_provinsi: str
    kode_kabupaten_kota: int
    nama_kabupaten_kota: str
    rasio_murid_guru: int
    satuan: str
    tahun_ajaran: str

class jds_jml_kepsek_guru_slb(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    kode_provinsi: int
    nama_provinsi: str
    kode_kabupaten_kota: int
    nama_kabupaten_kota: str
    jenis_kelamin: str
    ijazah_tertinggi: str
    jumlah_kepsek_guru: int
    satuan: str
    tahun: str

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, echo=True)

def select_jds_jml_slb(tahun_ajaran: str):
    with Session(engine) as session:
        jml_slb = session.exec(select(jds_jml_slb).where(jds_jml_slb.tahun_ajaran == tahun_ajaran)).all()
        return jml_slb

def select_jds_rasio_murid_guru_slb():
    with Session(engine) as session:
        rasio_murid_guru = session.exec(select(jds_rasio_murid_guru_slb)).all()
        return rasio_murid_guru

def select_jds_jml_kepsek_guru_slb(tahun: str):
    with Session(engine) as session:
        jml_kepsek_guru_slb = session.exec(select(jds_jml_kepsek_guru_slb).where(jds_jml_kepsek_guru_slb.tahun == tahun)).all()
        return jml_kepsek_guru_slb