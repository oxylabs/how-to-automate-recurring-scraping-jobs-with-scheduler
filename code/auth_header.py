import base64


def get_auth_header(username, password):
    """
    Takes `username` and `password`
    and returns Basic authentication header"""
    cred_string = f"{username}:{password}"
    cred_bytes = cred_string.encode("ascii")
    cred_encoded = base64.b64encode(cred_bytes)
    cred_encoded_string = cred_encoded.decode("ascii")

    return f"Basic {cred_encoded_string}"
