# 🛠️ Mini Build Challenge – Therapist Attachment Submission

## 📄 Deliverables

### 1. How did you validate PDF file types?

My application performs server side PDF file-type validation by reading the magic number of the uploaded file (first 4 bytes) and comparing against the standard signature for PDF files. Additional client side validation is performed to ensure the form is not submitted with a missing file or other fields missing data.

### 2. How would you change this to store files securely in S3?

To refactor this application to store files in S3, I would configure an S3 bucket on AWS and update the logic that currently saves the file locally to upload to S3.

### 3. How would you link this to a Patient model in a real application?

In a real application, I would link this to a patient model by defining a patients table in a databas and store each submission as a new patient record with the therpaist name, patient name, and file URL.
