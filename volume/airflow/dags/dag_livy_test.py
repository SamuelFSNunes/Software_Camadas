from datetime import datetime
from airflow import DAG
from airflow.providers.apache.livy.operators.livy import LivyOperator

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2022, 1, 1),
}

dag = DAG(
    'livy_operator_example',
    default_args=default_args,
    schedule_interval='@once',
    catchup=False,
)

livy_task = LivyOperator(
    task_id='run_livy_job',
    dag=dag,
    livy_conn_id='livy_spark_conn',
    file='s3a://airflow/dags/livy.py',
    executor_cores=1,
    num_executors=1,
)

livy_task
