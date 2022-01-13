<script lang="ts" setup>
import { ref } from 'vue';
import Inputs from './QuestionTypes/Inputs.vue';
import MultipleChoices from './QuestionTypes/MultipleChoices.vue';
import SurveyCreateForm from './SurveyCreateForm.vue';

const isCreateSurvey = ref(false)
const isAddQuestion = ref(false)
const questionType = ref("")

</script>

<template>
    <button class="hover:bg-neutral-100" @click="isCreateSurvey = true">
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
    </button>

    <div v-if="isCreateSurvey">
        <SurveyCreateForm></SurveyCreateForm>
        <div>
            <button
                class="bg-red-500 mw-2 w-full h-10 rounded-md hover:bg-red-600 my-3"
                @click="isCreateSurvey = false"
            >Exit</button>
        </div>
    </div>
</template>

<style scoped lang="scss">
</style>