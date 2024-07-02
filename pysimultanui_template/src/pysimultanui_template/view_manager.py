from pysimultanui import ViewManager
from pysimultanui.views.component_detail_base_view import ComponentDetailBaseView
from nicegui import ui

view_manager = ViewManager()


class Class1DetailView(ComponentDetailBaseView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @ui.refreshable
    def ui_content(self, *args, **kwargs):
        super().ui_content(*args, **kwargs)

        ui.label('attr1:')
        ui.input('attr1:').bind_value(self.component,
                                                  target_name='attr1',
                                                  forward=lambda x: float(x),
                                                  backward=lambda x: str(x))

        ui.label('attr2:')
        ui.input('attr2:').bind_value(self.component,
                                                  target_name='attr2',
                                                  forward=lambda x: float(x),
                                                  backward=lambda x: str(x))

        ui.label('attr3:')
        ui.label(self.component.attr3)


view_manager.views['class1'] = Class1DetailView
