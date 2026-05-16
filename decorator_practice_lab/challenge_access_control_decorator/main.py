IS_ADMIN = False

def require_admin(func):
    def wrapper(*args, **kwargs):
        if not IS_ADMIN:
            raise PermissionError("Admin privileges required")
        return func(*args, **kwargs)
    return wrapper

@require_admin
def sensitive_action():
    return "Sensitive action performed"

# Example usage
try:
    print(sensitive_action())
except PermissionError as e:
    print("PermissionError:", e)

IS_ADMIN = True
try:
    print(sensitive_action())
except PermissionError as e:
    print("PermissionError:", e)