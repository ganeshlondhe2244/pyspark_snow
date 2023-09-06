from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
import re
spark=SparkSession.builder.master('local[*]').appName('test').getOrCreate()

#Reading another json data which consists comples datatypes.

data1= "C:\Bigdata\driverscopy\world_bank.json"
df=spark.read.format('json').option('mode','dropmalformed').load(data1)
#df.printSchema()







