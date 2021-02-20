import React from 'react';
import { ProSidebar, Menu, MenuItem, SubMenu } from 'react-pro-sidebar';
import 'react-pro-sidebar/dist/css/styles.css';
import { FaGem, FaHeart, FaCat, FaCheese, FaChessKing } from "react-icons/fa";
import data from '../data.json';
import '../css/dowjones.css'
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link
  } from "react-router-dom";
function DowJones() {
    return (
        <div className="mainbody">
            <div className="sidebar">
                <ProSidebar>
                    <Menu iconShape="circle">
                        <SubMenu title="United State" icon={<FaHeart />}>
                            <MenuItem>
                                <Link to={`/DowJones`}>Dow Jones</Link>
                            </MenuItem>
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
                    </Menu>
                </ProSidebar>
            </div>
            <div className="bar">
                <div className="component">
                    <a href="/stock/dowjones/component">COMPONENT</a>
                </div>
                <div className="chart">
                    <a href="/stock/dowjones/chart">CHART</a>
                </div>
                <div className="history">
                    <a href="/stock/dowjones/history">HISTORY</a>
                </div>
            </div>
        </div>
    );
}

export default DowJones;