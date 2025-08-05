import streamlit as st
# إعداد الصفحة
st.set_page_config(page_title="ملخّص النصوص بالذكاء الاصطناعي", layout="centered")

# العنوان
st.title("📚 ملخّص النصوص")
st.write("ألصق أي نص هنا، واحصل على ملخص سريع وذكي ✨")

# حقل إدخال النص
text = st.text_area("✍️ أدخل النص هنا:")

# زر التلخيص
if st.button("🔍 تلخيص"):
    if not text.strip():
        st.warning("من فضلك أدخل نصًا أولًا.")
    else:
        # عملية التلخيص البسيطة
        if len(text) > 300:
            summary = text[:200] + "..."
        else:
            summary = text

        # عرض النتيجة
        st.success("✅ الملخص:")
        st.write(summary)

# خط فاصل
st.markdown("---")

st.caption("🚀 تم الإنشاء باستخدام Python + Streamlit | مجانًا")
