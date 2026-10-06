import flet as ft

def main(page: ft.Page):
    page.title = "Exemplo de contador de frota"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Campo de texto do contador
    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    # Função para diminuir 1
    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    # Função para aumentar 1
    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    # Adiciona a linha com os botões e o número na página
    page.add(
        ft.Row(
            [
                ft.IconButton(ft.Icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.Icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

# Inicializa a aplicação
ft.run(main)