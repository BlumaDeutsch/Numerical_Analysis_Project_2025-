import React, { useEffect, useState } from 'react';

const Modal = ({ isOpen, onClose, onCalculate, FormComponent }) => {

    if (!isOpen) return null;

    const handleCalculate = (data) => {

        onCalculate(data);
        onClose()
    };


    return (
        <div style={styles.overlay}>
            <div style={styles.modal}>
                <button style={styles.closeButton} onClick={onClose}>
                    &times;
                </button>
                <h2>Enter Values</h2>
                
                {FormComponent && <FormComponent calculate={handleCalculate} />}
            </div>
        </div>
    );
};

const styles = {
    overlay: {
        position: 'fixed',
        top: 0,
        left: 0,
        width: '100%',
        height: '100%',
        backgroundColor: 'rgba(0, 0, 0, 0.5)',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
    },
    modal: {
        backgroundColor: '#fff',
        padding: '20px',
        borderRadius: '8px',
        width: '300px',
        position: 'relative',
    },
    closeButton: {
        position: 'absolute',
        top: '10px',
        right: '10px',
        background: 'none',
        border: 'none',
        fontSize: '20px',
        cursor: 'pointer',
    },
};

export default Modal;
