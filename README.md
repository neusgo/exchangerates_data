# exchangerates_data

# Flask API for Currency Conversion

This project is a Flask-based web service that interacts with an exchange rate API to convert currencies.

## Table of Contents
- [API Documentation](#api-documentation)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)

## API Documentation

### Convert Currency
Endpoint: `/convert`

**Parameters:**
- `from` (string): The base currency code.
- `to` (string): The target currency code.
- `amount` (float): The amount to convert.

**Example Request:**

   ```bash
   curl -X GET "http://localhost:3000/convert?from=USD&to=EUR&amount=100"
   ```

**Example Result:**
{
  "result": 87.25
}


## Getting Started

### Prerequisites
- Python 3.x
- Flask
- requests

### Installation
1. **Clone this repository:**

   ```bash
   git clone https://github.com/neusgo/exchangerates_data.git

2. **Change into the project directory:**

   ```bash
   cd exchangerates_data

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt


## Usage
1. **Run the Flask application:**

   ```bash
   python app.py

2. **Open your web browser and visit http://localhost:3000/ and put in From Currency:CAD, To Currency:PEN and Amount:200  to test the currency conversion endpoint.**
