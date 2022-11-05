<template>
  <div>
    {{products.data.results}}
    <Slider />

    <div class="container my-8">
      <h2 class="text-xl pb-4">Featured products</h2>
      <div class="grid grid-cols-2 lg:grid-cols-4 md:grid-cols-3 sm:grid-cols-3 gap-8">
        <div class="relative" v-for="item in products.data.results" :key="item">
          <a class="absolute inset-4" href=""><Icon icon="akar-icons:star" width="20" /></a>
          <div class="flex flex-col gap-2">
            <img src="../../public/img/slider.png" alt="" />
            <h3 class="text-md font-bold">{{item.title}}</h3>
            <p>${{item.unit_price}}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, reactive, onMounted } from "vue";
import axios from "../plugins/axios.js";
import Slider from "../components/Slider.vue";
export default {
	components: {
		Slider
	},
  setup() {
    const products = reactive([]);

    const getProducts = async () => {
      const data = await axios.get("store/products/?format=json");
      Object.assign(products, data);
    };

    onMounted(async () => {
      try {
        getProducts();
      } catch (error) {
        errorText.value = "اررور داشتیم";
      }
    });

    return { products };

  }
}
</script>

<style>

</style>