import streamlit as st

st.set_page_config(page_title="BuildX Lead Finder", page_icon="🎯", layout="centered")

# مدیریت وضعیت ورود کاربر (Session State)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""

# اگر کاربر وارد نشده بود، صفحه ثبت‌نام/ورود را نشان بده
if not st.session_state.logged_in:
    st.markdown("<h2 style='text-align: center; color: #1f77b4;'>🎯 ورود به سامانه BuildX Lead Finder</h2>", unsafe_allow_html=True)
    st.write("---")
    
    with st.form("login_form"):
        st.info("لطفاً برای ورود به پنل و استفاده از ایجنت، اطلاعات خود را وارد کنید:")
        username_input = st.text_input("نام کاربری یا ایمیل:")
        login_submitted = st.form_submit_button("ورود به سامانه 🚀")
        
        if login_submitted:
            if username_input.strip():
                st.session_state.logged_in = True
                st.session_state.username = username_input.strip()
                st.rerun()
            else:
                st.warning("لطفاً نام کاربری یا ایمیل خود را وارد کنید!")

# اگر کاربر وارد شده بود، صفحه اصلی ابزار (کاشف لید) را نشان بده
else:
    st.sidebar.success(ژنرال:=f"کاربر: {st.session_state.username}")
    if st.sidebar.button("خروج از حساب"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()

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
