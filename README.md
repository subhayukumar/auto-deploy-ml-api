# Dockerized ML Model Deployment with Helm

This project demonstrates a simple approach to deploying machine learning models in a Docker container using Kubernetes Helm charts. It aims to provide a scalable and manageable solution for deploying machine learning models within a Kubernetes cluster.

## Prerequisites

- Docker installed on your local machine
- Kubernetes cluster set up
- Helm installed on your local machine
- Basic understanding of Docker, Kubernetes, and Helm

## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/subhayukumar/auto-deploy-ml-api.git
   cd auto-deploy-ml-api
   ```

2. **Build the Docker Image:**
   ```bash
   docker build -t your-image-name .
   ```

3. **Push the Docker Image to a Container Registry:**
   ```bash
   docker push your-image-name:your-tag
   ```

4. **Deploy the Helm Chart:**
   ```bash
   helm install myapp-release ./myapp-chart
   ```

5. **Access the API:**
   Once the Helm chart is deployed successfully, you can access the API using the NodePort or LoadBalancer IP address, depending on your setup.

## Using an External Model

If you have a pre-trained machine learning model hosted externally, you can configure the project to use this external model. Follow the steps below to incorporate the external model into the deployment:

- Update the `MODEL_URL` environment variable:
   1. Open the `values.yaml` file in the Helm chart directory.
   2. Modify the `modelUrl` field to include the URL of your externally hosted model.
   3. Redeploy the Helm chart using the `helm upgrade` command.


By following these steps, you can seamlessly integrate an externally hosted machine learning model into the Dockerized deployment using Helm.

## Running the Helm Chart with Custom Values

To run the Helm chart with custom values, you can use the `--set` flag with the `helm install` or `helm upgrade` command. Here's an example of how to deploy the Helm chart with custom values:

```bash
helm install myapp-release ./myapp-chart --set service.port=8000 --set image.repository=your-username/your-image-name --set image.tag=your-tag --set modelUrl=your-model-url
```

Ensure that you replace the placeholders `your-username/your-image-name`, `your-tag`, and `your-model-url` with the URL of your externally hosted model. You can modify other parameters as necessary according to your use case.

You can customize the deployment further by adjusting other parameters available in the `values.yaml` file in the Helm chart directory.

## Project Structure

- `Dockerfile`: Contains the basic structure for the ML model deployment. _[For demo purposes only. Use your own Dockerfile instead.]_
- `api.py`: Includes the code for the API endpoint that serves the machine learning model. _[For demo purposes only. Use your own code instead.]_
- `helm`: Contains the Helm chart for deploying the Dockerized ML model.
    - `values.yaml`: Contains the configuration for the Helm chart.
    - `Chart.yaml`: Contains the metadata for the Helm chart.
    - `templates`: Contains the templates for the Helm chart.
        - `deployment.yaml`: Contains the deployment specification for the Helm chart.
        - `service.yaml`: Contains the service specification for the Helm chart.
        - `_helpers.tpl`: Contains the helper functions for the Helm chart.
