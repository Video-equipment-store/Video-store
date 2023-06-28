# Store

#### Backend 8000 port:

- Python3 DRF

#### Frontend 8080 port: 

- Vue 3
- Bootstrap 5 (cdn in base template index.html) 
- Pinia
- axios (consection with api)

#### Database - Sqlite

#### nginx 80 port

#### Docer compose:

For local development (docker-compose.dev.yml), run the following command:

```bash
docker compose -f docker-compose.dev.yml up --build
```
_In development mode you can use Vue.js devtools in chrome_

#### API documentation:
dev: http://127.0.0.1:8000/api/v1/docs/swagger/