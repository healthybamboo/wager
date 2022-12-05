import { createAsyncThunk, createSlice, PayloadAction } from '@reduxjs/toolkit';
import { RootState } from '../store';
import axios, { AxiosRequestConfig } from 'axios';

import {User,LoginForm} from '../../utils/types';

// stateの初期値
const initialState: User = {
    id: null,
    name: null,
    token: null,
    status: ''
}

// axios.defaults.withCredentials = true; // global に設定してしまう場合

export const loginAsync = createAsyncThunk(
    'user/login',
    async (user: LoginForm, { rejectWithValue }) => {
        const config = {
            headers: {
                "Content-Type": "application/json",
                // "Content-Type": "plain/text",
                // "Access-Control-Allow-Origin": "http://localhost:9000",
                // 'X-CSRFToken': "EpOlXGMo2trFE6ki5gdeZwaEQWM4swHBEF6dvMdzbF4hdeubdeNEbeeuEOweI9t"
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

export const userSlice = createSlice({
    name: 'user',
    initialState,
    reducers: {
    },
    extraReducers: (builder) => {
        builder
            .addCase(loginAsync.fulfilled, (state, action) => {
                state.id = action.payload.id;
                state.name = action.payload.name;
                state.token =  action.payload.token;
                state.status = 'success';
            })
            .addCase(loginAsync.pending, (state, action) => {
                state.status = 'loading';
            })
            .addCase(loginAsync.rejected, (state, action) => {
                state.status = 'rejected';
            })
    },
});

export const selectUserName = (state: RootState) => state.user.name;
export const selectPassword = (state: RootState) => state.user.token;
export const selectToken = (state: RootState) => state.user.token;
export const selectLoginStatus = (state: RootState) => state.user.status;

export default userSlice.reducer;