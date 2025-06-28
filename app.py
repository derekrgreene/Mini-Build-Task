'''
Author: Derek R. Greene
Email: derek@derekrgreene.com

Description:
    Simple Flask application to process form with fields: first_name, last_name, DOB, 
    therapist_name. Validates that all fields are entered and DOB not in the future. 
    Upon successful submission fields are saved to SQlite database and a confirmation
    page is displayed with the entered info. 
'''

from flask import Flask, request, render_template
from datetime import datetime, date
import sqlite3

app = Flask(__name__)
DB_PATH = 'db/PHI.db'


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    '''
    Method to process/validate form data and store in SQlite database
    '''

    if request.method == 'POST':
        first = request.form['first_name']
        last = request.form['last_name']
        dob = request.form['date_of_birth']
        therapist = request.form['therapist_name']

        error = None
        dob_date = datetime.strptime(dob, "%Y-%m-%d").date()
        if dob_date > date.today():
            error = "Date of Birth cannot be in the future!"
            return render_template('form.html', title="Patient Form",
                                   error=error, max_date=date.today().isoformat(),
                                   first_name=first, last_name=last, dob=dob, therapist=therapist)

        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute(
                '''INSERT INTO patients (
                    first_name, last_name, date_of_birth, therapist_name)
                    VALUES (?, ?, ?, ?)''', (first, last, dob, therapist)
        )
        conn.commit()
        conn.close()

        return render_template('confirmation.html', title="Successful Submission",
                            first_name=first, last_name=last, dob=dob, therapist=therapist)

    return render_template('form.html', title="Patient Form", max_date=date.today().isoformat())


if __name__ == '__main__':
    app.run()
