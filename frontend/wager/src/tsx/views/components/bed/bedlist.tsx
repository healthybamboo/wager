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

// 収支の一覧
type BedListProps = {
    beds: TBed[]
}

const BedList = (props:BedListProps) => {
    return (
            <Stack sx={{ maxWidth: 500 }}>
                {/* 親子ポーネンとから収支の一覧を取得して、すべて取り出して表示する */}
                {props.beds.map((bed: TBed) => { return (<BedRow{...bed} />) })}
            </Stack>
    )
}

export default BedList;

