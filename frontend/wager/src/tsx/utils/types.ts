// ログインフォームの型
export type TSigninForm = {
    username: string;
    password: string;
}

// アカウント作成フォームの型
export type TSignupForm = {
    username: string;
    password: string;
    email: string;
}

// ユーザー情報の型
export type TUser = {
    id: number | null;
    name: string | null;
    token: string | null;
    status: string | null;
}

// 収支情報の型
export type TBed = {
    id: number,
    name: string
    tag:number
    date: string
    spend: number
    refund: number
    memo: string
}

// ゲーム情報の型
export type TGame = {
    name: string;
    way: number;
    unit: number;
    state: string;
    archive: boolean;
}

// 収支情報の取得する際のリクエストの型
export type TGetRequest = {
    year: number;
    month: number;
    day: number;
}

// 収支作成用フォームの型
export type TBedForm ={
    date : string;
    name : string;
    spend : number;
    refund : number;
    memo : string;
}