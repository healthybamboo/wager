import React, { useState } from "react";
import BedList from '../components/bed/bedlist';
import BasicModal from "../components/bed/modals/addmodal";
import BedHeader from "../components/bed/bedheader";
import BedSum from '../components/bed/bedsum';

import { Card, Grid, TextField, Button, Typography } from '@mui/material'

import { createTheme, ThemeProvider } from '@mui/material/styles';
import { CssBaseline, Container, Box } from '@mui/material';

import { useAppDispatch, useAppSelector } from '../../redux/hooks';

import { getBedAsync } from "../../redux/slices/bedSlice";
import { TBed, TGetRequest } from "../../utils/types";

import { useForm } from 'react-hook-form'

import { selectToken } from "../../redux/slices/userSlice";
import { selectStatus, selectBeds } from "../../redux/slices/bedSlice";

import { useEffect } from "react";
import { request } from "http";

/*
日付、
タグ、
ワードなどで検索して、データを絞ることができる。
その中でのデータ数を表示する。
TODO.ページネーションを追加する。
*/

const theme = createTheme();
const Beds = () => {
    const dispatch = useAppDispatch();

    const { register, handleSubmit } = useForm<TBed>();


    const [date, setDate] = useState(localStorage.getItem('date'));

    const token = useAppSelector(selectToken);
    const status = useAppSelector(selectStatus);
    const beds = useAppSelector(selectBeds);

    /* ページが読み込まれた時に一回だけ処理される */
    useEffect(() => {
        const item = localStorage.getItem('date');
        if (item !== null) {
            const date = new Date(item);
            const year = date.getFullYear();
            const month = date.getMonth() + 1;
            const day = date.getDate();
            setDate(year.toString() + "/" + month.toString() + "/" + day.toString());

            const request: TGetRequest = {
                year: year,
                month: month,
                day: day,
            }
            dispatch(getBedAsync(request));
        }
        console.log("ロードページ");
    }, []);

    /* 送信された時の処理 */
    const onSubmit = (data: any) => {
        const date = new Date(data.date);
        localStorage.setItem('date', data.date);
        const year = date.getFullYear();
        const month = date.getMonth() + 1;
        const day = date.getDate();
        setDate(year.toString() + "/" + month.toString() + "/" + day.toString());

        const request: TGetRequest = {
            year: year,
            month: month,
            day: day,
        }

        dispatch(getBedAsync(request));
        console.log(beds);
    }

    const [open, setOpen] = React.useState(false);
    const handleOpen = () => setOpen(true);
    const handleClose = () => setOpen(false);

    let sum = 0;
    for (let i = 0; i < beds.length; i++) {
        sum += (-beds[i].spend + beds[i].refund);
    }

    return (
        <ThemeProvider theme={theme}>
            <Container component="main" maxWidth="xs">
                <CssBaseline />

                <Box
                    sx={{
                        marginTop: 8,
                        display: 'flex',
                        flexDirection: 'column',
                        alignItems: 'center',
                    }}
                >

                    <TextField
                        id="name"
                        label="日付"
                        type="date"
                        sx={{ width: 220 }}
                        InputLabelProps={{
                            shrink: true,
                        }}
                        defaultValue={localStorage.getItem('date')}
                        {...register('date')}

                    />
                    <Button onClick={handleSubmit(onSubmit)} color={"inherit"} sx={{ bgcolor: "#DDD", mt: 3 }} >検索</Button>
                    {
                        status === "rejected" ? <Typography color="error">取得に失敗しました。</Typography> : null
                    }
                    <Grid >
                        <Card sx={{ m: 5, p: 2 }}>
                            <BedHeader date={date} handleOpen={handleOpen} />
                            {
                                beds.length > 0 ? <BedSum sum={sum} /> : null

                            }
                            <BedList beds={beds} />
                            <BasicModal open={open} handleClose={handleClose} />
                        </Card>
                    </Grid>
                </Box>
            </Container>
        </ThemeProvider>
    )
}

export default Beds;