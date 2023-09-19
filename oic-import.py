import os

# Define environment variables
OIC_USERNAME = os.environ.get("OIC_USERNAME")
OIC_PASSWORD = os.environ.get("OIC_PASSWORD")
URL = os.environ.get("URL")
APP_VAR = os.environ.get("APP_VAR")

#Import Integration Step
print("This is an Import Integration step")
os.system(f'curl -vvv -s -u {OIC_USERNAME}:{OIC_PASSWORD} -H "Accept: application/json" -X PUT -F "file=@myfile_01.iar;type=application/octet-stream" {URL}/ic/api/integration/v1/integrations/archive')

# Activate Integration Step
# print("This is an Activate Integration step")
# os.chdir("oic-migration")
# os.system(f'curl -X POST -u {OIC_USERNAME}:{OIC_PASSWORD} -H "Content-Type:application/json" -H "X-HTTP-Method-Override:PATCH" -d @activate.json {URL}/ic/api/integration/v1/integrations/{APP_VAR}')
