<script lang="ts" setup>import { ref } from 'vue';


enum questionTypes {
    Text = "TEXT",
    MultipleChoice = "MULTIPLE_CHOICE"
}


interface SurveyQuestion {
    type: questionTypes
    title: string
    optionCount?: number
    options?: Array<string>
}

interface SurveyQuestionRequest {
    questions: Array<SurveyQuestion>
}


const isAddQuestion = ref(true)
const surveyQuestionForm = ref({} as SurveyQuestionRequest)
const createQuestionForm = ref({} as SurveyQuestion)

</script>

<template>
    <div class="form-control">
        <label class="label">
            <span class="label-text font-bold">New survey name</span>
        </label>
        <input type="text" placeholder="Name" class="input input-bordered" />
    </div>

    <div class="divider"></div>
    <p>create question form {{ createQuestionForm }}</p>

    <div v-if="isAddQuestion" class="flex flex-col">
        <select v-model="createQuestionForm.type" class="select select-bordered w-full max-w-xs">
            <option disabled selected>Question type</option>
            <option :value="questionTypes.Text">Text</option>
            <option :value="questionTypes.MultipleChoice">Multiple Choice</option>
        </select>

        <span class="label-text font-bold">Question</span>
        <input
            type="text"
            placeholder="Title"
            class="input input-bordered"
            v-model="createQuestionForm.title"
        />

        <div v-if="createQuestionForm.type === questionTypes.MultipleChoice" class="mt-5">
            <div>
                <input
                    placeholder="Option"
                    class="input input-bordered w-full"
                    v-model="createQuestionForm.options"
                />
            </div>

            <button class="btn btn-outline btn-sm">Add Option</button>
            <button class="btn btn-outline btn-sm hover:bg-red-500">Remove Option</button>
        </div>
    </div>

    <button class="hover:bg-neutral-100 flex flex-row my-5" @click="surveyQuestionForm.count += 1">
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
    <button class="hover:bg-neutral-100 flex flex-row my-5" @click="surveyQuestionForm.count -= 1">
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
        <p>Remove question</p>
    </button>
    <div class="divider"></div>

    <div>
        <button
            class="bg-green-500 mw-2 w-full h-10 rounded-md hover:bg-green-600 my-3"
        >Create Survey</button>
    </div>
    <p>{{ surveyQuestionForm }}</p>
</template>

<style scoped lang="scss">
</style>