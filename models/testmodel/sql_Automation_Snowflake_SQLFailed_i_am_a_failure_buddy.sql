WITH qa_failure_seed AS (

  SELECT * 
  
  FROM {{ ref('qa_failure_seed')}}

),

qa_failures AS (

  SELECT *
  
  FROM qa_failure_seed

),

qa_failures_select AS (

  {#Selects specific fields from quality assurance failure records for review.#}
  SELECT 
    a AS a,
    b AS b
  
  FROM qa_failures AS in0

)

SELECT *

FROM qa_failures_select
