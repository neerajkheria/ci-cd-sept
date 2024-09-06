from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
  return "Welcome to New CI/CD Pipeline using Python! September 06, 2024"

if __name__=="__main__":
  app.run(debug=True)
