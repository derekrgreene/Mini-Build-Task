'''
Author: Derek R. Greene
Email: derek@derekrgreene.com

Description:
    Simple Flask application to process form with fields: therapist_name, patient_name, file. 
    Validates that all fields are entered and uploaded file is a .pdf.
    Upon successful submission the file is saved locally to the /uploads directory with the name format
    therapistName_patientName_timeStamp.pdf and a confirmation page is rendered displaying the 
    entered information, new file name, and a link to download the file.
'''

from flask import Flask, request, render_template, send_from_directory
from werkzeug.utils import secure_filename
from datetime import datetime, date
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    '''
    Method to process/validate form data and uploaded file (must be a pdf)
    '''

    if request.method == 'POST':
        therapist = "".join(request.form['therapist_name'].split()).replace(" ", "")
        patient = "".join(request.form['patient_name'].split()).replace(" ", "")
        pdf = request.files.get('file')

        error = None
        header = pdf.read(4)
        pdf.seek(0)

        if not header == b'%PDF':
            error = "Error: File must be a PDF!"
            return render_template('form.html', title="Error",
                                   error=error)

        timestamp = datetime.now().strftime("%Y%m%d%")
        unsecure_filename = f"{therapist}_{patient}_{timestamp}.pdf"
        filename = secure_filename(unsecure_filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        pdf.save(filepath)

        return render_template('confirmation.html', title="Successful Submission",
                            therapist=therapist, patient=patient, filename=filename)

    return render_template('form.html', title="Patient Form")


@app.route('/uploads/<filename>')
def download_pdf(filename):
    '''
    Method to return url to download the uploaded file
    '''
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)


if __name__ == '__main__':
    app.run()
