import React, { Component } from 'react';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import { SourceFilterData, CategoryFilterData, BrandFilterData, updateList } from '../actions/postAction';
import { Select } from 'antd';




const Option = Select.Option;
class SourceFilter extends Component {

    constructor(props) {
        super();

        this.onChange = this.onChange.bind(this);
    }

    componentWillMount() {

        this.props.SourceFilterData("");
    }

    onChange(e) {


        const post = {
            SelectedChannel: e
        }

        this.props.CategoryFilterData(post);
        this.props.updateList("channel", e)
        this.props.updateList("category", "Select a Category")
        this.props.updateList("brand", "Select a Brand")
    }

    render() {
        return (

            <Select
                showSearch
                style={{ width: 180, marginLeft: .5 + 'em' }}
                placeholder="Select Channel"
                optionFilterProp="children"
                defaultOpen={false}
                onChange={this.onChange}
                value={this.props.updatelist['channel']}
                filterOption={(input, option) => option.props.children.toLowerCase().indexOf(input.toLowerCase()) >= 0}
            >
                {this.props.posts.map((Channel) => {

                    return (
                        <Option key={Channel['mkt_name']}>{Channel['mkt_name']}</Option>
                    )
                }

                )}
            </Select>
        )
    }
}



const mapStatetoProps = state => ({
    posts: state.channel.channel,
    updatelist: state.update,
})

function mapDispatchToProps(dispatch) {
    return bindActionCreators({
        CategoryFilterData, SourceFilterData, BrandFilterData, updateList
    }, dispatch);
}
export default connect(mapStatetoProps, mapDispatchToProps)(SourceFilter);

