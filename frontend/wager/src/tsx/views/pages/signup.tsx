import * as React from 'react';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import Link from '@mui/material/Link';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import { createTheme, ThemeProvider } from '@mui/material/styles';


import { signupAsync, selectUserName, selectPassword, selectToken, selectUserStatus } from '../../redux/slices/userSlice'
import { useAppDispatch, useAppSelector } from '../../redux/hooks';

import { Navigate } from "react-router-dom";

import { useForm } from 'react-hook-form'

import { TSignupForm } from '../../utils/types';

const theme = createTheme();

// アカウント作成ページ
export default function SignUp() {
  const dispatch = useAppDispatch();

  //  フォームの設定
  const { register, handleSubmit, reset } = useForm<TSignupForm>();

  // ログイン状況
  const status = useAppSelector(selectUserStatus);

  const token = useAppSelector(selectToken);

  // 入力情報の送信
  const onSubmit = (data: TSignupForm) => {
    console.log(data);
    dispatch(signupAsync(data));
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
          <Avatar sx={{ m: 1, bgcolor: '#000' }}>
            <LockOutlinedIcon />
          </Avatar>
          <Typography component="h1" variant="h5">
            アカウントを作成
          </Typography>
          {
            // アカウントの作成に失敗した場合はエラーを表示し、成功した場合は収支一覧ページにリダイレクト
            status === 'rejected' ? <Typography component="p" variant="inherit" color="error">アカウントの作成に失敗しました</Typography> :
            status === 'success' ?  <Navigate to="/bed" /> : null
          }
          <Box component="form" noValidate sx={{ mt: 3 ,mb:5}}>
            <Grid container spacing={2}>
              <Grid item xs={12}>
                {/* ユーザー名の入力フィールド */}
                <TextField
                  required
                  fullWidth
                  id="User Name"
                  label="ユーザー名"
                  {...register("username")}
                />
              </Grid>
              <Grid item xs={12}>
                {/* メールアドレスの入力フィールド */}
                <TextField
                  required
                  fullWidth
                  id="email"
                  label="メールアドレス"
                  {...register("email")}
                />
              </Grid>
              <Grid item xs={12}>
                {/* パスワードの入力フィールド */}
                <TextField
                  required
                  fullWidth
                  label="パスワード"
                  type="password"
                  id="password"
                  {...register("password")}
                />
              </Grid>
              <Grid item xs={12}>
                {/* 利用規約に同意するかどうか */}
                <FormControlLabel
                  control={<Checkbox value="allowExtraEmails" color="primary" />}
                  label="利用規約に同意します。"
                />
              </Grid>
            </Grid>
            {/* アカウント作成ボタン */}
            <Button
              type="submit"
              fullWidth
              variant="contained"
              color="inherit"
              onClick={handleSubmit(onSubmit)}
              sx={{ mt: 3, mb: 2 }}
            >
              アカウントを作成
            </Button>
            <Grid container justifyContent="flex-end">
              <Grid item>
                {/* ログイン画面へのリンク */}
                <Link href="/signin" variant="body2">
                  既にアカウントをお持ちの方はこちら
                </Link>
              </Grid>
            </Grid>
          </Box>
        </Box>
      </Container>
    </ThemeProvider>
  );
}