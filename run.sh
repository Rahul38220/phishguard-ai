
#!/bin/bash
echo "Installing requirements..."
pip install -r backend/requirements.txt

echo "Starting backend server on http://localhost:8000 ..."
cd backend
uvicorn app:app --host 0.0.0.0 --port 8000
