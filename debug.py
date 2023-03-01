from app import app

if __name__ == "__main__":
    # defined host to open to LAN
    app.run(debug=True, host="0.0.0.0")
