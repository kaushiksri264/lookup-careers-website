from flask import Flask, render_template, jsonify

app = Flask(__name__)

jobs = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Irving, Tx',
    'salary': '$ 150000'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Austin, Tx',
    'salary': '$ 120000'
}, {
    'id': 3,
    'title': 'Data Engineer',
    'location': 'Irvine, CA'
}, {
    'id': 4,
    'title': 'Data Administrater',
    'location': 'New York, NYC',
    'salary': '$ 220000'
}]


@app.route("/")
def hello_lookup():
    return render_template(
        'home.html', jobs=jobs,
        company_name='LookUp')  #passes the jobs list to the html file


@app.route("/api/jobs")
def list_jobs():
    return jsonify(jobs)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
