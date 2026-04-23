WITH qa_failure_seed AS (

  SELECT * 
  
  FROM {{ ref('qa_failure_seed')}}

),

qa_failure_records AS (

  {#Lists all quality assurance failure records for review.#}
  SELECT *
  
  FROM qa_failure_seed

),

qa_failure_fields AS (

  {#Selects key details from quality assurance failure records for review.#}
  SELECT 
    a AS a,
    b AS b
  
  FROM qa_failure_records AS in0

)

SELECT *

FROM qa_failure_fields
