import os
from datetime import datetime

from cosmos.profiles import SnowflakeUserPasswordProfileMapping

from cosmos.airflow.dag import DbtDag
from cosmos.config import ProjectConfig, ProfileConfig, ExecutionConfig

profile_config = ProfileConfig(
    profile_name="default",
    target_name="dev",
    profile_mapping=SnowflakeUserPasswordProfileMapping(
        conn_id="snowflake_conn",
        profile_args={"database": "dbt_db", "schema": "dbt_schema"},
    )
)

dbt_snowflake_dag = DbtDag(
    project_config=ProjectConfig("/home/bluetab/Desarrollo/personal-projects/tpch-etl"),
    operator_args={"install_deps": True},
    profile_config=profile_config,
    execution_config=ExecutionConfig(dbt_executable_path=f"{os.environ['AIRFLOW_DBT']}"),
    schedule_interval="@daily",
    start_date=datetime(2024,4,18),
    catchup=False,
    dag_id="dbt_dag"
)