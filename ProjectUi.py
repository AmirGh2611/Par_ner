import gradio as gr
from NER_model import Model

obj = Model()


def highlight_entities(text):
    entities = obj.nering(text)
    highlighted_text = text

    # We need to process entities from right to left to maintain correct positions
    # Since Persian is RTL, we'll sort entities by their start position in descending order
    entities_sorted = sorted(entities, key=lambda x: x['start'], reverse=True)

    for entity in entities_sorted:
        word = entity['word']
        entity_type = obj.entity_expand(entity['entity_group'])
        start = entity['start']
        end = entity['end']

        # Create HTML span with highlighting and tooltip showing entity type
        highlighted_word = f'<span style="background-color: #6e1435; font-weight: bold;" title="{entity_type}">{word}</span>'

        # Replace the original word with highlighted version
        highlighted_text = highlighted_text[:start] + highlighted_word + highlighted_text[end:]

    return highlighted_text


demo = gr.Interface(
    fn=highlight_entities,
    inputs=gr.Textbox(label="متن فارسی را وارد کنید", placeholder="متن فارسی خود را اینجا بنویسید..."),
    outputs=gr.HTML(label="متن با موجودیت‌های نامدار مشخص شده"),
    title="تشخیص موجودیت‌های نامدار در متن فارسی",
    description="این برنامه موجودیت‌های نامدار (مانند نام افراد، مکان‌ها و ...) را در متن فارسی شناسایی و مشخص می‌کند"
)

# Add RTL direction to the interface
css = """
.rtl {direction: rtl; text-align: right;}
"""

demo.launch(share=True)
