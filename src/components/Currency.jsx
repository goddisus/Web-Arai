import React from 'react';
import { ProSidebar, Menu, MenuItem, SubMenu } from 'react-pro-sidebar';
import 'react-pro-sidebar/dist/css/styles.css';
import { FaGem, FaHeart, FaCat, FaCheese, FaChessKing } from "react-icons/fa";
import '../css/currency.css'
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link
  } from "react-router-dom";
function Currency() {
    return (
        <div className="mainbody">
            <div className="firbody">
                <ProSidebar>
                    <Menu iconShape="circle">
                        <SubMenu title="United State" icon={<FaHeart />}>
                            <a href="/eieiza/dowjones">
                                <MenuItem>
                                    DowJones
                                </MenuItem>
                            </a>
                            <MenuItem>S&P 500</MenuItem>
                            <MenuItem>Nasdaq</MenuItem>
                            <MenuItem>Small Cap 2000</MenuItem>
                            <MenuItem>S&P 500 VIX</MenuItem>
                        </SubMenu>
                        <SubMenu title="United Kingdom" icon={<FaGem />}>
                            <MenuItem>FTSE 100</MenuItem>
                        </SubMenu>
                        <SubMenu title="Russia" icon={<FaCat />}>
                            <MenuItem>MOEX</MenuItem>
                            <MenuItem>RTSI</MenuItem>
                        </SubMenu>
                        <SubMenu title="China" icon={<FaCheese />}>
                            <MenuItem>Shanghai</MenuItem>
                            <MenuItem>SZSE Component</MenuItem>
                            <MenuItem>China A50</MenuItem>
                            <MenuItem>DJ Shanghai</MenuItem>
                        </SubMenu>
                        <SubMenu title="Thai" icon={<FaChessKing />}>
                            <MenuItem>SET</MenuItem>
                        </SubMenu>
                        <div style={{visibility:"hidden"}}>
                            <SubMenu style={{display:"hidden"}} title="Thai" icon={<FaChessKing />}>
                                <MenuItem>SET</MenuItem>
                            </SubMenu>
                        </div>
                        
                    </Menu>
                </ProSidebar>
            </div>
            <div className="secbody">
                <div className="ff">
                    <div className="hello">
                        hello
                    </div>
                    <div className="eiei">
                        EIEI
                        eewrweg
                        weg
                        weg
                        effffffffffffffffffffffffffff
                    </div>
                    <div className="hihi">
                        HIHI
                    </div>
                </div>
            </div>
            
        </div>
    );
}

export default Currency;