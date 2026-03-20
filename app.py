import fastapi
import uvicorn

app=fastapi()

@app.get("/")
def greet():
	return "Welcome"

