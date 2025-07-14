import streamlit as st
from datetime import date

st.set_page_config(
    page_title="Arkilash & Brows Beauty Lounge",
    page_icon="✨",
    layout="wide",
)

# ---------- Hero section ----------
st.image(
    "https://images.unsplash.com/photo-1514679725449-7ec2e81918e9?auto=format&fit=crop&w=1600&q=80",
    use_column_width=True,
)
st.title("Arkilash & Brows Beauty Lounge")
st.subheader("Wake up and don’t make up – let your natural beauty shine ✨")
st.markdown(
    "Home‑based beauty studio in **Lumban, Laguna** offering brow, lash, nail, and waxing services in a cozy, safe space."
)

# ---------- Main tabs ----------
tabs = st.tabs(["Services", "Gallery", "Contact"])

# ----- SERVICES -----
with tabs[0]:
    st.header("Our Services")
    cols = st.columns(2)

    with cols[0]:
        st.subheader("Eyelash Extensions")
        st.image(
            "https://scontent.fmnl17-5.fna.fbcdn.net/v/t39.30808-6/440967317_122521025937453234_1010631581592211192_n.jpg?stp=dst-jpg_p600x600&_nc_cat=105&ccb=1-7&_nc_sid=3635dc&_nc_eui2=AeGQSV1AJ_M1VB7kgid-Mcob7v1Q0yHevB8dZ3YeEUj_dYd5sSi7KpMjh9r6VR9OrrJ0wC-hABTozDjfNe-VJ9A6&_nc_ohc=dq6-2OsZ9oAQ7kNvgGzvMKj&_nc_ht=scontent.fmnl17-5.fna&oh=00_AYAFTn9xnob2DQm3WeAqVChwIOfjZ6N64i2hBRpZAwug&oe=669A5425",
            caption="Full‑set Eyelash Extensions",
        )
        st.write("- Classic, Hybrid, Volume")

    with cols[1]:
        st.subheader("Lash Lift")
        st.image(
            "https://scontent.fmnl17-3.fna.fbcdn.net/v/t39.30808-6/441009280_122521025934321275_8016955130173887648_n.jpg?stp=dst-jpg_p600x600&_nc_cat=111&ccb=1-7&_nc_sid=3635dc&_nc_eui2=AeFbOjgK44o5Ho_MOGW6KHXDRRHmNu8P-RHmcKHJgn6LgYXyA3Tz8u46v93aBJMdKHb52XYcLb6EVf9soNpdqZSE&_nc_ohc=7uThCTMnAJ8Q7kNvgEtgtuo&_nc_ht=scontent.fmnl17-3.fna&oh=00_AYCmPgGkN77ehxZo_x3lmRyt5nRPoA91EwKYrgK2ZmVR-Q&oe=669A4D80",
            caption="Lash Lift Result",
        )
        st.write("- Curled natural lashes, lasts weeks")

    cols = st.columns(2)

    with cols[0]:
        st.subheader("6D Microblading")
        st.image(
            "https://scontent.fmnl17-4.fna.fbcdn.net/v/t39.30808-6/441154093_122521025928900692_8991160726433932710_n.jpg?stp=dst-jpg_p600x600&_nc_cat=101&ccb=1-7&_nc_sid=3635dc&_nc_eui2=AeFzY41PCncHdNDulWwsIedVwZ4Wdsfq0lwOSLRTPVCFrJgwqu7ol-cRQpXLo4dw_JA2DeINMJW0TE6JvVV--9r9&_nc_ohc=Vc8sw3MzFOoQ7kNvgHvpoRI&_nc_ht=scontent.fmnl17-4.fna&oh=00_AYBOOdfHqPO0hxJ-xSuVg7-BOZQgyR2WicmJ8fscEcxdiQ&oe=669A4F9F",
            caption="Microbladed Brows",
        )
        st.write("- Semi‑permanent hair‑like strokes")

    with cols[1]:
        st.subheader("Ombre / Powder & Combi Brows")
        st.image(
            "https://scontent.fmnl17-1.fna.fbcdn.net/v/t39.30808-6/439895883_122521025930146958_7273849604008829973_n.jpg?stp=dst-jpg_p600x600&_nc_cat=102&ccb=1-7&_nc_sid=3635dc&_nc_eui2=AeHTfnZnoYuy_QPUjrmKc_Z-CP8sUNs0ZqvFSllY9WcLmr8NUA8_1FiW3AI6oRbmhsm6h0zxsfLV_nJbPP6yoIya&_nc_ohc=BtKNeNDZ68oQ7kNvgGn77Vo&_nc_ht=scontent.fmnl17-1.fna&oh=00_AYBA2L4jozby4uZ3-K6g7ROcUIf65fS7g8n18yoJmD9gxg&oe=669A66B0",
            caption="Combi/Ombre Brows",
        )
        st.write("- Fully shaded or combi brows")

    with cols[0]:
        st.subheader("Nail Extensions & Gel Polish")
        st.image(
            "https://scontent.fmnl17-2.fna.fbcdn.net/v/t39.30808-6/441187949_122521025925470225_4082321274207403864_n.jpg?stp=dst-jpg_p600x600&_nc_cat=100&ccb=1-7&_nc_sid=3635dc&_nc_eui2=AeHZY0ey5k9I-BzJVGzWxAJTf3huXt_jL4J9FZAHAGB9QLrDCNG3fdZ9SkMu_s0x5SGHYBRnt3Rt6wMTxeEcgHuW&_nc_ohc=wVpivRA_A9EQ7kNvgE3UOeM&_nc_ht=scontent.fmnl17-2.fna&oh=00_AYDU3_9q_gzUj5vR9idMlBaGZBzNVblmoi4o6AmKnNz_6g&oe=669A552D",
            caption="Gel Nail Extensions",
        )
        st.write("- Acrylic extensions & gel polish")

    with cols[1]:
        st.subheader("Underarm & Leg Waxing")
        st.image(
            "https://scontent.fmnl17-5.fna.fbcdn.net/v/t39.30808-6/440899812_122521025939470232_7980870990804475814_n.jpg?stp=dst-jpg_p600x600&_nc_cat=106&ccb=1-7&_nc_sid=3635dc&_nc_eui2=AeHuI-JN3JgNEw2FJchzUgxfrboUpiGfbXBxCAWoiVzNQuCk1uqe2pGc4gJZMdWcScAqOlNv4zZ2w2by98tkydMg&_nc_ohc=8JGk_Cx7L8QQ7kNvgFb6Kzh&_nc_ht=scontent.fmnl17-5.fna&oh=00_AYAKk1ETEX5ZcTz_PNKrF_4wJRLWcvFXl0rDLjbiuBGrJQ&oe=669A6A94",
            caption="Underarm Waxing",
        )
        st.write("- Efficient & gentle waxing")

