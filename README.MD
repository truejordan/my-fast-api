# THIS IS A NEON POSTGRES FAST API CLEAN ARCHITECTURE SETUP

Set up environment:
`python -m venv .venv`

activate environment:
`. .venv/bin/activate` or 
1. Open the command pallet with cmd + shit + P
2. Type Python and select Python: Select Interpreter
3. Select available interpreter matching your environment 


To run the api use the following command:
`python -m uvicorn src.main:app --reload`

## View api + doucmentation interface:

- Swagger UI: http://localhost:8000/docs (can test endpoints)
- ReDoc: http://localhost:8000/redoc (non interactive)