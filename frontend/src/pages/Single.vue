<template>
<div class="">
  
  <div class="bg-[#F7FAFC] py-8">
    <div class="container">
    <section>
      <div class="mb-4">
        <p>Products / Shoes / Sportshoes</p>
      </div>
      <div class="grid grid-cols-12 gap-12">
        <div class="col-span-6">
          <img src="../../public/img/slider.png" alt="">
        </div>
        <div class="col-span-6">
          <div class="flex flex-col gap-8">
            <h1 class="text-3xl">Product Name</h1>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Neque interdum tristique commodo ac vitae condimentum mauris odio.</p>
            <span>$129</span>
            <div class="flex items-center gap-8">
              <Icon icon="akar-icons:star" color="black" width="32" />
              <button class="bg-[#3D81F5] rounded text-white p-2">View product</button>
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
            <img src="../../public/img/slider.png" alt="" />
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
import { useRoute } from "vue-router";
import { Icon } from '@iconify/vue';

const route = useRoute();
export default {
  components: {
    route, Icon
  },
}
</script>

<style>

</style>