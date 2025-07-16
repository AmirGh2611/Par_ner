import streamlit as st
from NER_model import obj

# رابط کاربری
st.title("تشخیص موجودیت‌های نام‌دار (NER) در متن فارسی")

text = st.text_area("متن خود را وارد کنید:")

if text:
    results = obj.nering(text)
    # هایلایت کردن موجودیت‌ها
    highlighted_text = text
    offset = 0  # برای تنظیم جایگزینی درست

    for entity in sorted(results, key=lambda x: x['start']):
        start = entity['start'] + offset
        end = entity['end'] + offset
        label = entity['entity_group']
        tag = f"<span style='background-color:#D1FFD6; padding:2px 4px; border-radius:4px;'>{text[start:end]} <b>[{label}]</b></span>"
        highlighted_text = highlighted_text[:start] + tag + highlighted_text[end:]
        offset += len(tag) - (end - start)

    st.markdown(highlighted_text, unsafe_allow_html=True)
