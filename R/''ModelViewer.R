# AUTO GENERATED FILE - DO NOT EDIT

#' @export
''Modelviewer <- function(id=NULL, alt=NULL, exposure=NULL, src=NULL, style=NULL) {
    
    props <- list(id=id, alt=alt, exposure=exposure, src=src, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Modelviewer',
        namespace = 'modelviewer',
        propNames = c('id', 'alt', 'exposure', 'src', 'style'),
        package = 'modelviewer'
        )

    structure(component, class = c('dash_component', 'list'))
}
