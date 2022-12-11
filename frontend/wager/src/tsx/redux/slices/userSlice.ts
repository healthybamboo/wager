import { createAsyncThunk, createSlice, PayloadAction } from '@reduxjs/toolkit';
import { RootState } from '../store';
import axios, { AxiosRequestConfig } from 'axios';

import {TUser,TSignupForm,TSigninForm} from '../../utils/types';

// stateの初期値
const initialState: TUser = {
    id: null,
    name: null,
    token: null,
    status: ''
}

// ログイン用の非同期処理
export const signinAsync = createAsyncThunk(
    'user/signin',
    async (user: TSigninForm, { rejectWithValue }) => {
        const config = {
            headers: {
                "Content-Type": "application/json",
            }
        }
        try {
            const result = await axios.post('/api/user/login/', {
                "username": user.username, "password": user.password
            },
            );
            return result.data;
        } catch (error: any) {
            if (!error.response) {
                throw error;
            }
            return rejectWithValue(error.response.data);
        } finally {
        }
    },
);

//　アカウント作成用の非同期処理
export const signupAsync = createAsyncThunk(
    'user/signup',
    async (user: TSignupForm, { rejectWithValue }) => {
        const config = {
            headers: {
                "Content-Type": "application/json",
                // CSRF　TOKENの取得処理
                "X-CSRFToken": "csrftoken"
            }
        }
        try {
            const result = await axios.post('/api/user/signup/', {
                "username": user.username, "password": user.password, "email": user.email
            },
            );
            return result.data;
        } catch (error: any) {
            if (!error.response) {
                throw error;
            }
            return rejectWithValue(error.response.data);
        } finally {
        }
    },
);

// ユーザー情報のstateを管理する
export const userSlice = createSlice({
    name: 'user',
    initialState,
    reducers: {
    },
    extraReducers: (builder) => {
        builder
            .addCase(signinAsync.fulfilled, (state, action) => {
                state.id = action.payload.id;
                state.name = action.payload.name;
                state.token =  action.payload.token;
                localStorage.setItem('token',action.payload.token);
                state.status = 'success';
            })
            .addCase(signinAsync.pending, (state, action) => {
                state.status = 'loading';
            })
            .addCase(signinAsync.rejected, (state, action) => {
                state.status = 'rejected';
            })
        builder
            .addCase(signupAsync.fulfilled, (state, action) => {
                state.id = action.payload.id;
                state.name = action.payload.name;
                state.token =  action.payload.token;
                state.status = 'success';
            })
            .addCase(signupAsync.pending, (state, action) => {
                state.status = 'loading';
            })
            .addCase(signupAsync.rejected, (state, action) => {
                state.status = 'rejected';
            })
    },
});

export const selectUserName = (state: RootState) => state.user.name;
export const selectPassword = (state: RootState) => state.user.token;
export const selectToken = (state: RootState) => state.user.token;
export const selectUserStatus = (state: RootState) => state.user.status;

export default userSlice.reducer;