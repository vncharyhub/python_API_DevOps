### BUILD Image
docker build -t flask-rest-api:V1 .

### Run the Container
docker run -d -p 5000:5000 flask-rest-api:V1

### Windows powershell
curl.exe http://127.0.0.1:5000/api/v1/books
Invoke-RestMethod -Uri "http://127.0.0.1:5000/api/v1/books"

### for linux
curl http://127.0.0.1:5000/api/v1/books
