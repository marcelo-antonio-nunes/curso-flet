import flet

from flet import IconButton, Page, Row, TextField, icons


def main(page: Page):
    page.title = 'Flet counter'
    page.vertical_alignment = 'center'
    
    txt_number = TextField(value="00", text_align='right', width=80, text_size=40, color='blue600', border_color='red600', border_radius=65)
    
    def minus_click(e):
        if int(txt_number.value) >= 11:
            txt_number.value = str(int(txt_number.value) - 1)
            page.update()
        elif int(txt_number.value) > 0 and int(txt_number.value) <= 10:
            txt_number.value = "0"+str(int(txt_number.value) - 1)
            page.update()
    
    def plus_click(e):
        if int(txt_number.value) >= 9 and int(txt_number.value) <= 98:
            txt_number.value = str(int(txt_number.value) + 1)
            page.update()
        elif int(txt_number.value) <= 8:
            txt_number.value = "0"+str(int(txt_number.value) + 1)
            page.update()
    
    page.add(
        Row(
            [
                IconButton(icons.REMOVE, on_click=minus_click, icon_color="blue400",
                    icon_size=60, ),
                txt_number,
                IconButton(icons.ADD, on_click=plus_click,  icon_color="blue400",
                    icon_size=60,)
                
            ],
            alignment='center'
            
        )
    )
    
flet.app(target=main)