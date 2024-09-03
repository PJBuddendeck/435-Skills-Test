Skills Assignment Submission by Peter Buddendeck
====================================================================

How to Run:

There should be four items within the working directory for this assignment. "README" is the text document you are currently reading. "Output" is the folder that annotated screenshots are sent to after being created. "Programming-Assignment-Data" contains all the required .xml and .png files. "assignment.py" contains all the code written for the assignment. It should be ran using the command "python assignment.py" while in the working directory.

The project utilizes the os, shutil, and PIL libraries. os and shutil are default Python libraries, but PIL must be installed. For information about installation, follow the link below:
https://pillow.readthedocs.io/en/stable/

It should be noted that the library is already installed on the W&M CS Lab Machines. It is recommended that this assignment is ran on the Lab Machines for ease of use.

When the Python file is ran, it will prompt the user to enter a file name. Names should be entered exactly as they appear within the "Project-Assignment-Data" directory, without the file extension included. For example, inputting "com.apalon.ringtones" will work, but "com.apalon.ringtones.xml" will not. Failure to enter a name correctly will result in a message stating that the file could not be opened.

====================================================================

Design Description and Rationale:

Basic information about how the project runs can be found within the code's comments. Please read the comments and browse over the code before reading this section.

Due to the smaller nature of this assignment, I decided to use Python for my code. This would end up causing a minor headache later on, but at that point in time, I was already too invested in finishing the job in Python.

The program starts by determining where the working directory is located, then prompting the user for a file name. After a name is received, the program attempts to parse the name and open the appropriate .xml file. A try-except block is included to prevent unintended consequences should the user input an incorrect file name. From there, a copy of the image with the same name is made for the sake of future editing. An image drawer is also initialized for later use.

The .xml file is then scanned through line by line, and each instance of coordinate bounds are extracted and placed into a separate list. I could have avoided this step and drew the rectangles without a separate list, but I chose to write the code in the same way that my brain sorted through the problem. When iterating through the boundary list, I isolated the corner coordinates and stored them within a 2D array. Using Python ended up greatly simplifying this step thanks to the many string functions it contains. After that, all I had to do was draw the boundary rectangle, but it ended up being harder than anticipated.

The minor headache I mentioned earlier had to do with PIL. I was having difficulties installing the library on my machine, so I decided to see if it was already installed on the W&M Lab Machines. Luckily for me, it already was, so I copied my code over to test it out. It took a minute, in part because the code is in Python, and in part because I needed to manually input the file names, but every image was successfully outputted to the "Output" directory I mentioned earlier.

While I could have condensed the code a bit more, and written it in a faster language, I am satisfied with my submission.
