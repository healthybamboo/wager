import * as React from 'react';
import { Box, Button, Typography, Modal ,TextField} from '@mui/material';
import { useForm, SubmitHandler } from "react-hook-form";
import { Stack } from '@mui/system';

const style = {
    position: 'absolute' as 'absolute',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    width: 500,
    bgcolor: 'background.paper',
    border: '2px solid #000',
    boxShadow: 24,
    p: 4,
};

export default function BasicModal() {
    const [open, setOpen] = React.useState(false);
    const handleOpen = () => setOpen(true);
    const handleClose = () => setOpen(false);

    return (
        <div>
            <Button onClick={handleOpen}>Open modal</Button>
            <Modal
                open={open}
                onClose={handleClose}
                aria-labelledby="modal-modal-title"
                aria-describedby="modal-modal-description"
            >
                <Box sx={style}>
                        <Typography>
                            名前
                        </Typography>
                        <TextField > </TextField>
                        <Typography > 
                            掛け金
                        </Typography>
                        <TextField > </TextField>
                </Box>
            </Modal>
        </div>
    );
}