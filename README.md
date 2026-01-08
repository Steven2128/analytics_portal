# Desafio Cala Analytics

## Bloque 1
### Tecnologias usada en el desarrollo

- Python 3.12
- Django 6.0
- PyCharm

### Iniciar proyecto Django

Abrir una terminal en la carpeta del proyecto y ejecutar los siguientes comandos

```bash
# Preparar entorno con virtualenv
virtualenv env
env\Scripts\activate
```

```bash
cd analytics_portal
pip install -r requirements.txt
```

Una vez configurado, inicie el proyecto

```bash
python manage.py runserver
```
Ir a http://127.0.0.1:8000/dashboard


## Bloque 2
1. Total de ventas por cliente
```sql
SELECT
  cliente_id,
  SUM(valor_venta) AS total_ventas
FROM `project.dataset.ventas_diarias`
GROUP BY cliente_id
ORDER BY total_ventas DESC;
```

2. Total de ventas por mes
```sql
SELECT
  FORMAT_DATE('%Y-%m', fecha) AS mes,
  SUM(valor_venta) AS total_ventas
FROM `project.dataset.ventas_diarias`
GROUP BY mes
ORDER BY mes;

```
3. Top 5 clientes por ventas
```sql
SELECT
  cliente_id,
  SUM(valor_venta) AS total_ventas
FROM `project.dataset.ventas_diarias`
GROUP BY cliente_id
ORDER BY total_ventas DESC
LIMIT 5;
```
Los datos serían consumidos desde Django mediante el cliente oficial de BigQuery, ejecutando consultas SQL directamente contra el data warehouse.
La lógica de acceso se encapsularía en una capa de servicios para mantener separada la lógica de negocio.
Los resultados se retornarían a las vistas y se presentarían en el frontend mediante templates HTML o a través de una API REST para su visualización en dashboards con gráficos y tablas.


## Bloque 3
### 1. ¿Cómo abordarías un requerimiento técnicamente incorrecto solicitado por un cliente?
Primero intento entender qué necesita realmente el cliente, luego explico de forma clara por qué la solución propuesta no es adecuada y qué problemas podría traer y por ultimo propongo una alternativa técnica que cumpla el mismo objetivo y busco acordarla antes de avanzar.
### 2. ¿Qué harías si debes trabajar con una tecnología que no dominas y el proyecto ya inició?
Reviso qué tan crítica es la tecnología dentro del proyecto, después acorde a ello aprendo lo necesario para avanzar apoyándome en documentación y en el equipo. Divido las tareas para ir implementando y aprendiendo al mismo tiempo, sin frenar el proyecto.
### 3. ¿Cómo aseguras calidad técnica cuando trabajas bajo presión de tiempo?
Priorizo lo más importante del requerimiento, también mantengo buenas prácticas básicas y evito soluciones improvisadas y si algo queda por mejorar, lo dejo identificado y documentado para después.