<script setup>
import { ref } from "vue";
import { useToast } from "vue-toastification";
import { useRouter } from "vue-router";

const router = useRouter();

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
      Created:
      {{ new Date(article.created_at).toLocaleString() }}
    </span>

  </div>
</template>

<style scoped>

</style>