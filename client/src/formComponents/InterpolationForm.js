import React, { useState } from 'react';

const InterpolationForm = ({ calculate = () => {} }) => {
    const [points, setPoints] = useState([]);
    const [xValue, setXValue] = useState('');

    const addPoint = () => {
        setPoints([...points, { x: '', y: '' }]);
    };

    const handlePointChange = (index, field, value) => {
        const updatedPoints = [...points];
        updatedPoints[index][field] = value;
        setPoints(updatedPoints);
    };

    const orderData = (points, xValue) => {
        const x_vals = points.map(point => point.x);
        const y_vals = points.map(point => point.y);
        const newData = {
            x_vals: x_vals,
            y_vals: y_vals,
            x: xValue
        }
        return newData;

    }

    const handleCalculate = () => {
        
        calculate(orderData(points, xValue));
    };

    return (
        <div>
            <button style={{ margin: '10px 0px' }} onClick={addPoint}>Add a Point</button>
            <div style={{ display: 'flex', flexWrap: 'wrap', gap: '10px' }}>
                {points.map((point, index) => (
                    <div key={index} style={{ display: 'flex', gap: '10px', alignItems: 'center' }}>
                        <input
                            style={{ width: '60px' }}
                            type="number"
                            placeholder={`x${index}`}
                            value={point.x}
                            onChange={(e) => handlePointChange(index, 'x', e.target.value)}
                        />
                        <input
                            style={{ width: '60px' }}
                            type="number"
                            placeholder={`y${index}`}
                            value={point.y}
                            onChange={(e) => handlePointChange(index, 'y', e.target.value)}
                        />
                    </div>
                ))}
            </div>
            <div>
                <input
                    style={{ margin: '10px 0px' }}
                    type="number"
                    placeholder="x value"
                    value={xValue}
                    onChange={(e) => setXValue(e.target.value)}
                />
            </div>
            <button onClick={handleCalculate}>Calculate</button>
        </div>
    );
};

export default InterpolationForm;