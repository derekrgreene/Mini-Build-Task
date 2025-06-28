## 🧪 Add-On Questions

### 1. Explain how your app handles form validation. What happens if a required field is missing or the date is in the future?

My app uses a combination of client-side and server-side validation. Required fields are enforced on the client side by adding the required attribute to each input, so the browser prevents submission if any required field is missing. For the Date of Birth (DOB), the app performs server-side validation upon form submission by comparing the submitted date against the current date. If the DOB is in the future, the app returns an error message without saving the data to the SQLite database, and the form is re-rendered with the user’s input preserved and the error displayed.

### 2. If we wanted to extend the app to support therapist logins, how would you structure that?

To add therapist logins, I would implement OAuth for authentication to avoid managing passwords directly. This would generate JWTs to securely maintain therapist sessions. I would create a new therapists table to store therapist-specific data, including a unique internal ID and the OAuth provider’s user ID to link external accounts. The app would include a /login endpoint to serve a login page, and backend logic to handle OAuth callbacks, issue JWTs, and verify session state.

### 3. How would you deploy this app to a HIPAA-compliant cloud environment?

I would deploy on a HIPAA-compliant cloud provider like GCP, AWS, or Azure. The infrastructure would be secured by isolating resources in private VPCs, enforcing HTTPS for all traffic, and encrypting all PHI data at rest using cloud-native encryption services. The database would run as a managed service with encrypted storage, separate from the app servers. Role-based access controls combined with OAuth/JWT authentication would restrict data access to authorized users only. Additionally, I would enforce MFA for all admin and developer accounts via IAM. Finally, comprehensive logging and audit trails would be enabled to track all access and changes to PHI for compliance.

### 4. Where would you place the code that initializes the database and why?

I would keep the code that initializes the database seperate from the main flask backend in a sperate file and directory. Doing this keeps the database setup seperate from the application logic and aids in preventing unauthorized changes to the data or schema, in addition to preventing accidental/unintentional overwrites. 

