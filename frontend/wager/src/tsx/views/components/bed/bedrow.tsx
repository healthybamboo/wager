import React from "react";
import {
    Card,
    Box,
    CardActionArea,
    Typography
} from "@mui/material";

import { TBed } from "../../../utils/types";

// 収支カード
const BedRow = (props: TBed) => {
    const amount = props.refund - props.spend
    return (
        <Card sx={{ mb: 1 }}>
            <CardActionArea>
                <Box sx={{ m: 0, p: 2, display: 'flex', flexGrow: 1 }} >
                    <Typography sx={{ flexGrow: 1 }} color="#000000" >
                        {props.name}
                    </Typography>
                    {
                        (amount) > 0 ?
                            <Typography color="#00CA69">{amount} </Typography>
                            : <Typography color="#FF0000">{amount}</Typography>}
                </Box>
            </CardActionArea>
        </Card>
    )
}

export default BedRow;