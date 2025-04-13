# 🐾 FARO

**FARO** is a Django-powered web application designed to help pet shops and pet care businesses streamline their operations. From managing customer information to handling appointments and services, this platform aims to make pet business management simpler and more efficient.

---

## 📦 Features

- 🐶 Customer and pet profile management  
- 📅 Appointment and service scheduling  
- 🧾 Invoicing and payment tracking  
- 🐾 Service history and pet medical records  
- 📊 Dashboard with business analytics (coming soon)

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/KaylerMm/FARO-2.0.git
cd FARO-2.0
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file
Create a `.env` file in the root of the project and add your environment variables:

```env
DB_NAME=faro
DB_USER=root
DB_PASSWORD=Root@1234
DB_HOST=localhost
DB_PORT=3306
```

> ℹ️ Your database configuration is now securely managed through environment variables using [`python-decouple`](https://github.com/henriquebastos/python-decouple).

### 5. Run migrations and start the development server
```bash
python manage.py migrate
python manage.py runserver
```

---

## 🧪 Running Tests
```bash
python manage.py test
```

---

## 📄 Documentation
Check the full documentation in the `/docs` folder.

---

## 🤝 Contributing
Pull requests are welcome! For major changes, open an issue first to discuss what you’d like to change.

---

## 🧱 Tech Stack
- **Backend**: Python 3.x, Django 4.x  
- **Frontend**: Django Templates  
- **Database**: MySQL (via environment variables)  
- **Security**: `python-decouple` for managing secrets  
- **Optional**: Docker support (coming soon)

---

## 🔮 Roadmap
- ✅ Use of environment variables with `.env`  
- 🔐 User authentication & roles (admin, staff)  
- 📣 Notification system (email/SMS)  
- 🔗 REST API support  
- 📱 Mobile-friendly interface  

---

## 📬 Contact
For feedback, bugs, or feature requests, feel free to open an issue or contact the maintainer via GitHub.
