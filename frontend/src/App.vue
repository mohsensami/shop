
<template>
  <div>
    <NavBar />
  

    <router-view></router-view>


    <Footer />



  </div>
</template>

<script lang="ts">
import NavBar from "./components/NavBar.vue";

import Footer from "./components/Footer.vue";
import { Icon } from '@iconify/vue';
export default {
	components: {
    NavBar, Footer
	}
}

</script>

<style scoped>
</style>
