import os
import time
import sys

# Define environment variables
OIC_USERNAME = sys.argv[1]
OIC_PASSWORD = sys.argv[2]
URL = sys.argv[3]
APP_VAR = sys.argv[4]
APP_VAR_VER = sys.argv[5]

# Export Integration Step
print("This is an Export Integration step")
os.system(f'curl -vvv -X GET -u {OIC_USERNAME}:{OIC_PASSWORD} -o "myfile_01.iar" {URL}/ic/api/integration/v1/integrations/{APP_VAR}%7C{APP_VAR_VER}/archive')
time.sleep(30)

# Import Integration Step
print("This is an Import Integration step")
os.system(f'curl -vvv -s -u {OIC_USERNAME}:{OIC_PASSWORD} -H "Accept: application/json" -X PUT -F "file=@myfile_01.iar;type=application/octet-stream" {URL}/ic/api/integration/v1/integrations/archive')

# Activate Integration Step
# print("This is an Activate Integration step")
# os.chdir("oic-migration")
# os.system(f'curl -X POST -u {OIC_USERNAME}:{OIC_PASSWORD} -H "Content-Type:application/json" -H "X-HTTP-Method-Override:PATCH" -d @activate.json {URL}/ic/api/integration/v1/integrations/{APP_VAR}')
