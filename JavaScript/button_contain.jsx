import { useState } from "react";
import React from "react";
function ButtonContain() {
    const [info, setinfo] = useState("aashish")
    return(
        <>
        <div>
            <H1>Info of student in separated tab</H1>
            <div>
                <button onClick={() => setinfo('aashish')}>Aashish</button>
                <button onClick={() => setinfo('veer')}>veer</button>
                <button onClick={() => setinfo('moru')}>moru</button>
                <button onClick={() => setinfo('jayesh')}>jayesh</button>
            </div>
            {(info === 'aashish') && <div> Aashish is a student of 3rd year</div>}
            {(info === 'veer') && <div> Veer is a student of 2nd year</div>}
            {(info === 'moru') && <div> Moru is a student of 1st year</div>}
            {(info === 'jayesh') && <div> Jayesh is a student of 4th year</div>}
        </div>
        </>
    )
}