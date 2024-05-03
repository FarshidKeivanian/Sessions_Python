#pip install pandasql
import pandas as pd
from pandasql import sqldf

pysql = lambda q: sqldf(q, globals())

df = pd.DataFrame({
    "Name": ["John Doe", "Jane Doe"],
    "Age": [30, 25]
})


query = """
SELECT *
FROM df
WHERE Age > 25
"""

result_df = pysql(query)

print(result_df)
