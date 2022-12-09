import * as React from 'react';
import {
    Typography,
    Box,
    Fab,

} from '@mui/material';
import AddIcon from '@mui/icons-material/Add';


const BedHeader = (props: { date:string, handleOpen: () => void }) => {
    const date = props.date
    return (
        <Box sx={{ display: 'flex', alignItems: 'center', mb: 3 ,minWidth:500}}>
            <Typography variant="h5" component="h1" sx={{ mb: 3, flexGrow: 1 }}>
                {date}
            </Typography>

            <Box sx={{ '& > :not(style)': { m: 1 } }}>
                <Fab color="inherit" aria-label="add" onClick={() => props.handleOpen()}>
                    <AddIcon />
                </Fab>
            </Box>

        </Box>


    )
}

export default BedHeader;
