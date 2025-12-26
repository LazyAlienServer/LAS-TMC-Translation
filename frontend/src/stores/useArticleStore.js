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

        return response
    }

    async function update(title, content) {
        const response = await updateSourceArticle(currentId.value, title, content)

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
