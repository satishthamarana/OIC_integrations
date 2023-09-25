import os
import time

# Get environment variables from secrets
OIC_USERNAME = os.getenv("OIC_USERNAME")
OIC_PASSWORD = os.getenv("OIC_PASSWORD")
URL = os.getenv("OIC_URL")
APP_VAR = os.getenv("APP_VAR")
APP_VAR_VER = os.getenv("APP_VAR_VERSION")

try:
    # Export Integration Step
    print("This is an Export Integration step")
    os.system(f'curl -v -X GET -u {OIC_USERNAME}:{OIC_PASSWORD} -o "myfile_01.iar" {URL}/ic/api/integration/v1/integrations/{APP_VAR}%7C{APP_VAR_VER}/archive')
    time.sleep(30)

    # Import Integration Step
    print("This is an Import Integration step")
    os.system(f'curl -s -u {OIC_USERNAME}:{OIC_PASSWORD} -H "Accept: application/json" -X PUT -F "file=@myfile_01.iar;type=application/octet-stream" {URL}/ic/api/integration/v1/integrations/archive')

    # Activate Integration Step
    print("This is an Activate Integration step")
    os.system(f'curl -v -X POST -u {OIC_USERNAME}:{OIC_PASSWORD} -H "Content-Type:application/json" -H "X-HTTP-Method-Override:PATCH" -d @activate.json {URL}/ic/api/integration/v1/integrations/{APP_VAR}%7C{APP_VAR_VER}')

except Exception as error:
    print("This is teh error occured: ", error)

finally:
    print("closing the connections")
    os.system(f'curl -u {OIC_USERNAME}:{OIC_PASSWORD} -H "Connection: close" {URL}/ic/home')
