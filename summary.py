def generate_summary(users, active_admins):
    return {
        "total_users": len(users),
        "active_users": sum(1 for u in users if u["is_active"]),
        "active_admins": len(active_admins),
        "active_admin_names": [u["name"] for u in active_admins],
    }


def print_summary(summary):
    print(f"Total users: {summary['total_users']}")
    print(f"Active users: {summary['active_users']}")
    print(f"Active admins: {summary['active_admins']}")
    print("Active admin names:")
    for name in summary["active_admin_names"]:
        print(name)