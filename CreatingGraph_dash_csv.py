import tkinter as tk
import tkinter.messagebox
import pandas as pd
import plotly.express as px
import dash
from dash import dcc
from dash import html

root = tk.Tk() # Create GUI
root.geometry("500x500") # Set geometry of GUI as 500x500
root.config(bg="lightblue") # Set color of Gui as light blue
root.resizable(0,0) # Do not allow user to expand the GUI
root.title("Create Graph") # Set GUI title as Create Graph

app = dash.Dash() # Open graph application


# The function for showing instruction of creating scatter graph
def instructionCSV():
    tkinter.messagebox.showinfo("Instructions", ''' 
    1.Put CSV file name without .csv

    2.Put X-value and Y-value from dataframe of the file

    3.Push the button name of "Create from csv"
    ''')
# Showing message above

# The function for showing instruction of converting Excel file into CSV file
def instructionCon():
    tkinter.messagebox.showinfo("Instructions", '''
    1.Put Excel file name without .xlsx

    2.Put name of the new csv file

    3.Push the button name of "Create CSV file"
    ''')
# Showing message above

# The function for converting Excel file to CSV file
def convert():
    EXfile = pd.read_excel(Excelvar.get() + ".xlsx") # Reading Excel file which user put in entry
    EXfile.to_csv(CSVname.get() + ".csv") # Converting Excel file in to CSV file with the name of user set
    tkinter.messagebox.showinfo("Message","Successfully created") # Showing message to let user know it has done


#---From Resource (Below)-----------#
# The function for creating scatter graph
def create():
    CSfile = pd.read_csv(csvvar.get() + ".csv") # Reading csv file which user put in entry
    figcv = px.scatter( # Setting of scatter graph
        CSfile, # The CSV file for creating scatter graph
        x=str(Xvar.get()), # X-value from dataframe of the CSV file. user can choose
        y=str(Yvar.get()), # Y-value from dataframe of the CSV file. user can choose
        size_max=60, # The maximum size of scatter. Set it as 60
        log_x=True, # Chart type(Scatter) = True
    )
    app.layout = html.Div([dcc.Graph(id="CSV_to_graph", figure=figcv)])
    # Layout of the graph
    # id - a unique identifier of the element = CSV_to_graph
    # figure of the graph is figcv
    if __name__ == "__main__":
        app.run_server(debug=True)
    # The function to run the dash app
#----------From Resource (Above)--------------#

Excelvar = tk.StringVar() # Name of the Excel file to convert
csvvar = tk.StringVar() # Name of the CSV file to creating graph
CSVname = tk.StringVar() # Name of the New CSV file converted from the Excel file

Xvar = tk.StringVar() # Name of the X-value
Yvar = tk.StringVar() # Name of the Y-value


# Entry for type Excel file name
ConvertEn = tk.Entry(root,width=20,textvariable=Excelvar,font="arial 15 bold",justify="center").place(x=25,y=350)
# Entry for type New CSV file name
NewCSV = tk.Entry(root,width=20,textvariable=CSVname,font="arial 15 bold",justify="center").place(x=270,y=350)
# Entry for type CSV file name to creating graph
CSVfileEn = tk.Entry(root,width=42,textvariable=csvvar,font="arial 15 bold",justify="center").place(x=25,y=100)
# Entry for type X-value
XEn = tk.Entry(root,width=15,textvariable=Xvar,font="arial 15 bold",justify="center").place(x=25,y=170)
# Entry for type Y-value
YEn = tk.Entry(root,width=15,textvariable=Yvar,font="arial 15 bold",justify="center").place(x=250,y=170)

# Label for Converting Excel file entry
ExLabel = tk.Label(root,text="Put Excel File Name Here").place(x=25,y=320)
# Label for New CSV file entry
NcsvLabel = tk.Label(root,text="Put New CSV File Name Here").place(x=270,y=320)
# Label for CSV file to creating graph entry
CsvLabel = tk.Label(root,text="Put CSV File Name Here").place(x=25,y=70)
# Label for X-value of the graph entry
XLabel = tk.Label(root,text="X-Value").place(x=25,y=140)
# Label for Y-value of the graph entry
YLabel = tk.Label(root,text="Y-Value").place(x=250,y=140)

# Button for converting Excel file to CSV file
Converter = tk.Button(root,text="Create CSV file",font="arial 15 bold",fg="White",bg="Black",command=convert).place(x=300,y=400)
# Button for creating graph
Create = tk.Button(root,text="Create from csv",font="arial 15 bold",fg="White",bg="Black",command=create).place(x=300,y=230)
# Button for showing instruction of creating graph
Instraction1 = tk.Button(root,text="Instructions",command=instructionCSV).place(x=25,y=40)
# Button for showing instruction of converting Excel file to CSV file
Instraction2 = tk.Button(root,text="Instructions",command=instructionCon).place(x=25,y=290)


root.mainloop() # Active the GUI

#Resource = https://towardsdatascience.com/plotly-dashboards-in-python-28a3bb83702c