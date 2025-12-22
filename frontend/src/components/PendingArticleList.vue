<script setup>
import { useRouter } from "vue-router";
import { ref, onMounted } from "vue";
import { getPendingArticles } from "@/api";
import { PendingArticleInfoCard } from "@/components";

const router = useRouter();

const articles = ref([])

onMounted(async() => {
  const response = await getPendingArticles()
  articles.value = response.data
  console.log("Load articles successfully!")
})
</script>

<template>
  <div class="flex flex-col gap-y-4 w-full h-135 overflow-y-auto">

    <PendingArticleInfoCard
        v-for="article in articles"
        :key="article.id"
        :article="article"
    />

  </div>
</template>