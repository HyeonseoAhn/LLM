import gradio as gr

def add(num1, num2):
    return num1 + num2
# interface: UI를 그려주는 하나의 전체적인 화면. Block은 화면의 부분임
interface = gr.Interface(
    fn=add,   # add라는 함수를 fn이라는 변수에 등록해놓은 것
    inputs = ['number', 'number'],
    outputs = 'number',
    title='계산기',
    description='숫자 두 개를 입력하세요',
    flagging_mode="never"  # flag를 하지 않음 즉, saving이 없어져 .gradio라는 폴더에 입출력 등이 저장되지 않음
)

interface.launch()