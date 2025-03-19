# ContainerRegistryAuthentication

Authentication configuration for various container registry types, including AWS ECR, Docker Hub, GCP GAR, GCP GCR, and basic authentication.

**Properties**

| Name       | Type                                     | Required | Description                                                                 |
| :--------- | :--------------------------------------- | :------- | :-------------------------------------------------------------------------- |
| aws_ecr    | ContainerRegistryAuthenticationAwsEcr    | ❌       | Authentication details for AWS Elastic Container Registry (ECR)             |
| basic      | ContainerRegistryAuthenticationBasic     | ❌       | Basic username and password authentication for generic container registries |
| docker_hub | ContainerRegistryAuthenticationDockerHub | ❌       | Authentication details for Docker Hub registry                              |
| gcp_gar    | ContainerRegistryAuthenticationGcpGar    | ❌       | Authentication details for Google Artifact Registry (GAR)                   |
| gcp_gcr    | ContainerRegistryAuthenticationGcpGcr    | ❌       | Authentication details for Google Container Registry (GCR)                  |
