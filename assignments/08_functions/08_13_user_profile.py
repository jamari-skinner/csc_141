def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

my_profile = build_profile('jamari', 'skinner',
    location='united states',
    field='automotive engineering',
    hobby='football')

print(my_profile)