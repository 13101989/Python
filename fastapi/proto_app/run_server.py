import uvicorn

if __name__ == "__main__":
    uvicorn.run("proto_app.main:app", reload=True)
