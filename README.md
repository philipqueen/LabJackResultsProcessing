# LabJackResultsProcessing
 Takes LabJack produced CSVs and saves plots of force over time, with max force value.
 
 ## File structure 
 Create a folder of your break test session, and then create a folder within that titled "CSVs". Place all of the LabJack .csv's you would like to process in the "CSVs" folder. Then, set the "session_folder_path" variable to the path of the session folder, which is *the folder that contains the "CSVs" folder*. Running the script will create a "GraphOutputs" folder, and then fill that folder with a graph for each .csv in the "CSVs" folder. 
 
 ## To run the script
 To run the script, download this repo to your local machine. Make sure you have put your data in a file structure as described above, and have downloaded all of the requirements listed below. Open a code editor, and change the "session_folder_path" variable to the path of your folder, and then run the script in the code editor. You should see console print outs as the script runs through the .csv's, and when it prints "All done!" you can find all of the graphs in the "GraphOutputs" folder.
 
 ## Requirements
 If you have already used Python on your machine, simply make sure the following libraries are installed. They are all very common, so there's a good chance you already have them downloaded:
 1. pandas
 2. numpy
 3. matplotlib

You can install them all at once by running ```pip install pandas numpy matplotlib``` in your terminal/command prompt. If you have them downloaded already, running the pip install code will simply tell you the requirements are already met. 

You will also need to have a code editor/IDE like VSCode or PyCharm installed, as well as Python itself. If you don't already have python and an IDE install, [here are instructions for downloading VSCode and using it with Python](https://code.visualstudio.com/docs/python/python-tutorial).

