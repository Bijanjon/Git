import dearpygui.dearpygui as dpg

if __name__ == "__main__":
    dpg.create_context()
    dpg.create_viewport(title='Custom', width=1000, height=620)
    def realtime(sender):
        sender_value = dpg.get_item_label(sender)
        if not sender_value:
            sender_value = "None"
        print(F"{sender_value}:{dpg.get_value(sender)}")


    with dpg.window(tag="Window", label="Windows", pos=(0, 0)) as window:
        buttonCheck = dpg.add_button(label='CheckButton', callback=realtime)

        sliderInt = dpg.add_slider_int(label='To left', width=100)
        sliderFloat = dpg.add_slider_float(label='To right', width=100)
        print(f"Printing item tag: {window},  {sliderInt},  {sliderFloat},  {buttonCheck}")

    button=dpg.add_button(label='Forgot', parent=window)

    # with dpg.window(tag="Windw", label="Window", pos=(100, 0)):
    #     pass
    dpg.show_item_registry()
    dpg.setup_dearpygui()
    dpg.show_viewport()
    # dpg.set_primary_window("Window", True)
    dpg.start_dearpygui()
    dpg.destroy_context()
