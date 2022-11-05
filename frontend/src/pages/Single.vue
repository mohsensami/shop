<template>
<div class="">
  <div class="bg-[#F7FAFC] py-8">
    <div class="container">
    <section>
      <div class="mb-4">
        <p>Products / {{product.collection?.title}} / {{product.title}}</p>
      </div>
      <div class="grid grid-cols-12 gap-12">
        <div class="col-span-6">
          <img :src="`https://picsum.photos/seed/` + product.id + `/800/500`" alt="">
        </div>
        <div class="col-span-6">
          <div class="flex flex-col gap-8">
            <h1 class="text-3xl">{{ product.title }}</h1>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Neque interdum tristique commodo ac vitae condimentum mauris odio.</p>
            <span>${{ product.unit_price }}</span>
            <div class="flex items-center gap-8">
              <Icon icon="akar-icons:star" color="black" width="32" />
              <button @click="addToCart()" class="btn-primary custom-transition"> Add to cart </button>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
  </div>

  <section>
      <div class="container my-8">
      <h2 class="text-xl pb-4">Related products</h2>
      <div class="grid grid-cols-2 lg:grid-cols-4 md:grid-cols-3 sm:grid-cols-3 gap-8">
        <div class="relative" v-for="item in 4" :key="item">
          <a class="absolute inset-4" href=""><Icon icon="akar-icons:star" width="20" /></a>
          <div class="flex flex-col gap-2">
            <img :src="`https://picsum.photos/seed/` + item + `/800/500`" alt="" />
            <h3 class="text-md font-bold">Product Name</h3>
            <p>$129</p>
          </div>
        </div>
      </div>
    </div>
    </section>
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
    const product = reactive({});
    const getProduct = async () => {
      const {data} = await axios.get(`store/products/${route.params.id}/?format=json`);
      Object.assign(product, data);
    };

    onMounted(async () => {
      try {
        await getProduct();
      } catch (error) {
        // errorText.value = "اررور داشتیم";
      }
    });

    return {  product, route  };

  }
}
</script>

<style>

</style>