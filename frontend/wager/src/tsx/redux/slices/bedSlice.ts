import { createAsyncThunk, createSlice, PayloadAction } from '@reduxjs/toolkit';
import { RootState } from '../store';
import axios, { AxiosRequestConfig } from 'axios';


import {User,TBed,LoginForm} from '../../utils/types';


// const initialState: User = 
// }

// axios.defaults.withCredentials = true; // global に設定してしまう場合

export const fetchBedAsync = createAsyncThunk(
    'bed/pull',
    async (user: User, { rejectWithValue }) => {
        const config = {
            headers: {
                "Authorization": "jwt " + user.token,
                "Content-Type": "application/json",
            }
        }
        try {
            const result = await axios.get('/api/bedlist/',config);
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

const initialState : TBed[] = [];
export const spendSlice = createSlice({
    name: 'bed',
    initialState,
    reducers: {
    },
    extraReducers: (builder) => {
        builder
            .addCase(fetchBedAsync.fulfilled, (state, action) => {
                // state.status = 'success';
            })
            .addCase(fetchBedAsync.pending, (state, action) => {
                // state.status = 'loading';
            })
            .addCase(fetchBedAsync.rejected, (state, action) => {
                // state.status = 'rejected';
            })
    },
});

// export const selectUserName = (state: RootState) => state.user.name;
// export const selectPassword = (state: RootState) => state.user.token;
// export const selectToken = (state: RootState) => state.user.token;
// export const selectLoginStatus = (state: RootState) => state.user.status;

export default spendSlice.reducer;