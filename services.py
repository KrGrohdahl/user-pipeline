def get_active_admins(users):
    active_admins = []

    for user in users:
        if user["is_active"] and user.get("is_admin", False):
            active_admins.append(user)

    return active_admins