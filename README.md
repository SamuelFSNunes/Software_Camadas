# Big Data Sandbox
For Portuguese version, click [here](README-pt-br.md)

This project aims to provide a sandbox environment for big data testing. It consists of a Docker environment with several containers containing:

```mermaid
classDiagram
    class Zeppelin {
        Porta: 8080
    }
    class HiveServer {
        Porta: 10000
        Porta: 10002
    }
    class Metastore {   
        Porta: 9083
    }
    class LivySpark {
        Porta: 8998
        Porta: 18080
        
    }
    class PostgreSQL {
        Porta: 5432
    }
    class MinIO {
        Porta: 9000
        Porta: 9001
    }

    Zeppelin <--> LivySpark
    LivySpark <--> Metastore: 
    LivySpark <--> MinIO: 
    MinIO <--> HiveServer: 
    Metastore <--> PostgreSQL: 
    Metastore <--> HiveServer: 
```  

### In this diagram:

- **Zeppelin (Zeppelin)**: Zeppelin is an interactive notebook tool for data analysis, similar to Jupyter Notebook. It supports multiple programming languages such as Scala, Python, SQL, and R, allowing the creation of graphs, tables, and interactive visualizations directly in the notebook.

- **Livy-Spark (Livy-Spark)**: Livy is a server for interacting with Apache Spark clusters remotely. It allows users to submit Spark tasks (such as large-scale data processing) via a REST API, facilitating the execution of Spark jobs in distributed environments.

- **Metastore (Metastore)**: Metastore is part of the Apache Hive ecosystem, used to store metadata for Hive tables. It manages information such as table schemas, data locations, and other important properties for Hive queries and operations.

- **HiveServer (HiveServer)**: HiveServer is a server that provides JDBC and Thrift interfaces for SQL queries in a Hive cluster. It allows external applications, such as Business Intelligence tools and other programs, to connect to Hive and execute SQL queries for data analysis stored in Hadoop.

- **PostgreSQL (PostgreSQL)**: PostgreSQL is an open-source relational database management system (RDBMS). It is known for its reliability, advanced SQL features, ACID transaction support, and extensibility, widely used in applications requiring a robust and scalable database.

- **MinIO (MinIO)**: MinIO is an open-source object storage server compatible with Amazon S3 (Simple Storage Service). It is designed to be scalable, high-performance, and suitable for cloud storage workloads, enabling efficient storage and retrieval of large amounts of unstructured data.

These containers are configured to communicate with each other, allowing for big data processing tasks.

### Access the port links
 Access the services at the following links:
- Zeppelin: 
    - [8080](http://localhost:8080): user interface
- Livy-Spark: 
    - [18080](http://localhost:18080): History Server user interface
    - [8998](http://localhost:8998): Livy Server user interface
- MinIO: 
    - 9000: MinIO 
    - [9001](http://localhost:9001): user interface
- Metastore:
    - 9083: Metastore
- HiveServer:
     - [10002](http://localhost:10002): user interface
     - 10000: HiveServer
- Postgre:
    - 5432: PostgreSQL

## Summary

- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Developers](#developers)

## Requirements

Before installing and running this project, ensure that your system meets the following requirements:

- Docker installed and properly configured.
- Sufficient disk space for containers and generated data.
- Internet connection to download Docker images and dependencies during the initial setup.

## Installation

Follow the steps below to install the project:

1. Clone this repository to your local environment.

```bash 
git clone https://github.com/SamuelFSNunes/Software_Camadas.git
```

2. Run the Docker initialization command.

```bash
docker compose up --build
```

## Setup

- Access MinIO through the link (http://localhost:9001).  
- Log in using the following credentials:  
  - **Username**: `minioadmin`  
  - **Password**: `minioadmin`  
- Go to the **Bucket** tab and click on `Create Bucket`.  
- In the **Bucket Name** field, type `warehouse` and select `Create Bucket`.  

## Configuration

After installation, the environment will be automatically configured. You can access the following services:

- MinIO: [http://localhost:9001](http://localhost:9000)
- Zeppelin: [http://localhost:8080](http://localhost:8080)

## Troubleshooting

If the services are not functioning as expected, follow these troubleshooting steps:

1. Ensure that Docker is running.
2. Check the container logs for error messages.
3. Restart the containers using the `docker compose restart` command.

## Developers

This project is maintained by:

- Erick M. Cassoli - [GitHub](https://github.com/ErickCassoli)
- Vinicius Antunes - [GitHub](https://github.com/viniciusantunes26)
- Rafael Mattos - [GitHub](https://github.com/RafaMattss)
