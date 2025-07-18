import gradio as gr
from NER_model import Model

obj = Model()

# Different colors for different entity types
ENTITY_COLORS = {
    "PER": "#FF9999",  # People - Light red
    "LOC": "#99FF99",  # Locations - Light green
    "ORG": "#9999FF",  # Organizations - Light blue
    "MISC": "#FFFF99",  # Miscellaneous - Light yellow
}


def highlight_entities(text):
    entities = obj.nering(text)
    highlighted_text = text

    # Sort entities from right to left for RTL languages
    entities_sorted = sorted(entities, key=lambda x: x['start'], reverse=True)

    for entity in entities_sorted:
        word = entity['word']
        entity_type = obj.entity_expand(entity['entity_group'])
        start = entity['start']
        end = entity['end']

        # Get color based on entity type (default to gray if not found)
        color = ENTITY_COLORS.get(entity['entity_group'], "#CCCCCC")

        # Create HTML span with highlighting
        highlighted_word = (
            f'<span style="background-color: {color}; padding: 2px; border-radius: 3px; '
            f'font-weight: bold;" title="{entity_type}">{word}</span>'
        )

        highlighted_text = highlighted_text[:start] + highlighted_word + highlighted_text[end:]

    return highlighted_text


# Custom CSS for better RTL display
css = """
.rtl {direction: rtl; text-align: right;}
.gradio-container {font-family: "B Nazanin", "Iranian Sans", Tahoma, sans-serif;}
"""

with gr.Blocks(css=css) as demo:
    gr.Markdown("## تشخیص موجودیت‌های نامدار در متن فارسی")
    gr.Markdown(
        "این برنامه موجودیت‌های نامدار (مانند نام افراد، مکان‌ها، سازمان‌ها و ...) را در متن فارسی شناسایی و مشخص می‌کند.")

    with gr.Row():
        with gr.Column():
            input_text = gr.Textbox(
                label="متن ورودی",
                placeholder="متن فارسی خود را اینجا بنویسید...",
                elem_classes="rtl"
            )
            btn = gr.Button("تجزیه و تحلیل متن")
        with gr.Column():
            output_html = gr.HTML(
                label="نتایج",
                elem_classes="rtl"
            )

    # Add legend for entity types
    with gr.Row():
        gr.Markdown("### راهنمای رنگ‌ها:")
        for entity_type, color in ENTITY_COLORS.items():
            gr.HTML(
                f'<span style="background-color: {color}; padding: 2px 5px; margin: 0 5px; '
                f'border-radius: 3px;">{obj.entity_expand(entity_type)}</span>'
            )

    btn.click(
        fn=highlight_entities,
        inputs=input_text,
        outputs=output_html
    )

demo.launch()