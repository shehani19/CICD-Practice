import subprocess
import secrets

def generate_reset_code():
    """Generate a secure six-digit reset code."""
    return str(secrets.randbelow(900000) + 100000)

def show_directory_contents():
    """Safer version for Windows."""
    subprocess.run(["cmd", "/c", "dir"], check=True)

def validate_username(username):
    """Return True when a username is acceptable."""
    if not isinstance(username, str):
        return False

    username = username.strip()

    if len(username) < 4 or len(username) > 20:
        return False

    return username.replace("_", "").isalnum()


def create_profile_message(username, role="student"):
    """Create a simple profile message for a valid username."""
    if not validate_username(username):
        raise ValueError("Invalid username")

    allowed_roles = {"student", "lecturer", "admin"}

    if role not in allowed_roles:
        raise ValueError("Invalid role")

    return f"User: {username.strip()} | Role: {role}"


if __name__ == "__main__":
    print(create_profile_message("student_01"))