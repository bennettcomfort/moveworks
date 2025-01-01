# User Data Processing

This repository contains scripts to fetch user data from an API, process it, and generate reports in CSV format.

## Setup

1. Create a virtual environment:
    ```sh
    python3 -m venv venv
    ```

2. Activate the virtual environment:
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```
    - On Windows:
        ```sh
        .\venv\Scripts\activate
        ```

3. Install the required packages:
    ```sh
    pip install requests
    ```

## Structure

## Scripts

### Question 1

- **Script**: task1_report.py
- **Description**: Fetches users from the API, filters active users with `.test` email domains, and saves them to [active_users_test_domain.csv](http://_vscodecontentref_/4).
- **Usage**:
    ```sh
    python Question\ 1/task1_report.py
    ```

### Question 2

- **Script**: task2_report.py
- **Description**: Fetches users from the API, processes email domains, and saves the domain counts to [domain_counts.csv](http://_vscodecontentref_/5).
- **Usage**:
    ```sh
    python Question\ 2/task2_report.py
    ```

## CSV Files

- **active_users_test_domain.csv**: Contains the list of active users with `.test` email domains.
- **domain_counts.csv**: Contains the count of email domains.

## Notes

- Replace the [API_TOKEN](http://_vscodecontentref_/6) in the scripts with your actual token.
- The scripts fetch up to 4 pages of user data from the API.

## License

This project is licensed under the MIT License.