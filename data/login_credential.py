import os
from dotenv import load_dotenv

load_dotenv()

# Access the environment variables
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

print(username)
print(password)
