# AUTO GENERATED FILE - DO NOT EDIT

export ''_modelviewer

"""
    ''_modelviewer(;kwargs...)

A ModelViewer component.
ExampleComponent is an example component.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.
Keyword arguments:
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `alt` (String; required): The src displayed in the input.
- `exposure` (String; required): The src displayed in the input.
- `label` (String; required): A label that will be printed when this component is rendered.
- `src` (String; required): The src displayed in the input.
- `style` (Dict; optional): The src displayed in the input.
"""
function ''_modelviewer(; kwargs...)
        available_props = Symbol[:id, :alt, :exposure, :label, :src, :style]
        wild_props = Symbol[]
        return Component("''_modelviewer", "ModelViewer", "modelviewer", available_props, wild_props; kwargs...)
end

