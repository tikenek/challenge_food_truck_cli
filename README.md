# Food Truck Locator Command Line Interface (CLI) application

Thank you for taking some time to review the code. I embarked on my journey to learn my very first programming language, Python, just two weeks ago. I'm looking forward to discussing my work in person, sharing my additional ideas, and explaining my approach to tackling this challenge. If you are new with challenges and python as well, this the beginner friendly  start to solve this challenge.


This is a Python script that allows you to interact with a CSV file containing data about food trucks. You can perform various operations to search for, list, and find information about food trucks based on different criteria.


## Getting Started

To run this script, you'll need to set up a Python environment, install the necessary packages, and have a CSV file with food truck data.

### Prerequisites

- Python 3.7+
- Virtual Environment (venv) - To create an isolated Python environment.
- geopy - A Python library for calculating distances between coordinates.

### Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/tikenek/challenge_food_truck_cli.git
    ```

2. Create a virtual environment:

    ```bash
    2.1. cd challenge_food_truck_cli

    2.2. python -m venv venv

    #On Mac use:
    2.3. source venv/bin/activate
    # On Windows, use: 
    .venv\Scripts\activate
    # On Linux, use:
    source venv/bin/activate
    ```

3. Install the required packages using pip:

    ```bash
    pip install geopy
    ```

### Usage

The script provides the following commands for interacting with food truck data:

First you need to run "python3 app.py" in the project directory to start the CLI

1. **List All Food Trucks:**



    ```bash
    list
    ```

2. **Search for Specific Food Trucks:**

    ```bash
    search
    ```

3. **Get Information About Food Trucks in a Specific Address:**

    ```bash
    address
    ```

4. **Calculate Distance to Food Trucks:**

    ```bash
    distance
    ```

5. **Find Nearby Food Trucks:**

    ```bash
    nearby
    ```

6. **Exit the Program:**

    ```bash
    exit
    ```

Make sure to answer questions after you type one of the above commands when prompted.

## Acknowledgments

- This script uses the [geopy](https://geopy.readthedocs.io/) library for geospatial calculations.
