import { UPDATED_FLAG_FALSE, UPDATED_FLAG, UPDATE_LIST, FETCH_COUNTRY_FILTER, FETCH_SOURCE_FILTER, FETCH_CATEGORY_FILTER, FETCH_BRAND_FILTER, FETCH_PSKU_DATA } from '../actions/types';

const initialState = {
    data: [],
    dataupdatd: false
}

const PSKUdataReducer = (state = initialState, action) => {

    switch (action.type) {

        case FETCH_PSKU_DATA:

            return {
                ...state,
                data: action.payload['Data']
            }

        case UPDATED_FLAG:
            return {
                ...state,
                dataupdatd: true
            }

        case UPDATED_FLAG_FALSE:
            return {
                ...state,
                dataupdatd: false
            }

        default:
            return state;
    }
}

export default PSKUdataReducer;