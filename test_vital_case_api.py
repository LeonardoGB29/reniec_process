import requests
import json

BASE_URL = "http://127.0.0.1:5000/register_vital/vital_cases"

payload = {
    "person_id": 123
}

headers = {
    "Content-Type": "application/json"
}

try:
    response = requests.post(BASE_URL, data=json.dumps(payload), headers=headers)

    print(f"🔄 Estado HTTP: {response.status_code}")

    if response.status_code == 201:
        print("✅ Caso creado exitosamente:")
        print(response.json())
    else:
        print("⚠️ Error en la creación:")
        print(response.text)

except Exception as e:
    print("❌ Error al hacer la petición:", str(e))
