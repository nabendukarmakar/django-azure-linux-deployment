import React, { Component } from 'react';
import { connect } from 'react-redux';
import {bindActionCreators} from 'redux';
import {BrandFilterData,updateList} from '../actions/postAction';
import PropTypes from 'prop-types';
import { Select } from 'antd';


const Option = Select.Option;
class BrandFilter extends Component {

    constructor(props)
    {
        super();
        this.state={
            SelectedBrand:"",
        }
        this.onChange=this.onChange.bind(this);
       
    }

    // componentWillMount()
    // {
      
    //     this.props.BrandFilterData("");
    //     this.props.updateList("brand", "Select a Brand")
    // }

   onChange(e)
    {
       
     
        const post={
            SelectedBrand:this.state.SelectedBrand
        }
        this.props.updateList("brand",e)
    }
    
    render() { 
       
       return(
        <Select
        showSearch
        style={{ width: 180 ,marginLeft:.5+'em'}}
        placeholder="Select Brand"
       optionFilterProp="children"
        defaultOpen={false}          
        onChange={this.onChange}
        value={this.props.updatelist['brand']}
        filterOption={(input, option) => option.props.children.toLowerCase().indexOf(input.toLowerCase()) >= 0}
      >
         {this.props.posts.map((Brand) => {
            
             return (
                <Option key={Brand['brand']}>{Brand['brand']}</Option>
             )
         } 
         
         )}
         </Select>
       )       
    }
}


const mapStatetoProps = state =>({
    posts:state.brand.brand,
    updatelist:state.update,
    
})

function mapDispatchToProps(dispatch){
    return bindActionCreators({
        BrandFilterData,updateList
    },dispatch);
}
export default connect(mapStatetoProps,mapDispatchToProps) (BrandFilter);

