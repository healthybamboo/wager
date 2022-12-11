import React from "react";
import {
    Card,
    Box,
    CardActionArea,
    Typography
} from "@mui/material";

import { TBed } from "../../../utils/types";

// 収支一覧の行部分
const BedRow = (props: TBed) => {
    // 払戻から掛金を引いた値を表示する
    const amount = props.refund - props.spend
    return (
        <Card sx={{ mb: 1 }}>
            <CardActionArea>
                <Box sx={{ m: 0, p: 2, display: 'flex', flexGrow: 1 }} >
                    {/* 収支の名前を表示する */}
                    <Typography sx={{ flexGrow: 1 }} color="#000000" >
                        {props.name}
                    </Typography>
                    {
                        // 収支が０より大きければ緑、収支が０以下であれば赤色で表示する
                        (amount) > 0 ?
                            <Typography color="#00CA69">{amount} </Typography>
                            : <Typography color="#FF0000">{amount}</Typography>
                    }
                </Box>
            </CardActionArea>
        </Card>
    )
}

export default BedRow;