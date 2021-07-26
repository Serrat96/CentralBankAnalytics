import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import *
import os
os.chdir('/app/centralbankanalytics/04-Webpage')
# Ratio oro/plata
gold_silver_ratio = pd.read_parquet(r'/app/centralbankanalytics/02-Data/03-Gold_vs_silver_ratio/01-Gold_vs_silver_ratio.parquet')
gold_silver_ratio_graph = px.line(gold_silver_ratio, labels={
                     "Date": "Date",
                     "value": "Gold/Silver ratio"},)
gold_silver_ratio_graph.update_layout(title='Gold/Silver ratio since 1791', xaxis_rangeslider_visible=True,
                                      showlegend=False, title_font_size=30, width= 850, height=600)
gold_silver_ratio_graph.update_xaxes(rangeslider_thickness=0.1)


# Gold is the perfect inflation Hedge
inflation_annually = pd.read_parquet(r'/app/centralbankanalytics/02-Data/05-Inflation/01_Inflation_percentage_1913-01-01_2021-06-01_monthly_fred.parquet')
gold_annually = pd.read_parquet(r'/app/centralbankanalytics/02-Data/01-Gold/05-Gold_percentage_1968-04_2021-07_monthly_datahub.parquet')
mask = (inflation_annually.index >= datetime.strptime('1970-01-01', '%Y-%m-%d'))
mask_2 = (gold_annually.index >= datetime.strptime('1970-01-01', '%Y-%m-%d'))
inflation_annually = inflation_annually.loc[mask]
gold_annually = gold_annually.loc[mask_2]
gold_inflation = make_subplots(specs=[[{"secondary_y": True}]])
gold_inflation.add_trace(go.Scatter(x=inflation_annually.index, y=inflation_annually['Value'],
                                    name='CPI<br>annual<br>change<br>(left)'),
                                    secondary_y=False,)
gold_inflation.add_trace(go.Scatter(x=gold_annually.index, y=gold_annually['Value'], name='Gold<br>(right)'),
                         secondary_y=True)
gold_inflation.update_layout(title='CPI annual change vs Gold annual change', xaxis_rangeslider_visible=True,
                                      title_font_size=30, width= 850, height=600)
gold_inflation.update_xaxes(rangeslider_thickness=0.1)
gold_inflation.update_yaxes(title_text="<b>CPI (annual change on monthly spot)</b>", tickformat='%', secondary_y=False)
gold_inflation.update_yaxes(title_text="<b>Gold (annual change on monthly spot)</b>", tickformat='%', secondary_y=True)


# M2 yearly growth vs inflation

inflation_annually_2 = pd.read_parquet(r'/app/centralbankanalytics/02-Data/05-Inflation/01_Inflation_percentage_1913-01-01_2021-06-01_monthly_fred.parquet')
m2_pct = pd.read_parquet(r'..\02-Data\06-M2\01_M2_percentage_1868-12-31-2021-01-01_yearly_fred.parquet')

mask_3 = (m2_pct.index >= datetime.strptime('1913-01-01', '%Y-%m-%d'))
m2_pct = m2_pct.loc[mask_3]

m2_inflation = make_subplots(specs=[[{"secondary_y": True}]])
m2_inflation.add_trace(go.Scatter(x=inflation_annually_2.index, y=inflation_annually_2['Value'], name='Inflation<br>annual<br>change<br>(left)'), secondary_y=False)
m2_inflation.add_trace(go.Scatter(x=m2_pct.index, y=m2_pct['Value'], name='M2<br>annual<br>change<br>(right)'),
                         secondary_y=True)

m2_inflation.update_layout(title='M2 yearly growth vs inflation', xaxis_rangeslider_visible=True,
                                      title_font_size=30, width= 850, height=600)

m2_inflation.update_yaxes(title_text="Inflation annual change", tickformat='%', secondary_y=False)
m2_inflation.update_yaxes(title_text="M2 annual change", tickformat='%', secondary_y=True)

m2_inflation.update_xaxes(rangeslider_thickness=0.1)

#10 year interest rate vs gold

