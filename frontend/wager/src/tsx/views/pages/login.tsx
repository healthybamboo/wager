
import { useForm, SubmitHandler } from "react-hook-form";
import {
    Avatar,
    Box,
    Button,
    Checkbox,
    FormControlLabel,
    Grid,
    Link,
    Paper,
    TextField,
    Typography
} from "@mui/material";

import LockOutlinedIcon from "@mui/icons-material/LockOutlined";
import { teal } from "@mui/material/colors";
import { PropaneSharp } from "@mui/icons-material";
import { redirect,Navigate} from "react-router-dom";

import { LoginForm } from "../../utils/types";

import { loginAsync, selectUserName, selectPassword, selectToken, selectLoginStatus } from '../../redux/slices/userSlice'
import { useAppDispatch, useAppSelector } from '../../redux/hooks';
import { stat } from "fs";
import { color } from "@mui/system";


const Login = () => {
    const dispatch = useAppDispatch()

    const { register, handleSubmit, reset } = useForm<LoginForm>();

    const loginStatus = useAppSelector(selectLoginStatus)

    const token = useAppSelector(selectToken)
    // フォーム送信時の処理
    const onSubmit: SubmitHandler<LoginForm> = (data) => {
        dispatch(loginAsync(data));
    }



    return (
        <Grid>
            <Paper
                elevation={3}
                sx={{
                    p: 4,
                    height: "70vh",
                    width: "300px",
                    m: "20px auto"
                }}
            >
                <Grid
                    container
                    direction="column"
                    justifyContent="flex-start" //多分、デフォルトflex-startなので省略できる。
                    alignItems="center"
                >
                    <Avatar sx={{ bgcolor: teal[400] }}>
                        <LockOutlinedIcon />
                    </Avatar>
                    <Typography variant={"h5"} sx={{ m: "30px" }}>
                        ログイン
                    </Typography>
                    {
                        loginStatus === "success" ? <Navigate to="/home" /> : 
                        <Typography variant={'inherit'}  color="error" sx={{ m: "30px" } }>
                            ログインに失敗しました。
                        </Typography>

                    }

                </Grid>

                {/* ユーザー名を入力するためのフォーム */}
                <TextField label="Username" variant="standard" fullWidth required  {...register('username')} />

                {/* パスワードを入力するためのフォーム */}
                <TextField
                    type="password"
                    label="Password"
                    variant="standard"
                    fullWidth
                    required
                    {...register('password')}
                />

                <Box mt={3}>

                    {/* ログインボタン */}
                    <Button type="submit" color="primary" variant="contained" onClick={handleSubmit(onSubmit)} fullWidth >
                        サインイン
                    </Button>

                    {/* パスワードを忘れた場合のリンク　TODO.リンクを追加する */}
                    <Typography variant="caption">
                        <Link href="#">パスワードを忘れましたか？</Link>
                    </Typography>

                    {/* アカウントを作成するページ */}
                    <Typography variant="caption" display="block">
                        アカウントを持っていますか？
                        <Link href="signup">アカウントを作成</Link>
                    </Typography>
                </Box>
            </Paper>
        </Grid>
    );
};

export default Login;