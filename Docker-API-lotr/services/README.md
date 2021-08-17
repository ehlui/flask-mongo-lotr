# Description
Directory explanation

- `docker-compose.ylm` Service / environment
- `/db` Database directory
  - Dockerfile (for db)
  - DB files
- `/api` api directory
  - Dockerfile (for api definition)
  - Volume directory (app structure)
- `/api/tolkien`
  - Endpoints and database connection
- `/api/logs`
  - Logs
- `/api/helpers`
  - Utils scripts
- `/api/data`
  - JSON files for insert as examples
- `/api/custom_settings`
  - Custom settings for example (animals database)
- `/api/app.py`
  - Script for init the flask-api
