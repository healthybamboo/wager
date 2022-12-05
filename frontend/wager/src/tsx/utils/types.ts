
export type TUser = {
    id: number;
    name: string;
    email: string;
    last_login: string;
    token: string;
}

export type LoginForm = {
    username: string;
    password: string;
}


export type User = {
    id: number | null;
    name: string | null;
    token: string | null;
    status : string | null;
}

export type TBed = {
    id : number;
    amount : number;
    name : string;
    date : string;
    category : string;
    memo : string;
}