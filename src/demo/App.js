/* eslint no-magic-numbers: 0 */
import React, { useState } from 'react';

import { Modelviewer } from '../lib';
import { none } from 'ramda';

const App = () => {

    const [state, setState] = useState({
        children: null,
        id: 'Type Here',
        src: 'assets/snes.glb',
        alt: "A rock",
        exposure: 0.5,
        autoplay: true,
        reveal: "auto",
        style: { "width": "100%", "height": "100%" },
    });
    const setProps = (newProps) => {
        setState(newProps);
    };

    return (
        <div>
            <Modelviewer
                setProps={setProps}
                {...state}
            />
        </div>
    )
};


export default App;
