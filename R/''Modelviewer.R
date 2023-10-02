# AUTO GENERATED FILE - DO NOT EDIT

#' @export
''Modelviewer <- function(children=NULL, id=NULL, alt=NULL, animation_crossfade_duration=NULL, animation_name=NULL, ar=NULL, ar_modes=NULL, ar_placement=NULL, ar_scale=NULL, ar_status=NULL, ar_tracking=NULL, auto_rotate=NULL, auto_rotate_delay=NULL, autoplay=NULL, camera_controls=NULL, camera_orbit=NULL, camera_target=NULL, disable_pan=NULL, disable_tap=NULL, disable_zoom=NULL, environment_image=NULL, exposure=NULL, field_of_view=NULL, interaction_prompt=NULL, interaction_prompt_style=NULL, interaction_prompt_threshold=NULL, interpolation_decay=NULL, ios_src=NULL, loading=NULL, max_camera_orbit=NULL, max_field_of_view=NULL, min_camera_orbit=NULL, min_field_of_view=NULL, orbit_sensitivity=NULL, orientation=NULL, pan_sensitivity=NULL, poster=NULL, reveal=NULL, rotation_per_second=NULL, scale=NULL, shadow_intensity=NULL, shadow_softness=NULL, skybox_image=NULL, src=NULL, style=NULL, touch_action=NULL, variant_name=NULL, with_credentials=NULL, xr_environment=NULL, zoom_sensitivity=NULL) {
    
    props <- list(children=children, id=id, alt=alt, animation_crossfade_duration=animation_crossfade_duration, animation_name=animation_name, ar=ar, ar_modes=ar_modes, ar_placement=ar_placement, ar_scale=ar_scale, ar_status=ar_status, ar_tracking=ar_tracking, auto_rotate=auto_rotate, auto_rotate_delay=auto_rotate_delay, autoplay=autoplay, camera_controls=camera_controls, camera_orbit=camera_orbit, camera_target=camera_target, disable_pan=disable_pan, disable_tap=disable_tap, disable_zoom=disable_zoom, environment_image=environment_image, exposure=exposure, field_of_view=field_of_view, interaction_prompt=interaction_prompt, interaction_prompt_style=interaction_prompt_style, interaction_prompt_threshold=interaction_prompt_threshold, interpolation_decay=interpolation_decay, ios_src=ios_src, loading=loading, max_camera_orbit=max_camera_orbit, max_field_of_view=max_field_of_view, min_camera_orbit=min_camera_orbit, min_field_of_view=min_field_of_view, orbit_sensitivity=orbit_sensitivity, orientation=orientation, pan_sensitivity=pan_sensitivity, poster=poster, reveal=reveal, rotation_per_second=rotation_per_second, scale=scale, shadow_intensity=shadow_intensity, shadow_softness=shadow_softness, skybox_image=skybox_image, src=src, style=style, touch_action=touch_action, variant_name=variant_name, with_credentials=with_credentials, xr_environment=xr_environment, zoom_sensitivity=zoom_sensitivity)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Modelviewer',
        namespace = 'modelviewer',
        propNames = c('children', 'id', 'alt', 'animation_crossfade_duration', 'animation_name', 'ar', 'ar_modes', 'ar_placement', 'ar_scale', 'ar_status', 'ar_tracking', 'auto_rotate', 'auto_rotate_delay', 'autoplay', 'camera_controls', 'camera_orbit', 'camera_target', 'disable_pan', 'disable_tap', 'disable_zoom', 'environment_image', 'exposure', 'field_of_view', 'interaction_prompt', 'interaction_prompt_style', 'interaction_prompt_threshold', 'interpolation_decay', 'ios_src', 'loading', 'max_camera_orbit', 'max_field_of_view', 'min_camera_orbit', 'min_field_of_view', 'orbit_sensitivity', 'orientation', 'pan_sensitivity', 'poster', 'reveal', 'rotation_per_second', 'scale', 'shadow_intensity', 'shadow_softness', 'skybox_image', 'src', 'style', 'touch_action', 'variant_name', 'with_credentials', 'xr_environment', 'zoom_sensitivity'),
        package = 'modelviewer'
        )

    structure(component, class = c('dash_component', 'list'))
}
