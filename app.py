import gradio
def temp(fahrenheit):
    return 9/5*(fahrenheit - 32)

app = gr.Interface(
    fn=temp,
    inputs=gr.Number(label="Temperature In Fahrenheit"),
    outputs=gr.Number(label="Temperature In Celsius"),
)

app.launch(
  server_name="0.0.0.0",
  server_port=int(os.environ.get("PORT",7860))
)
