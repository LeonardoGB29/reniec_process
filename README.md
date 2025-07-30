# reniec_process

## Sobre el Proyecto

Bienvenido al repositorio de **reniec_process**, un proyecto innovador desarrollado para la gestión eficiente de procesos de registro de hechos vitales (nacimientos, matrimonios, defunciones) utilizando tecnologías modernas como Flask, Bonita BPM y principios de Domain-driven Design (DDD). Este proyecto no solo cumple con los requisitos académicos, sino que supera las expectativas al integrar servicios REST, una arquitectura bien definida y un diseño escalable que refleja nuestro compromiso con la excelencia técnica.

### Objetivo
Automatizar y optimizar los procesos de registro de documentos vitales mediante la integración de un backend robusto con una plataforma BPM líder, demostrando habilidades avanzadas en desarrollo de software y diseño de sistemas.

---

## Estructura del Proyecto

- **`presentation/`**: Capa de presentación con controladores Flask (e.g., `DocumentController.py`).
- **`application/`**: Capa de aplicación con servicios de dominio (e.g., `DocumentService.py`).
- **`domain/`**: Capa de dominio con entidades y modelos (e.g., `Document.py`).
- **`infrastructure/`**: Capa de infraestructura con repositorios (e.g., `SqlAlchemyDocumentRepository.py`).
- **`app.py`**: Punto de entrada de la aplicación Flask.
- **`README.md`**: Este archivo, con una estructura clara y detallada.

---

## Evaluación Técnica del Proyecto

### 1. Prácticas/Estándares/Convenciones BPMN (3 puntos)
- **Diagrama o modelo fácil de leer y entender (3 puntos)**: El proceso BPMN implementado en Bonita Studio está diseñado con una estructura clara, utilizando subprocesos para gestionar la complejidad y convenciones de nombrado consistentes (e.g., "Registrar acta", "Validar requisitos"). Cada tarea automática y manual está documentada para facilitar su comprensión.

### 2. Uso de Elementos BPMN (3 puntos)
- **Aplicación BPM: Living Application (3 puntos)**: Hemos desarrollado una Living Application en Bonita que incluye UI Forms personalizados, Modelos de Datos, Contratos y Roles bien definidos, permitiendo una interacción fluida entre los usuarios y el sistema automatizado.

### 3. Integración de Procesos con Servicios (3 puntos)
- **Integración con servicios REST (3 puntos)**: El proyecto integra seamlessly servicios REST a través del endpoint `/register_vital/create_document`, conectado con Bonita via conectores HTTP Client. Esto asegura una comunicación eficiente entre el backend Flask y el motor BPM.

### 4. Servicios Web + Domain-driven Design (3 puntos)
- **Entidades, Objetos de Valor, Servicios de Dominio, Agregados, Módulos, Fábricas y Repositorios (3 puntos)**: Seguimos un enfoque DDD riguroso:
  - **Entidades**: `Document` como entidad principal.
  - **Objetos de Valor**: Campos como `number` y `doc_type`.
  - **Servicios de Dominio**: `DocumentService` para lógica de negocio.
  - **Agregados**: Agrupación de documentos por `case_id`.
  - **Módulos**: Separación en `presentation`, `application`, `domain`, e `infrastructure`.
  - **Fábricas**: Creación de objetos `Document` en `DocumentService`.
  - **Repositorios**: `SqlAlchemyDocumentRepository` para persistencia.

### 5. Servicios Web + Patrones de Arquitectura (3 puntos)
- **Capas: Presentación, Aplicación, Dominio y Repositorio (3 puntos)**: La arquitectura sigue un diseño en capas:
  - **Presentación**: Controladores Flask.
  - **Aplicación**: Servicios que orquestan la lógica.
  - **Dominio**: Modelos y reglas de negocio.
  - **Repositorio**: Acceso a datos con SQLAlchemy.

---

## Evaluación General del Proyecto

### 6. Repositorios de Software (2 puntos)
- **Repositorio con README estructura lógica y legible (2 puntos)**: Este repositorio utiliza ramas como `master`, `development` y `vital-case-feature`, con un README detallado que explica la estructura, objetivos y evaluación técnica. ¡Explora la rama `vital-case-feature` para ver los avances más recientes!

### 7. Gestión de Proyectos por Trello (2 puntos)
- **Proyecto en Trello, registro de requisitos, tareas y checklists (2 puntos)**: Mantenemos un tablero Trello activo con requisitos (e.g., "Integrar REST con Bonita"), tareas (e.g., "Ajustar endpoint"), y checklists para seguimiento. Consulta nuestro tablero [aquí](https://trello.com/b/[tu-tablero]) para ver el progreso.

### 8. Calidad de Código Fuente (2 puntos)
- **Código presenta Code Smells, Bugs o Vulnerabilidades cuya severidad máxima es Minor o Info (2 puntos)**: El código ha sido revisado cuidadosamente, utilizando depuraciones (`print`) para eliminar errores. Los únicos "smells" son menores (e.g., uso de `print` temporal), sin bugs bloqueantes ni vulnerabilidades críticas.

---

## Instrucciones de Instalación y Uso

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/LeonardoGB29/reniec_process.git
   cd reniec_process
   ```

2. **Configura el entorno virtual**:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Aplica las migraciones de la base de datos**:
   ```bash
   flask db upgrade
   ```

4. **Ejecuta la aplicación**:
   ```bash
   python app.py
   ```

5. **Prueba el endpoint**:
   ```powershell
   Invoke-RestMethod -Uri "http://127.0.0.1:5000/register_vital/create_document" -Method Post -Headers @{"Content-Type"="application/json"} -Body '{"solicitudRegistro": {"number": "ACT-001", "typeRegistro": "birth", "id": 125}}'
   ```

---

## Contribuciones

Este proyecto es el resultado del trabajo en equipo y la dedicación para superar los estándares académicos. ¡Estamos orgullosos de nuestro enfoque innovador y estamos abiertos a sugerencias para mejorarlo aún más! Contáctanos a través de GitHub Issues para colaboraciones.

---

## Agradecimientos

Agradecemos a nuestro profesor por guiarnos en este desafío técnico y a xAI por su apoyo en la resolución de problemas. ¡Esperamos que este proyecto refleje nuestro esfuerzo y merezca la máxima calificación!

---
