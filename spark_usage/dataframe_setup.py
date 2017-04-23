from pyspark import SparkContext
import numpy as np
import datetime
import numpy as np
import sklearn
import scipy
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql import SQLContext
sc = SparkContext.getOrCreate()

# DEFINE SCHEMAS
schema_fin_suite = StructType([
  StructField("gvkey",StringType(),True)
, StructField("adate",StringType(),True)
, StructField("qdate",StringType(),True)
, StructField("public_date",StringType(),True)
, StructField("CAPEI",DoubleType(),True)
, StructField("bm",DoubleType(),True)
, StructField("evm",DoubleType(),True)
, StructField("pe_op_basic",DoubleType(),True)
, StructField("pe_op_dil",DoubleType(),True)
, StructField("pe_exi",DoubleType(),True)
, StructField("pe_inc",DoubleType(),True)
, StructField("ps",DoubleType(),True)
, StructField("pcf",DoubleType(),True)
, StructField("dpr",DoubleType(),True)
, StructField("npm",DoubleType(),True)
, StructField("opmbd",DoubleType(),True)
, StructField("opmad",DoubleType(),True)
, StructField("gpm",DoubleType(),True)
, StructField("ptpm",DoubleType(),True)
, StructField("cfm",DoubleType(),True)
, StructField("roa",DoubleType(),True)
, StructField("roe",DoubleType(),True)
, StructField("roce",DoubleType(),True)
, StructField("efftax",DoubleType(),True)
, StructField("aftret_eq",DoubleType(),True)
, StructField("aftret_invcapx",DoubleType(),True)
, StructField("aftret_equity",DoubleType(),True)
, StructField("pretret_noa",DoubleType(),True)
, StructField("pretret_earnat",DoubleType(),True)
, StructField("GProf",DoubleType(),True)
, StructField("equity_invcap",DoubleType(),True)
, StructField("debt_invcap",DoubleType(),True)
, StructField("totdebt_invcap",DoubleType(),True)
, StructField("capital_ratio",DoubleType(),True)
, StructField("int_debt",DoubleType(),True)
, StructField("int_totdebt",DoubleType(),True)
, StructField("cash_lt",DoubleType(),True)
, StructField("invt_act",DoubleType(),True)
, StructField("rect_act",DoubleType(),True)
, StructField("debt_at",DoubleType(),True)
, StructField("debt_ebitda",DoubleType(),True)
, StructField("short_debt",DoubleType(),True)
, StructField("curr_debt",DoubleType(),True)
, StructField("lt_debt",DoubleType(),True)
, StructField("profit_lct",DoubleType(),True)
, StructField("ocf_lct",DoubleType(),True)
, StructField("cash_debt",DoubleType(),True)
, StructField("fcf_ocf",DoubleType(),True)
, StructField("lt_ppent",DoubleType(),True)
, StructField("dltt_be",DoubleType(),True)
, StructField("debt_assets",DoubleType(),True)
, StructField("debt_capital",DoubleType(),True)
, StructField("de_ratio",DoubleType(),True)
, StructField("intcov",DoubleType(),True)
, StructField("intcov_ratio",DoubleType(),True)
, StructField("cash_ratio",DoubleType(),True)
, StructField("quick_ratio",DoubleType(),True)
, StructField("curr_ratio",DoubleType(),True)
, StructField("cash_conversion",DoubleType(),True)
, StructField("inv_turn",DoubleType(),True)
, StructField("at_turn",DoubleType(),True)
, StructField("rect_turn",DoubleType(),True)
, StructField("pay_turn",DoubleType(),True)
, StructField("sale_invcap",DoubleType(),True)
, StructField("sale_equity",DoubleType(),True)
, StructField("sale_nwc",DoubleType(),True)
, StructField("rd_sale",DoubleType(),True)
, StructField("adv_sale",DoubleType(),True)
, StructField("staff_sale",DoubleType(),True)
, StructField("accrual",DoubleType(),True)
, StructField("ptb",DoubleType(),True)
, StructField("PEG_trailing",DoubleType(),True)
, StructField("DIVYIELD",DoubleType(),True)
, StructField("PEG_1yrforward",StringType(),True)
, StructField("PEG_ltgforward",StringType(),True)
])


schema_CRSP_comp = StructType([
  StructField("GVKEY",StringType(),True)
, StructField("iid",IntegerType(),True)
, StructField("datadate",StringType(),True)
, StructField("ajexm",DoubleType(),True)
, StructField("dvpspm",DoubleType(),True)
, StructField("dvpsxm",DoubleType(),True)
, StructField("dvrate",DoubleType(),True)
, StructField("prccm",DoubleType(),True)
, StructField("trfm",DoubleType(),True)
, StructField("sic",IntegerType(),True)
, StructField("spcsrc",StringType(),True)
])

