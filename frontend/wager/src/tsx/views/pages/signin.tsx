import * as React from 'react';
import {
   Avatar ,
   Button ,
   CssBaseline, 
   TextField ,
   Link  ,
   Grid ,
   Box ,
   Typography, 
   Container,
}from '@mui/material';

import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import { createTheme, ThemeProvider } from '@mui/material/styles';

import { useForm } from 'react-hook-form'
import { Navigate} from "react-router-dom";

import { signinAsync,selectUserStatus } from '../../redux/slices/userSlice'
import { useAppDispatch, useAppSelector } from '../../redux/hooks';
import { TSigninForm } from '../../utils/types';

const theme = createTheme();
// ログインにページ
export default function SignIn() {
  
  const dispatch = useAppDispatch();

  const { register, handleSubmit } = useForm<TSigninForm>();
  
  // ログイン状況
  const status = useAppSelector(selectUserStatus);


  // ログインボタンが押された場合の処理
  const onSubmit = (data: any) => {
    dispatch(signinAsync(data));
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
          <Avatar sx={{ m: 1, bgcolor: "#000" }}>
            <LockOutlinedIcon />
          </Avatar>
          <Typography component="h1" variant="h5">
            ログイン
          </Typography>
          {
            // ユーザーにエラーを表示する
            status === 'rejected' ? <Typography component="p" variant="inherit" color="error">ログインに失敗しました</Typography> :
            status === 'success' ?  <Navigate to="/bed" /> : null
          }
          <Box component="form" noValidate sx={{ mt: 1, mb: 5 }}>
            {/* ユーザー名を入力するフィールド　*/}
            <TextField
              margin="normal"
              required
              fullWidth
              id="username"
              label="ユーザー名"
              autoComplete="username"
              autoFocus
              {...register("username")}
            />

            {/* パスワードを入力するフィールド */}
            <TextField
              margin="normal"
              required
              fullWidth
              label="パスワード"
              type="password"
              id="password"
              autoComplete="current-password"
              {...register("password")}
            />
           {/* ログインボタン */}
            <Button
              type="submit"
              fullWidth
              variant="contained"
              color="inherit"
              sx={{ mt: 3, mb: 2 }}
              onClick={handleSubmit(onSubmit)}
            >
              ログイン
            </Button>
            <Grid container>
              {/* TODO. パスワードを忘れたユーザー用のリンクを追加する */}
              <Link href="#" variant="body2">
                パスワードを忘れましたか？
              </Link>
              {/*  アカウントを作成アカウント作成用のリンク　*/}
              <Link href="/signup" variant="body2">
                アカウントをお持ちでない方はこちら
              </Link>
            </Grid>
          </Box>
        </Box>
      </Container>
    </ThemeProvider>
  );
}