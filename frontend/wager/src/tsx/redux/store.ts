import { configureStore, ThunkAction, Action } from '@reduxjs/toolkit';
import userReducer from './slices/userSlice';
import bedReducer from './slices/bedSlice';
import gameReducer from './slices/gameSlice'

export const store = configureStore({
  reducer: {
    // ユーザー関連の状態管理
    user: userReducer,
    // 収支記録の状態管理
    bed : bedReducer,
    // ゲームの状態管理
    game : gameReducer,
  },
});

export type AppDispatch = typeof store.dispatch;
export type RootState = ReturnType<typeof store.getState>;
export type AppThunk<ReturnType = void> = ThunkAction<
  ReturnType,
  RootState,
  unknown,
  Action<string>
  >;