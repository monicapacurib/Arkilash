import streamlit as st
from datetime import date

# ---------- Page config ----------
st.set_page_config(
    page_title="Arkilash & Brows Beauty Lounge",
    page_icon="✨",
    layout="wide",
)

# ---------- Hero section ----------
st.image(
    "https://images.unsplash.com/photo-1514679725449-7ec2e81918e9"
    "?auto=format&fit=crop&w=1600&q=80",
    use_column_width=True,
)
st.title("Arkilash & Brows Beauty Lounge")
st.subheader("Wake up and don’t make up – let your natural beauty shine ✨")
st.markdown(
    "Home‑based beauty studio in **Lumban, Laguna** offering brow, lash, nail "
    "and waxing services in a cozy, safe space."
)

# ---------- Main content ----------
tabs = st.tabs(["Services", "Promos", "Gallery", "Contact"])

with tabs[0]:
    st.header("Our Services")
    st.markdown(
        """
* **Eyelash Extensions** – Classic, Hybrid, Volume sets  
* **Lash Lift**  
* **6D Microblading**  
* **Ombre / Powder Brows**  
* **Combination (Combi) Brows**  
* **Nail Extensions & Gel Polish**  
* **Underarm & Leg Waxing**
"""
    )

with tabs[1]:
    st.header("Latest Promos")
    st.success(
        "⛈️ **Rainy Day Brow Sale** – enjoy **25 % OFF** on our most popular "
        "brow services from **July 1 – 10**!"
    )
    st.info("Follow our Facebook page for flash deals!")

with tabs[2]:
    st.header("Client Gallery")
    st.write("Swipe to see some of our recent work:")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(
            "https://images.unsplash.com/photo-1544717305-2782549b5136"
            "?auto=format&fit=crop&w=600&q=80",
            caption="Soft‑arch brows",
        )
    with col2:
        st.image(
            "https://images.unsplash.com/photo-1522336572468-97b06e8ef143"
            "?auto=format&fit=crop&w=600&q=80",
            caption="Classic lash set",
        )
    with col3:
        st.image(
            "https://images.unsplash.com/photo-1508154048109-de555266b5c4"
            "?auto=format&fit=crop&w=600&q=80",
            caption="Volume lash set",
        )

with tabs[3]:
    st.header("Book Your Appointment")
    st.markdown(
        """
**Address**  
Tabia St., Brgy Bagong Silang, Lumban, Laguna  
*(Landmark: M Lhuillier)*  

**Operating Mode**  
By **appointment only** – no walk‑ins  

**How to book**  
* Message us on **[Facebook](https://www.facebook.com/eyelashextensionlumbanlaguna/)**  
* SMS / Viber: **+63 912 345 6789**  

_We can’t wait to pamper you!_
"""
    )
    st.write(f"© {date.today().year} ArkiLash & Brows Beauty Lounge")

# ---------- Optional – Hide Streamlit footer & menu ----------
st.markdown(
    """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
""",
    unsafe_allow_html=True,
)
