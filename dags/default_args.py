from airflow import DAG 
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'depends_on_past': False,
    'start_date': datetime(2025,2,6),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=10),
}


dag = DAG('default_args', description= "args example", 
          default_args=default_args,
          schedule_interval='@hourly', start_date=datetime(2025,2,6),
          catchup=False, default_view='graph', tags=['processo','tags','pipeline'])


task1 = BashOperator(task_id="tsk1", bash_command="sleep 5", dag=dag, retries=3 )

task2 = BashOperator(task_id="tsk2", bash_command="sleep 5", dag=dag)

task3 = BashOperator(task_id="tsk3", bash_command="sleep 5", dag=dag)

task4 = BashOperator(task_id="tsk4", bash_command="sleep 5", dag=dag)


task1 >> task2 >> task3 >> task4
