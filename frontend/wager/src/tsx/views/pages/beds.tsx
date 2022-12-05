import React from "react";

import { TBed } from "../../utils/types";

import BedCard  from '../components/bed_card';
import BasicModal  from "../components/modal";


const Beds = () => {
    const bed1 : TBed = {
        id: 1,
        name: "お小遣い",
        amount: 1000,
        date: "2021-10-01",
        category: "食費",
        memo: "おにぎり",
    }
    const bed2 : TBed ={
        id: 2,
        name: "中山競馬第２",
        amount: -1200,
        date: "2021-10-02",
        category: "交通費",
        memo: "電車",
    }
    const spends = [ 
        bed1,
        bed2,
    ]
    
    return (
        <React.Fragment>
            {spends.map((spend : TBed) => {return (<BedCard{...spend}/>)})}
            <BasicModal  />
        </React.Fragment>
    )
}

export default Beds;