# RENIEC Process

Este proyecto modela e implementa servicios BPM (Business Process Management) para el **Registro Nacional de Identificación y Estado Civil – RENIEC**, una entidad pública peruana responsable del registro de identidad de los ciudadanos y hechos vitales como nacimiento, matrimonio y defunción.

---

## Sobre RENIEC

**RENIEC** es un organismo autónomo del Estado peruano. Su misión es garantizar la identidad y los derechos civiles de los ciudadanos mediante el registro confiable de datos personales y hechos vitales.

- **Misión**:
  - Registrar, actualizar, y unificar la identificación de las personas.
  - Registrar los hechos vitales y los actos que modifican el estado
civil.
  - Emitir documentos que acrediten la identidad de las personas.
  - Participar en el sistema electoral. Promover el uso de servicios
digitales.

- **Visión**: Ser una institución líder en identidad y registro civil, reconocida por su transparencia, innovación y excelencia.

---

## Proceso Principal: Registrar Hechos Vitales

Este proceso permite al ciudadano solicitar el registro de un hecho vital (como un nacimiento), el cual es validado por el **Registrador Civil** y posteriormente gestionado por el **Técnico TI**. Si todo es correcto, se inscribe el acta; si hay errores, se generan observaciones que deben ser subsanadas.

### Diagrama general:

<img width="1002" height="714" alt="image" src="https://github.com/user-attachments/assets/e7e4ea65-1ddc-46e4-8321-70b1c9500350" />
<img width="1141" height="892" alt="image" src="https://github.com/user-attachments/assets/7f26ae44-8f3e-49a1-a1a9-bfc283750f31" />

---

## Subprocesos Identificados

Además del proceso principal, el análisis BPMN incluyó también otros procesos claves en RENIEC:

| Proceso | Breve Descripción |
|--------|--------------------|
| Gestión de la Identidad Ciudadana | Incluye verificación, captura biométrica, emisión de DNI. |
| Actualización de Datos Registrales | Para actualizar datos como dirección, estado civil. |
| Validación de Identidad para Servicios | Verificación ante entidades públicas y privadas. |
| Generación de Información Estadística | Reportes y análisis sobre hechos vitales registrados. |

---


## 📋 Organización de Tareas con Trello

Durante el desarrollo del proyecto, utilizamos **Trello** como herramienta de gestión de tareas.

El tablero contiene las siguientes columnas:

- **Backlog**: Tareas por priorizar.
- **To Do**: Tareas planificadas por iniciar.
- **Doing**: Tareas en desarrollo.
- **Testing**: Tareas en etapa de validación o revisión.
- **Done ✅**: Tareas completadas, incluyendo microservicios y pruebas.

### Actividades destacadas

- Formularios de registro para **Nacimiento**, **Matrimonio**, y **Defunción**.
- Implementación de **RabbitMQ** para comunicación entre servicios.
- Análisis de código con **SonarQube**.
- Desarrollo de **microservicios** para documentos y observaciones.
- Modelado BPMN y validación funcional en Bonita.

### 🔍 Vista del tablero:
<img width="1916" height="952" alt="image" src="https://github.com/user-attachments/assets/bbeaebd9-ccba-4fd3-8b5b-1124e48d04fa" />

##  Iniciar el proyecto
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

## Migración de base de datos

```bash
flask db migrate -m "descripcion"   # nueva migración
flask db upgrade                    # aplicar
flask db downgrade                  # revertir (dev)
```

## División interna

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



# Pruebas

<img width="2878" height="1558" alt="image" src="https://github.com/user-attachments/assets/65655c1d-d4fd-4ca9-aaa0-b51759be4fd1" />

<img width="1802" height="606" alt="image" src="https://github.com/user-attachments/assets/0d81ce9c-0b21-4b52-b98f-da35880019be" />

