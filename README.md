# apiRequest

apiRequest is a Python project that fetches gold price data from the National Bank of Poland's API and displays the prices for the last 30 days.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [API Details](#api-details)
- [Project Structure](#project-structure)
- [License](#license)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/apiRequest.git
    ```

2. Navigate to the project directory:
    ```bash
    cd apiRequest
    ```

3. Set up a virtual environment:
    ```bash
    python3 -m venv .venv
    ```

4. Activate the virtual environment:
    - On macOS/Linux:
      ```bash
      source .venv/bin/activate
      ```
    - On Windows:
      ```bash
      .venv\Scripts\activate
      ```

5. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the script to fetch and display the gold prices for the last 30 days:
    ```bash
    python3 api_request.py
    ```

2. The script will output a list of dates and corresponding gold prices in PLN (Polish Złoty).

## API Details

- **API Endpoint**: [National Bank of Poland's Gold Prices API](http://api.nbp.pl/api/cenyzlota/last/30/?format=json)
- **Purpose**: Fetches the gold prices for the last 30 days.

## Project Structure

apiRequest/
├── .venv/ # Virtual environment (ignored by Git)
├── api_request.py # Main script for fetching and displaying gold prices
├── .gitignore # Files and directories to be ignored by Git
├── README.md # Project overview and instructions
└── requirements.txt # Dependencies for the project


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