interest_rates_10_year = pd.read_parquet(r'/app/centralbankanalytics/02-Data/07-Interest_rates/05-10YearTreasuryInflationIndexedSecurity_percentage_2003-01-02_2021-07-22_daily_fred.parquet')
gold_ounce = pd.read_parquet(r'..\02-Data\01-Gold\01_Gold_USD-GBP-EUR_1968-01-02_2021-07-22_daily_lbma.parquet')

mask_4 = (gold_ounce.index >= datetime.strptime('2003-01-02', '%Y-%m-%d'))
gold_ounce = gold_ounce.loc[mask_4]

interest_10_years_gold = make_subplots(specs=[[{"secondary_y": True}]])
interest_10_years_gold.add_trace(go.Scatter(x=interest_rates_10_year.index, y=interest_rates_10_year['Value'],
                                            name='10<br>year<br>real<br>interest<br>rates<br>(left)'),
                                            secondary_y=False)

interest_10_years_gold.add_trace(go.Scatter(x=gold_ounce.index, y=gold_ounce['Value'],
                                            name='Gold<br>price<br>per<br>ounce<br>(right)'),
                                            secondary_y=True)

interest_10_years_gold.update_layout(title='10-year USD real interest rates vs gold price', xaxis_rangeslider_visible=True,
                                      title_font_size=30, width=850, height=600)

interest_10_years_gold.update_yaxes(title_text="Real 10-year interest rates for USD", tickformat='%', secondary_y=False)
interest_10_years_gold.update_yaxes(title_text="Gold price (per ounce)", secondary_y=True)

interest_10_years_gold.update_xaxes(rangeslider_thickness=0.1)

# Plata a largo plazo (escala logarítmica)

silver_log = pd.read_parquet(r'/app/centralbankanalytics/02-Data/02-Silver/04_Silver_USD_1791-12-31_2020-12-31_yearly_logarithmic_denvergold.parquet')
silver_log_graph = px.line(silver_log, labels={
                     "Date": "Date",
                     "value": "USD"})
silver_log_graph.update_xaxes(rangeslider_thickness=0.1)
silver_log_graph.update_layout(title='Silver in logarithmic scale', xaxis_rangeslider_visible=True, showlegend=False,
                                      title_font_size=30, width=850, height=600)

# Plata a largo plazo (escala logarítmica ajustada por inflación)

silver_log_inflation = pd.read_parquet(r'/app/centralbankanalytics/02-Data/02-Silver/05-Silver_USD_inflation-adjusted_1791-12-31_2020-12-31_yearly_logarithmic_denvergold.parquet')
silver_log_inflation_graph = px.line(silver_log_inflation, labels={
                     "Date": "Date",
                     "value": "USD"})
silver_log_inflation_graph.update_xaxes(rangeslider_thickness=0.1)
silver_log_inflation_graph.update_layout(title='Silver in logarithmic scale (adjusted by inflation)',
                                         xaxis_rangeslider_visible=True, showlegend=False,
                                         title_font_size=30, width=850, height=600)

#Tipos de interés reales en Europa y EE.UU

real_interest_rates_USA = pd.read_parquet(r'/app/centralbankanalytics/02-Data/08-Real_interest_rates/01-RealInterestRates_percentage_1954-07-01_2021-06-01_monthly_fred.parquet')
real_interest_rates_europe = pd.read_parquet(r'/app/centralbankanalytics/02-Data/11-Real_interest_rates_Europe/01-Real_interest_rates_2003-01-31_2021-05-31_monthly_ecb.parquet')

real_interest_rates_USA_graph = px.line(real_interest_rates_USA, labels={
                     "index": "Date",
                     "value": "Percentage"},)
real_interest_rates_USA_graph.update_xaxes(rangeslider_thickness=0.1)
real_interest_rates_USA_graph.update_layout(title='Real interest rates in USA', xaxis_rangeslider_visible=True,
                                      showlegend=False, title_font_size=30, width= 850, height=600)

real_interest_rates_europe_graph = px.line(real_interest_rates_europe, labels={
                     "Date": "Date",
                     "value": "Percentage"},)
real_interest_rates_europe_graph.update_xaxes(rangeslider_thickness=0.1)
real_interest_rates_europe_graph.update_layout(title='Real interest rates in Europe', xaxis_rangeslider_visible=True,
                                      showlegend=False, title_font_size=30, width= 850, height=600)


