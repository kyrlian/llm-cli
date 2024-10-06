from dash import Dash, dcc, html, callback, Output, Input
from llm_cli.prompts import prompts
from llm_cli.engines.engine_ollama import Engine

def buildapp(engine, prompts):
    app = Dash()

    def list_models():
        return engine.list()

    @callback(
        Output("result_box", "value"),
        Input("instructions_drop", "value"),
        Input("payload_box", "value"),
        Input("result_box", "value"),
        Input("model_drop", "value"),
        prevent_initial_call = True
    )
    def generate(instructions, payload, result, model=None):
        if "{payload}" in instructions:
            prompt = instructions.format(payload=payload, result=result)
        else:
            prompt = instructions + "\n\n" + payload
        return engine.generate(prompt, model)


    @callback(
        Output("instructions_drop", "options"),
        Output("instruction_box", "value"),
        Input("lang_drop", "value"),
        Input("instructions_drop", "value"),
    )
    def change_lang_or_instruction(lang, instruction):
        return list(prompts[lang].keys()), prompts[lang][instruction]

    default_lang = list(prompts.keys())[0]
    default_instruction = list(prompts[default_lang].keys())[0]
    app.layout = [
        dcc.Dropdown(id="model_drop", options=list_models(), value=list_models()[0]),
        dcc.Dropdown(id="lang_drop", options=list(prompts.keys()), value=default_lang),
        dcc.Dropdown(id="instructions_drop", options=list(prompts[default_lang].keys()),value=default_instruction),
        html.Br(),
        dcc.Textarea(id="instruction_box", value = prompts[default_lang][default_instruction], cols=60, rows=10),
        html.Br(),
        dcc.Textarea(id="payload_box", cols=60, rows=10),
        html.Br(),
        html.Button("Generate", id="generate_btn"),
        html.Br(),
        dcc.Textarea(id="result_box", cols=60, rows=10),
    ]
    return app



def main():
    engine = Engine()
    buildapp(engine,prompts).run(debug=True)

if __name__ == "__main__":
    main()
