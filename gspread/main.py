
# Load key from file
with open('GOOGLE_API.SECRET') as f:
	google_api_key = f.read()

print("Using Google API key: %s" % google_api_key)

# Load spreadsheet from google docs

# Load to a dataframe
