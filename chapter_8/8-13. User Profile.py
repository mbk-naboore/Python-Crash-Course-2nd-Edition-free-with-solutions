def build_profile(first_name, last_name, **info):
    info["First name"] = first_name
    info["Last name"] = last_name
    info["Full name"] = f"{first_name} {last_name}"
    return info


user_info = build_profile(first_name="Muhammad", last_name="Ali", age=18, location="Kentucky", job="boxer")
print(user_info)

