from services import get_active_admins, calc_active_users

def run_tests():
    test_users = [
        {"name": "Alice", "is_active": True, "is_admin": True},
        {"name": "Bob", "is_active": False, "is_admin": False},
        {"name": "Charlie", "is_active": True, "is_admin": False},
    ]

    active_admins = get_active_admins(test_users)
    active_count = calc_active_users(test_users)

    print("Active admin names:", [u["name"] for u in active_admins])
    print("Active user count:", active_count)


if __name__ == "__main__":
    run_tests()