# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Modelviewer(Component):
    """A Modelviewer component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The children of this component.

- id (string; required):
    The ID used to identify this component in Dash callbacks.

- alt (string; optional):
    Configures the model with custom text that will be used to
    describe the model to viewers who use a screen reader or otherwise
    depend on additional semantic context to understand what they are
    viewing.

- animation_crossfade_duration (number; optional):
    When the current animation is changed, <model-viewer>
    automatically crossfades between the previous and next animations.
    This attribute controls how long the crossfade is in milliseconds.

- animation_name (string; optional):
    Selects an animation to play by name. This animation will play
    when the .play() method is invoked, or when the <model-viewer> is
    configured to autoplay. If no animation-name is specified,
    <model-viewer> always picks the first animation it finds in the
    model.

- ar (boolean; optional):
    Enable the ability to launch AR experiences on supported devices.

- ar_modes (a value equal to: "webxr", "scene-viewer", "quick-look"; optional):
    A prioritized list of the types of AR experiences to enable.
    Allowed values are \"webxr\", to launch the AR experience in the
    browser, \"scene-viewer\", to launch the Scene Viewer app,
    \"quick-look\", to launch the iOS Quick Look app. You can specify
    any number of modes separated by whitespace. Including quick-look
    here without an ios-src (our default) will generate a USDZ on the
    fly rather than downloading a separate ios-src file.

- ar_placement (a value equal to: "floor", "wall"; optional):
    Selects whether to place the object on the floor (horizontal
    surface) or a wall (vertical surface) in AR. The back (negative Z)
    of the object's bounding box will be placed against the wall and
    the shadow will be put on this surface as well. Note that the
    different AR modes handle the placement UX differently.

- ar_scale (a value equal to: "auto", "fixed"; optional):
    Controls the scaling behavior in AR mode. Set to \"fixed\" to
    disable scaling of the model, which sets it to always be at 100%
    scale. Defaults to \"auto\" which allows the model to be resized
    by pinch.

- ar_status (a value equal to: "N/A", "not-presenting", "session-started", "object-placed", "failed"; optional):
    This read-only attribute enables DOM content to be styled based on
    the status of the WebXR AR presentation. For instance, a prompt
    for the user to move their phone until the object is successfully
    placed in their space can be shown by scoping a CSS rule to
    model-viewer[ar-status=\"session-started\"]. Setting this
    attribute has no effect.

- ar_tracking (a value equal to: "N/A", "tracking", "not-tracking"; optional):
    This read-only attribute enables DOM content to be styled based on
    the state of the WebXR AR tracking. For instance, a failure
    message can be shown by scoping a CSS rule to
    model-viewer[ar-tracking=\"not-tracking\"]. Setting this attribute
    has no effect. Most AR tracking failures are due to the camera
    being covered or seeing little discernable texture.

- auto_rotate (boolean; optional):
    Enables the auto-rotation of the model.

- auto_rotate_delay (number; optional):
    Sets the delay before auto-rotation begins. The format of the
    value is a number in milliseconds.

- autoplay (boolean; optional):
    If this is True and a model has animations, an animation will
    automatically begin to play when this attribute is set (or when
    the property is set to True). If no animation-name is specified,
    plays the first animation.

- camera_controls (string; optional):
    Enables controls via mouse/touch. This attribute should nearly
    always be specified, unless all model motion is being controlled
    by JavaScript functions.

- camera_orbit (string; optional):
    Set the starting and/or subsequent orbital position of the camera.
    You can control the azimuthal, theta, and polar, phi, angles (phi
    is measured down from the top), and the radius from the center of
    the model. Accepts values of the form \"$theta $phi $radius\",
    like \"10deg 75deg 1.5m\". Also supports units in radians
    (\"rad\") for angles and centimeters (\"cm\") or millimeters
    (\"mm\") for camera distance. Camera distance can also be set as a
    percentage ('%'), where 100% gives the model tight framing within
    any window based on all possible theta and phi values. Any time
    this value changes from its initially configured value, the camera
    will interpolate from its current position to the new value. Any
    value set to 'auto' will revert to the default. For camera-orbit,
    camera-target and field-of-view, parts of the property value can
    be configured with CSS-like functions. The CSS calc() function is
    supported for these values, as well as a specialized form of the
    env() function. You can use env(window-scroll-y) anywhere in the
    expression to get a number from 0-1 that corresponds to the
    current top-level scroll position of the current frame. For
    example, a value like \"calc(30deg - env(window-scroll-y) * 60deg)
    75deg 1.5m\" cause the camera to orbit horizontally around the
    model as the user scrolls down the page.

- camera_target (string; optional):
    Set the starting and/or subsequent point the camera orbits around.
    Accepts values of the form \"$X $Y $Z\", like \"0m 1.5m -0.5m\".
    Also supports units in centimeters (\"cm\") or millimeters
    (\"mm\"). A special value \"auto\" can be used, which sets the
    target to the center of the model's bounding box in that
    dimension. Any time this value changes from its initially
    configured value, the camera will interpolate from its current
    position to the new value.

- disable_pan (boolean; optional):
    Disables panning interactions, which are enabled by default using
    two-finger touch, or dragging with right-click or modifier keys.

- disable_tap (boolean; optional):
    Disables tap-to-recenter behavior (both center-the-tapped-point
    and reset-view-when-tapping-outside). This attribute has no effect
    in combination with 'disable-pan', as the tap-to-recenter behavior
    is part of the panning interactions. It is recommended to create
    custom re-centering behavior when using 'disable-tap' as after
    panning and rotating, it is effectively impossible for the user to
    exactly return to their starting view.

- disable_zoom (boolean; optional):
    Disables user zoom when camera-controls is enabled (has no effect
    otherwise). Has the secondary effect of not swallowing mouse wheel
    events and pinch gestures, so these will then scroll and zoom the
    page, respectively.

- environment_image (string; optional):
    Controls the environmental reflection of the model. Normally if
    skybox-image is set, that image will also be used for the
    environment-image. Use environment-image to only set the
    reflection without affecting the background. If neither is
    specified, default neutral lighting will be applied. If 'legacy'
    is specified without a skybox, then our old default environment is
    applied instead.

- exposure (number; optional):
    Controls the exposure of both the model and skybox, for use
    primarily with HDR environments.

- field_of_view (string; optional):
    Used to configure the vertical field of view of the camera.
    Accepts values in both degrees and radians (e.g., \"30deg\" or
    \"0.5rad\"). Accepts any value between the configured min and max
    field of view. Any time this value changes from its initially
    configured value, the camera will interpolate from its current
    value to the new value. Defaults to \"auto\", which sets either
    the vertical or horizontal field of view to 45 degrees depending
    on the dimensions of the model and the aspect ratio of the canvas.

- interaction_prompt (a value equal to: "auto", "none"; optional):
    Allows you to disable the visual and audible interaction prompt.
    If set to \"auto\", the interaction prompt will be displayed as
    soon as the interaction-prompt-threshold (see below) time has
    elapsed (after the model is revealed). The interaction prompt will
    only display if camera-controls are enabled.

- interaction_prompt_style (a value equal to: "wiggle", "basic"; optional):
    Configures the presentation style of the interaction-prompt when
    it is raised. When set to \"wiggle\", the prompt will animate
    horizontally and the model will rotate as though the prompt is
    interacting with it. When set to \"basic\", the prompt is not
    animated, and instead simply appears until it is dismissed by user
    interaction.

- interaction_prompt_threshold (number; optional):
    When camera-controls are enabled, <model-viewer> will prompt the
    user visually (and audibly, for screen readers) to interact if
    they focus it but don't interact with it for some time. This
    attribute allows you to set how long <model-viewer> should wait
    (in milliseconds) before prompting to interact. Defaults to 3000.

- interpolation_decay (number; optional):
    Controls the rate of interpolation when the camera or model moves,
    due to either user interaction or attribute changes. The decay is
    asymptotic and the value is in milliseconds, where the majority of
    the movement will occur within this value's time. Doubling this
    value will cut the speed in half.

- ios_src (string; optional):
    The url to a USDZ model which will be used on supported iOS 12+
    devices via AR Quick Look on Safari. The presence of this
    attribute will automatically enable the quick-look ar-mode,
    however it is no longer necessary. If instead the quick-look
    ar-mode is specified and ios-src is not specified (the default),
    then we will generate a USDZ on the fly when the AR button is
    pressed. This means modifications via the scene-graph API will now
    be reflected in Quick Look. However, USDZ generation is not
    perfect, for instance animations are not yet supported, so in some
    cases supplying ios-src may give better results.

- loading (a value equal to: "auto", "lazy", "eager"; optional):
    An enumerable attribute describing under what conditions the model
    should be preloaded. The supported values are \"auto\", \"lazy\"
    and \"eager\". Auto is equivalent to lazy, which loads the model
    when it is near the viewport for reveal=\"auto\", and when
    interacted with for reveal=\"interaction\". Eager loads the model
    immediately.

- max_camera_orbit (string; optional):
    Set the maximum orbital values of the camera. Takes values in the
    same form as camera-orbit, but does not support env(). Note
    \"Infinity\" is not an accepted keyword, but the default can still
    be obtained by passing \"auto\". The radius value for \"auto\" is
    the same as the camera-orbit radius \"auto\" value.

- max_field_of_view (string; optional):
    Set the maximum field of view of the camera, corresponding to
    maximum zoom-out. Takes values in the same form as field-of-view,
    but does not support env(). The default \"auto\" is the same as
    the default field-of-view.

- min_camera_orbit (string; optional):
    Set the minimum orbital values of the camera. Note \"Infinity\" is
    not an accepted keyword, but the default can still be obtained by
    passing \"auto\". The radius value for \"auto\" is a conservative
    value to ensure the camera never enters the model, so be careful
    when setting this to another value.

- min_field_of_view (string; optional):
    Set the minimum field of view of the camera, corresponding to
    maximum zoom-in. Takes values in the same form as field-of-view,
    but does not support env(). Set this to a small value to get close
    zoom-in without the camera entering the model.

- orbit_sensitivity (number; optional):
    Adjusts the speed of theta and phi orbit interactions. Can also be
    set negative to reverse, which is helpful when using zero radius
    to look around the inside of a cave-like model. Default: 1.

- orientation (string; optional):
    Rotates the model to the orientation specified by roll, pitch, yaw
    Euler angles, where yaw is first applied about the Y-axis, then
    pitch about the new local X-axis (positive is front-down), then
    roll about the new local Z-axis. If specified before the model
    loads, automatic camera framing will take this change into
    account; otherwise the updateFraming() method must be called
    manually.

- pan_sensitivity (number; optional):
    Adjusts the speed of pan interactions.

- poster (string; optional):
    Displays an image instead of the model, useful for showing the
    user something before a model is loaded and ready to render.

- reveal (a value equal to: "auto", "manual"; optional):
    This attribute controls when the model should be revealed. If
    reveal is set to \"auto\", the model will be revealed as soon as
    it is done loading and rendering. If reveal is set to \"manual\",
    the model will remain hidden until dismissPoster() is called.

- rotation_per_second (string; optional):
    Sets the speed of auto-rotate, when enabled. Accepts values with
    units in degrees or radians (e.g., \"30deg\" or \"0.5rad\"), as
    well as percent (e.g. \"-100%\") of the default value of pi/32
    radians.

- scale (string; optional):
    Scales the model as specified in the X, Y, and Z directions. Scale
    is applied before orientation. If specified before the model
    loads, automatic camera framing will take this change into
    account; otherwise the updateFraming() method must be called
    manually.

- shadow_intensity (number; optional):
    Controls the opacity of the shadow. Set to 0 to turn off the
    shadow entirely.

- shadow_softness (number; optional):
    Controls the blurriness of the shadow. Set to 0 for hard shadows.
    Softness should not be changed every frame as it incurs a
    performance cost. Softer shadows render faster.

- skybox_image (string; optional):
    Sets the background image of the scene. Takes a URL to an
    equirectangular projection image that's used for the skybox, as
    well as applied as an environment map on the model. Supports png,
    jpg and hdr (recommended) images.

- src (string; required):
    The URL to the 3D model. Only glTF/GLB models are supported.

- style (dict; optional):
    The src displayed in the input.

- touch_action (a value equal to: "pan-y", "pan-x", "none"; optional):
    Akin to the CSS touch-action property (which does not work due to
    some iOS bugs), the default 'pan-y' allows touch users to
    vertically scroll the <model-viewer> element, but can interact if
    their gesture starts horizontal. Legacy behavior can be achieved
    with 'none', where all scrolling is prevented, while 'pan-x' is
    the opposite of 'pan-y'. The normal CSS default 'auto' is not
    allowed here, as this can be achieved by not including the
    camera-controls attribute. Default: \"pan-y\".

- variant_name (string; optional):
    Selects a model variant by name.

- with_credentials (boolean; optional):
    This attribute makes the browser include credentials (cookies,
    authorization headers or TLS client certificates) in the request
    to fetch the 3D model. It's useful if the 3D model file is stored
    on another server that require authentication. By default the file
    will be fetch without credentials. Note that this has no effect if
    you are loading files locally or from the same domain.

- xr_environment (boolean; optional):
    Enables AR lighting estimation in WebXR mode; this has a
    performance cost and replaces the lighting selected with
    environment-image during an AR session. Known issues: sometimes
    too dark, sudden updates, shiny materials look matte.

- zoom_sensitivity (number; optional):
    Adjusts the speed of zoom interactions."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'modelviewer'
    _type = 'Modelviewer'
    @_explicitize_args
    def __init__(self, children=None, id=Component.REQUIRED, src=Component.REQUIRED, alt=Component.UNDEFINED, poster=Component.UNDEFINED, loading=Component.UNDEFINED, reveal=Component.UNDEFINED, with_credentials=Component.UNDEFINED, camera_controls=Component.UNDEFINED, disable_pan=Component.UNDEFINED, disable_tap=Component.UNDEFINED, touch_action=Component.UNDEFINED, disable_zoom=Component.UNDEFINED, orbit_sensitivity=Component.UNDEFINED, zoom_sensitivity=Component.UNDEFINED, pan_sensitivity=Component.UNDEFINED, auto_rotate=Component.UNDEFINED, auto_rotate_delay=Component.UNDEFINED, rotation_per_second=Component.UNDEFINED, interaction_prompt=Component.UNDEFINED, interaction_prompt_style=Component.UNDEFINED, interaction_prompt_threshold=Component.UNDEFINED, camera_orbit=Component.UNDEFINED, camera_target=Component.UNDEFINED, field_of_view=Component.UNDEFINED, max_camera_orbit=Component.UNDEFINED, min_camera_orbit=Component.UNDEFINED, max_field_of_view=Component.UNDEFINED, min_field_of_view=Component.UNDEFINED, interpolation_decay=Component.UNDEFINED, skybox_image=Component.UNDEFINED, environment_image=Component.UNDEFINED, exposure=Component.UNDEFINED, shadow_intensity=Component.UNDEFINED, shadow_softness=Component.UNDEFINED, animation_name=Component.UNDEFINED, animation_crossfade_duration=Component.UNDEFINED, autoplay=Component.UNDEFINED, variant_name=Component.UNDEFINED, orientation=Component.UNDEFINED, scale=Component.UNDEFINED, ar=Component.UNDEFINED, ar_modes=Component.UNDEFINED, ar_scale=Component.UNDEFINED, ar_placement=Component.UNDEFINED, ios_src=Component.UNDEFINED, xr_environment=Component.UNDEFINED, ar_status=Component.UNDEFINED, ar_tracking=Component.UNDEFINED, style=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'alt', 'animation_crossfade_duration', 'animation_name', 'ar', 'ar_modes', 'ar_placement', 'ar_scale', 'ar_status', 'ar_tracking', 'auto_rotate', 'auto_rotate_delay', 'autoplay', 'camera_controls', 'camera_orbit', 'camera_target', 'disable_pan', 'disable_tap', 'disable_zoom', 'environment_image', 'exposure', 'field_of_view', 'interaction_prompt', 'interaction_prompt_style', 'interaction_prompt_threshold', 'interpolation_decay', 'ios_src', 'loading', 'max_camera_orbit', 'max_field_of_view', 'min_camera_orbit', 'min_field_of_view', 'orbit_sensitivity', 'orientation', 'pan_sensitivity', 'poster', 'reveal', 'rotation_per_second', 'scale', 'shadow_intensity', 'shadow_softness', 'skybox_image', 'src', 'style', 'touch_action', 'variant_name', 'with_credentials', 'xr_environment', 'zoom_sensitivity']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'alt', 'animation_crossfade_duration', 'animation_name', 'ar', 'ar_modes', 'ar_placement', 'ar_scale', 'ar_status', 'ar_tracking', 'auto_rotate', 'auto_rotate_delay', 'autoplay', 'camera_controls', 'camera_orbit', 'camera_target', 'disable_pan', 'disable_tap', 'disable_zoom', 'environment_image', 'exposure', 'field_of_view', 'interaction_prompt', 'interaction_prompt_style', 'interaction_prompt_threshold', 'interpolation_decay', 'ios_src', 'loading', 'max_camera_orbit', 'max_field_of_view', 'min_camera_orbit', 'min_field_of_view', 'orbit_sensitivity', 'orientation', 'pan_sensitivity', 'poster', 'reveal', 'rotation_per_second', 'scale', 'shadow_intensity', 'shadow_softness', 'skybox_image', 'src', 'style', 'touch_action', 'variant_name', 'with_credentials', 'xr_environment', 'zoom_sensitivity']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['id', 'src']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(Modelviewer, self).__init__(children=children, **args)
