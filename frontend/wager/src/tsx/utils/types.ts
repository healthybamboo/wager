export type TSigninForm = {
    username: string;
    password: string;
}

export type TSignupForm = {
    username: string;
    password: string;
    email: string;
}

export type TUser = {
    id: number | null;
    name: string | null;
    token: string | null;
    status: string | null;
}

export type TBed = {
    id: number,
    name: string
    tag:number
    date: string
    spend: number
    refund: number
    memo: string
}

export type TGame = {
    name: string;
    way: number;
    unit: number;
    state: string;
    archive: boolean;
}


export type TAuthedGetRequest = {
    token: string;
    year: number;
    month: number;
    day: number;
}