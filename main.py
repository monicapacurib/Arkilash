import streamlit as st
from datetime import date

st.set_page_config(
    page_title="Arkilash & Brows Beauty Lounge",
    page_icon="✨",
    layout="wide",
)

st.image("https://images.unsplash.com/photo-151467...")  # Hero

st.title("Arkilash & Brows Beauty Lounge")
st.subheader("Wake up and don’t make up – let your natural beauty shine ✨")
st.markdown("Home‑based beauty studio in **Lumban, Laguna** offering brow, lash, nail, and waxing services in a cozy, safe space.")

tabs = st.tabs(["Services", "Promos", "Gallery", "Contact"])

with tabs[0]:
    st.header("Our Services")
    cols = st.columns(2)
    with cols[0]:
        st.subheader("Eyelash Extensions")
        st.image("https://image.shutterstock.com/lash-extension", caption="Full‑set eyelash extensions")
        st.write("- Classic, Hybrid, Volume")
    with cols[1]:
        st.subheader("Lash Lift")
        st.image("https://image.shutterstock.com/lash-lift", caption="Lifted & curled lashes")
        st.write("- Curled natural lashes, lasts weeks")
    cols = st.columns(2)
    with cols[0]:
        st.subheader("6D Microblading")
        st.image("https://image.shutterstock.com/microblading", caption="Hair‑stroke brow art")
        st.write("- Semi‑permanent hair‑like strokes")
    with cols[1]:
        st.subheader("Ombre / Powder & Combi Brows")
        st.image("https://image.shutterstock.com/ombre-brows", caption="Soft‑shade ombre brows")
        st.write("- Fully shaded or combi brows")
    with cols[0]:
        st.subheader("Nail Extensions & Gel Polish")
        st.image("https://image.shutterstock.com/nails", caption="Gel nails & tips")
        st.write("- Acrylic extensions & gel polish")
    with cols[1]:
        st.subheader("Underarm & Leg Waxing")
        st.image("https://image.shutterstock.com/waxing", caption="Smooth waxing results")
        st.write("- Efficient & gentle waxing")

with tabs[1]:
    st.header("Latest Promos")
    st.success("⛈️ **Rainy Day Brow Sale** – 25% OFF brow services from July 1–10!")
    st.info("Follow our [Facebook](https://www.facebook.com/eyelashextensionlumbanlaguna) for flash deals!")

with tabs[2]:
    st.header("Client Gallery")
    st.write("Swipe through some of our recent work:")
    c1, c2, c3 = st.columns(3)
    c1.image("https://images.unsplash.com/photo-1544717305...", caption="Soft‑arch brows")
    c2.image("https://images.unsplash.com/photo-1522336572468...", caption="Classic lash set")
    c3.image("https://images.unsplash.com/photo-1508154048109...", caption="Volume lash set")

with tabs[3]:
    st.header("Book Your Appointment")
    st.markdown("""
**Address**  
Tabia St., Brgy Bagong Silang, Lumban, Laguna  
*(Landmark: M Lhuillier)*  

**Operating Mode**  
By **appointment only**  

**How to book**  
- Message us on **[Facebook]**(https://www.facebook.com/eyelashextensionlumbanlaguna)  
- SMS / Viber: **+63 912 345 6789**

© {year} ArkiLash & Brows Beauty Lounge
""".replace("{year}", str(date.today().year)))

st.markdown("""
<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;}</style>
""", unsafe_allow_html=True)
