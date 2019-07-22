import React, { Component } from 'react';
import { connect } from 'react-redux';
import {bindActionCreators} from 'redux';
import {CategoryFilterData,BrandFilterData,updateList} from '../actions/postAction';
import PropTypes from 'prop-types';
import { Select } from 'antd';


const Option = Select.Option;
class CategoryFilter extends Component {

    constructor(props)
    {
        super();
        this.state={
            SelectedCategory:"",
        }
        this.onChange=this.onChange.bind(this);
       
    }

    componentWillMount()
    {
       
        this.props.CategoryFilterData("");
    }

    onChange(e)
    {
        
        const post={
            SelectedCategory:e
        }

    console.log("Selected Category",post)
        
    this.props.BrandFilterData(post);
      this.props.updateList("category",e)
     this.props.updateList("brand","Select a Brand")
    }
    
    render() { 
       return(
        <Select
        showSearch
        style={{ width: 180,marginLeft:.5+'em' }}
        placeholder="Select Category"
       optionFilterProp="children"
        defaultOpen={false}          
        onChange={this.onChange}
        value={this.props.updatelist['category']}
        filterOption={(input, option) => option.props.children.toLowerCase().indexOf(input.toLowerCase()) >= 0}
      >
         {this.props.posts.map((Category) => {
            
             return (
                <Option key={Category['level1']}>{Category['level1']}</Option>
             )
         } 
         
         )}
         </Select>
       )       
    }
}



const mapStatetoProps = state =>({
    posts:state.category.category,
    updatelist:state.update,
    
})

function mapDispatchToProps(dispatch){
    return bindActionCreators({
        CategoryFilterData,BrandFilterData,updateList
    },dispatch);
}
export default connect(mapStatetoProps,mapDispatchToProps) (CategoryFilter);

