import gradio as gr
from prompts import prompts
from engine_ollama import engine_ollama

def build_app(engine, prompts):
    def list_engines():
        return engine.list()
    
    def generate(instructions, payload, result, model=None):
        if "{payload}" in instructions: 
            prompt = instructions.format(payload=payload, result=result)
        else:
            prompt = instructions + "\n\n" + payload
        return engine.generate(prompt, model)

    def change_lang(lang, instruction):
        return gr.Dropdown(choices=prompts[lang]), prompts[lang][instruction]

    def change_instruction(lang, instruction):
        return prompts[lang][instruction]

    default_lang = list(prompts.keys())[0]
    default_instruction = list(prompts[default_lang].keys())[0]
    # https://www.gradio.app/guides/blocks-and-event-listeners#blocks-structure
    with gr.Blocks() as myapp:
        with gr.Row():
            gr.Markdown("# LLM Assistant")
            model_drop = gr.Dropdown(
                choices=list_engines(),
                value=list_engines()[0],
                label="Model",
                show_label=False,
            )
            lang_drop = gr.Dropdown(
                choices=list(prompts.keys()),
                value=default_lang,
                label="Language",
                show_label=False,
            )
            instructions_drop = gr.Dropdown(
                choices=list(prompts[default_lang].keys()),
                value=default_instruction,
                label="Instructions",
                show_label=False,
            )
        # https://www.gradio.app/guides/controlling-layout#rows
        with gr.Column():
            instruction_box = gr.Textbox(value = prompts[default_lang][default_instruction] , label="instruction - use {payload} {result} placeholders")
            payload_box = gr.Textbox(label="Payload - {payload}")
            generate_btn = gr.Button("Generate")
            result_box = gr.Textbox(label="Result - {result}")
        # match button - function
        lang_drop.select(
            fn=change_lang,
            inputs=[lang_drop, instructions_drop],
            outputs=[instructions_drop, instruction_box],
            api_name="changelang",
        )
        instructions_drop.select(
            fn=change_instruction,
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
                model_drop,
            ],
            outputs=result_box,
            api_name="generate",
        )
    return myapp


if __name__ == "__main__":
    engine = engine_ollama()
    build_app(engine, prompts).launch()
