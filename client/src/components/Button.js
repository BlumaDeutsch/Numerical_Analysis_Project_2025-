import React from 'react';
import { Button } from "@mui/material";

const Button1 = ({ label, onClick, example, key, type = 'button', className = '' }) => {
    return (
        <button style={{padding: 5, margin: 5}} onClick={onClick}>
            {label}
        </button>
    );
};


export default Button1;