# 🎨 I-Talent Creatief Portfolio

Een Django-webapplicatie voor het beheren en presenteren van creatieve portfolio's. Dit project is volledig dockerized.

---

## ⚙️ Functionaliteiten

- Creatief portfolio-systeem
- Gebouwd met Django
- Volledig te runnen in een Docker-container

---

## 🚀 Installatie (met Docker)

### 1. Clone of unzip dit project

```bash
git clone <repo-url>
cd I-Talent-creatief-portfolio
```

### 2. Build de Docker container

```bash
docker build -t mijn-django-app .
```

### 3. Start de container (interactief)

```bash
docker run -it --rm --name mijn-portfolio-container -p 8000:8000 mijn-django-app
```

Ga vervolgens naar [http://localhost:8000](http://localhost:8000).

---

## 🔧 Belangrijke commando’s

**Database migreren:**

```bash
docker run --rm mijn-django-app python manage.py migrate
```

**Superuser aanmaken:**

```bash
docker run -it --rm mijn-django-app python manage.py createsuperuser
```

**Container stoppen (als je zonder `--rm` runt):**

```bash
docker stop mijn-portfolio-container
```

---

## 🐳 Dockerfile & Entrypoint

- De `Dockerfile` installeert alle dependencies en start automatisch de Django server.
- Een `entrypoint.sh` script voert eerst `migrate` uit, zodat je database altijd up-to-date is.

---

## 🧪 Vereisten

De volgende Python dependencies worden geïnstalleerd via `requirements.txt`:

- Django
- transformers
- langchain
- faiss-cpu
- sentence-transformers

---

## 📁 Projectstructuur

```
I-Talent-creatief-portfolio/
├── creative_portfolio/       # Django settings app
├── main/                     # Hoofdapplicatie
├── db.sqlite3                # SQLite database
├── manage.py                 # Django entrypoint
├── requirements.txt          # Python dependencies
├── Dockerfile                # Docker configuratie
├── entrypoint.sh             # Startscript (met migraties)
└── README.md                 # Documentatie
```

---

## 🧠 Mogelijke uitbreidingen

- Deployment met Gunicorn + Nginx
- CI/CD pipeline (bv. GitHub Actions)
- Hosting via Heroku, Render of VPS
- Cloud storage integratie voor uploads (bv. AWS S3)

---

## 👤 Auteur

Gemaakt met ❤️ door [jouw naam hier].
