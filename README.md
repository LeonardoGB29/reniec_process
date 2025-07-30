# RENIEC Process 🚀

Servicios y procesos BPM, teniendo en cuenta el proceso de negocio princiapl para la implementación de estos, la registración de los hecho vitales, es decir, la inscripción y gestión de identidad civil en el Perú, por ejemplo, el resgitro de nacimiento, de defunción o de matrimonio.

## Iniciar proyecto ⚡ 

```bash
# 1. Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate      # windows: venv\Scripts\activate

# 2. Instalar dependencias
python -m pip install -r requirements.txt

# 3. Inicializar base de datos (solo la 1ª vez)
flask db upgrade

# 4. Levantar el servidor
flask --app app --debug run
```

La aplicación queda en <http://127.0.0.1:5000/>.

## 📜 Migración de base de datos

```bash
flask db migrate -m "descripcion"   # nueva migración
flask db upgrade                    # aplicar
flask db downgrade                  # revertir (dev)
```

## 🧩 División interna

- **presentation** – blueprints y validaciones HTTP  
- **application**  – orquestación de reglas de negocio  
- **domain**       – entidades y repositorios abstractos  
- **infrastructure** – implementaciones concretas (SQLAlchemy, RabbitMQ…)

## 🗂 Estructura de carpetas (vista parcial)

```
reniec_process/
├── app.py
├── extensions.py
├── requirements.txt
├── application/
│   └── vital/
│       └── document_service.py
├── domain/
│   └── vital/
│       ├── model/
│       │   └── document.py
│       └── repository/
│           └── document_repository.py
├── infrastructure/
│   └── vital/
│       └── sqlalchemy_document_repository.py
├── presentation/
│   └── vital/
│       └── document_controller.py
├── migrations/
└── instance/
```



#pruebas

<img width="2878" height="1558" alt="image" src="https://github.com/user-attachments/assets/65655c1d-d4fd-4ca9-aaa0-b51759be4fd1" />

<img width="1802" height="606" alt="image" src="https://github.com/user-attachments/assets/0d81ce9c-0b21-4b52-b98f-da35880019be" />
