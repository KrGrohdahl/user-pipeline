from loader import load_users_from_file
from services import get_active_admins
from summary import generate_summary, print_summary
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = "users.txt"

def main():
    users = load_users_from_file(filename)
    active_admins = get_active_admins(users)
    summary = generate_summary(users, active_admins)
    print_summary(summary)

if __name__ == "__main__":
    main()