<img width="2159" height="1263" alt="image" src="https://github.com/user-attachments/assets/b9eca7dc-a0ad-4d78-844b-92a1bca1df49" />

---

## Flujo de tareas y formularios en Bonita BPM

A continuación, se muestra cómo se ejecuta el proceso `Registrar Hechos Vitales` en la **Bonita User Application**, incluyendo las tareas por rol y los formularios asociados.

### 1. Crear documento de solicitud (Ciudadano)

El ciudadano inicia la solicitud seleccionando el tipo de registro, ingresando su DNI y redactando la solicitud:

<img width="1863" height="471" alt="image" src="https://github.com/user-attachments/assets/be3e4972-1fc2-43c7-a367-e7cbc4d34656" />


---

### 2. Validar estructura del documento (Registrador Civil)

El registrador evalúa si la estructura del expediente cumple con los requisitos iniciales. Puede determinar el estado (válido / inválido) y redactar observaciones si es necesario.

<img width="787" height="311" alt="image" src="https://github.com/user-attachments/assets/6008590a-9367-453e-86d7-1ac03aba9ed3" />

---

### 3. Validar viabilidad legal

Se valida legalmente el contenido. En caso de observaciones, se detallan en el formulario:

<img width="795" height="323" alt="image" src="https://github.com/user-attachments/assets/0dc1e2cc-fcf0-4bfd-b88b-b65b23e6b811" />

---

### 4. Redactar acta (Técnico TI)

Si el expediente es válido, se redacta el acta en este formulario:

<img width="781" height="177" alt="image" src="https://github.com/user-attachments/assets/4de9e05c-f54d-48bc-a289-ed62b719de34" />

Esto genera una solicitud a un **microservicio externo**, encargado de registrar y asociar digitalmente el acta al documento.

---

### 5. Redactar observación (Técnico TI)

Si el expediente no es válido, se redacta una observación técnica:

<img width="786" height="175" alt="image" src="https://github.com/user-attachments/assets/f731ae0c-6369-4f79-a881-099d4ed94208" />


También se invoca un **microservicio** para registrar y asociar la observación al expediente.

---

### 6. Subsanar observación (Ciudadano)

El ciudadano recibe la observación, revisa el motivo y tiene la oportunidad de corregir y reenviar la solicitud:

<img width="788" height="323" alt="image" src="https://github.com/user-attachments/assets/c378bea7-2668-4dc2-b298-a950b6567dac" />

---
---

## Objetos de Negocio

En el modelado del proceso en Bonita BPM se utilizaron diversos **objetos de negocio (BOs)** para representar las entidades clave del sistema. Uno de los principales es `SolicitudRegistro`, el cual encapsula los datos que el ciudadano envía y que se procesan a lo largo del flujo.

### `SolicitudRegistro` (paquete: `per.reniec.model`)

| Atributo          | Tipo   | Descripción                                   |
|------------------|--------|-----------------------------------------------|
| `id`             | LONG   | Identificador único del registro              |
| `tipoRegistro`   | STRING | Tipo de hecho vital: nacimiento, matrimonio...|
| `dniSolicitante` | STRING | DNI del ciudadano que realiza la solicitud    |
| `fechaSolicitud` | STRING | Fecha en la que se generó la solicitud        |
| `estado`         | STRING | Estado actual del proceso (VALIDADO, OBSERVADO, etc.) |
| `observaciones`  | STRING | Comentarios u observaciones del registrador   |
| `solicitudTexto` | STRING | Texto de la solicitud redactada por el ciudadano |


<img width="1503" height="395" alt="image" src="https://github.com/user-attachments/assets/d0f56ac6-6ed8-41b1-98f4-741a2cd64926" />


---
## Modelo de Organización
<img width="1867" height="186" alt="image" src="https://github.com/user-attachments/assets/6120606e-e67f-4ec2-bccd-e9617221d827" />



<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/03ded3ae-f563-4f94-9a88-e78a4e0c618c" />



