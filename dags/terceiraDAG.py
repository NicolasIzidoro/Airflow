from airflow import DAG 
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

dag = DAG('terceira_dag', description= " terceira dag rodando task 1 e 2 juntas dps a 3 DAG", 
          schedule_interval=None, start_date=datetime(2025,1,8),
          catchup=False)


task1 = BashOperator(task_id="tsk1", bash_command="sleep 5", dag=dag)

task2 = BashOperator(task_id="tsk2", bash_command="sleep 5", dag=dag)

task3 = BashOperator(task_id="tsk3", bash_command="sleep 5", dag=dag)


[task1, task2] >> task3