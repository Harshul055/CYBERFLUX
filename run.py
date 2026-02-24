from backend import create_app

app = create_app()

if __name__ == "__main__":
    port = int(input("Enter port number (e.g., 5000, 8000, 8080): "))
    app.run(debug=True, host="0.0.0.0", port=port)
