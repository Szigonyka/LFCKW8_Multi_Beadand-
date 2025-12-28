import streamlit as st
import pandas as pd
import requests

# Backend címe
URL = "http://127.0.0.1:8000"

st.title("Bitcoin Árfolyamfigyelő")

# Frissítés gomb oldalt
st.sidebar.write("Vezérlőpult")
if st.sidebar.button("Frissítés"):
    st.rerun()

try:
    # Adatok lekérése a szerverről
    res = requests.get(f"{URL}/adatok/")
    statisztika_res = requests.get(f"{URL}/statisztika/")
    
    # Ha minden oké
    if res.status_code == 200 and statisztika_res.status_code == 200:
        lista = res.json()
        stat = statisztika_res.json()
        
        if len(lista) > 0:
            # Pandas dataframe készítése
            df = pd.DataFrame(lista)
            
            # Időformátum javítása, hogy szép legyen a grafikonon
            df["rogzites_ideje"] = pd.to_datetime(df["rogzites_ideje"])
            
            # Legfrissebb ár kiszedése
            mostani_ar = df.iloc[0]["aktualis_ar"]
            
            # Kártyák kirajzolása (Metrics)
            k1, k2, k3 = st.columns(3)
            k1.metric("Aktuális ár", f"{mostani_ar:,.0f} Ft")
            k2.metric("Átlag (teljes)", f"{stat['atlag_ar_huf']:,.0f} Ft")
            
            # Itt látszik a backend szűrése
            szurt_szam = stat.get("20m_feletti_meresek_szama", 0)
            k3.metric("Magas árfolyamok (>28.8M)", f"{szurt_szam} db")
            
            st.divider()
            
            # Grafikon
            st.subheader("Árfolyam alakulása")
            chart_data = df.set_index("rogzites_ideje")["aktualis_ar"]
            st.line_chart(chart_data)
            
            # Táblázat a végére
            st.write("Részletes adatok:")
            st.dataframe(df)
            
        else:
            st.info("Még nincs adat, várj kicsit...")
            
    else:
        st.error("Hiba a szerver kommunikációban.")

except:
    st.warning("Nem érem el a szervert. Fut a backend?")