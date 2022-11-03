
<template>
  <div>
    <NavBar />
    <Slider />

    <div class="container my-8">
      <h2 class="text-xl pb-4">Featured products</h2>
      <div class="grid grid-cols-2 lg:grid-cols-4 md:grid-cols-3 sm:grid-cols-3 gap-8">
        <div class="relative" v-for="item in 12" :key="item">
          <a class="absolute inset-4" href=""><Icon icon="akar-icons:star" width="20" /></a>
          <div class="flex flex-col gap-2">
            <img src="../public/img/slider.png" alt="" />
            <h3 class="text-md font-bold">Product Name</h3>
            <p>$129</p>
          </div>
        </div>
      </div>
    </div>


    <Footer />



  </div>
</template>

<script lang="ts">
import NavBar from "./components/NavBar.vue";
import Slider from "./components/Slider.vue";
import Footer from "./components/Footer.vue";
import { Icon } from '@iconify/vue';
export default {
	components: {
		Icon, NavBar, Slider, Footer
	}
}

</script>

<style scoped>
</style>
