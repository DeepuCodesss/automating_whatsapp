requirements:
selenium
pandas
openpyxl

how it will work:-
Step 1: Prepare the Project Folder First, create a new folder on your computer for this project. Inside that folder, you need to have three specific files: your Python script (e.g., whatsapp_bot.py), the list of numbers in an Excel file named contacts.xlsx, and a text file named requirements.txt. Make sure the Excel file has a column header named "Phone" and that all numbers are in the international format (like +919876543210).

Step 2: Create a Virtual Environment To keep your computer clean and avoid software conflicts, you should use a Virtual Environment. Open your Terminal or Command Prompt, navigate to your project folder, and type python -m venv venv. Once created, you must activate it. On Windows, type venv\Scripts\activate. On a Mac or Linux machine, type source venv/bin/activate. You will know it worked because you’ll see (venv) appear at the start of your command line.

Step 3: Install the Required Modules With your virtual environment active, you need to install the libraries that allow Python to control the browser and read Excel. Instead of installing them one by one, simply run the command pip install -r requirements.txt. This will automatically read your text file and install Selenium, Pandas, and Openpyxl all at once.

Step 4: Launch the Automation Run the script by typing python whatsapp_bot.py. A Google Chrome window will open automatically. Scan the QR code with your phone as you normally would for WhatsApp Web. Wait until your chat list fully loads on the left side of the screen. Once everything is visible, go back to your terminal window and press the Enter key.

Step 5: Focus and Safety This is the most important part: immediately after pressing Enter in the terminal, you must click once inside the Chrome window. The script uses keyboard shortcuts (Ctrl + Alt + N) and the Tab key to navigate, and these only work if the browser is the "active" window on your screen. The script will then open the menu, add 100 members, name the group, and create it. It includes a built-in "cool down" timer between groups to protect your account from being flagged as a bot.
