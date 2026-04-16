
import base64

# 1. Your credentials
api_key = "41243792ZXqpXLhGowFsjTzYXLCpLIMKFjtAX"
api_secret = "8666HTbV_AqrO_LnsMb1c4CjLpmlzmdlaQyukvQBaxA"


# 2. Combine them into a single string
credentials_string = f"{api_key}:{api_secret}"


# 3. Encode the string to bytes, then Base64 encode it
encoded_credentials = base64.b64encode(credentials_string.encode('utf-8')).decode('utf-8')


# 4. The final header value
auth_header = f"Basic {encoded_credentials}"


print(auth_header)
