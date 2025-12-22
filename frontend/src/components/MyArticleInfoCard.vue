<script setup>
import { submitArticle } from "@/api";
import { ref } from "vue";
import { useToast } from "vue-toastification";
import { useRouter } from "vue-router";

const toast = useToast();
const router = useRouter();
const loading = ref(false)

const props = defineProps({
  article: {
    type: Object,
    required: true,
  }
})

async function handleSubmit(id) {
  loading.value = true;

  try {
    await submitArticle(id);
    toast.success("Article submitted successfully!");
    await router.push({ name: 'my-articles' });

  } catch (error) {
    toast.error(error.response?.data?.toast_error);
    console.error("Failed to submit the article", error);

  } finally {
    loading.value = false;
  }
}
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
      {{ new Date(article.created_at).toLocaleString() }}
    </span>

    <span>
      Updated:
      {{ new Date(article.updated_at).toLocaleString() }}
    </span>

    <button type="button" @click="handleSubmit(article.id)" :disabled="loading">
      Submit
    </button>

  </div>
</template>

<style scoped>

</style>