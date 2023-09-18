
import json
import requests

CSF_PPM_ImportProjectBudgets_Callback_Recipe = "https://integration.us.oraclecloud.com/ic/api/integration/v1/integrations/"

def clone_integration(integration_name, new_integration_name):
  """Clones an integration in OIC.

  Args:
    integration_name: The name of the integration to clone.
    new_integration_name: The name of the new integration.
  """

  # Get the integration details.
  response = requests.get(
      CSF_PPM_ImportProjectBudgets_Callback_Recipe + integration_name)
  integration_details = json.loads(response.content)

  # Create the new integration.
  response = requests.post(
      CSF_PPM_ImportProjectBudgets_Callback_Recipe,
      json={"name": new_integration_name, "integrationDetails": integration_details})

  # Check the response status code.
  if response.status_code != 201:
    raise Exception("Failed to create integration: " + response.content)

# Clone the integration.
clone_integration("CSF_PPM_ImportProjectBudgets_Callback_Recipe", "new_integration")
