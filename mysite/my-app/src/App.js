import React from 'react';
import logo from './logo.svg';
import './App.css';
import TableComponent from './table/table.js'
import Helmet from 'react-helmet';
import { Row, Col, Layout } from 'antd';
const { Header, Footer, Content } = Layout;
function App() {
  return (

    <div className="App">

      <Layout style={{'height': '100vh'}}>
        <Header>Header</Header>
        <Content style={{'background-color': 'white'}}>
          <Row>
            <Col span={4}></Col>
            <Col span={16}><TableComponent></TableComponent></Col>
            <Col span={4}></Col>
          </Row>
        </Content>
        <Footer style={{'height': '1rem'}}><div style={{'margin': '-0.5rem auto'}}>©2019 CMPUT401 Team callback Cats</div></Footer>
      </Layout>

    </div>
  );
}

export default App;
