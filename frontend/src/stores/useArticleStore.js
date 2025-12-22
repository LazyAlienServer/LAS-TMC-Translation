import { defineStore } from 'pinia';
import { computed, ref } from 'vue';
import { createSourceArticle, updateSourceArticle } from "@/api";

export const useArticleStore = defineStore('article', () => {
    /* states */
    const currentId = ref(null)

    /* getter */
    const hasCurrent = computed(() => !!currentId.value)

    /* actions */
    function switchArticle(id) {
        currentId.value = id
    }

    async function create() {
        const response = await createSourceArticle()

        switchArticle(response.data.id, response.data.status)
        console.log("Article successfully created!")

        return response
    }

    async function update(title, content) {
        const response = await updateSourceArticle(currentId.value, title, content)

        console.log("Article successfully updated!")

        return response
    }

    return {
        currentId,
        hasCurrent,
        switchArticle,
        create,
        update,
    };
});
