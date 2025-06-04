import gradio as gr

def handle_input(text):
    return text

with gr.Blocks() as demo:
    text_input = gr.Textbox(label="문자입력", lines=1)  # 문자입력칸에 입력한 문자는 text_input에 저장됨/Textbox라는 메서드는 글자를 쓸 수 있는 칸을 만들어줌
    output_text = gr.Textbox(label="출력")
    text_input.submit(handle_input, inputs=text_input, outputs=output_text) # handle_input에 의해 인풋 데이터를 아웃풋 데이터로 사용 가능

demo.launch()