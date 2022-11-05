<template>
  <div class="">
    <div class="container">
        <h1 class="text-3xl py-8">Shopping cart</h1>
        <!-- <p class="text-md">{{cart.items.length}} products in cart.</p> -->
    
    <div class="grid grid-cols-12 gap-4">
        <div class="col-span-9">
            <div class="bg-primary border-primary rounded p-2">
                <h3 class="text-xl pb-8">Your shopping cart</h3>
                <ul class="flex flex-col gap-8">
                    <li v-for="item in cart.items" :key="item.id">
                        <div class="flex items-center justify-between">
                            <div><img width="62" :src="`https://picsum.photos/seed/` + item.id + `/64/64`"></div>
                            <div><h4><router-link :to="{ name: 'single', params: { id: item.product.id } }">{{item.product.title}}</router-link></h4></div>
                            <div><p>{{item.quantity}}</p></div>
                            <div class="flex flex-col">
                                <div><p>${{item.total_price}}</p></div>
                                <div><p>${{item.product.unit_price}} / per item</p></div>
                            </div>
                            <div><button>Remove</button></div>
                        </div>
                    </li>
                </ul>
            </div>
        </div>
        <div class="col-span-3">
            <div class="bg-primary border-primary rounded p-2">
                <div class="flex flex-col">
                    <div class="flex justify-between"><p>Total price:</p><p>${{cart.total_price}}</p> </div>
                    <hr>
                    <a class="btn-primary text-center" href="#"> Make Purchase </a>
                    <a class="text-center" href="#"> Back to shop </a>
                </div>
            </div>
        </div>
    </div>
  </div>
  </div>
</template>

<script>
import axios from "../plugins/axios.js";
import { reactive, onMounted } from "vue";

import { useRoute } from "vue-router";
import { Icon } from '@iconify/vue';

export default {
  components: {
    Icon
  },
  setup() {
    const route = useRoute();
    const cart = reactive({});
    const getCart = async () => {
      const {data} = await axios.get(`store/carts/798e1379-5685-4caf-b62b-f04e7f99fdf6/`);
      Object.assign(cart, data);
    };

    onMounted(async () => {
      try {
        await getCart();
      } catch (error) {
        // errorText.value = "اررور داشتیم";
      }
    });

    return {  cart, route  };

  }
}
</script>

<style>

</style>