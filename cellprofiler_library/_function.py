from napari_plugin_engine import napari_hook_implementation

@napari_hook_implementation
def napari_experimental_provide_dock_widget():
    from .expandorshrinkobjects import shrink_to_point
    return [shrink_to_point]