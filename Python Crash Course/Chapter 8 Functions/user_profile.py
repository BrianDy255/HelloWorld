def build_profile(first,last, **user_info):
    """build a dictionary containing everything we know about a user"""
    user_info["First: "] = first.title()
    user_info["Last: "] = last.title()
    return user_info

user_profile = build_profile('Albert',
                             'einstein',
                             location='princeton',
                             age=32,
                             field= 'Physics')
print(user_profile)

