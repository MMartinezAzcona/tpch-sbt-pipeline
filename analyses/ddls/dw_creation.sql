USE ROLE ACCOUNTADMIN;

CREATE WAREHOUSE dbt_wh WITH warehouse_size='x-small';
CREATE DATABASE dbt_db;
CREATE ROLE dbt_role;

GRANT usage ON WAREHOUSE dbt_wh TO ROLE dbt_role;
GRANT ROLE dbt_role TO USER MMARTINEZAZCONA;
GRANT ALL ON DATABASE dbt_db TO ROLE dbt_role;

CREATE SCHEMA dbt_db.dbt_schema;