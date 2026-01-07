<script setup>
import { useEditor, EditorContent } from '@tiptap/vue-3'
import StarterKit from '@tiptap/starter-kit'
import { useToast } from "vue-toastification";
import { useRouter, useRoute } from "vue-router";
import { onMounted, ref } from "vue";
import { getTheSourceArticle, submitArticle } from "@/api";

const toast = useToast();
const router = useRouter();
const route = useRoute();

const id = ref(null)
const title = ref(null)
const content = ref(null)

const loading = ref(false);

const title_editor = useEditor({
  content: '',
  extensions: [StarterKit],
  editable: false,
})

const content_editor = useEditor({
  content: '',
  extensions: [StarterKit],
  editable: false,
})

onMounted(async () => {
  const response = await getTheSourceArticle(route.params.id)

  id.value = response.data.id
  title.value = response.data.title
  content.value = response.data.content

  title_editor.value.commands.setContent(title.value)
  content_editor.value.commands.setContent(content.value)
})

async function handleSubmit() {
  loading.value = true;

  try {
    await submitArticle(id.value);
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

    <div class="editor-title p-3 bg-white text-black">
      <EditorContent :editor="title_editor"/>
    </div>

    <div class="editor-content p-3 bg-white text-black">
      <EditorContent :editor="content_editor"/>
    </div>

    <button type="button" @click="handleSubmit(id.value)" :disabled="loading">
      Submit
    </button>

  </div>
</template>
