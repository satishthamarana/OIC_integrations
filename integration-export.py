import requests

# Set the integration ID
integration_id = 'CSF_IMPSUPADD_CALLBACK_RECIPE%01.00.0000'

# clineturl

client_url = 'https://oic99214919-ocuocictrng29-ld.integration.ocp.oraclecloud.com'

# Set the access token
access_token = 'YOUR_ACCESS_TOKEN'

# Set the output file name
output_file_name = 'myfile.iar'

# Build the REST call URL
url = '%s/ic/api/integration/v1/integrations/%s/archive' % (client_url, integration_id)

# Create a GET request
request = requests.Request('GET', url)

# Add the authorization header
request.headers['Authorization'] = 'Bearer %s' % access_token

# Send the request and get the response
response = requests.send(request)

# Raise an exception if the request failed
if response.status_code != 200:
    raise Exception('Failed to export integration: %s' % response.content)

# Save the response to the output file
with open(output_file_name, 'wb') as f:
    f.write(response.content)

# Print a success message
print('Integration successfully exported to %s' % output_file_name)
