# Project Prototype

TODO: The result of your work will be the delivery of some type of proof-of-concept prototype which will likely contain software programming solutions (i.e., Python code, HTML pages, or similar). All source code for the prototype must be stored in this directory. If your prototype uses data, please create `data/` subdirectory in `src/` and include your data file(s) in `src/data/` directory.

To allow the user to experience and execute your prototype, you must first explain how to set up the initial conditions to run or use the artifact. Be sure to offer explicit details and instructions regarding the installation of the necessary foundational libraries, drivers, external software projects, containers and similar types of tertiary software which are involved in executing your artifact. Once these initial software installations have been completed, then you are asked to offer the necessary instructions for actually executing the artifact. For this, please provide all command line parameters or associated bash commands for execution. Please remember that users are unwilling to "figure-out" how to use code in absence of the essential instructions concerning the execution of project artifacts.

## Key Features

* Player Statistic Retrieval: Users can enter the name of an NBA player to retrieve detailed career statistics.
* Data Visualization: The prototype provides visual representations of the data such as points per game over time using matplotlib and seaborn.
* Interactive Web Interface: Implemented using streamlit, allowing users to interactively query NBA player stats and view results in a web browser.

## Requirements

* Hardware: No specific hardware requirements; any standard computer with internet access will suffice.
* Software:
  * Python 3.8 or newer.
  * Libraries: pandas, matplotlib, seaborn, nba_api, streamlit.
  * A web browser to access the Streamlit application.

## Using the Prototype

Running the Streamlit App:

1. Navigate to the Project Directory:
Open a command line interface and change to the directory where your project is stored.
`cd path/to/your/project`
2. Start the Streamlit App:
Run the Streamlit app using the following command. Replace streamlit_nba_stats.py with the name of your Streamlit script.
`streamlit run streamlit_nba_stats.py`
3. Access the App:
Open your web browser and go to http://localhost:8501 to view and interact with the application.
Input the name of an NBA player to retrieve and display their statistics.
Example Usage:

Once the app is running, enter a player’s name like "LeBron James" into the input field and click the "Show Stats" button to view the statistics.
