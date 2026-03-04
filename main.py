from loader import load_users_from_file
from services import get_active_admins
from summary import generate_summary, print_summary
import sys
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)
logger = logging.getLogger(__name__)

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = "users.txt"

def main():
    try:
        users = load_users_from_file(filename)
    except FileNotFoundError:
        logger.error(f"{filename} not found.")
        return

    active_admins = get_active_admins(users)
    summary = generate_summary(users, active_admins)
    print_summary(summary)

    logger.info("Starting user pipeline")
    logger.info("Loading users from file: " + filename)
    logger.info("Total Users Loaded: " + str(len(users)))
    logger.info(f"Total admins: {len(active_admins)}")

if __name__ == "__main__":
    main()