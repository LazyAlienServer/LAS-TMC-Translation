<script setup>

import {ref, onMounted, onUnmounted} from 'vue'
import {fetchSnapshot} from "@/apis/snapshot";

const snapshot = ref({})
let intervalId = null

async function loadSnapshot() {
  try {
    const response = await fetchSnapshot();
    snapshot.value = response.data
    console.log("Fetch channel snapshot successfully:", response.data)
  } catch (error) {
    console.log('Failed to fetch channel snapshot:', error)
  }
}

onMounted(() => {
  loadSnapshot()
  intervalId = setInterval(loadSnapshot, 60 * 1000)
})

onUnmounted(() => {
  clearInterval(intervalId)
})

</script>

<template>
  <div class="body-container">
    <h1>{{ snapshot.title }}</h1>
    <p class="whitespace-pre-line">{{ snapshot.description }}</p>
    <ul>
      <li>Subscribers: {{ snapshot.subscriber_count }}</li>
      <li>Total Views: {{ snapshot.view_count }}</li>
      <li>Total Videos: {{ snapshot.video_count }}</li>
    </ul>
  </div>
</template>

<style scoped>

</style>
