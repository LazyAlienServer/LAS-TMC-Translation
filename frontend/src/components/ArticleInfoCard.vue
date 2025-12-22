<script setup>
const props = defineProps({
  article: {
    type: Object,
    required: true,
  }
})
</script>

<template>
  <div class="flex flex-col gap-2 p-4 w-full bg-white rounded-lg border-0 shadow items-start">
    <!-- Title -->
    <h3 class="text-lg font-semibold truncate">
      {{ article.title }}
    </h3>

    <!-- Meta -->
    <span>
      Status:
      <span class="font-medium">{{ article.status_display }}</span>
    </span>

    <span>
      Created:
      {{ new Date(article.created_at).toLocaleDateString() }}
    </span>

    <span>
      Updated:
      {{ new Date(article.updated_at).toLocaleDateString() }}
    </span>

  </div>
</template>

<style scoped>

</style>