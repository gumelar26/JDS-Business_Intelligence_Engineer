# JDS-Business_Intelligence_Engineer

## 📁 Project Structure
```
.
├── README.md             # Documentation Guide
├── jds_dashboard
│   ├── dash_app          # Dashboard Script
│   ├── fast_app          # Api Script
├── scripts
│   ├── db                # Database Schema
│   ├── jds_data          # JDS Data       
├── docker-compose.yaml
├── Dockerfile.dash
├── Dockerfile.fastapi
├── Dockerfile.postgres
```

## 🔰 Data Sources :

1. [Jumlah Sekolah SLB di Jabar](https://opendata.jabarprov.go.id/id/dataset/jumlah-sekolah-luar-biasa-slb-berdasarkan-kabupatenkota-di-jawa-barat)

2. [Rasio Guru dan Murid SLB di Jabar](https://opendata.jabarprov.go.id/id/dataset/rasio-murid-dan-guru-sekolah-luar-biasa-slb-berdasarkan-kabupatenkota-di-jawa-barat)

3. [Jumlah Kepsek dan Guru SLB Berdasarkan Ijazah Tertinggi](https://opendata.jabarprov.go.id/id/dataset/jumlah-kepala-sekolah-dan-guru-sekolah-luar-biasa-slb-berdasarkan-jenis-kelamin-dan-ijazah-tertinggi-di-jawa-barat)

## 🚀 How to run this app
1. Open CLI
2. Start the services via docker compose :

    - Run `docker compose up -d`
    - Wait untill all sevices running 

3. Access API Services

    - You can access the API at `http://localhost:8080` or `http://localhost:8080/docs` if you want to interact interactively with Swagger.
    - Token to access data : `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRob3IiOiJhZG1pbiIsInJvbGUiOiJwZXJtYW5lbnRfdG9rZW4iLCJ0YXNrIjoiamRzX2JpIn0.SELUgDbqR7Wq7-wjFNkfRgQ19g9ZVlWuPTCp_kQei6w`

4. Access Dashboard App

    - You can access the Dash app at `http://localhost:8085`