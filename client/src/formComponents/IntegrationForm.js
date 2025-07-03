import React, { useState } from 'react';

const IntegrationForm = ({ calculate = () => { } }) => {
    const [func, setFunc] = useState("");
    const [A, setA] = useState();
    const [B, setB] = useState();
    const [n, setn] = useState();


    const handleCalculate = () => {

        calculate({
            func: func, 
            a: parseFloat(A),
            b: parseFloat(B),  
            n: parseInt(n)
        });
    };

    return (
        <div>
            <div>
                <input
                    style={{ margin: '10px 0px' }}
                    type="string"
                    placeholder="Function (e.g., x**2)"
                    value={func}
                    onChange={(e) => setFunc(e.target.value)}
                />
            </div>
            <div style={{ display: 'flex', gap: '10px', alignItems: 'center' }}>
                <input
                    style={{ width: '60px' }}
                    type="number"
                    placeholder={`A`}
                    value={A}
                    onChange={(e) => setA(e.target.value)}
                />
                <input
                    style={{ width: '60px' }}
                    type="number"
                    placeholder={`B`}
                    value={B}
                    onChange={(e) => setB(e.target.value)}
                />

            </div>
            <div>
                <input
                    style={{ margin: '10px 0px' }}
                    type="number"
                    placeholder="n (number of intervals)"
                    value={n}
                    onChange={(e) => setn(e.target.value)}
                />
            </div>
            <button onClick={handleCalculate}>Calculate</button>
        </div>
    );
};

export default IntegrationForm;