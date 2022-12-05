import React from "react";
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
    Typography
} from "@mui/material";

import { TBed } from "../../utils/types";
import { maxWidth } from "@mui/system";

// 収支カード
const BedCard = (props: TBed) => {
    return (
        <Card sx={{ minWidth: 275, margin:3}}>
            <CardContent>
                <Stack direction={"row"} spacing="30px">
                    <Typography sx={{ mb: 1.5 }} color="text.secondary">
                        {props.date}
                    </Typography>
                    <Typography >
                        {props.name}
                    </Typography>
                    <Typography >
                        {props.memo}
                    </Typography>
                    {props.amount > 0 ?
                        <Typography color="#00CA69">{props.amount}</Typography>
                        : <Typography color="#FF0000">{props.amount}</Typography>}
                </Stack>
            </CardContent>
        </Card>
    )
}

export default BedCard;