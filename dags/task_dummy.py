from airflow import DAG 
from airflow.operators.bash_operator import BashOperator
from datetime import datetime
from airflow.operators.dummy_operator import DummyOperator

dag = DAG('Dummy', description= "exemple Dummy", 
          schedule_interval=None, start_date=datetime(2025,1,8),
          catchup=False)



task1 = BashOperator(task_id="tsk1", bash_command="sleep 1", dag=dag)
task2 = BashOperator(task_id="tsk2", bash_command="sleep 1", dag=dag)
task3 = BashOperator(task_id="tsk3", bash_command="sleep 1", dag=dag)
task4 = BashOperator(task_id="tsk4", bash_command="sleep 1", dag=dag)
task5 = BashOperator(task_id="tsk5", bash_command="sleep 1", dag=dag)
taskDummy = DummyOperator(task_id="taskDummy", dag=dag) 

[task1 , task2, task3] >> taskDummy >> [task4, task5]