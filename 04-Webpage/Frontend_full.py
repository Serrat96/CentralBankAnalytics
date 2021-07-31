import os
import streamlit as st
try:
    os.chdir(r'C:\Users\serra\REPOSITORIOS\CentralBankAnalytics\04-Webpage')
except:
    pass
import silver_analysis as sa

st.set_page_config(page_title='Central Bank Analytics', page_icon='euro')

def main():
    language = st.sidebar.radio('Language:', ('EN', 'ES'))
    if language == 'EN':
        menu = st.sidebar.radio('Select:', ('Is it worth it to buy gold or silver?', 'How the actual bearish trend can revert?'))
    if language == 'ES':
        menu = st.sidebar.radio('Selección:', ('¿Vale la pena comprar plata y/o oro?', '¿Cómo puede revertir la tendencia alcista actual?'))


    if menu == 'Is it worth it to buy gold or silver?' and language == 'EN':
        st.markdown('# Is it worth it to buy silver or gold?')
        st.markdown('## **1- Historical relationship between gold and silver**')
        st.write('Gold and silver have had a close relationship for a long time.\n\n'
                 'In the following graph it can be seen that since 1791 the two assets maintain one'
                 'close relationship for a long time. Having areas of soil where it is preferable '
                 'having gold to having silver and roof areas where it is preferable to have silver to having'
                 'gold.')
        st.plotly_chart(sa.gold_silver_ratio_graph)
        st.markdown('## **2- Relationship between inflation and gold**')
        st.write('These two assets are characterized because they are the best alternative in times of inflation.\n\n'
                 "It can be seen that since 1970, gold tends to rise when inflationary pressures occur.")
        st.plotly_chart(sa.gold_inflation)
        st.markdown('## **3- Relationship between inflation and M2**')
        st.write('As can be seen in the following graph, the unprecedented increase that is'
                 'occurring with respect to the amount of M2 (in USD), currently 25%,'
                 'indicates that inflation is closely linked to M2, which tells us'
                 'the beginning at this time of strong inflationary pressures.')
        st.plotly_chart(sa.m2_inflation)
        st.markdown('## **4- Relationship between real interest rates, gold and silver **')
        st.write('This explained above serves to put us in context of what the situation is'
                 'current and whether it can benefit gold and silver or not. Notwithstanding the gold and the'
                 'Silver is really driven by real interest rates.')
        st.markdown('### **What are real interest rates?**')
        st.write('Real interest rate = Nominal interest rate - Inflation.\n\n'
                 'The nominal interest rate represents the official rate set by central banks'
                 'to grant credits.'
                 'As can be seen in the graph above, inflationary pressures are already beginning'
                 'to appear strongly and investors are counting on them. If central bank'
                 'they continue with the policy of keeping rates close to 0% the real interest rate'
                 'it will fall more and more.'
                 'It can be seen in the following two graphs how these rates are found'
                 'currently declining due to expansion policies by the'
                 'American and European central banks.')
        st.plotly_chart(sa.real_interest_rates_USA_graph)
        st.plotly_chart(sa.real_interest_rates_europe_graph)
        st.write('In the following graph we can see how the relationship between gold and'
                 'interest rates are inverse, which indicates that gold is an asset capable of'
                 'protect its owner against the loss of value of FIAT currencies, plus'
                 'known as inflation.')
        st.plotly_chart(sa.interest_10_years_gold)
        st.write('Also, if we look at the logarithmic scale, silver has a trend'
                 'Very clear long-term bullish, trading far from all-time highs.')
        st.plotly_chart(sa.silver_log_graph)
        st.write('Finally, if we adjust silver for inflation we see that it really is not'
                 'expensive and right now may be a good time to buy.')
        st.plotly_chart(sa.silver_log_inflation_graph)
        st.markdown('## Sources')
        st.write(
            'Gold/silver ratio since 1791: [Gold price](https://www.denvergold.org/precious-metal-prices-charts/historical-gold-prices/) '
            '[Silver price](https://www.denvergold.org/precious-metal-prices-charts/historical-silver-prices/)')
        st.write(
            'EE.UU inflation vs gold (annual increment): [EE.UU inflation](https://fred.stlouisfed.org/series/CPIAUCNS) '
            '[Gold](https://www.lbma.org.uk/prices-and-data/precious-metal-prices#/) ')
        st.write(
            'M2 vs EE.UU inflation (annual increment) [M2 since 1867](https://www.dropbox.com/s/8areriurrxs4te8/M2%20calculation.xlsx?dl=0) '
            '[EE.UU inflation](https://fred.stlouisfed.org/series/CPIAUCNS)')
        st.write('EE.UU real interest rates [EE.UU inflation](https://fred.stlouisfed.org/series/CPIAUCNS) '
                 '[EE.UU 10-year nominal interest rate](https://fred.stlouisfed.org/series/DFII10)')
        st.write(
            'Europe real interest rates [Europe inflation](https://sdw.ecb.europa.eu/quickview.do?SERIES_KEY=122.ICP.M.U2.N.000000.4.ANR) '
            '[Europe 10-year interest rates](https://sdw.ecb.europa.eu/quickview.do?SERIES_KEY=124.MIR.M.U2.B.A20.A.R.A.2240.EUR.O)')
        st.write(
            'Silver logarithmic scale [Source](https://www.denvergold.org/precious-metal-prices-charts/historical-silver-prices/) ')
        st.write(
            'Silver logarithmic scale inflation adjusted [Source](https://www.denvergold.org/precious-metal-prices-charts/historical-silver-prices/) ')

    if menu == '¿Vale la pena comprar plata y/o oro?' and language == 'ES':
        st.markdown('# ¿Merece la pena comprar plata y/o oro?')
        st.markdown('## **1- Relación histórica entre el oro y la plata**')
        st.write('El oro y la plata tienen una estrecha relación hace tiempo.\n\n'
                 'En la siguiente gráfica se puede apreciar que desde 1791 los dos activos mantienen una'
                 ' relación estrecha desde hace tiempo. Teniendo zonas de suelo donde es preferible'
                 'tener oro a tener plata y zonas de techo donde es preferible tener plata a tener'
                 'oro.')
        st.plotly_chart(sa.gold_silver_ratio_graph)
        st.markdown('## **2- Relación entre la inflación y el oro**')
        st.write('Estos dos activos se caracterizan porque son la mejor alternativa en épocas de inflación.\n\n'
                 'Puede apreciarse que desde el año 70 el oro tiende a subir cuando ocurren presiones inflacionistas.')
        st.plotly_chart(sa.gold_inflation)
        st.markdown('## **3- Relación entre la inflación y la M2**')
        st.write('Como puede apreciarse en el siguiente gráfico, el incremento sin precedentes que está'
                 ' ocurriendo con respecto a la cantidad de M2 (en USD), actualmente del 25%, '
                 'indica que la inflación está estrechamente ligada con la M2, lo cual nos indica'
                 ' el comienzo en estos momentos de fuertes presiones inflacionistas.')
        st.plotly_chart(sa.m2_inflation)
        st.markdown('## **4- Relación entre los tipos de interés reales, oro y plata **')
        st.write('Esto explicado anteriormente sirve para ponernos en contexto de cual es la situación\n'
                 'actual y de si ésta puede beneficiar al oro y la plata o no. No obstante el oro y la\n'
                 'plata se guían realmente por por los tipos de interés reales. '
                 '')
        st.markdown('### **¿Qué son los tipos de interés reales?**')
        st.write('Tipo de interés real = Tipo de interés nominal - Inflación.\n\n'
                 'El tipo de interés nominal representa el tipo oficial que fijan los bancos centrales\n'
                 'para conceder créditos.\n\n'
                 'Como se aprecia en la gráfica anterior, las presiones inflacionistas ya están empezando\n'
                 'a aparecer con fuerza y los inversores cuentan con ellas. Si los bancos centrales\n'
                 'siguen con la política de mantener tipos cercanos al 0% la tasa de interés real\n'
                 'irá cayendo cada vez mas.\n\n'
                 'Puede observarse en los dos gráficos siguientes como estas tasas se encuentran\n'
                 'actualmente descendiendo debido a políticas de expansión por parte de los\n'
                 'bancos centrales estadounidense y europeo.')
        st.plotly_chart(sa.real_interest_rates_USA_graph)
        st.plotly_chart(sa.real_interest_rates_europe_graph)
        st.write('En el siguiente gráfico podemos apreciar como como la relación entre el oro y los\n'
                 'tipos de interés es inversa, lo cual nos indica que el oro es un activo capaz de\n'
                 'proteger a su propietario frente a la pérdida de valor de las divisas FIAT, más\n'
                 'conocida como inflación.')
        st.plotly_chart(sa.interest_10_years_gold)
        st.write('También, si observamos en escala logarítmica la plata tiene una tendencia\n'
                 'alcista a largo plazo muy clara, cotizando lejos de máximos históricos.')
        st.plotly_chart(sa.silver_log_graph)
        st.write('Por último, si ajustamos la plata a la inflación vemos que realmente no está\n'
                 'cara y ahora mismo puede ser un buen momento para su compra.')
        st.plotly_chart(sa.silver_log_inflation_graph)
        st.markdown('## Fuentes')
        st.write('Ratio plata/oro desde 1791: [Precios oro](https://www.denvergold.org/precious-metal-prices-charts/historical-gold-prices/) '
                 '[Precios plata](https://www.denvergold.org/precious-metal-prices-charts/historical-silver-prices/)')
        st.write('Inflación EE.UU vs oro (incremento anual): [Inflación EE.UU](https://fred.stlouisfed.org/series/CPIAUCNS) '
                 '[Oro](https://www.lbma.org.uk/prices-and-data/precious-metal-prices#/) ')
        st.write('M2 vs inflación EE.UU (incremento anual) [M2 desde 1867](https://www.dropbox.com/s/8areriurrxs4te8/M2%20calculation.xlsx?dl=0) '
                 '[Inflación EE.UU](https://fred.stlouisfed.org/series/CPIAUCNS)')
        st.write('Tasas de interés reales en EE.UU [Inflación EE.UU](https://fred.stlouisfed.org/series/CPIAUCNS) '
                 '[Interés nominal a 10 años EE.UU](https://fred.stlouisfed.org/series/DFII10)')
        st.write('Tasas de interés reales en Europa [Inflación Europa](https://sdw.ecb.europa.eu/quickview.do?SERIES_KEY=122.ICP.M.U2.N.000000.4.ANR) '
                 '[Interés nominal a 10 años Europa](https://sdw.ecb.europa.eu/quickview.do?SERIES_KEY=124.MIR.M.U2.B.A20.A.R.A.2240.EUR.O)')
        st.write('Plata escala logarítmica [Fuente](https://www.denvergold.org/precious-metal-prices-charts/historical-silver-prices/) ')
        st.write('Plata escala logarítmica ajustada por inflación [Fuente](https://www.denvergold.org/precious-metal-prices-charts/historical-silver-prices/) ')



if __name__ == '__main__':
    main()