schema_link_table = StructType([
  StructField("GVKEY",StringType(),True)
, StructField("conm",StringType(),True)
, StructField("tic",StringType(),True)
, StructField("cusip",StringType(),True)
, StructField("cik",StringType(),True)
, StructField("sic",StringType(),True)
, StructField("LINKPRIM",StringType(),True)
, StructField("LIID",StringType(),True)
, StructField("LINKTYPE",StringType(),True)
, StructField("LPERMNO",StringType(),True)
, StructField("LPERMCO",StringType(),True)
, StructField("LINKDT",StringType(),True)
, StructField("LINKENDDT",StringType(),True)
, StructField("CONML",StringType(),True)
, StructField("BUSDESC",StringType(),True)
, StructField("ipodate",StringType(),True)
, StructField("dldte",StringType(),True)
, StructField("STKO",StringType(),True)
, StructField("GSECTOR",StringType(),True)
, StructField("GGROUP",StringType(),True)
, StructField("GIND",StringType(),True)
, StructField("GSUBIND",StringType(),True)
, StructField("SPCINDCD",StringType(),True)
, StructField("SPCSECCD",StringType(),True)
])


schema_beta_suite = StructType([
StructField("PERMNO",StringType(),True)
, StructField("DATE",StringType(),True)
, StructField("n",IntegerType(),True)
, StructField("RET",StringType(),True)
, StructField("alpha",FloatType(),True)
, StructField("b_mkt",FloatType(),True)
, StructField("b_smb",FloatType(),True)
, StructField("b_hml",FloatType(),True)
, StructField("b_umd",FloatType(),True)
, StructField("ivol",StringType(),True)
, StructField("tvol",StringType(),True)
, StructField("R2",StringType(),True)
, StructField("exret",StringType(),True)
])


schema_recs = StructType([
  StructField("TICKER",StringType(),True)
, StructField("CUSIP",StringType(),True)
, StructField("OFTIC",StringType(),True)
, StructField("CNAME",StringType(),True)
, StructField("STATPERS",StringType(),True)
, StructField("MEANREC",FloatType(),True)
, StructField("MEDREC",FloatType(),True)
, StructField("STDEV",FloatType(),True)
, StructField("NUMREC",FloatType(),True)
, StructField("NUMUP",FloatType(),True)
, StructField("NUMDOWN",FloatType(),True)
, StructField("BUYPCT",FloatType(),True)
, StructField("SELLPCT",FloatType(),True)
, StructField("HOLDPCT",FloatType(),True)
, StructField("USFIRM",IntegerType(),True)
])

# SET PATHS TO FILES
sparkcsv = "com.databricks.spark.csv"
financial_suite_path = "hdfs:///user/w205/financial_data/financial_suite/financial_ratios.csv"
crsp_path = "hdfs:///user/w205/financial_data/crsp_compustat/crsp_compustat_small.csv"
link_path = "hdfs:///user/w205/financial_data/linking_table/link_table_small.csv"
beta_path = "hdfs:///user/w205/financial_data/beta_suite/beta_suite.csv"
recs_path = "hdfs:///user/w205/financial_data/recommendations/recommendations.csv"

# READ IN FILES
financial_suite = sqlContext.read.format(sparkcsv).options(header='true').load(financial_suite_path, schema=schema_fin_suite)
crsp = sqlContext.read.format(sparkcsv).options(header='true').load(crsp_path, schema=schema_CRSP_comp)
link = sqlContext.read.format(sparkcsv).options(header='true').load(link_path, schema=schema_link_table)
beta = sqlContext.read.format(sparkcsv).options(header='true').load(beta_path, schema=schema_beta_suite)
recs = sqlContext.read.format(sparkcsv).options(header='true').load(recs_path, schema=schema_recs)

# EXPORT TO PARQUET
financial_suite.write.parquet("hdfs:///user/w205/financial_data/parquet_files/fin_suite")
crsp.write.parquet("hdfs:///user/w205/financial_data/parquet_files/crsp")
link.write.parquet("hdfs:///user/w205/financial_data/parquet_files/link_table")
beta.write.parquet("hdfs:///user/w205/financial_data/parquet_files/beta")
recs.write.parquet("hdfs:///user/w205/financial_data/parquet_files/recs")
