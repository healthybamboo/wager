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

import { useForm } from 'react-hook-form'
import { redirect,Navigate} from "react-router-dom";

import { signinAsync, selectUserName, selectPassword, selectToken,selectUserStatus } from '../../redux/slices/userSlice'
import { useAppDispatch, useAppSelector } from '../../redux/hooks';
import { TSigninForm,TSignupForm } from '../../utils/types';

const theme = createTheme();

export default function SignIn() {
  const dispatch = useAppDispatch();

  const { register, handleSubmit, reset } = useForm<TSigninForm>();

  const status = useAppSelector(selectUserStatus);

  const token = useAppSelector(selectToken);


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
            status === 'rejected' ? <Typography component="p" variant="inherit" color="error">ログインに失敗しました</Typography> :
            status === 'success' ?  <Navigate to="/bed" /> : null
          }
          <Box component="form" noValidate sx={{ mt: 1, mb: 5 }}>
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
              <Link href="#" variant="body2">
                パスワードを忘れましたか？
              </Link>
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