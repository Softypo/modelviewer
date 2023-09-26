# AUTO GENERATED FILE - DO NOT EDIT

#' @export
''ModelViewer <- function(id=NULL, alt=NULL, exposure=NULL, label=NULL, src=NULL, style=NULL) {
    
    props <- list(id=id, alt=alt, exposure=exposure, label=label, src=src, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'ModelViewer',
        namespace = 'modelviewer',
        propNames = c('id', 'alt', 'exposure', 'label', 'src', 'style'),
        package = 'modelviewer'
        )

    structure(component, class = c('dash_component', 'list'))
}
