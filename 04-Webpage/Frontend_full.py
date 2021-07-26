import streamlit as st
import os
#os.chdir(path=r'.\04-Webpage')
import Silver_analysis as sa

st.text('Frontend full:')
st.text(os.path.dirname(os.path.realpath(__file__)))
st.text(sa.a)
st.text(sa.b)
'''st.set_page_config(page_title='Central Bank Analytics', page_icon='euro')

def main():
    menu = st.sidebar.radio('Select:', ('Silver analysis', 'Crisis financiera'))
    if menu == 'Silver analysis':
        st.title('¿Merece la pena comprar plata?')
        st.text('El oro y la plata tienen una esatrecha relación hace tiempo.\n\n'
                'En la siguiente gráfica se puede apreciar que desde 1791 los dos activos mantienen una\n'
                'relación estrecha desde hace tiempo. Teniendo zonas de suelo donde es preferible\n'
                'tener oro a tener plata y zonas de techo donde es preferible tener plata a tener\n'
                'oro.\n')
        st.plotly_chart(sa.gold_silver_ratio_graph)
        st.text('Estos dos activos se caracterizan porque son la mejor alternativa en épocas de inflación.\n\n'
                'Puede apreciarse que desde el año 70 el oro tiende a subir cuando ocurren presiones\n'
                'inflacionistas.')
        st.plotly_chart(sa.gold_inflation)
        st.text('Como puede apreciarse en el siguiente gráfico, el incremento sin precedentes que está\n'
                'ocurriendo con respecto a la cantidad de M2 (en USD), actualmente del 25%,\n'
                'indica que la inflación está estrechamente ligada con la M2, lo cual nos indica\n'
                'el comienzo en estos momentos de fuertes presiones inflacionistas.')
        st.plotly_chart(sa.m2_inflation)
        st.text('Esto explicado anteriormente sirve para ponernos en contexto de cual es la situación\n'
                'actual y de si ésta puede beneficiar al oro y la plata o no. No obstante el oro y la\n'
                'plata se guían realmente por por los tipos de interés reales. Pero, ¿qué son los tipos\n'
                'reales de interés?\n\n'
                'Tipo de interés real = Tipo de interés nominal - Inflación.\n\n'
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
        st.text('En el siguiente gráfico podemos apreciar como como la relación entre el oro y los\n'
                'tipos de interés es inversa, lo cual nos indica que el oro es un activo capaz de\n'
                'proteger a su propietario frente a la pérdida de valor de las divisas FIAT, más\n'
                'conocida como inflación.')
        st.plotly_chart(sa.interest_10_years_gold)
        st.text('También, si observamos en escala logarítmica la plata tiene una tendencia\n'
                'alcista a largo plazo muy clara, cotizando lejos de máximos históricos.')
        st.plotly_chart(sa.silver_log_graph)
        st.text('Por último, si ajustamos la plata a la inflación vemos que realmente no está\n'
                'cara y ahora mismo puede ser un buen momento para su compra.')
        st.plotly_chart(sa.silver_log_inflation_graph)



if __name__ == '__main__':
    main()
'''