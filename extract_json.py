# import json

# def get_user_info_from_json(email):

#   try:
#     filename = "user_data.json"
#     with open(filename, 'r') as f:
#       data = json.load(f)

#     # Search for user data matching the email
#     for user_data in data:
#       if 'email' in user_data and user_data['email'] == email:
#         return user_data.get('name')
        

#     # Email not found
#     print(f"Email '{email}' not found in user data")
#     return None

#   except json.JSONDecodeError:
#     print(f"Error: Invalid JSON format in file '{filename}'")
#     return None




import json

def get_user_info_from_json(email):
    with open('user_data.json') as f:
        users = json.load(f)
        for user in users:
            if user['email'] == email:
                return user
    return None
