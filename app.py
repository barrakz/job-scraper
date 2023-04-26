from flask import Flask, render_template
from main import get_job_titles

app = Flask(__name__)

@app.route('/')
def home():
    job_titles = get_job_titles()
    return render_template('home.html', job_titles=job_titles)

if __name__ == '__main__':
    app.run(debug=True)