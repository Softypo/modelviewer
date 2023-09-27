import React, { useState } from 'react';
import PropTypes from 'prop-types';
import "@google/model-viewer/dist/model-viewer";

/**
 * ExampleComponent is an example component.
 * It takes a property, `label`, and
 * displays it.
 * It renders an input with the property `value`
 * which is editable by the user.
 */
const Modelviewer = (props) => {
    const { id, setProps, src, alt, exposure, style } = props;

    return (
        <model-viewer
            id={id}
            src={src}
            alt={alt}
            exposure={exposure}
            camera-controls
            ar-modes="webxr"
            style={style}
        // onChange={
        //     /*
        //         * Send the new value to the parent component.
        //         * setProps is a prop that is automatically supplied
        //         * by dash's front-end ("dash-renderer").
        //         * In a Dash app, this will update the component's
        //         * props and send the data back to the Python Dash
        //         * app server if a callback uses the modified prop as
        //         * Input or State.
        //         */
        //     e => setProps({ value: e.target.value })
        // }
        />
    );
}

Modelviewer.defaultProps = {};

Modelviewer.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * The src displayed in the input.
    */
    src: PropTypes.string.isRequired,

    /**
     * The src displayed in the input.
    */
    alt: PropTypes.string.isRequired,

    /**
     * The src displayed in the input.
    */
    exposure: PropTypes.string.isRequired,

    /**
     * The src displayed in the input.
    */
    style: PropTypes.object,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default Modelviewer;
