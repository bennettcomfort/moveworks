import requests
import csv
# API URL and Token
API_URL = "https://gorest.co.in/public/v2/users"
API_TOKEN = "e82e412b4142b08abd1e5953dd439b88b0d4ee9353c70b5c077f458042e0fea6"  # Replace with your actual token

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

# Function to filter users with `.test` emails and active status
def filter_users(users):
    return [
        {"id": user["id"], "email": user["email"]}
        for user in users
        if user["status"] == "active" and user["email"].endswith(".test")
    ]


# Function to save users to CSV
def save_to_csv(users, filename):
    with open(filename, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["id", "email"])
        writer.writeheader()
        writer.writerows(users)
    print(f"CSV report generated: {filename}")


# Main function
def main():
    print("Starting process...")
    users = fetch_users()
    if not users:
        print("No users fetched.")
        return
    filtered_users = filter_users(users)
    if filtered_users:
        save_to_csv(filtered_users, "active_users_test_domain.csv")
    else:
        print("No matching users found.")

        
if __name__ == "__main__":
    main()