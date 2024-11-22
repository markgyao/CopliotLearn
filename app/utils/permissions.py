# # app/utils/permissions.py

# role_permissions = {
#     "admin": {
#         "users": ["create", "read", "edit", "delete"],
#         "students": ["create", "read", "edit", "delete"],
#         "roles": ["create", "read", "edit", "delete"],
#         # Add other resources as needed
#     },
#     "student": {
#         "users": ["read", "edit"],
#         "students": ["read", "edit"],
#     },
#     "teacher": {
#         "users": ["read", "edit"],
#         "students": ["read", "edit"],
#         "classes": ["read", "edit"],
#     },
#     # Add other roles as needed
# }

# role_id_to_name = {
#     1: "admin",
#     2: "student",
#     3: "teacher",
#     4: "parent",
# }

# def has_permission(user_role_id, resource, action):
#     role_name = role_id_to_name.get(user_role_id)
#     if not role_name:
#         return False
#     permissions = role_permissions.get(role_name, {})
#     actions = permissions.get(resource, [])
#     return action in actions
