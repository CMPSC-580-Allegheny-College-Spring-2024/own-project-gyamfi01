# Project Prototype
1. Installation Requirements:
   
* Python: The prototype is built using Python, so ensure Python 3.8 or newer is installed. You can download it from python.org.
* Libraries: Install necessary Python libraries using pip. This includes pandas for data manipulation, matplotlib and seaborn for data visualization, nba_api for accessing NBA statistics, and streamlit for creating the web application.
`pip install pandas matplotlib seaborn nba_api streamlit`
2. Data Setup:

* If your prototype uses historical NBA data, store these in the src/data/ directory. Ensure this data is correctly formatted and accessible by your scripts.

3. Software and Drivers:

* Web Browser: Any modern web browser (e.g., Chrome, Firefox, Safari) to access the Streamlit app.
* IDE/Code Editor: Recommended to use an IDE like PyCharm or VS Code for running and editing the Python scripts.

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
