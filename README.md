# ResultNotifier
This Python Script is Intended to Notify the User about the Exam Results declared on the College/University Website and was Specifically scripted for my Results. 

# resultsnotifier.py
The Code checks the internet connection, if its up : grabs the HTML content of the Target Page and then Searches for the Keywords 
If Keyword is found, another file resultsconfirm.py is called

# resultsconfirm.py
This file enters Credentials like Annual/semester and course to search the Database of Declared results for the Keywords of my Course
If found, another file resultsnotifier.py is called

# resultsnotifier.py
This code enters the Student specific details and searches for gradecard. Further it takes a screenshot and saves the files as studentname.jpeg

