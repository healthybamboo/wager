import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';
import { RootState } from '../store';
import axios from 'axios';


import { TBed, TBedForm, TGetRequest } from '../../utils/types';



export const getBedAsync = createAsyncThunk(
    'bed/get',
    async (request: TGetRequest, { rejectWithValue }) => {
        const token = localStorage.getItem('token');
        if (!token) {
            // TODO.ここにログイン画面へのリダイレクト処理を追加したい
            console.log('nothing token');
            return
        }
        const config = {
            headers: {
                "Authorization": "jwt " + token,
                "Content-Type": "application/json",
            },
            params: {
                "year": request.year,
                "month": request.month,
                "day": request.day,
            }
        }
        try {
            const result = await axios.get('/api/beds/', config);
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

export const postBedAsync = createAsyncThunk(
    'bed/post',
    async (form: TBedForm, { rejectWithValue }) => {
        const token = localStorage.getItem('token');
        if (!token) {
            // TODO.ここにログイン画面へのリダイレクト処理を追加したい
            console.log('nothing token');
            return
        }

        const headers = {
            "Authorization": "jwt " + token,
            "Content-Type": "application/json",
        }
        const data = {
            "date": form.date,
            "name": form.name,
            "spend": form.spend,
            "refund": form.refund,
            "memo": form.memo,
        }

        try {
            const result = await axios.post('/api/beds/', data, { headers: headers });
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





type TBeds = {
    status: string,
    beds: TBed[]
}

const initialState: TBeds = {
    status: "",
    beds: []
};
export const bedSlice = createSlice({
    name: 'bed',
    initialState,
    reducers: {
    },
    extraReducers: (builder) => {
        builder
            // 取得処理が成功した場合
            .addCase(getBedAsync.fulfilled, (state, action) => {

                state.beds = action.payload.concat()
                state.status = 'success';
            })
            // 取得処理中の場合
            .addCase(getBedAsync.pending, (state, action) => {
                state.status = 'loading';
            })
            // 取得処理が失敗した場合
            .addCase(getBedAsync.rejected, (state, action) => {
                state.status = 'rejected';
            })
            // 追加処理が成功した場合
            .addCase(postBedAsync.fulfilled, (state, action) => {
                state.beds.push(action.payload)
                state.status = 'success';
            })
            // 追加処理中の場合
            .addCase(postBedAsync.pending, (state, action) => {
                state.status = 'loading';
            })
            // 追加処理が失敗した場合
            .addCase(postBedAsync.rejected, (state, action) => {
                state.status = 'rejected';
            })

    },
});

// 
export const selectStatus = (state: RootState) => state.bed.status;
export const selectBeds = (state: RootState) => state.bed.beds;


export default bedSlice.reducer;