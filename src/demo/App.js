/* eslint no-magic-numbers: 0 */
import React, { useState } from 'react';

import { Modelviewer } from '../lib';

const App = () => {

    const [state, setState] = useState({
        id: 'Type Here',
        src: 'assets/M08.glb',
        alt: "A rock",
        exposure: "0.008",
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
