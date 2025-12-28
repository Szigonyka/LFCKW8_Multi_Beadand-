import streamlit as st
import pandas as pd
import requests
import time

# URL = "http://127.0.0.1:8000"  
URL = "https://lfckw8-multi-beadand.onrender.com"

st.set_page_config(page_title="Kripto Figyelő", layout="wide")

st.title(" Bitcoin Árfolyamfigyelő")

st.sidebar.header("Vezérlőpult")
if st.sidebar.button("Frissítés most"):
    st.rerun()

st.sidebar.caption(f"Utolsó frissítés: {time.strftime('%H:%M:%S')}")

try:
  
    res = requests.get(f"{URL}/adatok/")
    statisztika_res = requests.get(f"{URL}/statisztika/")
    
 
    if res.status_code == 200 and statisztika_res.status_code == 200:
        lista = res.json()
        stat = statisztika_res.json()
        
        if len(lista) > 0:
   
            df = pd.DataFrame(lista)
            
            if "rogzites_ideje" in df.columns:
                df["rogzites_ideje"] = pd.to_datetime(df["rogzites_ideje"])
            
            mostani_ar = df.iloc[0].get("aktualis_ar", 0)
            
            k1, k2, k3 = st.columns(3)
            
            k1.metric("Aktuális ár", f"{mostani_ar:,.0f} Ft")
            
            atlag = stat.get("atlag_ar", 0)
            k2.metric("Átlag ár", f"{atlag:,.0f} Ft")
            
            magas_db = stat.get("magas_aruak_szama", stat.get("dragak_szama", 0))
            k3.metric("Drága mérések", f"{magas_db} db")
            
            st.divider()
            
            st.subheader("Árfolyam alakulása")
            if "aktualis_ar" in df.columns and "rogzites_ideje" in df.columns:

                chart_data = df.set_index("rogzites_ideje")["aktualis_ar"]
                st.line_chart(chart_data)
            else:
                st.warning("Hiányzó adatok a grafikonhoz.")
            
            with st.expander("Részletes táblázat megtekintése"):
                st.dataframe(df, use_container_width=True)
        else:
            st.info("A szerver elérhető, de még nincs adat az adatbázisban. Várj, amíg a scraper dolgozik!")           
    else:
        st.error(f"Hiba a szerver válaszában! Kód: {res.status_code}")

except requests.exceptions.ConnectionError:
    st.error("Nem érem el a szervert!")
except Exception as e:
    st.error(f"Váratlan hiba történt a kódban: {e}")