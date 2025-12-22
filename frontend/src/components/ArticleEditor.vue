<script setup>
import { useEditor, EditorContent } from '@tiptap/vue-3'
import StarterKit from '@tiptap/starter-kit'
import { useToast } from "vue-toastification";
import { useRouter } from "vue-router";
import { onMounted, ref } from "vue";
import { useArticleStore } from '@/stores';
import { getTheSourceArticle } from "@/api";

const toast = useToast();
const router = useRouter();
const articleStore = useArticleStore();

const title = ref(null)
const content = ref(null)

const loading = ref(false);

const title_editor = useEditor({
  content: '',
  extensions: [StarterKit],
})

const content_editor = useEditor({
  content: '',
  extensions: [StarterKit],
})

onMounted(async () => {
  const response = await getTheSourceArticle(articleStore.currentId)

  title.value = response.data.title
  content.value = response.data.content

  title_editor.value.commands.setContent(title.value)
  content_editor.value.commands.setContent(content.value)
})

async function handleSave() {
  loading.value = true;

  const title = title_editor.value.getText().trim();
  const content = content_editor.value.getJSON();

  try {
    await articleStore.update(title, content)
    toast.success("Article saved successfully!");
    await router.push({ name: 'my-articles' });

  } catch (error) {
    toast.error(error.response?.data?.toast_error);
    console.error("Failed to save the article", error);

  } finally {
    loading.value = false;
  }
}
</script>

<style>
  .editor-title .ProseMirror {
    outline: none;
  }
  .editor-content .ProseMirror {
    outline: none;
    min-height: 200px;
  }
</style>

<template>
  <div class="col-body-container">

    <div class="editor-title border rounded-lg p-3 bg-white text-black">
      <EditorContent :editor="title_editor"/>
    </div>
    <div class="editor-content border rounded-lg p-3 bg-white text-black">
      <EditorContent :editor="content_editor"/>
    </div>

    <button type="button" @click="handleSave()" :disabled="loading">
      Save Draft
    </button>
  </div>
</template>
