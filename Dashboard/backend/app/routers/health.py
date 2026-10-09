

@app.get("/health")
def health_check():
    logging.debug("Health check endpoint called")
    return JSONResponse(content={"Health_status": "ok"}, status_code=200)
