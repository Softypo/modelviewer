# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class ModelViewer(Component):
    """A ModelViewer component.
ExampleComponent is an example component.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.

Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- alt (string; required):
    The src displayed in the input.

- exposure (string; required):
    The src displayed in the input.

- label (string; required):
    A label that will be printed when this component is rendered.

- src (string; required):
    The src displayed in the input.

- style (dict; optional):
    The src displayed in the input."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'modelviewer'
    _type = 'ModelViewer'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, label=Component.REQUIRED, src=Component.REQUIRED, alt=Component.REQUIRED, exposure=Component.REQUIRED, style=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'alt', 'exposure', 'label', 'src', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'alt', 'exposure', 'label', 'src', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['alt', 'exposure', 'label', 'src']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(ModelViewer, self).__init__(**args)
