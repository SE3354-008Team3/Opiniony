# Opiniony

This code is split into three main files. To run any file, call "python {filename}" in the directory containing the file
1. createaccount.py
  - Creates a user account and stores it in the database
2. login.py
  - Logs in a user if given credentials that are stored in the database
3. analysis.py
  - Upload text for analysis

The other main files are the database controller (dbcontroller.py), the user class (user.py), the sentiment analysis model (sentiClass.py), and an unfinished account page UI (account.py). The database controller communicates with the database to upload and receive data. The user class is used to store user data after logging in. The sentiment analysis model will be used to actually analyze the text that a user submits to it.
