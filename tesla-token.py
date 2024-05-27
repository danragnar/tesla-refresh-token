# A python script for getting a OIDC refresh token from auth.tesla.com using PKCE Code authorization flow

import requests
import base64
import hashlib
import secrets
import urllib.parse

# Step 1: Generate a code verifier
code_verifier = secrets.token_urlsafe(32)

# Step 2: Derive a code challenge from the code verifier
code_challenge = hashlib.sha256(code_verifier.encode('ascii')).digest()
code_challenge = base64.urlsafe_b64encode(code_challenge).rstrip(b'=')

# Step 3: Construct the authorization URL
auth_endpoint = 'https://auth.tesla.com/oauth2/v3/authorize'
client_id = 'ownerapi'
redirect_uri = 'https://auth.tesla.com/void/callback'
scope = 'openid email offline_access'
state = secrets.token_urlsafe(16)

params = {
    'client_id': client_id,
    'code_challenge': code_challenge,
    'code_challenge_method': 'S256',
    'redirect_uri': redirect_uri,
    'response_type': 'code',
    'scope': scope,
    'state': state
}

auth_url = f"{auth_endpoint}?{urllib.parse.urlencode(params)}"

# Step 4: Open the authorization URL in a browser and complete the user authentication flow
print(f"Please visit the following URL and complete the authentication flow:\n{auth_url}")

# Step 5: Receive the authorization code from the redirect URI
auth_code = input("Enter the authorization code: ")

# Step 6: Exchange the authorization code for an access token and refresh token
token_endpoint = 'https://auth.tesla.com/oauth2/v3/token'

data = {
    'grant_type': 'authorization_code',
    'client_id': client_id,
    'code': auth_code,
    'code_verifier': code_verifier,
    'redirect_uri': redirect_uri
}

response = requests.post(token_endpoint, data=data)
response_data = response.json()

if 'refresh_token' in response_data:
    refresh_token = response_data['refresh_token']
    print(f"Refresh token: {refresh_token}")
else:
    print("Failed to obtain refresh token.")

