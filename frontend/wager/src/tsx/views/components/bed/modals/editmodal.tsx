// 編集用のモーダル

import * as React from 'react';
import {
    Box,
    Button,
    Typography,
    Modal,
    Grid,
    TextField,
    Select
} from '@mui/material';


import { useForm, SubmitHandler } from "react-hook-form";
import { Stack } from '@mui/system';

import { TBedForm } from '../../../../utils/types';

import { postBedAsync } from '../../../../redux/slices/bedSlice';
import { useAppDispatch, useAppSelector } from '../../../../redux/hooks';

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


export default function BasicModal(props: { open: boolean, handleClose: () => void }) {
    const dispatch = useAppDispatch();
    const { register, handleSubmit } = useForm<TBedForm>();

    const onSubmit = (data: any) => {
        console.log("SUBMIT");
        props.handleClose();
        const request: TBedForm = {
            date: data.date,
            name: data.name,
            spend: data.spend,
            refund: data.refund,
            memo: data.memo,
        }

        dispatch(postBedAsync(request));
    }

    return (
        <div>
            <Modal
                open={props.open}
                aria-labelledby="modal-modal-title"
                aria-describedby="modal-modal-description"
            >
                <Box sx={style}>
                    <Grid container sx={{ flexGrow: 1 }}>
                        <Grid item sx={{ flexGrow: 1 }}>
                            <Button onClick={() => props.handleClose()} >キャンセル</Button>
                        </Grid>
                        <Grid item>
                            <Button onClick={handleSubmit(onSubmit)} >保存</Button>
                        </Grid>
                    </Grid>
                    <Stack spacing={2}>
                        <TextField
                            id="date"
                            label="日付"
                            type="date"
                            sx={{ width: 220 }}
                            InputLabelProps={{
                                shrink: true,
                            }}
                            {...register('date')}
                        />
                        <TextField
                            id="name"
                            label="名前"
                            type="text"
                            InputLabelProps={{
                                shrink: true,
                            }}
                            {...register('name')}
                        />

                        <TextField
                            id="spend"
                            label="賭け金"
                            type="number"
                            defaultValue="0"
                            InputLabelProps={{
                                shrink: true,
                            }}
                            {...register('spend', {
                                required: {
                                    value: true,
                                    message: '入力が必須の項目です。',
                                }
                            })}
                        > </TextField>
                        <TextField
                            id="spend"
                            label="払戻し"
                            type="number"
                            defaultValue="0"
                            InputLabelProps={{
                                shrink: true,
                            }}
                            required
                            {...register('refund')}
                        > </TextField>

                        <TextField
                            id="memo"
                            label="メモ"
                            variant="outlined"
                            color="primary"
                            margin="none"
                            InputLabelProps={{
                                shrink: true,
                            }}
                            {...register('memo')}
                        />
                    </Stack>
                </Box>
            </Modal>
        </div>
    );
}