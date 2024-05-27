# Install

Install dependencies:

   
pip install -r requirements.txt
   

# Run

- python3 ./tesla-token.py


Please visit the following URL and complete the authentication flow:

https://auth.tesla.com/oauth2/v3/authorize?client_id=ownerapi&code_challenge=w3D-_6SSwjKyy1Mnw9_Dr_8d8X5wiIvMTSZpyM0GmEU&code_challenge_method=S256&redirect_uri=https%3A%2F%2Fauth.tesla.com%2Fvoid%2Fcallback&response_type=code&scope=openid+email+offline_access&state=JDWVLOrak4wiEnRsPQyzWg


Go to url, login and copy the "code" parameter from the URL bar after login, paste into terminal. The refresh token can be copied into application that needs to auth to tesla API.