import asyncio
from nicegui import ui


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



ui.button('Compute', on_click=compute)

ui.separator()
with ui.expansion('Expand!', icon='work').classes('w-full'):
    ui.label('Processing options')

ui.run()