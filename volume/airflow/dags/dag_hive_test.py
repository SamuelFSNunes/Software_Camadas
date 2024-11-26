from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.apache.hive.operators.hive import HiveOperator

# Define os argumentos padrão para a DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 4, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define o nome da DAG
dag = DAG(
    'hive_test_dag',
    default_args=default_args,
    description='A DAG to test Apache Hive connection in Airflow',
    schedule_interval=timedelta(days=1),  # Executa diariamente
)

# Define a tarefa que executa uma consulta no Hive
hive_query_task = HiveOperator(
    task_id='hive_query_task',
    hql='SELECT * FROM spark_airflow LIMIT 10;',  # Sua consulta Hive aqui
    hive_cli_conn_id='hive_server2_conn',  # Nome da conexão Hive configurada no Airflow
    dag=dag,
)

# Define as dependências da DAG
hive_query_task
