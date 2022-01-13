<script lang="ts" setup>import { ref } from 'vue';

const isAddQuestion = ref(false)

</script>

<template>
    <div class="form-control">
        <label class="label">
            <span class="label-text font-bold">New survey name</span>
        </label>
        <input type="text" placeholder="Name" class="input input-bordered" />
    </div>

    <div v-if="isAddQuestion">
        <span class="label-text font-bold">Question type</span>
    </div>

    <button class="hover:bg-neutral-100 flex flex-row my-5" @click="isAddQuestion = !isAddQuestion">
        <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-6 w-6"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
        >
            <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="{2}"
                d="M12 4v16m8-8H4"
            />
        </svg>
        <p>Add question</p>
    </button>

    <div>
        <button
            class="bg-green-500 mw-2 w-full h-10 rounded-md hover:bg-green-600 my-3"
        >Create Survey</button>
    </div>
</template>

<style scoped lang="scss">
</style>