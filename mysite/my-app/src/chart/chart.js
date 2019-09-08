import React from 'react';
import 'antd/dist/antd.css';
import { Select, Typography, Button } from 'antd';
const { Option } = Select;
const { Text } = Typography;


class ChartComponent extends React.Component {
  state = {
    locations: ['Jack', 'Jack1', 'Jack2'],
    years: ['1', '2', '3'],
    types: ['t1', 't2']
  };

  render() {
    return (
      <div>
        <div style={{ 'marginButton': 10 , 'marginLeft': 'auto', 'marginRight': 'auto'}}>
          <span style={{ 'marginRight': 5 }}>
            <Text>Location: </Text>
            <Select style={{ width: 200 }} >
              {this.state.locations.map(value => {
                return <Option value={value}>{value}</Option>
              })}
            </Select>
          </span>
          <span style={{ 'marginLeft': 5 }}>
            <Text>Location: </Text>
            <Select style={{ width: 200 }} >
              {this.state.locations.map(value => {
                if (value != this.state.select2) {
                  return <Option value={value}>{value}</Option>
                }
              })}
            </Select>
          </span>
        </div>
        <div style={{ 'marginTop': 10 }}>

          <Text>Type: </Text>
          <Select style={{ width: 200 }} >
            {this.state.years.map(value => {
              if (value != this.state.select1) {
                return <Option value={value}>{value}</Option>
              }
            })}
          </Select>
        </div>
        <div style={{ 'marginTop': 10 }}>

          <Text>Year: </Text>
          <Select style={{ width: 200 }} >
            {this.state.types.map(value => {
              return <Option value={value}>{value}</Option>
            })}
          </Select>

        </div>
        <div style={{ 'marginTop': 10 }}>
          <Button type="primary"  icon="search"> Search</Button>
        </div>
      </div>
    )
  }
}
export default ChartComponent;