# ----- GALLERY -----
with tabs[1]:
    st.header("Client Gallery")
    st.write("Swipe through some of our recent work:")
    c1, c2, c3 = st.columns(3)
    c1.image(
        "https://images.unsplash.com/photo-1544717305-2782549b5136?auto=format&fit=crop&w=600&q=80",
        caption="Soft‑arch brows",
    )
    c2.image(
        "https://images.unsplash.com/photo-1522336572468-97b06e8ef143?auto=format&fit=crop&w=600&q=80",
        caption="Classic lash set",
    )
    c3.image(
        "https://images.unsplash.com/photo-1508154048109-de555266b5c4?auto=format&fit=crop&w=600&q=80",
        caption="Volume lash set",
    )

# ----- CONTACT -----
with tabs[2]:
    st.header("Book Your Appointment")
    st.markdown(
        f"""
**Address**  
Tabia St., Brgy Bagong Silang, Lumban, Laguna  
*(Landmark: M Lhuillier)*  

**Operating Mode**  
By **appointment only** – no walk‑ins  

**How to book**  
* Message us on **[Facebook](https://www.facebook.com/eyelashextensionlumbanlaguna/)**  
* SMS / Viber: **+63 912 345 6789**  

_We can’t wait to pamper you!_

© {date.today().year} ArkiLash & Brows Beauty Lounge
"""
    )

# ---------- Hide default Streamlit menu/footer ----------
st.markdown(
    """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
""",
    unsafe_allow_html=True,
)
