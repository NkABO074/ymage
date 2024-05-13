import asyncio
from nicegui import ui

ui.add_css('''
    .w-64 {
        border-radius:10px;
    }
    .title {
        font-size:40px;
        font-weight:bold;
    }
    .header{
        width:100%;
        border-radius:10px;
        background-color:rgba(0, 10, 200,.5);
        padding: 5px;
        color:white;
    }
''')

async def compute():
    n = ui.notification(timeout=None)
    for i in range(10):
        n.message = f'Computing {i/10:.0%}'
        n.spinner = True
        await asyncio.sleep(10)
    n.message = 'Done!'
    n.spinner = False
    await asyncio.sleep(1)
    n.dismiss()

with ui.row().classes('header'):
    ui.label('Ymage').classes("title")
    ui.space()
    ui.label(" ")
    
ui.separator()

ui.button('Compute', on_click=compute)

ui.separator()
with ui.expansion('Scaling option', icon='work').classes('w-full'):
    ui.label("Image Scaling factor:")
    ui.radio(['x2', 'x4', 'x8'], value='x').props('inline color=blue')
    

ui.separator()    
with ui.link(target='https://github.com/zauberzeug/nicegui'):
    img = ui.image('https://picsum.photos/640/360').classes('w-64')


ui.run()