# FastAPI Todo App

This is a simple FastAPI application to manage a list of todo items.

Requirements

- Python 3.12
- FastAPI
- Uvicorn
- Pydantic

## Installation

1. Clone the repository:
2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

The app will be running at `http://127.0.0.1:8000`.

## API Endpoints

Get Todos

- Endpoint: /todos
- Method: GET
- Description: Retrieve all todo items.

Example Request

    ```bash
    curl -X GET "http://127.0.0.1:8000/todos"
    ```

Example Response

    ```json
    {
      "todos": ["Buy milk"]
    }
    ```

Add Todo

- Endpoint: /todos
- Method: POST
- Description: Add a new todo item.
- Headers: `Content-Type: application/json`
- Body: JSON object with a text field.

Example Request

    ```bash
    curl -X POST "http://127.0.0.1:8000/todos" -H "Content-Type: application/json" -d '{"text": "Walk the dog"}'
    ```

## Deploy to Azure Web App

There are multiple ways to deploy a Python app to Azure Web App. Below is one of the simplest approaches using the Azure Portal

Option A: Using Azure Portal (GUI)

1. Create an Azure Web App:

   - Go to the Azure Portal.
   - Click on Create a resource > Web App.
   - Fill in the required details (resource group, name, runtime stack = Python, etc.) and click Create.

2. Set Startup Command (if needed):

   - In your Web App, go to Configuration > General settings.
   - Under Startup Command, you may specify:

     ```bash
     uvicorn main:app --host 0.0.0.0 --port 8000
     ```

3. Configure Deployment (e.g., from GitHub or local zip):

   - In your new Web App, go to Deployment Center.
   - Choose the source (e.g., GitHub) and connect your repo.

4. Save and Restart

   - Azure will run your app using your specified command or auto-detect.
   - Test your endpoints at https://<your-azure-web-app-name>.azurewebsites.net/todos.

## Create an API Management Instance

1. Go to the Azure Portal at https://portal.azure.com.
2. Click on Create a resource in the upper-left corner.
3. Search for API Management and click Create.
4. Select your Subscription, choose an existing Resource Group (or create a new one).
5. Provide a Name for your API Management service, e.g., myTodoAPIM.
6. Select a Location and choose a Pricing tier. (For demo purposes, you can pick the Developer tier, which is cheaper for testing but not for production.)
7. Fill in Publisher name (e.g., your organization) and Publisher email.
8. Click Review + create, then Create. Provisioning can take several minutes.

## 2.2 Attach Your Web App to API Management

Once the API Management (APIM) instance is provisioned, follow these steps:

1. Go to your newly created API Management resource.
2. In the left-hand menu, click APIs under the API Management section.
3. Click + Add API (top toolbar).
4. You have multiple import options (OpenAPI, App Service, Function App, etc.). Since your FastAPI app is deployed as an App Service, choose App Service.
5. On the Create from App Service blade:
   - Subscription: select the subscription you used.
   - Resource Group: select the resource group containing your Web App.
   - App name: pick your Azure Web App from the dropdown (e.g., my-fastapi-todo).
   - API URL suffix: choose a suffix for your API’s URL path (e.g., todo).
   - Name: give the API a friendly name (e.g., TodoAppApi).
6. Click Create.

or

4. You can choose HTTP and provide the URL of your FastAPI app (e.g., https://my-fastapi-todo.azurewebsites.net).
5. Click Create.
6. Once the API is created, you add operations (GET, POST, etc.) to the API by clicking + Add operation.
7. You can test your API by clicking on the Test tab and sending a request.
