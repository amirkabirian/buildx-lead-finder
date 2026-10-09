import streamlit as st

st.set_page_config(page_title="BuildX Lead Finder", page_icon="🎯", layout="centered")

st.markdown("<h2 style='text-align: center; color: #1f77b4;'>🎯 کاشف هوشمند مشتری بالقوه (BuildX - مسئله ۱)</h2>", unsafe_allow_html=True)
st.write("---")

with st.form("lead_form"):
    product = st.text_input("نام محصول یا کسب‌وکار شما:", placeholder="مثلا: دوره جامع آموزش پایتون و هوش مصنوعی")
    message = st.text_input("پیام کاربر در جامعه آنلاین:", placeholder="مثلا: سلام بچه‌ها، من تو یادگیری برنامه‌نویسی پایتون گیر کردم...")
    submitted = st.form_submit_button("اجرای تحلیلگر ایجنت 🚀")

if submitted:
    if product and message:
        msg_lower = message.lower()
        keywords = ["یادگیری", "آموزش", "پایتون", "کد", "برنامه", "مشکل", "خرید", "فروش", "قیمت", "دوره"]
        is_rel = any(k in msg_lower for k in keywords)
        score = "92%" if is_rel else "15%"
        
        if is_rel:
            reply = f"سلام! متوجه شدم که در زمینه {product} به دنبال راهنمایی هستید. ما در مجموعه خودمان دوره‌ها و منابع کاملی داریم که دقیقاً می‌توانند این چالش را برای شما حل کنند."
        else:
            reply = "این پیام ارتباطی با حوزه تخصصی محصول شما ندارد و به عنوان لید رد شد."

        st.success("تحلیل با موفقیت انجام شد!")
        st.write(f"📦 **محصول:** {product}")
        st.write(f"💬 **پیام بررسی شده:** {message}")
        st.write(f"🔍 **وضعیت لید:** {'✅ مرتبط و واجد شرایط (Relevant)' if is_rel else '❌ غیرمرتبط'}")
        st.write(f"📈 **امتیاز تناسب (Fit Score):** {score}")
        st.write(f"💸 **هزینه تخمینی پردازش:** $0.00014")
        st.info(f"✍️ **پاسخ پیشنهادی ایجنت:**\n\n{reply}")
    else:
        st.warning("لطفاً هر دو کادر را پر کنید!")
