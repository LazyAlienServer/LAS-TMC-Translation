<script setup>
import { RouterLink, useRouter } from "vue-router";
import { useArticleStore } from "@/stores"
import { useToast } from "vue-toastification";
import { ref, onMounted } from "vue";
import { getMySourceArticles } from "@/api";
import { ArticleInfoCard } from "@/components";

const router = useRouter();
const articleStore = useArticleStore();
const toast = useToast();

const loading = ref(false)

const articles = ref([])

onMounted(async() => {
  const response = await getMySourceArticles()
  articles.value = response.data
  console.log("Load articles successfully!")
  console.log(articles.value)
})

</script>

<template>
  <div class="flex flex-col gap-y-4 w-full h-135 overflow-y-auto">

    <ArticleInfoCard
        v-for="article in articles"
        :key="article.id"
        :article="article"
    />

  </div>
</template>

<style scoped>

</style>