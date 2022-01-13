<script lang="ts" setup>import { ref } from 'vue';

const isAddQuestion = ref(true)
const questionOptions = ref([] as Array<any>)
const questionTitle = ref("")
const questionType = ref("Text")

function addOption() {
    questionOptions.value.push({ option: '' })
}

function removeOption() {
    questionOptions.value.pop()
}

</script>

<template>
    <div class="form-control">
        <label class="label">
            <span class="label-text font-bold">New survey name</span>
        </label>
        <input type="text" placeholder="Name" class="input input-bordered" />
    </div>

    <div class="divider"></div>

    <div v-if="isAddQuestion" class="flex flex-col">
        <div class="tabs">
            <button class="tab tab-bordered" @click="questionType = 'Text'">Text</button>
            <button
                class="tab tab-bordered"
                @click="questionType = 'Multiple choice'"
            >Multiple choice</button>
        </div>

        <p>question title{{ questionTitle }}</p>
        <p>question options{{ questionOptions }}</p>

        <span class="label-text font-bold">Question</span>
        <input type="text" placeholder="Title" class="input input-bordered" v-model="questionTitle" />

        <div v-if="questionType === 'Multiple choice'" class="mt-5">
            <div v-for="(questionOption, index) in questionOptions">
                <input
                    v-model="questionOption.option"
                    placeholder="Option"
                    class="input input-bordered w-full"
                />
            </div>

            <button @click="addOption" class="btn btn-outline btn-sm">Add Option</button>
            <button
                @click="removeOption"
                class="btn btn-outline btn-sm hover:bg-red-500"
            >Remove Option</button>
        </div>
    </div>

    <!-- <button class="hover:bg-neutral-100 flex flex-row my-5" @click="isAddQuestion = !isAddQuestion">
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
    </button>-->
    <div class="divider"></div>

    <div>
        <button
            class="bg-green-500 mw-2 w-full h-10 rounded-md hover:bg-green-600 my-3"
        >Create Survey</button>
    </div>
</template>

<style scoped lang="scss">
</style>