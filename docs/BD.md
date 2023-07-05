# Estructura de la base de datos

_Version 0.0.1_

## Descripción

- Base de datos: `MongoDB`
- Nombre de la base de datos: `detector-api`
- Colecciones:
  - `registers`
  - `cars`
  - `logs`

### Colección `registers`:

```json
{
  "id": "ObjectId",
  "type": "string",
  "date": "datetime",
  "prediction_accuracy": "float",
  "vehicle_image": "string",
  "license_plate_image": "string",
  "vehicle_id": "ObjectId"
}
```

### Colección `cars`:

```json
{
  "id": "ObjectId",
  "license_plate": "string",
  "is_blocked": "boolean"
}
```
