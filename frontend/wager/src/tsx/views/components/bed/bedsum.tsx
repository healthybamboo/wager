import * as React from 'react';
import {
    Typography,
    Box,
    Fab,
    Grid,

} from '@mui/material';
import AddIcon from '@mui/icons-material/Add';


const BedSum = (props: { sum: number }) => {
    const date = "2022年11月9日"
    const sum = props.sum;
    return (
        <Grid container justifyContent={"right"} sx={{flexGrow:1}}>
            <Grid item  sx={{mr:2}}>
                {sum > 0 ?
                    <Typography variant="h5" color="#00CA69" component="h1" sx={{ mb: 1,}}>
                        {sum}
                    </Typography> :
                    <Typography variant="h5" color="#FF0000" component="h1" sx={{ mb: 2,}}>
                        {sum}
                    </Typography>
                }
            </Grid>
        </Grid>


    )
}

export default BedSum;
