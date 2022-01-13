<script lang="ts" setup>import { CreateSurveyQuestion, CreateSurveyRequest, getCreateSurveyResponse } from '@/services/survey/getCreateSurveyResponse';
import { ref } from 'vue';

const isAddQuestion = ref(true)
const createSurveyForm = ref({ title: "", questions: [] } as CreateSurveyRequest)
const createQuestionForm = ref({
} as CreateSurveyQuestion)


async function createSurvey(): Promise<void> {
    const { ok: isSuccessful, val: response } = await getCreateSurveyResponse(createSurveyForm.value)
    //To add in error handling here
}



</script>

<template>
    <div class="form-control">
        <label class="label">
            <span class="label-text font-bold">New survey name</span>
        </label>
        <input
            type="text"
            placeholder="Name"
            class="input input-bordered"
            v-model="createSurveyForm.title"
        />
    </div>

    <div class="divider"></div>

    <div v-if="isAddQuestion" class="flex flex-col">
        <span class="label-text font-bold m-2">Question</span>
        <input
            type="text"
            placeholder="Title"
            class="input input-bordered"
            v-model="createQuestionForm.title"
        />
    </div>

    <button
        class="hover:bg-neutral-100 flex flex-row my-5"
        @click="createSurveyForm.questions.push({ title: createQuestionForm.title })"
    >
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

    <button
        class="hover:bg-neutral-100 flex flex-row my-5"
        @click="createSurveyForm.questions.pop()"
    >
        <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-6 w-6"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
        >
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="{2}" d="M20 12H4" />
        </svg>
        <p>Remove question</p>
    </button>
    <div class="divider"></div>
    <p>Question list</p>
    <li v-for="question in createSurveyForm.questions" :key="question.title">{{ question.title }}</li>

    <div class="divider"></div>

    <div>
        <button
            @click="createSurvey"
            class="bg-green-500 mw-2 w-full h-10 rounded-md hover:bg-green-600 my-3"
        >Create Survey</button>
    </div>
</template>

<style scoped lang="scss">
</style>
