<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { getChannelSnapshot } from "@/api";

const snapshot = ref({})
let intervalId = null

async function loadSnapshot() {
  try {
    const response = await getChannelSnapshot(snapshot);
    snapshot.value = response.data
    console.log("Fetch channel snapshot successfully")
  } catch (error) {
    console.warn('Failed to fetch channel snapshot:', error)
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
  <div class="flex flex-row px-14 gap-40 items-center">

    <div class="flex flex-col items-start pl-15 pt-8">
      <h1 class="text-[57px]">LAS Technical Minecraft<br>Translation Team</h1>
      <br>
      <p class="text-[32px]">Build a bridge between Minecraft communities.</p>

      <div class="flex flex-row items-start gap-6 my-8">

        <div class="hero-card">
          <p class="text-2xl font-bold">{{ snapshot.since }}</p>
          <p class="text-[14px]">Days Running</p>
        </div>

        <div class="hero-card">
          <p class="text-2xl font-bold">{{ snapshot.subscriber_count }}</p>
          <p class="text-[14px]">Subscribers</p>
        </div>

        <div class="hero-card">
          <p class="text-2xl font-bold">{{ snapshot.video_count }}</p>
          <p class="text-[14px]">Videos</p>
        </div>

        <div class="hero-card">
          <p class="text-2xl font-bold">{{ snapshot.view_count }}</p>
          <p class="text-[14px]">Views</p>
        </div>

      </div>
    </div>

    <img src="@/assets/logo.svg" alt="Logo" class="self-center w-70 h-70" />
  </div>
</template>
