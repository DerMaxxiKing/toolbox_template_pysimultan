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
        ui.label(self.component.attr1)

        ui.label('attr2:')
        ui.label(self.component.attr2)

        ui.label('attr3:')
        ui.label(self.component.attr3)


view_manager.views['class1'] = Class1DetailView
