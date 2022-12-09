import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';
import { RootState } from '../store';
import axios  from 'axios';

import { TGame} from '../../utils/types';


// stateの初期値
const initialState = {
    status: "loading",
    games: [],
}

/* (GET)ゲームを取得するための非同期処理*/
export const getGameAsync = createAsyncThunk(
    'game/get',
    async (date: Date, { rejectWithValue }) => {
        // const config = {
        //     headers: {
        //         "Content-Type": "application/json",
        //     },
        // }

        try {
            const result = await axios.get('/api/games/', {
                params: {
                    "year": date.getFullYear(),
                    "month": date.getMonth(),
                    "day": date.getDate()
                }
            });
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

/*　(POST)ゲームを追加するための非同期処理*/
export const postGameAsync = createAsyncThunk(
    'game/post',
    async (game: TGame, { rejectWithValue }) => {
        const config = {
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": "csrftoken"
            }
        }
        try {
            const result = await axios.post('/api/games/', {
                "name": game.name,
                "date": game.way,
                "unit": game.unit,
                "state": game.state,
                "archive": game.archive,
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

/* ゲーム情報のstateを管理する*/
export const gameSlice = createSlice({
    name: 'game',
    initialState,
    reducers: {
    },
    extraReducers: (builder) => {
        builder
            // 取得処理が成功した場合
            .addCase(getGameAsync.fulfilled, (state, action) => {
                state.status = 'success';
            })
            // 取得処理中の場合
            .addCase(getGameAsync.pending, (state, action) => {
                state.status = 'loading';
            })
            // 取得処理が失敗した場合
            .addCase(getGameAsync.rejected, (state, action) => {
                state.status = 'rejected';
            })
            // 追加処理が成功した場合
            .addCase(postGameAsync.fulfilled, (state, action) => {
                state.status = 'success';
            })
            // 追加処理中の場合
            .addCase(postGameAsync.pending, (state, action) => {
                state.status = 'loading';
            })
            // 追加処理が失敗した場合
            .addCase(postGameAsync.rejected, (state, action) => {
                state.status = 'rejected';
            })
    },
});

export const selectStatus = (state: RootState) => state.game.status;
export const selectGames = (state: RootState) => state.game.games;

export default gameSlice.reducer;