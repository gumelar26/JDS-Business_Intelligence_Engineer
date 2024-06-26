-- CreateTable
CREATE TABLE IF NOT EXISTS jds_jml_kepsek_guru_slb (
    "id" SERIAL PRIMARY KEY,
    "kode_provinsi" INT NOT NULL,
    "nama_provinsi" VARCHAR(255) NOT NULL,
    "kode_kabupaten_kota" INT NOT NULL,
    "nama_kabupaten_kota" VARCHAR(255) NOT NULL,
    "jenis_kelamin" VARCHAR(255) NOT NULL,
    "ijazah_tertinggi" VARCHAR(255) NOT NULL,
    "jumlah_kepsek_guru" INT NOT NULL DEFAULT 0,
    "satuan" VARCHAR(255) NOT NULL,
    "tahun" VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS jds_jml_slb (
    "id" SERIAL PRIMARY KEY,
    "kode_provinsi" INT NOT NULL,
    "nama_provinsi" VARCHAR(255) NOT NULL,
    "kode_kabupaten_kota" INT NOT NULL,
    "nama_kabupaten_kota" VARCHAR(255) NOT NULL,
    "jumlah_sekolah" INT NOT NULL DEFAULT 0,
    "satuan" VARCHAR(255) NOT NULL,
    "tahun_ajaran" VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS jds_rasio_murid_guru_slb (
    "id" SERIAL PRIMARY KEY,
    "kode_provinsi" INT NOT NULL,
    "nama_provinsi" VARCHAR(255) NOT NULL,
    "kode_kabupaten_kota" INT NOT NULL,
    "nama_kabupaten_kota" VARCHAR(255) NOT NULL,
    "rasio_murid_guru" INT NOT NULL DEFAULT 0,
    "satuan" VARCHAR(255) NOT NULL,
    "tahun_ajaran" VARCHAR(255) NOT NULL
);

COPY jds_jml_kepsek_guru_slb
FROM '/app/scripts/jds_data/jml_kepala_sekolah_guru_slb__jk_ija_data.csv'
DELIMITER ','
CSV HEADER;

COPY jds_jml_slb
FROM '/app/scripts/jds_data/jml_slb__kabupatenkota_data.csv'
DELIMITER ','
CSV HEADER;

COPY jds_rasio_murid_guru_slb
FROM '/app/scripts/jds_data/rasio_murid_guru_slb__kabupatenkota_data.csv'
DELIMITER ','
CSV HEADER;