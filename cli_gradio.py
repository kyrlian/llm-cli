import gradio as gr
from prompts import prompts
from engine_ollama import engine_ollama

def buildapp(engine, prompts):
    def generate(instructions, payload, result):
        prompt = instructions.format(payload=payload, result=result)
        return engine.generate(prompt)

    def changelang(lang):
        return prompts[lang]

    def changeinstruction(lang, instruction):
        return prompts[lang][instruction]

    default_lang = list(prompts.keys())[0]
    default_instruction = list(prompts[default_lang].keys())[0]
    # https://www.gradio.app/guides/blocks-and-event-listeners#blocks-structure
    with gr.Blocks() as myapp:
        with gr.Row():
            gr.Markdown("# LLM Assistant")
            lang_drop = gr.Dropdown(
                choices=list(prompts.keys()),
                value=default_lang,
                label="Language",
                show_label=False,
            )
        # https://www.gradio.app/guides/controlling-layout#rows
        with gr.Row():
            with gr.Column():
                instructions_drop = gr.Dropdown(
                    choices=list(prompts[default_lang].keys()),
                    value=default_instruction,
                    label="Instructions",
                    show_label=False,
                )
                instruction_box = gr.Textbox(value = default_instruction , label="instruction - use {payload} {result} placeholders")
                payload_box = gr.Textbox(label="Payload - {payload}")
                result_box = gr.Textbox(label="Result - {result}")
                generate_btn = gr.Button("Generate")

        # match button - function
        lang_drop.change(
            fn=changelang,
            inputs=[lang_drop],
            outputs=[instructions_drop],
            api_name="changelang",
        )
        instructions_drop.change(
            fn=changeinstruction,
            inputs=[lang_drop, instructions_drop],
            outputs=[instruction_box],
            api_name="changeinstruction",
        )
        generate_btn.click(
            fn=generate,
            inputs=[
                instruction_box,
                payload_box,
                result_box,
            ],
            outputs=result_box,
            api_name="generate",
        )

    return myapp


if __name__ == "__main__":
    engine = engine_ollama()
    buildapp(engine, prompts).launch()
