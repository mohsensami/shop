
<template>
<div>
  <NavBar />

<div class="bg-no-repeat h-[600px] w-screen bg-cover bg-center" style="background-image: url(../public/img/slider.png);">
  <div class="container">
    <div class="flex flex-col h-[600px] items-start justify-center gap-8">
      <h1 class="text-6xl bg-black bg-opacity-75 text-white p-1">New shoe!</h1>
      <h3 class="text-2xl bg-black bg-opacity-75 text-white p-1">Nike AirMax Something for only $129</h3>
      <button class="bg-[#3D81F5] rounded text-white p-2">View product</button>
    </div>
  </div>
</div>
</div>

</template>

<script setup lang="ts">
import NavBar from './components/NavBar.vue'

</script>

<style scoped>

</style>
