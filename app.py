from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World from VERCEL!"
    
@app.route("/api")
def api():
    return "API: Ni mimi uyo SASA!"

if __name__ == "__main__":
    app.run()
