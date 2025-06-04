import gradio as gr

def handle_fruit(fruit):  # 
    return f'선택한 과일: {fruit}'   # 리턴된 게 outputs로 이동하는데 이때 outputs가 output_fruit를 가리키니까 output_fruit를 통해 출력됨

with gr.Blocks() as demo:
    fruit_dropdown = gr.Dropdown(label="과일", choices=['사과', '오렌지', '바나나', '메론']) # Dropdown메서드: 선택지를 줌
    output_fruit = gr.Textbox(label='구입한 과일')
    fruit_dropdown.change(handle_fruit, inputs=fruit_dropdown, outputs=output_fruit)

demo.launch()