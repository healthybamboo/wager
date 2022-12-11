import * as React from 'react';
import {
    Typography,
    Box,
    Fab,
    Grid,

} from '@mui/material';
import AddIcon from '@mui/icons-material/Add';

// 収支の合計部分
const BedSum = (props: { sum: number }) => {

    const sum = props.sum;
    return (
        <Grid container justifyContent={"right"} sx={{ flexGrow: 1 }}>
            <Grid item sx={{ mr: 2 }}>
                {
                    // 収支の合計が０より大きければ緑、０以下であれば赤色で表示する
                    sum > 0 ?
                        <Typography variant="h5" color="#00CA69" component="h1" sx={{ mb: 1, }}>
                            {sum}
                        </Typography> :
                        <Typography variant="h5" color="#FF0000" component="h1" sx={{ mb: 2, }}>
                            {sum}
                        </Typography>
                }
            </Grid>
        </Grid>


    )
}

export default BedSum;
