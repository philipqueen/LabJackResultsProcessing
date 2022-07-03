import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from glob import glob

plt.rcParams["figure.figsize"] = (10,8)

# set data path for break test session
session_folder_path = Path(r"/Users/Philip/Documents/BreakTests/Dyneemite") #set this to the folder containing your "CSVs" folder

# get folder path for CSV/TSV files
csv_data_folder_name = "CSVs" #if you change the name of the subfolder containing your CSV info, change this to match
csv_data_folder_path = session_folder_path / csv_data_folder_name

# create folder for graphs
graph_folder_name = "GraphOutputs"
graph_folder_path = session_folder_path / graph_folder_name
os.makedirs(graph_folder_path, exist_ok=True)

# get all files of given file type from the data folder
os.chdir(csv_data_folder_path)
file_type = ".csv" #change this to match file extension if it ever changes to ".tsv"
file_list = glob('*' + file_type) #finds any file in the directory ending with the file type

# load and process all files coded file for testing
for file in file_list:
    # create name and path for file
    file_name = file.split(".csv")[0]
    graph_name = file_name + ".jpg"
    graph_path = graph_folder_path / graph_name

    # load csv data into pandas dataframe
    print(f"Opening {file_name}...")
    rows_to_skip = 2 #csv's from lab jack have a few nonconforming rows at the top that will mess with pandas
    df = pd.read_csv(csv_data_folder_path / file, sep='\t', skiprows = rows_to_skip)

    # set column names
    df.columns = ['Time', 'Voltage1', 'Voltage2', 'Distance_Traveled', 'Force_in_kN']

    # find max force
    max_force = df['Force_in_kN'].max()
    # index_of_max_force = df['Force_in_kN'].idxmax() #find the index where that max occurred
    # time_of_max_force = df['Time'][index_of_max_force] # get the time value for that index

    # create plot
    ax = df.plot(x = 'Time',
       y = 'Force_in_kN',)

    # add text giving max force info
    ax.text(0, (max_force * 0.8), f'Max Force is {max_force} kN', fontsize = 20)

    # remove legend and set label and title
    ax.get_legend().remove()
    ax.set_ylabel("Force in kN")
    ax.set_title(file_name)

    # save figure
    print("Saving figure...")
    ax.figure.savefig(graph_path, dpi = 300)

    # clear matplotlib for next plot
    plt.cla()
    plt.clf()


print("All done!")


