import requests
import csv
from collections import defaultdict

# API URL and Token
API_URL = "https://gorest.co.in/public/v2/users"
API_TOKEN = "9d911e8c06c5c4ff6157a4d11bc8ec2b9193d68f73465115cb4b0a4ff77a4b89"  # Replace with your actual token

# Function to fetch users
def fetch_users():
    users = []
    page = 1
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    while True:
        print(f"Fetching page {page}...")
        response = requests.get(API_URL, headers=headers, params={"page": page})
        if response.status_code != 200:
            print(f"Error: {response.status_code} - {response.text}")
            break
        data = response.json()
        if not data:  # Break if no more data
            break
        users.extend(data)
        page += 1
        if page == 5:
            break
    return users

# Function to process email domains
def process_email_domains(users):
    domain_count = defaultdict(int)
    domain_counts = {}
    for user in users:
        domain = user["email"].split("@")[-1].split(".")[-1]
        domain_counts[domain] = domain_counts.get(domain, 0) + 1
    return [{"domain": domain, "count": count} for domain, count in domain_counts.items()]

# Function to save domain counts to CSV
def save_to_csv(filename, data, headers):
    try:
        with open(filename, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)
        print(f"Data written to {filename}")
    except Exception as e:
        print(f"Error writing to CSV: {e}")

# Main function
def main():
    print("Starting process...")
    users = fetch_users()
    if not users:
        print("No users fetched.")
        return
    domain_counts = process_email_domains(users)
    save_to_csv("domain_counts.csv", domain_counts, ["domain", "count"])
if __name__ == "__main__":
    main()