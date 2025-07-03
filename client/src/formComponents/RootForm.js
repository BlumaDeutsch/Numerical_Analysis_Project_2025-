import React, { useState } from 'react';

const RootForm = ({ calculate = () => { } }) => {
    const [func, setFunc] = useState("");
    const [x0, setx0] = useState();
    const [x1, setx1] = useState();
    const [tol, setTol] = useState(1e-5);
    const [max_iter, setMax_iter] = useState(100);


    const handleCalculate = () => {

        calculate({
            func: func, 
            x0: parseFloat(x0),
            x1: parseFloat(x1),
            tol: parseFloat(tol),
            max_iter: parseInt(max_iter)  
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
            <div style={{ display: 'flex', gap: '10px', alignItems: 'center',margin: '10px 0px' }}>
                <input
                
                    style={{ width: '60px' }}
                    type="number"
                    placeholder={`x0`}
                    value={x0}
                    onChange={(e) => setx0(e.target.value)}
                />
                <input
                    style={{ width: '60px' }}
                    type="number"
                    placeholder={`x1`}
                    value={x1}
                    onChange={(e) => setx1(e.target.value)}
                />

            </div>
            <div style={{ display: 'flex', gap: '10px', alignItems: 'center', margin: '10px 0px' }}>
                <input
                    style={{ width: '60px' }}
                    type="number"
                    placeholder={`tolerance`}
                    value={tol}
                    onChange={(e) => setTol(e.target.value)}
                />
                <input
                    style={{ width: '60px' }}
                    type="number"
                    placeholder={`max_iter`}
                    value={max_iter}
                    onChange={(e) => setMax_iter(e.target.value)}
                />

            </div>
            <button onClick={handleCalculate}>Calculate</button>
        </div>
    );
};

export default RootForm;