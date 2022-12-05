import React from "react";
import { redirect,Navigate} from "react-router-dom";

import { loginAsync, selectUserName, selectPassword, selectToken, selectLoginStatus } from '../../redux/slices/userSlice'

const Top = () => {
    
    return (
        <div>
            <h1>Top</h1>
        </div>
    )
}

export default Top;