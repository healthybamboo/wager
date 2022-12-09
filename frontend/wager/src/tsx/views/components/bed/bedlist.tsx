import {
    Card,
    Avatar,
    Box,
    Button,
    Checkbox,
    FormControlLabel,
    Grid,
    Link,
    Paper,
    TextField,
    CardContent,
    Stack,
    Typography, Container
} from "@mui/material";

import BedRow from "./bedrow";
import { TBed } from "../../../utils/types";
import React from "react";
import { maxWidth } from "@mui/system";


// import AddButton from "./addbutton"

type BedListProps = {
    beds: TBed[]
}

const BedList = (props:BedListProps) => {

    const date = "2021年10月01"
    return (
            <Stack sx={{ maxWidth: 500 }}>
                {props.beds.map((bed: TBed) => { return (<BedRow{...bed} />) })}
            </Stack>
    )
}

export default BedList;

