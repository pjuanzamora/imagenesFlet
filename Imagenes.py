import flet as ft

def main(page: ft.Page):
    page.title = "Images Example"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 50
    page.update()


    nombreFruta = ""

    def dropdown_changed(e):
        if (dd.value == "Fresa"):
            nombreFruta = "fresa.jpeg"
            print(f"fresa al poder {nombreFruta}")
        elif (dd.value == "Platano"):
            nombreFruta = "platano.jpeg"
            print("platano al poder")
        else:
            nombreFruta = "https://loremflickr.com/640/360"
            print("gatito al poder")

        page.update()

    dd = ft.Dropdown(
        width=100,
        options=[
            ft.dropdown.Option("Fresa"),
            ft.dropdown.Option("Platano"),
            ft.dropdown.Option("Gatito"),
        ],
        on_change=dropdown_changed
    )

    page.add(dd)

    

    img = ft.Image(
        src=f"imagenes/{nombreFruta}"
        #width=20,
        #height=30
    )

    page.add(img)
    
'''
    img2 = ft.Image(
        src=f"imagenes/platano.jpeg"
        #width=100,
        #height=100,
    )

    img3 = ft.Image(
        src=f"https://loremflickr.com/640/360"
        #width=100,
        #height=100,
    )
    
'''
   


ft.app(target=main, assets_dir="recursos")