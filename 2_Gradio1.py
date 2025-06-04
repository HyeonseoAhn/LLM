import gradio as gr # 모델의 입력과 출력을 정의하면 gradio가 자동으로 웹기반 인터페이스 실행해줌. 간단한 파이썬 문법만으로도 이용 가능
# Markdown: 글자를 쓸 수 있음
with gr.Blocks() as demo:  # Blocks: 하나의 인터페이스에 블록을 만드는 것
    gr.Markdown("# 안녕하세요")
    gr.Markdown("## 여기는 제목을 입력합니다")
    gr.Markdown("- 첫번째 아이템\n- 두번째 아이템\n- 세번째 아이템")

demo.launch()