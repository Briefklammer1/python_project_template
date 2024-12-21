from shiny import App, ui, render, reactive

app_ui = ui.page_fluid(
    ui.h1("Simple Submit Example - Hot Reload Test"),
    ui.input_text("name", "What's your name?", ""),
    ui.input_action_button("submit", "Click me!", class_="btn-primary"),
    ui.output_text("txt")
)

def server(input, output, session):
    # Create a reactive value to store the message
    message = reactive.Value("Please click the button")
    
    @reactive.Effect
    @reactive.event(input.submit)
    def _():
        message.set(f"Hello, {input.name()}! Welcome to the app 2.0!")
    
    @output
    @render.text
    def txt():
        return message.get()

app = App(app_ui, server, debug=True)

if __name__ == "__main__":
    app.run(port=8080)
