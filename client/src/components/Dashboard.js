import React, { useState } from 'react';

import { Stack, Typography, Paper } from "@mui/material";
import Button1 from './Button';
import Modal from './Modal';
import InterpolationForm from '../formComponents/InterpolationForm';
import IntegrationForm from '../formComponents/IntegrationForm';
import RootForm from '../formComponents/RootForm';
import NewtonRaphsonForm from '../formComponents/NewtonRaphsonForm';

const Dashboard = ({ onClick, output, className = '' }) => {

    const [isOpenInterpolation, setIsOpenInterpolation] = useState(false);
    const [isOpenIntegration, setIsOpenIntegration] = useState(false);
    const [isRoot, setIsRoot] = useState(false);
    const [isNewton, setIsNewton] = useState(false);
    const [action, setAction] = useState("");
    // const [formComponent, setFormComponent] = useState(InterpolationForm);
    // ===== Example Data =====

    const exampleJacobi = {
        coefficients: [
            [10.0, 2.0, -1.0],
            [-3.0, -6.0, 2.0],
            [1.0, 1.0, 5.0],
        ],
        constants: [27.0, -61.5, -21.5],
        tolerance: 1e-5,
        initial_guess: [0, 0, 0],
    };

    const exampleCondition = [
        [10.0, 2.0, -1.0],
        [-3.0, -6.0, 2.0],
        [1.0, 1.0, 5.0],
    ];


    return (
        <div style={{ padding: "2rem", fontFamily: "Arial, sans-serif" }}>
            <Typography variant="h4" gutterBottom>
                🧮 Python Library via FastAPI
            </Typography>

            {isOpenInterpolation && (<Modal isOpen={isOpenInterpolation} onClose={() => setIsOpenInterpolation(false) } onCalculate={(data) => onClick(action, data)} FormComponent={InterpolationForm}></Modal>)}
            {isOpenIntegration && (<Modal isOpen={isOpenIntegration} onClose={() => setIsOpenIntegration(false) } onCalculate={(data) => onClick(action, data)} FormComponent={IntegrationForm}></Modal>)}
            {isRoot && (<Modal isOpen={isRoot} onClose={() => setIsRoot(false) } onCalculate={(data) => onClick(action, data)} FormComponent={RootForm}></Modal>)}
            {isNewton && (<Modal isOpen={isNewton} onClose={() => setIsNewton(false) } onCalculate={(data) => onClick(action, data)} FormComponent={NewtonRaphsonForm}></Modal>)}

            <Stack spacing={2} direction="row" flexWrap="wrap">
                <Button1 label={"Jacobi"} onClick={() => onClick("jacobi", exampleJacobi, "iterations")} />
                <Button1 label={"Gauss-Seidel"} onClick={() => onClick("gauss_seidel", exampleJacobi, "iterations")}>

                </Button1>
                <Button1 label={"Condition Number"} onClick={() => onClick("condition_number", exampleCondition, "condition_number")}>

                </Button1>
                <Button1 label={"Newton-Raphson"} onClick={() => {
                    setAction("newton_raphson");
                    setIsNewton(true);
                }} />
                <Button1 label={"Bisection"} onClick={() => {
                    setAction("bisection");
                    setIsRoot(true);
                }} />
                <Button1 label={"Secant"} onClick={() => {
                    setAction("secant");
                    setIsRoot(true);
                }} />
                <Button1 label={"Romberg Integration"} onClick={() => {
                    setAction("romberg");
                    setIsOpenIntegration(true);
                }} />
                <Button1 label={"Simpson's Rule"} onClick={() => {
                    setAction("simpsons");
                    setIsOpenIntegration(true);
                }} />
                <Button1 label={"Trapezoidal Rule"} onClick={() => {
                    setAction("trapezoidal");
                    setIsOpenIntegration(true);
                }} />
                <Button1 label={"Linear Interpolation"} onClick={() => {
                    setAction("linear_interpolation");
                    setIsOpenInterpolation(true);
                }} />
                <Button1 label={"Polynomial Interpolation"} onClick={() => {
                    setAction("polynomial_interpolation");
                    setIsOpenInterpolation(true);    
                }} />
                <Button1 label={"Lagrange Interpolation"} onClick={() => {
                    setAction("lagrange");
                    setIsOpenInterpolation(true);    
                }} />
                <Button1 label={"Neville's Interpolation"} onClick={() => {
                    setAction("neville");
                    setIsOpenInterpolation(true);    
                }} />
                <Button1 label={"Cubic Spline"} onClick={() => {
                    setAction("cubic_spline");
                    setIsOpenInterpolation(true);    
                }} />
            </Stack>

            <Paper elevation={3} style={{ marginTop: "2rem", padding: "1rem", whiteSpace: "pre-wrap" }}>
                <Typography variant="h6">Result:</Typography>
                <Typography variant="body1">{output}</Typography>
            </Paper>
        </div>
    );
};


export default Dashboard;