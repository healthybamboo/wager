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

import { selectStatus, selectBeds } from "../../redux/slices/bedSlice";

import { useEffect } from "react";

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

    // 日付を入力するためのフォーム
    const { register, handleSubmit } = useForm<TBed>();

    // 日付を設定するためのステータス
    const [date, setDate] = useState(localStorage.getItem('date'));

    // 収支の取得状況のステータス
    const status = useAppSelector(selectStatus);

    // 収支一覧
    const beds = useAppSelector(selectBeds);

    // ページが読み込まれた時に一回だけ処理される 
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
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, []);

    // 検索ボタンがクリックされた場合の処理
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

    // モーダルが開いているかどうかのステータス
    const [open, setOpen] = React.useState(false);
    // モーダルが開く時のイベントハンドラー
    const handleOpen = () => setOpen(true);
    // モーダルを閉じた時のイベントハンドラー
    const handleClose = () => setOpen(false);

    // 収支の合計値を計算
    let sum = 0;
    for (let i = 0; i < beds.length; i++) {
        // spendの値は、プラスならば収支上はマイナスである
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
                    <Grid container sx={{ mb: 4, flexGrow: 1 }}>
                        <Grid item flexGrow={1}>
                            <Button href="/bed">収支</Button>
                        </Grid>
                        <Grid item>
                            <Button href="/game">ゲーム</Button>
                        </Grid>

                    </Grid>
                    {/* 日付を選択するためのフィールド */}
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
                    {/* フォームで詮索した日付の収支を取得するボタン */}
                    <Button onClick={handleSubmit(onSubmit)} color={"inherit"} sx={{ bgcolor: "#DDD", mt: 3 }} >検索</Button>
                    {
                        status === "rejected" ? <Typography color="error">取得に失敗しました。</Typography> : null
                    }
                    <Grid >
                        <Card sx={{ m: 5, p: 2 }}>
                            {/* 収支一覧のヘッダ部分 */}
                            <BedHeader date={date} handleOpen={handleOpen} />
                            {
                                beds.length > 0 ? <BedSum sum={sum} /> : null

                            }
                            {/* 収支一覧 */}
                            <BedList beds={beds} />
                            {/* 収支を登録するためのモーダル */}
                            <BasicModal open={open} handleClose={handleClose} />
                        </Card>
                    </Grid>
                </Box>
            </Container>
        </ThemeProvider>
    )
}

export default Beds;