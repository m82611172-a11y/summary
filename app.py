
import streamlit as st
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

# إعداد الصفحة
st.set_page_config(page_title="ملخّص النصوص بالذكاء الاصطناعي", layout="centered")

# العنوان
st.title("📚 ملخّص النصوص")
st.write("✨ ألصق أي نص هنا، واحصل على ملخص سريع وذكي")

# حقل إدخال النص
text = st.text_area("✍️ أدخل النص هنا:")

# زر التلخيص
if st.button("🔍 تلخيص"):
    if not text.strip():
        st.warning("من فضلك أدخل نصًا أولاً.")
    else:
        # التلخيص باستخدام sumy
        parser = PlaintextParser.from_string(text, Tokenizer("arabic"))
        summarizer = LsaSummarizer()
        summary = summarizer(parser.document, 3)  # عدد الجمل في الملخص

        st.subheader("📄 الملخص:")
        for sentence in summary:
            st.write(str(sentence))

# تذييل
st.markdown("---")
st.caption("🚀 تم الإنشاء باستخدام Python + Streamlit | مجانًا")
