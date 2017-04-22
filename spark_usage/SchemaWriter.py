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
, StructField("LINKPRIM",StringType(),True)
, StructField("LIID",IntegerType(),True)
, StructField("LINKTYPE",StringType(),True)
, StructField("LPERMNO",IntegerType(),True)
, StructField("LPERMCO",IntegerType(),True)
, StructField("LINKDT",StringType(),True)
, StructField("LINKENDDT",StringType(),True)
, StructField("iid",IntegerType(),True)
, StructField("datadate",StringType(),True)
, StructField("tic",StringType(),True)
, StructField("cusip",IntegerType(),True)
, StructField("conm",StringType(),True)
, StructField("ajexm",DoubleType(),True)
, StructField("ajpm",DoubleType(),True)
, StructField("isalrt",StringType(),True)
, StructField("primiss",StringType(),True)
, StructField("spgim",StringType(),True)
, StructField("spiim",StringType(),True)
, StructField("spmim",StringType(),True)
, StructField("cheqvm",StringType(),True)
, StructField("curcddvm",StringType(),True)
, StructField("dvpspm",StringType(),True)
, StructField("dvpsxm",StringType(),True)
, StructField("dvrate",StringType(),True)
, StructField("csfsm",StringType(),True)
, StructField("cshtrm",DoubleType(),True)
, StructField("curcdm",StringType(),True)
, StructField("navm",StringType(),True)
, StructField("prccm",DoubleType(),True)
, StructField("prchm",DoubleType(),True)
, StructField("prclm",DoubleType(),True)
, StructField("trfm",DoubleType(),True)
, StructField("trt1m",DoubleType(),True)
, StructField("rawpm",StringType(),True)
, StructField("rawxm",StringType(),True)
, StructField("sph100",StringType(),True)
, StructField("sphcusip",StringType(),True)
, StructField("sphiid",StringType(),True)
, StructField("sphmid",StringType(),True)
, StructField("sphname",StringType(),True)
, StructField("sphsec",StringType(),True)
, StructField("sphtic",StringType(),True)
, StructField("sphvg",StringType(),True)
, StructField("cshoq",StringType(),True)
, StructField("exchg",IntegerType(),True)
, StructField("secstat",StringType(),True)
, StructField("cik",StringType(),True)
, StructField("fic",StringType(),True)
, StructField("add1",StringType(),True)
, StructField("add2",StringType(),True)
, StructField("add3",StringType(),True)
, StructField("add4",StringType(),True)
, StructField("addzip",StringType(),True)
, StructField("busdesc",StringType(),True)
, StructField("city",StringType(),True)
, StructField("conml",StringType(),True)
, StructField("costat",StringType(),True)
, StructField("county",StringType(),True)
, StructField("dlrsn",IntegerType(),True)
, StructField("ein",StringType(),True)
, StructField("fax",StringType(),True)
, StructField("fyrc",IntegerType(),True)
, StructField("ggroup",StringType(),True)
, StructField("gind",StringType(),True)
, StructField("gsector",StringType(),True)
, StructField("gsubind",StringType(),True)
, StructField("idbflag",StringType(),True)
, StructField("incorp",StringType(),True)
, StructField("loc",StringType(),True)
, StructField("naics",StringType(),True)
, StructField("phone",StringType(),True)
, StructField("prican",StringType(),True)
, StructField("prirow",StringType(),True)
, StructField("priusa",IntegerType(),True)
, StructField("sic",IntegerType(),True)
, StructField("spcindcd",IntegerType(),True)
, StructField("spcseccd",IntegerType(),True)
, StructField("spcsrc",StringType(),True)
, StructField("state",StringType(),True)
, StructField("stko",IntegerType(),True)
, StructField("weburl",StringType(),True)
, StructField("dldte",StringType(),True)
, StructField("ipodate",StringType(),True)
])


schema_link_table = StructType([
  StructField("GVKEY",StringType(),True)
, StructField("LINKPRIM",StringType(),True)
, StructField("LIID",StringType(),True)
, StructField("LINKTYPE",StringType(),True)
, StructField("LPERMNO",StringType(),True)
, StructField("LPERMCO",StringType(),True)
, StructField("LINKDT",StringType(),True)
, StructField("LINKENDDT",StringType(),True)
, StructField("conm",StringType(),True)
, StructField("tic",StringType(),True)
, StructField("cusip",StringType(),True)
, StructField("cik",StringType(),True)
, StructField("sic",StringType(),True)
, StructField("naics",StringType(),True)
, StructField("EIN",StringType(),True)
, StructField("COSTAT",StringType(),True)
, StructField("DLRSN",StringType(),True)
, StructField("PRIUSA",StringType(),True)
, StructField("PRICAN",StringType(),True)
, StructField("PRIROW",StringType(),True)
, StructField("IDBFLAG",StringType(),True)
, StructField("FIC",StringType(),True)
, StructField("LOC",StringType(),True)
, StructField("INCORP",StringType(),True)
, StructField("STATE",StringType(),True)
, StructField("COUNTY",StringType(),True)
, StructField("CITY",StringType(),True)
, StructField("CONML",StringType(),True)
, StructField("WEBURL",StringType(),True)
, StructField("PHONE",StringType(),True)
, StructField("FAX",StringType(),True)
, StructField("ADD1",StringType(),True)
, StructField("ADD2",StringType(),True)
, StructField("ADD3",StringType(),True)
, StructField("ADD4",StringType(),True)
, StructField("ADDZIP",StringType(),True)
, StructField("BUSDESC",StringType(),True)
, StructField("ipodate",StringType(),True)
, StructField("dldte",StringType(),True)
, StructField("STKO",StringType(),True)
, StructField("FYRC",StringType(),True)
, StructField("GSECTOR",StringType(),True)
, StructField("GGROUP",StringType(),True)
, StructField("GIND",StringType(),True)
, StructField("GSUBIND",StringType(),True)
, StructField("SPCINDCD",StringType(),True)
, StructField("SPCSECCD",StringType(),True)
])


