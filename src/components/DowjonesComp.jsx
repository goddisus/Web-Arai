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
function DowJonesComp() {
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
                    <a href="/stock/component">COMPONENT</a>
                </div>
                <div className="chart">
                    <a href="/stock/chart">CHART</a>
                </div>
                <div className="history">
                    <a href="/stock/history">HISTORY</a>
                </div>
            </div>
            <table className="hhh">
                <tbody className="BodyTable">
                    <tr className="TTT" style={{borderBottom:"1px solid gray"}}>
                        <th className="headerT"><strong>NAME</strong></th>
                        <th><strong>LAST PRICE/PV PRICE</strong></th>
                        <th><strong>LOW/HIGH</strong></th>
                        <th><strong>PRICE DIFF/% DIFF</strong></th>
                        <th><strong>TIME DATE</strong></th>
                        <th><strong>3 MO PRICE DIFF/% DIFF</strong></th>
                        <th><strong>6 MO PRICE DIFF/% DIFF</strong></th>
                        <th style={{paddingRight:"10px"}}><strong>1 YEAR PRICE DIFF/% DIFF</strong></th>
                    </tr>
                    {data.map(item => (
                        <tr style={{borderBottom:"1px solid gray"}}>
                            <td className="bodyT">{item.name}</td>
                            <td>{item.lastestprice}/{item.previouseprice}</td>
                            <td>{item.low}/{item.high}</td>
                            <td>{item.nowpricediff}/{item.nowperdiff}</td>
                            <td>{item.time}</td>
                            <td>{item.threepricediff}/{item.threeperdiff}</td>
                            <td>{item.sixpricediff}/{item.sixperdiff}</td>
                            <td style={{paddingRight:"10px"}}>{item.yearpricediff}/{item.yearperdiff}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
            {false &&
            <div>
                {false &&
                <div>
                <div className="headwh1 bd">NAME</div>
                <div className="headwh bd">LAST PRICE/PV PRICE</div>
                <div className="headwh bd">LOW/HIGH</div>
                <div className="headwh bd">PRICE DIFF/% DIFF</div>
                <div className="headwh bd">TIME DATE</div>
                <div className="headwh bd">3 MO PRICE DIFF/% DIFF</div>
                <div className="headwh bd">6 MO PRICE DIFF/% DIFF</div>
                <div className="headwh bd">1 YEAR PRICE DIFF/% DIFF</div>
                </div>}
                <tr className="hhh">
                    <td>NAME</td>
                    <td>LAST PRICE/PV PRICE</td>
                    <td>LOW/HIGH</td>
                    <td>PRICE DIFF/% DIFF</td>
                    <td>TIME DATE</td>
                    <td>3 MO PRICE DIFF/% DIFF</td>
                    <td>6 MO PRICE DIFF/% DIFF</td>
                    <td>1 YEAR PRICE DIFF/% DIFF</td>
                </tr>
                {data.map(item => (
                    <div>
                    {false &&
                        <div>
                        
                        <div className="wh bd">{item.name}</div>
                        <div className="wh1 bd">{item.lastestprice}/{item.previouseprice}</div>
                        <div className="wh1 bd">{item.low}/{item.high}</div>
                        <div className="wh1 bd">{item.nowpricediff}/{item.nowperdiff}</div>
                        <div className="wh1 bd">{item.time}</div>
                        <div className="wh1 bd">{item.threepricediff}/{item.threeperdiff}</div>
                        <div className="wh1 bd">{item.sixpricediff}/{item.sixperdiff}</div>
                        <div className="wh1 bd">{item.yearpricediff}/{item.yearperdiff}</div>
                        <br />
                    </div>}
                    </div>
                ))}
            </div>}
        </div>
    );
}

export default DowJonesComp;