import gradio as gr  

def handle_checkbox(selected):
    if selected:
        return "동의했습니다"
    return "동의하지 않았습니다"

with gr.Blocks() as demo:
    checkbox = gr.Checkbox(label="개인정보 사용에 동의하겠습니까?") #label은 제목
    output_checkbox = gr.Textbox(label='출력')
    checkbox.change(handle_checkbox, inputs = checkbox, outputs=output_checkbox) # change: 인풋이 변경될 떄마다 handle_checkbox를 콜백함

demo.launch()