import json
import requests

def clone_integration(integration_name, new_integration_name):
  """Clones an integration in OIC.

  Args:
    integration_name: The name of the integration to clone.
    new_integration_name: The name of the new integration.
    https://oic99214919-ocuocictrng29-ld.integration.ocp.oraclecloud.com/
    https://integration.us.oraclecloud.com/ic/api/integration/v1/integrations/HELLO_WORLD%7C01.02.0000/clone
    
  """

  # Get the integration details.
  response = requests.get(
      "https://integration.us.oraclecloud.com/ic/api/integration/v1/integrations/" + CSF_PPM_ImportProjectBudgets_Callback_Recipe)
  integration_details = json.loads(response.content)

  # Create the new integration.
  response = requests.post(
      "https://integration.us.oraclecloud.com/ic/api/integration/v1/integrations/",
      json={"name": CSF_PPM_ImportProjectBudgets_Callback_Recipe_new, "integrationDetails": integration_details})

  # Check the response status code.
  if response.status_code != 201:
    raise Exception("Failed to create integration: " + response.content)

# Clone the integration.
clone_integration("my-integration", "new-integration")