schema_beta_suite = StructType([
  StructField("gvkey",StringType(),True)
, StructField("adate",StringType(),True)
, StructField("qdate",StringType(),True)
, StructField("public_date",StringType(),True)
, StructField("CAPEI",FloatType(),True)
, StructField("bm",FloatType(),True)
, StructField("evm",FloatType(),True)
, StructField("pe_op_basic",StringType(),True)
, StructField("pe_op_dil",StringType(),True)
, StructField("pe_exi",FloatType(),True)
, StructField("pe_inc",FloatType(),True)
, StructField("ps",FloatType(),True)
, StructField("pcf",FloatType(),True)
, StructField("dpr",FloatType(),True)
, StructField("npm",FloatType(),True)
, StructField("opmbd",FloatType(),True)
, StructField("opmad",FloatType(),True)
, StructField("gpm",FloatType(),True)
, StructField("ptpm",FloatType(),True)
, StructField("cfm",FloatType(),True)
, StructField("roa",FloatType(),True)
, StructField("roe",FloatType(),True)
, StructField("roce",FloatType(),True)
, StructField("efftax",FloatType(),True)
, StructField("aftret_eq",FloatType(),True)
, StructField("aftret_invcapx",FloatType(),True)
, StructField("aftret_equity",FloatType(),True)
, StructField("pretret_noa",FloatType(),True)
, StructField("pretret_earnat",FloatType(),True)
, StructField("GProf",FloatType(),True)
, StructField("equity_invcap",FloatType(),True)
, StructField("debt_invcap",FloatType(),True)
, StructField("totdebt_invcap",FloatType(),True)
, StructField("capital_ratio",FloatType(),True)
, StructField("int_debt",FloatType(),True)
, StructField("int_totdebt",FloatType(),True)
, StructField("cash_lt",FloatType(),True)
, StructField("invt_act",FloatType(),True)
, StructField("rect_act",FloatType(),True)
, StructField("debt_at",FloatType(),True)
, StructField("debt_ebitda",FloatType(),True)
, StructField("short_debt",FloatType(),True)
, StructField("curr_debt",FloatType(),True)
, StructField("lt_debt",FloatType(),True)
, StructField("profit_lct",FloatType(),True)
, StructField("ocf_lct",FloatType(),True)
, StructField("cash_debt",FloatType(),True)
, StructField("fcf_ocf",FloatType(),True)
, StructField("lt_ppent",FloatType(),True)
, StructField("dltt_be",FloatType(),True)
, StructField("debt_assets",FloatType(),True)
, StructField("debt_capital",FloatType(),True)
, StructField("de_ratio",FloatType(),True)
, StructField("intcov",FloatType(),True)
, StructField("intcov_ratio",FloatType(),True)
, StructField("cash_ratio",FloatType(),True)
, StructField("quick_ratio",FloatType(),True)
, StructField("curr_ratio",FloatType(),True)
, StructField("cash_conversion",FloatType(),True)
, StructField("inv_turn",FloatType(),True)
, StructField("at_turn",FloatType(),True)
, StructField("rect_turn",FloatType(),True)
, StructField("pay_turn",FloatType(),True)
, StructField("sale_invcap",FloatType(),True)
, StructField("sale_equity",FloatType(),True)
, StructField("sale_nwc",FloatType(),True)
, StructField("rd_sale",FloatType(),True)
, StructField("adv_sale",FloatType(),True)
, StructField("staff_sale",FloatType(),True)
, StructField("accrual",FloatType(),True)
, StructField("ptb",FloatType(),True)
, StructField("PEG_trailing",StringType(),True)
, StructField("DIVYIELD",StringType(),True)
, StructField("PEG_1yrforward",StringType(),True)
, StructField("PEG_ltgforward",StringType(),True)
])


schema_recs = StructType([
  StructField("TICKER",StringType(),True)
, StructField("CUSIP",StringType(),True)
, StructField("OFTIC",StringType(),True)
, StructField("CNAME",StringType(),True)
, StructField("STATPERS",StringType(),True)
, StructField("MEANREC",IntegerType(),True)
, StructField("MEDREC",IntegerType(),True)
, StructField("STDEV",FloatType(),True)
, StructField("NUMREC",IntegerType(),True)
, StructField("NUMUP",IntegerType(),True)
, StructField("NUMDOWN",IntegerType(),True)
, StructField("BUYPCT",IntegerType(),True)
, StructField("SELLPCT",IntegerType(),True)
, StructField("HOLDPCT",IntegerType(),True)
, StructField("USFIRM",IntegerType(),True)
])
