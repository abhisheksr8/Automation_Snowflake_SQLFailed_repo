from staging_abhisheks_e2etests_automation_snowflake_sqlfailed_sql_automation_snowflake_sqlfailed_i_am_a_failure_buddy_job.utils import *

def Model_0():
    from airflow.operators.python import PythonOperator
    from datetime import timedelta
    import os
    import zipfile
    import tempfile

    return PythonOperator(
        task_id = "Model_0",
        python_callable = invoke_dbt_runner,
        op_kwargs = {
          "is_adhoc_run_from_same_project": False,
          "is_prophecy_managed": False,
          "run_deps": False,
          "run_seeds": True,
          "run_parents": False,
          "run_children": False,
          "run_tests": True,
          "run_mode": "project",
          "entity_kind": None,
          "entity_name": None,
          "project_id": "21444",
          "git_entity": "branch",
          "git_entity_value": "testBranch",
          "git_ssh_url": "https://github.com/abhisheksr8/Automation_Snowflake_SQLFailed_repo.git",
          "git_sub_path": "",
          "select": "",
          "threads": "",
          "exclude": "",
          "run_props": " --profile run_profile_snowflake",
          "envs": {
            "DBT_DATABRICKS_INVOCATION_ENV": "prophecy", 
            "DBT_PROFILES_DIR": "/usr/local/airflow/dags", 
            "DBT_SEND_ANONYMOUS_USAGE_STATS": "false", 
            "DBT_FULL_REFRESH": "true"
          }
        },
        retries = 1, 
        max_retry_delay = timedelta(minutes = 1.0)
    )
