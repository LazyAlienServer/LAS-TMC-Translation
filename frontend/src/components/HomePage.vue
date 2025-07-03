<script setup>

import {ref, onMounted} from 'vue'
import {fetchSnapshot} from "@/apis/snapshot";

const snapshot = ref({});

onMounted(async () => {
  try {
    const response = await fetchSnapshot();
    snapshot.value = response.data
    console.log("Fetch channel snapshot successfully:", response.data)
  } catch (error) {
    console.log('Failed to fetch channel snapshot:', error)
  }
})

</script>

<template>
  <div class="font-sans">
    <h1>{{ snapshot.title }}</h1>
    <p>{{ snapshot.description }}</p>
    <ul>
      <li>{{ snapshot.subscriber_count }}</li>
      <li>{{ snapshot.view_count }}</li>
      <li>{{ snapshot.video_count }}</li>
    </ul>
  </div>
</template>

<style scoped>

</style>
