from constructs import Construct
from cdktf import App, TerraformStack
from imports.azurerm import ResourceGroup, ContainerRegistry, ContainerAppsEnvironment, ContainerApp

class MyStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        # Resource Group
        resource_group = ResourceGroup(self, "ResourceGroup",
            name="example-rg",
            location="East US"
        )

        # Azure Container Registry
        acr = ContainerRegistry(self, "ContainerRegistry",
            name="exampleacr123",
            resource_group_name=resource_group.name,
            location=resource_group.location,
            sku="Basic",
            admin_enabled=True
        )

        # Azure Container Apps Environment
        env = ContainerAppsEnvironment(self, "ContainerAppsEnvironment",
            name="example-env",
            resource_group_name=resource_group.name,
            location=resource_group.location
        )

        # Azure Container App for the backend
        ContainerApp(self, "BackendApp",
            name="backend-app",
            resource_group_name=resource_group.name,
            location=resource_group.location,
            container_app_environment_id=env.id,
            configuration={
                "ingress": {"external_enabled": True, "target_port": 8080}
            },
            template={
                "containers": [
                    {"name": "backend", "image": "exampleacr123.azurecr.io/backend:latest"}
                ]
            }
        )

        # Azure Container App for the frontend
        ContainerApp(self, "FrontendApp",
            name="frontend-app",
            resource_group_name=resource_group.name,
            location=resource_group.location,
            container_app_environment_id=env.id,
            configuration={
                "ingress": {"external_enabled": True, "target_port": 8501}
            },
            template={
                "containers": [
                    {"name": "frontend", "image": "exampleacr123.azurecr.io/frontend:latest"}
                ]
            }
        )

app = App()
MyStack(app, "cdktf")
app.synth()
