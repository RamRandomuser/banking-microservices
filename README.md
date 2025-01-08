# banking-microservices
 Super simple Microservices-based banking application

## Overview
This repository contains a basic banking application built using Flask microservices. The application is designed to demonstrate the use of microservices architecture in a simple banking domain.

## Microservices
The application consists of the following three microservices:

1. **Account Service**: Manages user accounts, including account creation, retrieval, and updates.
2. **Transaction Service**: Handles all transactions, including deposits, withdrawals, and transfers between accounts.
3. **Notification Service**: Sends notifications to users about their account activities and transactions.

## Prerequisites
- Python 3.8 or higher
- Flask
- Docker 

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/banking-microservices.git
    cd banking-microservices
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Services
Each microservice can be run independently. Navigate to the respective service directory and start the Flask server:

1. **Account Service**:
    ```bash
    cd account_service
    flask run
    ```

2. **Transaction Service**:
    ```bash
    cd transaction_service
    flask run
    ```

3. **Notification Service**:
    ```bash
    cd notification_service
    flask run
    ```

## Usage
Once the services are running, you can interact with them using HTTP requests. Below are some example endpoints:

- **Account Service**:
    - `POST /accounts` - Create a new account
    - `GET /accounts/<account_id>` - Retrieve account details

- **Transaction Service**:
    - `POST /transactions` - Create a new transaction
    - `GET /transactions/<transaction_id>` - Retrieve transaction details

- **Notification Service**:
    - `POST /notifications` - Send a new notification

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.