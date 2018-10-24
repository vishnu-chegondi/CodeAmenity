#### Amazon ECS

-------

Amazon Elastic Container Service(ECS) is a container management service provider for running,stopping and managing docker containers on a cluster. You can host your cluster on a **serverless** infrastructure that is managed by ECS

##### Launching containerised Applications

Your application containers can be launched in two ways:

- Fargate Launch Type
- Amazon Ec2 Launch Type

###### Fargate Launch Type

In this you define the tasks and services, Fargate launches the containers for you. No need of any backend infrastructure.
Clusters are completely maintained by the fargate. You need to just specify the services and task needed for your application.

###### Amazon Ec2 Launch Type

In this you build the infrastructure needed for the docker deployement is maintained by deploying the EC2 Cluster.This provides you the more control over your cluster.

###### Task Definition

Task definition is a text file containing the data in json format. This specifies the various parameters which are used in launching the containers of your applications. The parameter you define depends on the launch type.

> Your entire application does not need to be or must not be in single task definition. 

Your application can span multiple task definitions by combining related containers into their own task definitions, each representing single component

You should put multiple containers in the same task definition if:

- Containers share a common lifecycle (that is, they should be launched and terminated together).
- Containers are required to be run on the same underlying host (that is, one container references the other on a localhost port).
- You want your containers to share resources.
- Your containers share data volumes.

Otherwise, you should define your containers in separate tasks definitions so that you can scale, provision, and deprovision them separately.
