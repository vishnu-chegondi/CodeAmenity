### Amazon ECS

-------

Amazon Elastic Container Service(ECS) is a container management service provider for running,stopping and managing docker containers on a cluster. You can host your cluster on a **serverless** infrastructure that is managed by ECS

#### Launching containerised Applications

Your application containers can be launched in two ways:

- Fargate Launch Type
- Amazon Ec2 Launch Type

##### Fargate Launch Type

In this you define the tasks and services, Fargate launches the containers for you. No need of any backend infrastructure.

##### Amazon Ec2 Launch Type

In this you build the infrastructure needed for the docker deployement is maintained by deploying the EC2 Cluster
