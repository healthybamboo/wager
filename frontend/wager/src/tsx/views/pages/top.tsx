import React from "react";
import { redirect,Navigate} from "react-router-dom";

import {Container, CssBaseline} from "@mui/material";

const Top = () => {
    
    return (
        <Container component="main" maxWidth="xs">
            <CssBaseline />
                <div>
                    <h1>Top</h1>
                </div>
        </Container>
    )
}

export default Top;