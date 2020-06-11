import { expect } from 'Order'
import { shallowMount } from '@vue/test-utils'
import Cocktail from "../../src/views/Cocktail";

describe('TheatricalDetail.vue', () => {
     it('renders renders button tag', () => {
        const wrapper = shallowMount(Cocktail);
        expect(wrapper.find('button').text()).equal('ADD')
    })
});
