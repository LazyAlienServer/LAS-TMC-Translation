<script setup>
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
  <div class="article-card">
    <!-- Title and Status-->
    <div class="flex flex-row items-center gap-2">

      <router-link
          :to="{ name: 'article-editor', params: { id: article.id } }"
          class="text-lg font-semibold truncate hover:text-blue-500 hover:underline transition"
      >
        {{ article?.title }}
      </router-link>

      <div class="border border-gray-300 rounded-full flex flex-col py-0.5 px-2 items-center">
        <span class="text-[12px] font-bold text-gray-600 ">{{ article?.status_display }}</span>
      </div>

    </div>

    <!-- Meta -->

    <span>
      Created:
      {{ new Date(article?.created_at).toLocaleString() }}
    </span>

    <span>
      Updated:
      {{ new Date(article?.updated_at).toLocaleString() }}
    </span>

  </div>
</template>

<style scoped>

</style>